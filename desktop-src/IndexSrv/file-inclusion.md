---
title: File Inclusion
description: File Inclusion
ms.assetid: 8320d2a8-36a7-4b7b-864e-c46945832630
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# File Inclusion

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The &lt;%include%&gt; keyword can interpolate the contents of a file into the .htx file. The syntax of the construct is

``` syntax
<%include filename%> 
```

where *filename* is the name of the file to be included. The file is named with a full virtual path name, and HTML extension constructs are interpreted if found in the file. File includes can be nested, but the total number of include files cannot exceed 31.

 

 




