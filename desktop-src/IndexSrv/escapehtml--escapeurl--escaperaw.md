---
title: EscapeHTML, EscapeURL, EscapeRAW
description: EscapeHTML, EscapeURL, EscapeRAW
ms.assetid: 0fe2de82-d05f-41aa-a2db-710ffa9b19e0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EscapeHTML, EscapeURL, EscapeRAW

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The &lt;%EscapeHTML%&gt;, &lt;%EscapeURL%&gt;, and &lt;%EscapeRAW%&gt; keywords can be used to affect the formatting of output strings. These are typically used with [variables](variables-in-forms-and-in-idq-files.md) such as CiRestriction or with CiScope when used in a form or in an anchor.

The output of variables is normally suitable for HTML format. The preceding keywords affect the output format so that the variable can be used correctly in different contexts. The form of the construct is:


```
<%EscapeHTML variable%>     or
<%EscapeURL variable%>      or
<%EscapeRAW variable%>
```



where *variable* is any parameter or variable that could be used in the HTTP Extension file. Constant values can also be used, as in, &lt;%EscapeURL /scripts/query.idq%&gt;.

&lt;%EscapeHTML%&gt; (the default formatting) is used to escape characters that are meaningful in HTML. For example, the symbol &gt; will appear as &gt;.

&lt;%EscapeURL%&gt; is used to do standard escaping for strings that will be URLs (as in the HREF tag of an anchor). For example, the string @size &gt; 10000; will appear as %40size+%3E+10000.

&lt;%EscapeRAW%&gt; is used when no escaping should be done. This might be the case for a variable that is being used as the value of a form variable, or to have the value of a variable that contains HTML code to be interpreted correctly.

 

 




