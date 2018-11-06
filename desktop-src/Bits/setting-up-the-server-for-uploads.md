---
title: Setting Up the Server for Uploads
description: To upload files to a server using BITS, the server must have IIS and the BITS server extension ISAPI installed. For IIS requirements, see IIS Requirements for BITS Uploads.
ms.assetid: 2f3a2f99-b9de-41da-897f-a4d9c6d5e8c0
ms.topic: article
ms.date: 05/31/2018
---

# Setting Up the Server for Uploads

To upload files to a server using BITS, the server must have IIS and the BITS server extension ISAPI installed. For IIS requirements, see [IIS Requirements for BITS Uploads](iis-requirements-for-bits-uploads.md).

For information on configuring the IIS virtual directory that BITS uses for uploads, see the following topics.

-   [Setting Permissions on Virtual Directories](setting-permissions-on-virtual-directories.md)
-   [Writing a Script to Configure the Virtual Directory](writing-a-script-to-configure-the-virtual-directory.md)
-   [Using the IIS UI to Configure the Virtual Directory](using-the-iis-ui-to-configure-the-virtual-directory.md)
-   [Preventing Multiple Uploads](preventing-multiple-uploads.md)
-   [Upload Best Practices](upload-best-practices.md)

> [!Note]  
> Some IIS installations include the UrlScan filtering component. If UrlScan is enabled, the administrator must add the "BITS\_POST" verb to UrlScan's list of allowed HTTP verbs. Otherwise, BITS client uploads will fail. For further details on enabling verbs in UrlScan, see the UrlScan documentation.

 

 

 




