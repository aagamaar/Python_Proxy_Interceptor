# 🕵️‍♂️ The Python Proxy Interceptor: A "Man-in-the-Middle" Proxy

 

## 👋 What is this project?

Imagine you are passing a note to your friend in class. Normally, you hand it directly to them.
Now, imagine a **middleman** sits between you. You hand the note to the middleman, they read it (and maybe change what it says\!), and then they hand it to your friend. Your friend thinks the note came straight from you.

**I built that "Middleman" for the Internet.**

This tool is a **Proxy Server** written in Python. It sits between your web browser (eg. Firefox) and the Internet. It catches every website request you make, reads it, and can even change the website before it reaches your screen.

-----

## 💥 The "Cool" Part: How I Hacked a Website (Locally)

I used this tool to perform a classic cybersecurity attack called a **"Man-in-the-Middle" Attack**.

1.  **The Setup:** I told my browser to send all traffic to my Python script instead of the real internet.
2.  **The Trick:** When I visited `http://example.com`, my script intercepted the website's reply.
3.  **The Attack:** My script searched for the word **"Example"** in the website's code and replaced it with **"HACKED\!"**.
4.  **The Result:** The browser displayed the "HACKED\!" version. I changed the website on my screen without ever touching the real server\!

-----

## 🛠️ How it Works (Under the Hood)

This project combines concepts from **Networking** and **Operating Systems**.

### 1\. The Listener (The Ears)

My script starts a "Server" on my laptop. It opens a digital door (Port 8888) and waits for my browser to connect. This is called **Socket Programming**.

### 2\. The Multitasker (The Brain)

If I open 10 tabs in my browser, my script needs to handle all 10 at once. I used **Threading** (a concept from Operating Systems) to create a "mini-worker" for every single connection so the proxy never freezes.

### 3\. The Translator (The Logic)

Websites usually send data compressed (like a ZIP file) to save speed. My script couldn't read that.

  * **My Fix:** I stripped out the headers that said "I accept GZIP".
  * **The Result:** I forced the big internet servers to talk to me in **Plain Text** so I could read and modify the data.

-----

## 🎓 What I Learned (Connecting to my Degree)

This wasn't just for fun. It maps directly to my engineering syllabus:

  * **Computer Networks :** I didn't just read about HTTP and TCP; I built a tool that speaks them. I learned how data packets are structured.
  * **Operating Systems :** I learned how to manage computer resources using Threads and Buffers (handling data in chunks).
  * **Cyber Security :** I successfully performed an **Integrity Attack**. I proved that if data isn't encrypted (HTTPS), anyone in the middle can tamper with it.

-----

## 🚀 How to Run It

1.  **Clone this repo.**
2.  **Run the script:** `python proxy.py`
3.  **Configure Firefox:** Set your Network Proxy to `127.0.0.1` port `8888`.
4.  **Visit:** `http://example.com` and watch the magic happen in your terminal\!

-----

**⚠️ Note:** This tool is for educational purposes only. It runs locally on your own machine. Intercepting traffic on networks you don't own is illegal.
