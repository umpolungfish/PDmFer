import os
import sys
from typing import Optional
import fitz
from PyPDF2 import PdfReader, PdfWriter


class PDFProcessor:
    
    def __init__(
        self,
        input_path: str,
        output_path: str,
        link: str = "",
        blur: str = "None",
        password: Optional[str] = None,
        redirect_message: Optional[str] = None,
        title: Optional[str] = None,
        author: Optional[str] = None,
        subject: Optional[str] = None,
        keywords: Optional[str] = None,
        verbose: bool = False
    ):
        self.input_path = input_path
        self.output_path = output_path
        self.link = link
        self.blur = blur
        self.password = password
        self.redirect_message = redirect_message
        self.title = title
        self.author = author
        self.subject = subject
        self.keywords = keywords
        self.verbose = verbose
        
        self.blur_values = {
            "None": 0,
            "Low": 1,
            "Medium": 2,
            "High": 3
        }
        
    def log(self, message: str):
        if self.verbose:
            print(f"[VERBOSE] {message}")
    
    def validate_inputs(self) -> bool:
        if not os.path.exists(self.input_path):
            print(f"Error: Input file does not exist: {self.input_path}")
            return False
            
        if not self.input_path.lower().endswith('.pdf'):
            print(f"Error: Input file must be a PDF: {self.input_path}")
            return False
            
        if self.link and not self.link.startswith(('http://', 'https://')):
            print(f"Error: Link must start with http:// or https://: {self.link}")
            return False
            
        if self.blur not in self.blur_values:
            print(f"Error: Invalid blur level. Must be one of: {list(self.blur_values.keys())}")
            return False
            
        return True
    
    def process(self) -> bool:
        try:
            if not self.validate_inputs():
                return False
                
            doc = fitz.open(self.input_path)
            
            if self.blur != "None":
                blurred_doc = self.apply_blur_to_new_doc(doc)
                
                doc.close()
                doc = blurred_doc
            else:
                self.log("No blur applied")
            
            self.set_metadata_pymupdf(doc)
            
            if self.redirect_message:
                doc = self.add_popup_redirect_message(doc)
            else:
                self.add_download_redirect(doc)
            
            if self.password:
                doc.save(
                    self.output_path,
                    encryption=fitz.PDF_ENCRYPT_AES_128,
                    owner_pw=self.password,
                    user_pw=self.password,
                    permissions=(fitz.PDF_PERM_ACCESSIBILITY | fitz.PDF_PERM_COPY)
                )
            else:
                doc.save(self.output_path)
            
            doc.close()
            
            self.log(f"Successfully processed PDF: {self.input_path} -> {self.output_path}")
            return True
            
        except Exception as e:
            print(f"Error processing PDF: {str(e)}", file=sys.stderr)
            return False
    
    def apply_blur_to_new_doc(self, original_doc):
        from PIL import Image, ImageFilter
        import io
        
        blur_radii = {
            "Low": 2,
            "Medium": 5,
            "High": 10
        }
        
        radius = blur_radii.get(self.blur, 0)
        
        new_doc = fitz.open()
        
        for page_num in range(len(original_doc)):
            page = original_doc[page_num]
            
            mat = fitz.Matrix(zoom, zoom)
            
            pix = page.get_pixmap(matrix=mat)
            
            img_data = pix.tobytes("ppm")
            img_stream = io.BytesIO(img_data)
            pil_img = Image.open(img_stream)
            
            if radius > 0:
                pil_img = pil_img.filter(ImageFilter.GaussianBlur(radius=radius))
                
            temp_img_stream = io.BytesIO()
            pil_img.save(temp_img_stream, format="PDF", resolution=72*zoom)
            temp_img_stream.seek(0)
            
            blurred_page_doc = fitz.open("pdf", temp_img_stream.read())
            new_doc.insert_pdf(blurred_page_doc)
            blurred_page_doc.close()
        
        if self.redirect_message:
            new_doc = self.add_popup_redirect_message(new_doc)
        else:
            if self.link:
                if len(new_doc) > 0:
                    first_page = new_doc[0]
                    
                    rect = fitz.Rect(50, 50, 200, 100)  # x0, y0, x1, y1
                    
                    link = {
                        "kind": fitz.LINK_URI,
                        "from": rect,
                        "uri": self.link
                    }
                    
                    first_page.insert_link(link)

        
        return new_doc
    
    def add_redirect_message_annotation_to_page(self, page):
        self.log(f"Adding redirect message annotation: {self.redirect_message}")
        
        point = fitz.Point(50, 120)
        
        text_annot = page.add_text_annot(point, self.redirect_message)
        text_annot.update()

    def set_metadata_pymupdf(self, doc):
        info = doc.metadata
        if self.title:
            info["title"] = self.title
            self.log(f"Setting title: {self.title}")
        if self.author:
            info["author"] = self.author
            self.log(f"Setting author: {self.author}")
        if self.subject:
            info["subject"] = self.subject
            self.log(f"Setting subject: {self.subject}")
        if self.keywords:
            info["keywords"] = self.keywords
            self.log(f"Setting keywords: {self.keywords}")
        
        doc.set_metadata(info)

    def add_download_redirect(self, doc):
        if not self.link:
            self.log("No link provided, skipping download redirect")
            return
        
        self.log("Adding download redirect functionality with popup message")
        
        if len(doc) > 0:
            page = doc[0]
            
            rect = fitz.Rect(50, 50, 200, 100)  # x0, y0, x1, y1
            
            link = {
                "kind": fitz.LINK_URI,
                "from": rect,
                "uri": self.link
            }
            
            page.insert_link(link)
            

    
    def add_popup_redirect_message(self, doc):
        if not self.redirect_message:
            self.log("No redirect message, adding direct link if provided")
            if self.link:
                if len(doc) > 0:
                    page = doc[0]
                    
                    rect = fitz.Rect(50, 50, 200, 100)  # x0, y0, x1, y1
                    
                    link = {
                        "kind": fitz.LINK_URI,
                        "from": rect,
                        "uri": self.link
                    }
                    
                    page.insert_link(link)
                    
            return doc
            
        self.log(f"Adding popup redirect message: {self.redirect_message}")
        
        js_code = f'''
        var message = "{self.redirect_message}";
        app.alert(message, 2, 0, "Download Notice");
        app.launchURL("{self.link}", true);
        '''
        
        try:
            import io
            temp_pdf_bytes = doc.tobytes()
            
            from PyPDF2 import PdfReader, PdfWriter
            temp_stream = io.BytesIO(temp_pdf_bytes)
            reader = PdfReader(temp_stream)
            
            writer = PdfWriter()
            
            for page in reader.pages:
                writer.add_page(page)
            
            writer.add_js(js_code)
            
            temp_output = io.BytesIO()
            writer.write(temp_output)
            temp_output.seek(0)
            
            new_doc_bytes = temp_output.getvalue()
            doc.close()  # Close the original document
            
            new_doc = fitz.open("pdf", new_doc_bytes)
            
            if len(new_doc) > 0:
                page = new_doc[0]
                
                rect = fitz.Rect(50, 50, 200, 100)  # x0, y0, x1, y1
                
                link = {
                    "kind": fitz.LINK_URI,
                    "from": rect,
                    "uri": self.link
                }
                
                page.insert_link(link)
                

            
            return new_doc
            
        except Exception as e:
            self.log(f"Error adding popup JavaScript: {str(e)}")
            if len(doc) > 0:
                page = doc[0]
                
                rect = fitz.Rect(50, 50, 200, 100)  # x0, y0, x1, y1
                
                link = {
                    "kind": fitz.LINK_URI,
                    "from": rect,
                    "uri": self.link
                }
                
                page.insert_link(link)
                
                page.insert_text(fitz.Point(50, 40), 
                                f"Click to download: {self.link}", 
                                fontsize=12)
                
            return doc
    
    def add_redirect_message_annotation(self, doc):
        if not self.redirect_message:
            self.log("No redirect message to add")
            return
            
        self.log(f"Adding redirect message annotation: {self.redirect_message}")
        
        if len(doc) > 0:
            page = doc[0]
            point = fitz.Point(50, 120)
            
            text_annot = page.add_text_annot(point, self.redirect_message)
            text_annot.update()

    def process_download_redirect(self):
        if self.redirect_message:
            self.log("Processing DownloadRedirect with popup message")
        else:
            self.log("Processing DownloadRedirect without popup message")