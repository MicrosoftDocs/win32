---
title: CiWebhitsFile
description: CiWebhitsFile
ms.assetid: 107449eb-e443-40bb-81d6-bd2066be76bf
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CiWebhitsFile

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Format: **CiWebhitsFile**=*virtual\_path*

Specifies the virtual path of the document to be hit highlighted. This parameter is required.

> [!Note]  
> The Secure Sockets Layer (SSL) setting for the Webhits template (.htw file) and the setting for **CiWebhitsFile** must be the same, or else the **CiWebhitsFile** must have a setting of 0. If this is not the case, Webhits will fail with an appropriate error message.

 

If your site requires all documents to be accessed only with SSL, be sure to set the same SSL access on the .htw file. If your site has some documents with SSL access required and others with no SSL access required, set the SSL access on the .htw file to be the same as those that require SSL access. Alternatively, you can create two .htw files (one for each type of document).

 

 




