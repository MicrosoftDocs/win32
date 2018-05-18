---
title: To create a KLink in an HTML file to a keyword in a target file
description: To create a KLink in an HTML file to a keyword in a target file
ms.assetid: '1CFB961E-1187-481f-8B4C-297BEB382EA5'
---

# To create a KLink in an HTML file to a keyword in a target file

1.  Open the HTML file you want to link from, and then position your cursor at the location where you want to create a Keyword link (KLink).
2.  Click **HTML Help ActiveX Control**. 

    |                        |                                                                                                                         |
    |------------------------|-------------------------------------------------------------------------------------------------------------------------|
    | ![](images/sb-wiz.gif) | Opens the HTML Help ActiveX Control Wizard, which enables you to insert or edit the control in an HTML file.<br/> |

    

     

3.  In the **Specify the command** box, click **Keyword Search**, and then select the appropriate display type and button options.
4.  In the **Related Topics** dialog box, specify the keywords you want to jump to.

## Notes

-   You must [add keywords](to-add-a-klink-keyword-to-an-html-file.md) to the appropriate target files before the KLink search will work.
-   Adding a KLink to an HTML file adds an &lt;OBJECT&gt; tag to your file. This allows you to link to any other files that contain the keywords you specify. When a user clicks the KLink, any topics that contain the keywords you have specified will appear.
-   To use this feature, your help project must be set up to [include keywords from HTML files](to-generate-keywords-from-html-files.md).
-   For more information about KLinks, see the [HTML Help ActiveX control reference](klink.md).

## Related topics

<dl> <dt>

[About Working with KLinks](working-with-klinks.md)
</dt> </dl>

 

 





