---
Description: Some protocols require multiple authentication messages.
ms.assetid: b4c4c38c-0286-49b1-b93d-4c6b885fe0f6
title: Client Continuation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Client Continuation

Some protocols require multiple authentication messages. In this case, the client parses the response from the server and calls [**InitializeSecurityContext (General)**](/windows/desktop/api/Sspi/) again using the continue status from the previous call. The client checks the return status from this call and might be required to continue for additional legs. It uses the information in *pOutput* to construct a message and sends it to the server.

 

 



