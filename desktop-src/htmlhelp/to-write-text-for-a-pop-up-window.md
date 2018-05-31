---
title: To write text for a pop-up window
description: To write text for a pop-up window
ms.assetid: 883EBE0F-39FF-4e06-A0F2-39FBA1AE16DB
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To write text for a pop-up window

Write the text for your pop-up windows, using any text editor, in the following format:


```
<SCRIPT Language=JavaScript> 
<i>font_variable</i>="<i>Facename[, point size[, charset[, PLAIN BOLD ITALIC UNDERLINE]]]</i>" 
<i>text_variable</i>="<i>A Pop-up Window</i>" 
<i>text_variable2</i>="<i>Another Pop-up Window"</i> 
</SCRIPT> 
```



where *font\_variable* is the name of the variable that specifies the font attributes for the text, and *text\_variable* is the name of the variable that specifies the text to appear in the pop-up window.

## Example

The following script specifies 10 point italic Helvetica as the font to use for the text and defines one pop-up window:


```
<SCRIPT Language=JavaScript>
   MyFont="Helvetica,10,,italic"
   MyText="This is a pop-up window."
</SCRIPT>
```



## Notes

-   You can place the pop-up windows anywhere within the **&lt;BODY&gt;** start and end tags of your HTML file.
-   The text for pop-up windows can also be stored in a [text file](example--to-store-text-for-pop-up-windows-in-a-text-file.md) with the .js file name extension that you reference from your HTML file.

## Related topics

<dl> <dt>

[Step 2: Insert the HTML Help ActiveX Control in Your HTML File](to-insert-the-html-help-activex-control-in-your-html-file.md)
</dt> </dl>

 

 




