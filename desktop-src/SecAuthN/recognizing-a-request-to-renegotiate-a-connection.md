---
Description: The DecryptMessage (General) function traps requests for renegotiation coming from the message sender. It notifies your application by decrypting the message data and returning the SEC\_I\_RENEGOTIATE value.
ms.assetid: 036a93dc-7f52-42f8-945d-7f654289ef63
title: Recognizing a Request to Renegotiate a Connection
ms.topic: article
ms.date: 05/31/2018
---

# Recognizing a Request to Renegotiate a Connection

The [**DecryptMessage (General)**](https://msdn.microsoft.com/en-us/library/Aa375211(v=VS.85).aspx) function traps requests for renegotiation coming from the message sender. It notifies your application by decrypting the message data and returning the SEC\_I\_RENEGOTIATE value.

Your application must handle such requests by calling [**AcceptSecurityContext (General)**](https://msdn.microsoft.com/en-us/library/Aa374703(v=VS.85).aspx) (servers) or [**InitializeSecurityContext (General)**](https://msdn.microsoft.com/en-us/library/Aa375506(v=VS.85).aspx) (clients) and passing the contents of SECBUFFER_EXTRA returned from DecryptMessage in the SECBUFFER_TOKEN. After this initial call returns a value, proceed as though your application were creating a new connection.

 

 



