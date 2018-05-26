---
title: Example Create a New Window Using JavaScript
description: Example Create a New Window Using JavaScript
ms.assetid: 1932EE4C-D99A-4c3a-9DFC-6486E341842A
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Example: Create a New Window Using JavaScript

You can use JavaScript to launch a new window (an instance of Internet Explorer). The code in this example can be used on both standard Web pages and within compiled help (.chm) files.

Create the link as follows:


```
<A HREF= "#" onClick="window.open('examples/sample.htm',
  'Sample','toolbar=no,width=190,height=190,left=500,top=200, 
  status=no,scrollbars=no,resize=no');return false">
See the sample</A>.
```



where examples/sample.htm is the path to the file that will appear in the new window, "Sample" is the *name* argument for the new window, and the remaining values are the attributes for the pop-up window (width and height in pixels, toolbar, scroll bar, status bar, and resize). These attributes are separated by commas, and the entire line is enclosed in single quotes.

## Notes

-   The hashmark ("\#") character ensures that the state of the current help window will be retained. return false prevents the hashmark from appearing in the location field of the main window, which would interfere with the functionality of the Back and Forward buttons.
-   All of the code must be on the same line or it will not work. The lines in this example are broken for legibility.
-   When working with compiled help (.chm) files, all HTML files referred to by this code must be included in your project before compiling. Also, because the compiler can only include graphics files in **&lt;IMG&gt;** tags, it will miss any graphics files that are included in this script. If you use this script in a compiled help file, make it point to an HTML file rather than a graphics file.

## Related topics

<dl> <dt>

[About the Script and DHTML Examples](script-and-dhtml-examples.md)
</dt> </dl>

 

 




