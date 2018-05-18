---
title: Parameters from Internet Data Query Files
description: Parameters from Internet Data Query Files
ms.assetid: 'db0c59fe-a14e-4745-89ec-5d40280a5821'
---

# Parameters from Internet Data Query Files

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A number of predefined parameters are supplied, which can be set in the Internet Data Query (.idq) files. See [Variables in .htx and .idq Files](variables-in-idq-and-htx-files.md).

In addition, any Common Gateway Interface (CGI) variable, form parameter, or variable defined in an .idq file can be referred to in the HTML extension file by enclosing the variable name in &lt;% and %&gt;. If a variable is referred to that has not been assigned a value, the variable reference will be sent unchanged.

 

 




