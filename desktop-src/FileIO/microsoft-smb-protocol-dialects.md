---
description: To establish a connection between a client and a server using Microsoft SMB Protocol, you must first determine the dialect with the highest level of functionality that both the client and server support.
ms.assetid: ad48391b-fcc7-4e58-83bb-6084503c8d61
title: Microsoft SMB Protocol Dialects
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft SMB Protocol Dialects

The list of Microsoft SMB Protocol message packets has grown over the years to accommodate the increasing functionality of Microsoft SMB Protocol, and now numbers in the hundreds. Each stage of its growth is marked by a standard packet set, or dialect. Each dialect is identified by a standard string such as "PC NETWORK PROGRAM 1.0", "MICROSOFT NETWORKS 3.0", "DOS LANMAN 2.1", or "NT LM 0.12". The first string identifies the first dialect of SMB, and the last string identifies CIFS, the first dialect of Microsoft SMB Protocol.

Most Windows clients support at least six different dialects of Microsoft SMB Protocol, so one of the first steps in establishing a connection between a client and a server using Microsoft SMB Protocol is to determine the dialect with the highest level of functionality that both the client and server support. This process is known as "negotiating the dialect." The dialect strings mentioned above are included in the dialect negotiation request and response packets for this purpose.

 

 



