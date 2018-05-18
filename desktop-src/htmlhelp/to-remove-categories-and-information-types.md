---
title: To remove categories and information types
description: To remove categories and information types
ms.assetid: '9A00B2C8-9E75-4bc7-92D9-F61F059B63A0'
---

# To remove categories and information types

1.  Open the project (.hhp) file in a text editor, such as Microsoft Notepad, and delete the \[INFOTYPES\] section.
2.  In a text editor, open the contents (.hhc) file that contains the categories or information types you want to remove.
3.  Delete the &lt;OBJECT type="text/site properties"&gt; tag, delete all the information types listed, and delete the &lt;/OBJECT&gt; end tag from the file.
4.  Delete the &lt;param name="Type" value=&gt; tags from each table of contents entry that an information type is assigned to.

## Related topics

<dl> <dt>

[About Assigning Information Types](assign-information-types.md)
</dt> </dl>

 

 




