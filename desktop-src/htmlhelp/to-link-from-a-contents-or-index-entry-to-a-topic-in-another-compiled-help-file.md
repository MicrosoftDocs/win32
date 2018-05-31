---
title: To link from a contents or index entry to a topic in another compiled help file
description: To link from a contents or index entry to a topic in another compiled help file
ms.assetid: 65CE6829-C91B-45bf-B123-2934CA9B6463
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To link from a contents or index entry to a topic in another compiled help file

1.  Open a contents (.hhc) or index (.hhk) file, and then click **Add** if you are adding a new entry or **Edit** if you are changing an existing one.
2.  In the **File or URL** box, add the following syntax:

    ```
    ms-its:file name.chm::/topic.htm
    ```

    

    where file name.chm is the name of the compiled help file and topic.htm is the name of the HTML file to which you want to link.

Make sure that the compiled help file you want to link to is located in the same directory as the file you are linking from.

## Notes

-   The MS-ITS protocol works with Microsoft Internet Explorer 4.0 or later. If your users have Internet Explorer 3.0 installed, they need to use the following protocol, which also works with later versions of the browser: mk:@MSITStore:file name.chm::/topic.htm.
-   If you want to link to a compiled help file that is located in a directory on the Web, you need to provide the full URL including the HTTP address. For example, ms-its:http://www.sample.com/file name.chm::/topic.htm.

## Related topics

<dl> <dt>

[About Creating a Link to Another Compiled Help File](creating-links-to-other-help-files.md)
</dt> </dl>

 

 




