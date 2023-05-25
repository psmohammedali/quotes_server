## Quotes Server

This project is a minimatur model of Client-Server Application framework that we use in daily life. This project recreate our own computer machine is a local server and client. As a Client, It sends request to generate quotes based on the theme and Server accepts the request and generates the response respectively.

- - -

### **Project Exceution**
<br>
1\. First\, Clone the git repo in your local machine
<br>
```
git clone https://[github.com/psmohammedali/quotes\_server.git](http://github.com/psmohammedali/quotes_server.git)
```
<br>
2\. Second\, change your directory to project directory `server_quote`
<br>
```
cd server_quote
```
<br>
3, Install the required package in requirement.txt

```
pip install requirements.txt
```
<br>
4\. Before exceuting client\.py\, First execute server\.py program for the server to listen\, up and running\.

```
python server.py
```
<br>
5\. Then\, run client\.py and entering your name as a parmater for customization purposes\.

`Format : python client.py --name your_name`
                                    `(or)`
                    `python client.py -n your_name`
<br>
```
python client.py --name ali
```

6\. Once\, you enter the command\, you get list of numeric choice to chose to request quotes from the server that we have set up earlier\.

<br>
7\. You can stop the server by sending request as "stop"\.
![ss3.PNG](/images/ss3.PNG)  