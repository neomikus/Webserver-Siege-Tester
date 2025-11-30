<h1>📝 Webserver-Siege-Tester 📝</h1>
Tester battery made in Python 3.14 for <a href="https://www.42network.org/">42 School</a> project <a href="https://www.github.com/neomikus/42-Webserv">Webserv</a>, using GNU Siege as testing tool

<h2>🔎 Tests featured 🔎 (WIP)</h2>
<b>Basic tests (Only checking server availaibility)</b>

- GET:
    - [x] Small (2 seconds/10 connections)
    - [x] Medium (5 seconds/200 connections)
    - [x] Big (10 seconds/1000 connections)
    - [ ] Medium Internet (5 seconds/500 connections simulating internet)
    - [ ] Big Internet (10 seconds/1000 connections simulating internet)
  
- POST:
    - [ ] No content (10 seconds/1000 connections with no content in body)
    - [ ] Form data (10 seconds/1000 connections with form data as content)
    - [ ] Small files (10 seconds/500 connections with multipart form data as content)
    - [ ] Big files (10 connection/1 request per connection with big multipart form data as content)

- DELETE:
    - [ ] Small (2 seconds/10 connections)
    - [ ] Medium (5 seconds/200 connections)
    - [ ] Big (10 seconds/1000 connections)
    - [ ] Medium Internet (5 seconds/500 connections simulating internet)
    - [ ] Big Internet (10 seconds/1000 connections simulating internet)

<b>Performance tests (Average response time/Transaction rate)</b>

Planned but not implemented!

<h2>🛠️ Usage 🛠️</h2>
Not implemented yet!
