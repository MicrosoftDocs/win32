---
title: To link from a topic in a WinHelp file to a topic in an HTML Help file
description: To link from a topic in a WinHelp file to a topic in an HTML Help file
ms.assetid: '2CCA58B5-E181-4d1b-8155-D78A29302E6F'
---

# To link from a topic in a WinHelp file to a topic in an HTML Help file

Open the appropriate WinHelp topic and add the following macro syntax to the link:


```
!execfile(hh.exe, ms-its:file name.chm::/topic.htm)
```



where !execfile is the name of the WinHelp macro, hh.exe is the HTML Help executable file, file name.chm is the name of the compiled help file and topic.htm is the name of the HTML file.

Make sure that the compiled help (.chm) file you want to link to is located in the same directory as the WinHelp file you are linking from.

## Notes

-   If you do not need to link to a specific topic in the HTML Help file, omit ::/topic.htm from the syntax.
-   Using the !if macro, you can also check the return value of the !execfile macro and display an alternate topic if the compiled help file could not be loaded.
-   The MS-ITS protocol works with Microsoft Internet Explorer 4.0 or later. If your users have Internet Explorer 3.0 installed, they need to use the following protocol, which also works with later versions of the browser: mk:@MSITStore:file name.chm::/topic.htm.
-   If you want to link to a compiled help file that is located in a directory on the Web, you need to provide the full URL including the HTTP address. For example, ms-its:http://www.sample.com/file name.chm::/topic.htm.

## Related topics

<dl> <dt>

[About Creating a Link to Another Compiled Help File](creating-links-to-other-help-files.md)
</dt> </dl>

 

 




