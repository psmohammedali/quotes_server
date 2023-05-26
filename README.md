# **Quotes Marathon**

This project is a miniature model of the Client-Server Application framework that we use in our daily life. This project recreates our computer machine as a local server and client. As a Client, It sends requests to generate quotes based on the theme, and the server accepts the request and generates the response respectively.

![/images/ss1.PNG](https://user-images.githubusercontent.com/48435733/241138841-ed808c03-9580-4f40-b00d-2958b045560a.PNG))

- - -

## **Project Exceution**

1. First, Clone the git repo in your local machine

[`git clone https://github.com/psmohammedali/quotes_server.git`](http://github.com/psmohammedali/quotes_server.git)


2. Second, change your directory to project directory `server_quote`

```
cd server_quote
```

3. Install the required package in `requirements.txt`

```
pip install requirements.txt
```

4. Before exceuting client.py. First, execute server.py program for the server to listen\, up and running.

```
python server.py
```

5. The, run client\.py and entering your name as a parmater for customization purposes.

`Format:` `python client.py --name your_name` `(or)` `python client.py -n your_name`

```
python client.py --name ali
```

6. Once, you enter the command, you get list of numeric choice to chose to request quotes from the server that we have set up earlier.

![ss2.png](/images/ss2.PNG)

7. You can stop the server by sending request as "stop".

![ss3.PNG](/images/ss3.PNG)  

---

**Feedback are most Welcome...**

_Regards,<br>
P S Mohammed Ali._
