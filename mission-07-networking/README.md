# Mission 7 — How Computers Communicate

### Task 7.1 — Explain network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | Local Area Network connects devices within a small geographical area. | Home Wi-Fi or computer lab. |
| MAN | Metropolitan Area Network connects networks across a city or large campus. | A city-wide network. |
| WAN | Wide Area Network connects networks over large geographical areas. | The Internet. |
| DNS | Domain Name System translates domain names into IP addresses. | Resolving example.com. |
| Router | A router connects different networks and forwards data between them. | Home Wi-Fi router. |
| Protocol | A protocol is a set of rules used for communication between devices. | HTTP and HTTPS. |
| Packet switching | Data is divided into smaller packets that travel through a network. | Sending information over the Internet. |
| Client-server | A client requests a service and a server provides it. | A browser requesting a webpage. |

### Task 7.2 — Observe network information

I used Terminal to test network connectivity and perform a DNS lookup.

Commands:

```bash
ping -c 4 example.com
nslookup example.com
```

**1. What does a connectivity test help check?**

A connectivity test checks whether my computer can communicate with another device or server over a network. It can also provide information about response time and packet loss.

**2. What information does a DNS lookup display?**

A DNS lookup displays information about a domain name, including the IP address associated with it when available.

**3. What is the role of DNS when entering a website name?**

DNS helps translate a human-readable website name into an IP address so that the computer can locate the correct server.

**My observation:**

- Ping result: [Write whether you received replies or experienced timeouts.]
- DNS result: [Write whether nslookup returned an address.]

### Task 7.3 — What happens when you open a website?

1. The user enters a website address into a web browser. The browser acts as the client.
2. The computer checks DNS to translate the domain name into an IP address.
3. The computer sends a request through the network and router towards the destination server.
4. The client and server communicate using network protocols such as HTTPS.
5. The web server receives the request and processes it.
6. The server sends the requested information back to the client.
7. The browser processes the response and displays the website to the user.





