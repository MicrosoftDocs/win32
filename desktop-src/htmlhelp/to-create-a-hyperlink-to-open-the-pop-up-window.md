---
title: To create a hyperlink to open the pop-up window
description: To create a hyperlink to open the pop-up window
ms.assetid: B4134683-E42D-4cab-AD99-72A255B69E83
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To create a hyperlink to open the pop-up window

-   Copy the following code in your HTML file to call the [TextPopup](textpopup-method.md) method of the HTML Help ActiveX control:

    ```
    <A HREF="JavaScript:<i>popup</i>.TextPopup(<i>text_variable</i>, <i>font_variable</i>,9,9,-1,-1)"><i>Click Here</i></a> 
    ```

    

    where *popup* is the ID you specified in [step 2](to-insert-the-html-help-activex-control-in-your-html-file.md), *text\_variable* and *font\_variable* are the variable names you specified in [step 1](to-write-text-for-a-pop-up-window.md), the numeric values are the left and right margins (9,9) and the foreground and background colors (-1, -1) of the window, and *Click Here* is the link text.

## Notes

You do not have to create a text link to call [TextPopup](textpopup-method.md). You can also use a script to call it.

## Related topics

<dl> <dt>

[About the Script and DHTML Examples](script-and-dhtml-examples.md)
</dt> </dl>

 

 




