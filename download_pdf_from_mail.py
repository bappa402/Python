import imaplib
import email
import os

# 🔐 Your credentials
EMAIL = 'xyz@gmail.com'     #your gamil id
PASSWORD = ''  # App password from Google (generate it and paste it here, remove spaces between)

# 📁 Folder to store downloaded PDFs
PDF_DIR = r'C:\Users\91700\Downloads\statements'

os.makedirs(PDF_DIR, exist_ok=True)

# 📬 Connect to Gmail
print("Connecting to Gmail...")
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)
mail.select("inbox")

# 🔍 Search for ICICI statements
print("Searching for ICICI bank statement emails...")
status, messages = mail.search(None, '(FROM "estatement@icicibank.com" SUBJECT "ICICI Bank Statement")')

pdf_count = 0
for num in messages[0].split():
    _, data = mail.fetch(num, "(RFC822)")
    message = email.message_from_bytes(data[0][1])
    for part in message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        filename = part.get_filename()
        if filename and filename.endswith('.pdf'):
            filepath = os.path.join(PDF_DIR, filename)
            with open(filepath, 'wb') as f:
                f.write(part.get_payload(decode=True))
            pdf_count += 1
            print(f"✅ Downloaded: {filename}")

mail.logout()
print(f"\n🎉 All done! {pdf_count} PDF(s) downloaded to '{PDF_DIR}'")
