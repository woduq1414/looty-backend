from xhtml2pdf import pisa             # import python module

# Define your data
source_html = """
<style>
body { font-family: HYGothic-Medium !important; }
</style>

<p><strong style="font-size: 24px;">아아 <span style="background-color: rgb(0, 0, 255);">안녕하세요!!</span></strong></p>
<p><strong style="font-size: 24px;"><img src="http://storage.localhost/fastapi-minio/0187e23d-47a8-7ff2-ad37-eba174b733d3621eeaad-5cc0-4162-81ce-06670907ef0a.JPEG?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=minioadmin%2F20230503%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230503T153120Z&amp;X-Amz-Expires=604800&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=f598a1bfad3710d6869a4244ff2c97f2273c37e94a215324f37dd45a5fdd669b" width="456" height="811"></strong></p>
<p><strong style="font-size: 24px;"><span style="background-color: rgb(255, 255, 0); color: rgb(255, 153, 0);">반가워요!</span> <u>Hel<s>lo</s></u></strong></p>

"""
output_filename = "test.pdf"

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convert_html_to_pdf(source_html, output_filename)