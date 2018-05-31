---
title: To automatically generate a table of contents
description: To automatically generate a table of contents
ms.assetid: 0CA471F1-6110-4cc4-9DEB-5D40CB83B469
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To automatically generate a table of contents

1.  Open a project (.hhp) file.
2.  Click **Change Project Options**, and then click the **Files** tab. 

    |                        |                                                                            |
    |------------------------|----------------------------------------------------------------------------|
    | ![](images/sb-cpo.gif) | Specifies files, compiler, window, and other project settings. <br/> |

    

     

3.  Click **Browse**, next to the **Contents file** box, and then locate the folder that you want to store your contents file in.
4.  In **File name** box, type a name (using .hhc for the file name extension) for your contents file.
5.  Click **Open**. The name of your contents file and the full path appear in the **Contents file** box.
6.  Select the **Automatically create contents file (.hhc) when compiling** check box.
7.  In the **Maximum head level** box, click the maximum heading level you want entries generated for in your contents file. For example, if you click **3** for the maximum head level, entries will be generated with &lt;H1&gt;, &lt;H2&gt;, and &lt;H3&gt; heading tags.

## Note

If you make changes to a contents file that has been automatically generated, you will lose them if you compile the project again. To prevent this, make sure the **Automatically create contents file when compiling** check box is cleared before you recompile.

## Related topics

<dl> <dt>

[About Creating Table of Contents Files](create-a-table-of-contents-file.md)
</dt> </dl>

 

 





