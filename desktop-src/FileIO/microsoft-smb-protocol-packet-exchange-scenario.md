---
description: Example of a Microsoft SMB Protocol packet exchange between a client and a server.
ms.assetid: f831d0de-0e38-4141-811c-892a1b5c4037
title: Microsoft SMB Protocol Packet Exchange Scenario
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft SMB Protocol Packet Exchange Scenario

This topic gives an example of a Microsoft SMB Protocol packet exchange between a client and a server. The following steps are an overview of the process:

1.  The client and server establish a NetBIOS session.
2.  The client and server negotiate the Microsoft SMB Protocol dialect.
3.  The client logs on to the server.
4.  The client connects to a share on the server.
5.  The client opens a file on the share.
6.  The client reads from the file.

First, a full-duplex TCP connection is established by the client with the server. Then the client builds and sends a NetBIOS session request packet over the TCP connection. If the packet was formatted correctly, the server then returns a packet that contains a message acknowledging that the session has been established. After this, the client sends the first Microsoft SMB Protocol packets to the server.



|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Packet 1:  SMB\_COM\_NEGOTIATE**<br/> **Direction:** Client to server<br/> **Description:** The client requests that the server negotiate the Microsoft SMB Protocol dialect. A list of strings identifying the dialects that the client can work with is included in the packet.<br/>                                                                                                                                                                                                                                                                                                                                   |
| **Packet 2:  SMB\_COM\_NEGOTIATE**<br/> **Direction:** Server to client<br/> **Description:** The server responds to the client's request to identify the Microsoft SMB Protocol dialect that is going to be used in the session. The returned packet also includes an 8-byte random string that will be used in the next step to authenticate the client during the logon process.<br/>                                                                                                                                                                                                                                   |
| **Packet 3:  SMB\_COM\_SESSION\_SETUP\_ANDX**<br/> **Direction:** Client to server<br/> **Description:** This packet includes information about client capabilities, so this packet must be sent even if the server has implemented only share-level security.<br/> **Packet 3:  SMB\_COM\_SESSION\_SETUP\_ANDX**<br/> **Direction:** Server to client<br/> **Description:** If the challenge/response is accepted by the server, a valid UID is included in the packet that is returned to the client. If it is not accepted, the server will return an error code in this packet and deny access.<br/> |
| **Packet 4:  SMB\_COM\_TREE\_CONNECT\_ANDX**<br/> **Direction:** Client to server<br/> **Description:** The client requests access to the share. The packet contains the fully specified path of the share in UNC format.<br/>                                                                                                                                                                                                                                                                                                                                                                                             |
| **Packet 5:  SMB\_COM\_TREE\_CONNECT\_ANDX**<br/> **Direction:** Server to client<br/> **Description:** If access to the share is granted, then the server returns the 16-bit tree ID (TID) that corresponds to the share in this packet. If the share does not exist or the user has insufficient credentials to access the share, the server will return an error code in this packet and deny access to the share.<br/>                                                                                                                                                                                                 |
| **Packet 6:  SMB\_COM\_OPEN\_ANDX**<br/> **Direction:** Client to server<br/> **Description:** The client requests the server to open a file on the accessed share on behalf of the client. This packet contains the name of the file to be opened.<br/>                                                                                                                                                                                                                                                                                                                                                                   |
| **Packet 7:  SMB\_COM\_OPEN\_ANDX**<br/> **Direction:** Server to client<br/> **Description:** If access to the file is granted, then the server returns the file ID of the requested file. If the file does not exist or the user has insufficient credentials to access the file, the server will return an error code in this packet and deny access to the file.<br/>                                                                                                                                                                                                                                                  |
| **Packet 8:  SMB\_COM\_READ\_ANDX**<br/> **Direction:** Client to server<br/> **Description:** The client requests the server to read data from the opened file on behalf of the client and return this data to the client. The file ID that is obtained by the client when the file was opened is included in this packet in order to identify which opened file the server should read data from.<br/>                                                                                                                                                                                                                   |
| **Packet 9:  SMB\_COM\_READ\_ANDX**<br/> **Direction:** Server to client<br/> **Description:** The server returns the requested file data in this packet. An error here is unlikely given that access to the server, share, and file has been granted. It can happen in some situations, however: for example, if access to a share is changed between the time the file is opened and the time it is read from.<br/>                                                                                                                                                                                                      |



 

> [!Note]  
> If you implement a CIFS that does not support change notifications, Windows cannot keep an outstanding handle to the file system, and the SMB connection can go away without notice.

 

 

 




