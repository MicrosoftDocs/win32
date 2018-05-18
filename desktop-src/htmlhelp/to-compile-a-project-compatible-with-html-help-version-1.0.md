---
title: To compile a project compatible with HTML Help version 1.0
description: To compile a project compatible with HTML Help version 1.0
ms.assetid: '35E7F6D0-A88B-4d1d-BF9C-F145860D4C19'
---

# To compile a project compatible with HTML Help version 1.0

1.  Open a project (.hhp) file, click **Change Project Options**, and then click the **Compiler** tab. 

    |                        |                                                                           |
    |------------------------|---------------------------------------------------------------------------|
    | ![](images/sb-cpo.gif) | Specifies files, compiler, window, and other project settings.<br/> |

    

     

2.  In the **Compatibility** box, click **1.0**.

## Notes

-   This option is useful if you are recompiling files that you created for previous versions of Microsoft Internet Explorer or HTML Help.
-   Setting the version to 1.0 creates a [site map rather than a binary version](the-difference-between-binary-and-site-map-indexes.md) of the index when the project file is compiled. It also disables the merge feature. If more than one compiled help file is referenced, indexes, Keyword links (KLinks), Associative links (ALinks), and full-text search lists are not merged.

## Related topics

<dl> <dt>

[About Compiling a Help Project](compile-a-help-project.md)
</dt> </dl>

 

 





