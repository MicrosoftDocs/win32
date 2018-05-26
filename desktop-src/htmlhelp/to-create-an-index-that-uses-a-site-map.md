---
title: To create an index that uses a site map
description: To create an index that uses a site map
ms.assetid: 08C48181-6224-4c69-B3CC-EC5B84BBE3AA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To create an index that uses a site map

1.  On the **File** menu, click **New**, and then click **Index**.
2.  [Add keywords](to-add-a-keyword-to-an-index-file.md), and then save the index file.

## Notes

-   To work on a Web site this file does not need to be compiled. If you compile it (for use in a compiled help file), and want to use the site map format, open your project file, and then click **Change Project Options**. Click the **Compiler** tab, and then clear the **Create a binary index** check box.

    

    |                        |                                                                           |
    |------------------------|---------------------------------------------------------------------------|
    | ![](images/sb-cpo.gif) | Specifies files, compiler, window, and other project settings.<br/> |

    

     

-   If you are authoring an [index for a Web site](the-difference-between-binary-and-site-map-indexes.md), make sure you [add the HTML Help ActiveX control](inserting-the-html-help-activex-control.md) to the topic files you want the index to appear in. Specify as the command, and then specify the name and location for your index file.
-   An index compiled using the binary format will not work on a Web site. You can use a site map index for both a Web site and a compiled help file.
-   If you compile a help file and [set the compatibility to version 1.0](htmlhelp.to_compile_a_project_compatible_with_html_help_version_1.0), a site map index will be created.

## Related topics

<dl> <dt>

[About Creating Index Files](create-an-index-file.md)
</dt> </dl>

 

 





