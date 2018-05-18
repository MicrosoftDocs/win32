---
title: IISAdmin Sample
description: IISAdmin Sample
ms.assetid: 'a7a849df-dd6f-44c9-94eb-5d9d03c54e94'
---

# IISAdmin Sample

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The IISAdmin sample is a set of HTML and ASP forms that demonstrates how to use IIS to administer Indexing Service. The forms retrieve indexing statistics, force a master merge, rescan paths, and check for documents that could not be filtered.

Source: mssdk\\samples\\winbase\\indexing\\IISAdmin\\

**To install the sample files**

1.  Open a command window and change the directory to the source path of the sample.
2.  At the command-line prompt, type "install".

> [!Note]  
> The sample files are copied to the directory %windir%\\system32\\inetsrv\\iisadmin\\isadmin.

 

**To use the sample forms**

1.  Start Microsoft Internet Explorer.
2.  Enter the URL "http://localhost/iisadmin/isadmin/admin.htm".
3.  In the left frame, select the desired administration operation.

### Programming Notes

The forms in the IISAdmin sample require that IIS be running.

The main sample form is admin.htm, which controls all the administrative operations.

 

 




