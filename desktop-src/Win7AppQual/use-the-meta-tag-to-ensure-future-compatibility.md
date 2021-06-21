---
description: Use the Meta Tag to Ensure Future Compatibility
ms.assetid: 254A1C0D-B24B-4014-8D15-662FC7F2AB81
title: Use the Meta Tag to Ensure Future Compatibility
ms.topic: article
ms.date: 05/31/2018
---

# Use the Meta Tag to Ensure Future Compatibility

Windows Internet Explorer 8 enables you to control document compatibility modes, so you can instruct the browser to render webpages in the same way as older browser versions. You can also choose when to update the webpage, while it continues to be usable and function correctly.

## Setting the Meta Element

The **meta** element includes a **content** attribute that enables you to specify the mode that content is rendered in for the webpage, as the following table shows.



| Value | Rendering mode                                                 |
|-------|----------------------------------------------------------------|
| IE=9  | Use the Windows Internet Explorer 9 standards rendering mode   |
| IE=8  | Use the Internet Explorer 8 standards rendering mode           |
| IE=7  | Use the Windows Internet Explorer 7 standards rendering mode   |
| IE=5  | Use the Microsoft Internet Explorer 5 standards rendering mode |



 

For more information about compatibility and the X-UA-Compatible header, see [Defining Document Compatibility](/previous-versions/windows/internet-explorer/ie-developer/compatibility/cc288325(v=vs.85)) in the MSDN Library.

The following code example demonstrates how to force a webpage to be rendered in Internet Explorer 8 mode.


```HTML
<html>
   <head>
   <!-- Mimic Internet Explorer 8 -->
      <title>My Web Page</title>
      <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE8" />
   </head>
   <body>
      <p>Content goes here.</p>
   </body>
</html>
```



## Using an HTTP Header

Many websites contain thousands (or tens of thousands) of individual webpages so setting the **meta** element on each document is impractical. If you want to set the **meta** element for all pages or a collection of pages that are selected by folder, you can adjust your server configuration instead and add the X-UA-Compatible metadata in the [HTTP header](/previous-versions/cc817572(v=msdn.10)).

For sites that require different **meta** element values for pages on the same server, there are several tools that automatically generate and insert the appropriate **meta** element for you. For example, the [ArtinSoft Web Tools](https://www.mobilize.net/what-is-aggiorno-ie8-compatibility-tagging.aspx) utility from Aggiorno inserts and removes the Internet Explorer 8 compatibility tag feature and can help your site meet specific compatibility standards.

## Related topics

<dl> <dt>

[Fixing Compatibility Issues in Web Applications by Using Compatibility View](remediating-web-applications-with-compatibility-view.md)
</dt> </dl>

 

 
