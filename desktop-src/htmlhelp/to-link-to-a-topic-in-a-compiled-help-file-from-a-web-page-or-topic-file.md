---
title: To link to a topic in a compiled help file from a Web page or topic file
description: To link to a topic in a compiled help file from a Web page or topic file
ms.assetid: 49457E11-C506-4999-BAC6-9A386B940C10
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To link to a topic in a compiled help file from a Web page or topic file

To link to a topic in a compiled help file that is located on an Internet or intranet Web site, create a link using the following syntax:


```
<A HREF="ms-its:http://www.sample.com/filename.chm::/topic.htm>Link Text Here</a>.
```



This will work on any HTML Web page or help topic.

To link to a topic in a compiled help file that is stored on a local computer, create a link using the following syntax:


```
<A HREF="ms-its:C:\filename.chm::/topic.htm">Link Text Here</a>
```



The complete local path must be specified. In this example, the target file is located on the root of the C:\\ drive.

In these examples, filename.chm is the name of the compiled help file and topic.htm is the name of the topic to which you want to link.

## Notes

-   Use this procedure if you want to pull a single topic from a compiled help file. You can also create a link that will [download the entire help file](running-a-compiled-help-file-from-the-web.md).
-   The MS-ITS protocol works with Microsoft Internet Explorer 4.0 or later. If your users are running Internet Explorer 3.0, they need to use the following protocol, which also works with later versions of the browser: mk:@MSITStore:file name.chm::/topic.htm.

## Related topics

<dl> <dt>

[About Creating a Link to Another Compiled Help File](creating-links-to-other-help-files.md)
</dt> </dl>

 

 




