---
title: To merge multiple help files at run time
description: To merge multiple help files at run time
ms.assetid: '5C815B74-EFBE-4190-A8B9-1240157C1CCB'
---

# To merge multiple help files at run time

1.  Open a project (.hhp) file, and then click **Change Project Options**.

    

    |                        |                                                                          |
    |------------------------|--------------------------------------------------------------------------|
    | ![](images/sb-cpo.gif) | Specifies files, compiler, window, and other project settings<br/> |

    

     

2.  On the **Merge Files** tab, click **Add**.
3.  In the **Specify the name of the file to merge** box, enter the appropriate file name.

## Notes

-   The merge occurs at run time, which is when the compiled help (.chm) file is opened. Because of this, all merged compiled help files must be shipped with the main compiled help file, and all must be located in the same directory.
-   This procedure merges the index, Keyword links (KLinks), Associative links (ALinks), and full-text search information from multiple compiled help files. Unified index and search information appears in the Navigation pane of the Help Viewer.
-   If you also want a unified table of contents, you must [create a contents file that links to other contents files](creating-links-from-one-contents-file-to-another.md).
-   The merge feature will not work if you compile a help file and [set the compatibility to version 1.0](htmlhelp.to_compile_a_project_compatible_with_html_help_version_1.0).
-   There are special considerations when [linking between merged help files](linking-between-merged-help-files.md).

## Related topics

<dl> <dt>

[About Merging Help Files at Run Time](merging-help-files-at-run-time.md)
</dt> </dl>

 

 





