---
title: To move topics to the root during compile
description: To move topics to the root during compile
ms.assetid: 'C02A6FC9-7095-4645-B768-13EC44DA3834'
---

# To move topics to the root during compile

1.  Open a project (.hhp) file, click **Change Project Options**, and then click the **Compiler** tab.

    

    |                        |                                                                          |
    |------------------------|--------------------------------------------------------------------------|
    | ![](images/sb-cpo.gif) | Specifies files, compiler, window, and other project settings<br/> |

    

     

2.  Select the **Don't include folders in compiled file** check box.

## Notes

-   This procedure consolidates your compiled help file by removing all unnecessary references to folders. All URL references in the project are updated to reflect the new file location.
-   File naming is important when using this feature. Files in different folders that have the same name will not compile properly when consolidated at the root.

## Related topics

<dl> <dt>

[About Compiling a Help Project](compile-a-help-project.md)
</dt> </dl>

 

 





