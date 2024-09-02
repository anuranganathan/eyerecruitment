import tkinter as tk
from tkinter import scrolledtext



phishing_keywords=["urgent","verify","account","login","security","suspicious","confirm"]
def is_phishing(email_body):
    for keyword in phishing_keywords:
        if keyword in email_body.lower():
            return True
    return False


email_samples=[
    "Dear user, please verify your account details immediately.",
    "your order has been shipped and will arrive soon"
    "urgent:your account has been compromised. please login and update your security settings"

]

for email in email_samples:
    if is_phishing(email):
        print("Phishing Detected !")
    else:
        print("Safe Email.")

        

def check_email():
    email_body=email_text.get("1.0",tk.END)
    if is_phishing(email_body):
        result_label.config(text="Phishing Detected !",fg="red")
    else:
        result_label.config(text="Safe Email.",fg="green")


#setting up GUI.


root=tk.Tk()
root.title("Phishing Email Detector")

email_text=scrolledtext.ScrolledText(root,width=50,height=20)
email_text.pack()

check_button=tk.Button(root,text="check email",command=check_email)
check_button.pack()
result_label=tk.Label(root,text="",font=("Arial",14))
result_label.pack()
root.mainloop()                            
            
