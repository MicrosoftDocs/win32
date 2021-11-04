---
description: User Agent String
ms.assetid: 'bcf0a534-c123-40c4-91b4-645c4912f31a'
title: User Agent String
ms.topic: article
ms.date: 05/31/2018
---

# User Agent String

The *User Agent String* contains information about a browser's identity. The User Agent String is reported to the web server as an HTTP header every time that a browser makes a request to a web server. You can also access it through a client-side script. For example, you can display the User Agent String by typing the following URL into the Windows Internet Explorer 8 address bar: "javascript:alert(navigator.userAgent)". The following illustration shows the typical resulting dialog box from Internet Explorer 8 running on Windows 7.

![screen shot of the internet explorer diaog box that has the user agent string](images/useragent-alert.png)

Typically, the User Agent String is parsed specifically for the MSIE substring. Based on the reported version of the browser, the client-side or server-side programming logic takes a different action. For more information about the User Agent String, see [What Will Windows Internet Explorer Report as the User-Agent String?](/previous-versions/cc817582(v=msdn.10)) in the MSDN Library.

## Related topics

<dl> <dt>

[Fixing Compatibility Issues in Web Applications by Using Compatibility View](remediating-web-applications-and-add-ons.md)
</dt> </dl>

 

 



