---
description: A version vector processes conditional comments in an HTML webpage. That is, version vectors enable you to create markup based on the browser version.
ms.assetid: 526080CD-CE76-48B8-AEBC-6A135FD95BB0
title: Version Vectors
ms.topic: article
ms.date: 05/31/2018
---

# Version Vectors

A *version vector* processes conditional comments in an HTML webpage. That is, version vectors enable you to create markup based on the browser version.

Consider the following code example.


```HTML
<!-[if gte IE 5.5]
   <p>you are using IE5 or higher</p>
<![endif]->
<!-[if IE6]
   <linkrel=”stylesheet” type=”text/css” href=”/stylesheets/ie6.css”/>
<![endif]->
<!-[if IE7]
   <linkrel=”stylesheet” type=”text/css” href=”/stylesheets/ie7.css”/>
<![endif]->
<!-[if gte IE8]
   <linkrel=”stylesheet” type=”text/css” href=”/stylesheets/standards.css”/>
<![endif]->
```



In this case, if the Windows Internet Explorer browser version is at least 5.5, the corresponding paragraph is displayed in the webpage. Although the first condition in this example illustrates the function of conditional comments, these comments are not typically used to display markup like the first condition. Instead, the remaining conditional comments in the previous example are more common. In these remaining comments, the conditional comments use a different style sheet for each different version of the browser.

The preceding code example also checks for equality for Microsoft Internet Explorer 6 and Windows Internet Explorer 7. But for Windows Internet Explorer 8, the example uses the gte operator (greater than or equal). This operator helps future-proof the example so that the most standards-compliant version of the style sheet is used when a new version of the browser is released (instead of using the wrong style sheet or no style sheet). Existing applications often do not consider a version of Internet Explorer past 7 (or the newest version of Internet Explorer that the site is built for). For more information about version vectors, see [Version Vectors](/previous-versions/cc817577(v=msdn.10)) in the MSDN Library.

## Related topics

<dl> <dt>

[Fixing Compatibility Issues in Web Applications by Using Compatibility View](remediating-web-applications-and-add-ons.md)
</dt> </dl>

 

 



