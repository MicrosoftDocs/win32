---
title: Linking Between Merged Help Files
description: You need to use a special link when linking between merged compiled help (.chm) files.
ms.assetid: '84EF69C8-4062-4eb1-95ED-8249AAB3D6BA'
---

# Linking Between Merged Help Files

You need to use a special link when linking between merged compiled help (.chm) files.

## To link between merged help files

1.  Open the HTML file you want to link from.
2.  Create a link using the following syntax:

    ```
    <A HREF="ms-its:file name.chm::/topic.htm">
    ```

    

    where file name.chm is the name of the merged compiled help file and topic.htm is the name of the HTML file to which you want to link.

## Notes

-   The MS-ITS protocol works with Microsoft Internet Explorer 4.0 or later. If your users are running Internet Explorer 3.0, they need to use the following protocol, which also works with later versions of the browser: mk:@MSITStore:file name.chm::/topic.htm.
-   The merge occurs at run time, which is when the compiled help (.chm) file is opened. Because of this, all merged compiled help files must be shipped with the main compiled help file, and all must be located in the same directory.

## Related topics

<dl> <dt>

[About Merging Help Files at Run Time](merging-help-files-at-run-time.md)
</dt> </dl>

 

 




