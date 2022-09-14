---
title: Configuring RPC for SPX/IPX
description: When using the ncacn\_spx and ncadg\_ipx transports, the server name is exactly the same as the server name on Windows.
ms.assetid: b2543046-8cdc-4cba-94e4-40188701fad3
ms.topic: article
ms.date: 05/31/2018
---

# Configuring RPC for SPX/IPX

When using the **ncacn\_spx** and **ncadg\_ipx** transports, the server name is exactly the same as the server name on Windows. However, since the names are distributed using Novell protocols, they must conform to the Novell naming conventions. If a server name is not a valid Novell name, servers will not be able to create endpoints with the **ncacn\_spx** or **ncadg\_ipx** transports.

A valid Novell server name contains only the characters between 0x20 and 0x7f. Lowercase characters are changed to uppercase. The following characters cannot be used:

"\*,./:;<=>?\[\]\\\|\]

To maintain compatibility with the first version of Windows NT, **ncacn\_spx** and **ncadg\_ipx** also enable you to use a special format of the server name known as the tilde name. The tilde name consists of a tilde (~), followed by the server's eight-digit network number, and then followed by its 12-digit Ethernet address. Tilde names have an advantage in that they do not require any name service capabilities. Thus, if you are connected to a server, the tilde name will work.

The following tables contain two sample configurations that illustrate the points previously described.



| Component                            | Configured as      |
|--------------------------------------|--------------------|
| Windows server                       | NWCS               |
| Windows client                       | NWCS               |
| 16-bit Windows client, MS-DOS client | NetWare Redirector |



 

The configuration in the previous table requires that you have NetWare file servers or routers on your network. It will produce the best performance because the server names are stored in the NetWare Bindery.



| Component                            | Configured as |
|--------------------------------------|---------------|
| Windows server                       | SAP Agent     |
| Windows client                       | IPX/SPX       |
| 16-bit Windows client, MS-DOS client | IPX/SPX       |



 

The second configuration works in an environment that does not contain NetWare file servers or routers (for example, a network of two computers: a Windows server and an MS-DOS client). Name resolution, which is accomplished during the first call over a binding handle, will be slightly slower than in the first configuration. In addition, the second configuration results in more traffic generated over the network.

To implement name resolution, when an RPC server uses an SPX or IPX endpoint, the server name and endpoint are registered as a Service Advertising Protocol (SAP) server of type 640 (hexadecimal). To resolve a server name, the RPC client sends a SAP request for all services of the same type, and then scans the list of responses for the name of the server. This process occurs during the first RPC call over each binding handle. For additional information on the SAP protocol for Novell, see your NetWare documentation.

> [!Note]  
> The 16-bit Windows client applications that use the **ncacn\_spx** or **ncadg\_ipx** transports require that the file Nwipxspx.dll be installed in order to run under the WOW subsystem. Contact Novell to obtain this file.

 

 

 




