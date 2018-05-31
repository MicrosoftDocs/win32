---
title: To add hyperlinks to each region of the image map
description: To add hyperlinks to each region of the image map
ms.assetid: 562C7E53-195B-42db-824E-2C83E83FF9F3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To add hyperlinks to each region of the image map

1.  Copy the following code inside each &lt;AREA&gt; tag of your image map to call the TextPopup method of the HTML Help ActiveX control:

    ```
    A HREF="JavaScript:image_popup.TextPopup(text_variable, font_variable,9,9,-1,-1)" 
    ```

    

    where image\_popup is the ID you specified in[step 4](to-insert-the-html-help-activex-control-in-your-html-file.md), text\_variable and font\_variable are the variables names you specified in [step 2](to-write-text-for-pop-up-windows.md), and the numeric values are the left and right margins (9,9) and the foreground and background colors (-1, -1) of the window.

2.  Repeat step 1 for each region in your image map.

## Example

The hyperlinks shown below have been added to the example image map shown in [step 1](to-create-an-image-map.md):


```
<AREA SHAPE=RECT COORDS="4,2,108,103" A HREF="JavaScript:image_popup(square1,popfont,9,9,-1,-1)" Title="Square 1">
<AREA SHAPE=RECT COORDS="117,6,212,104" A HREF="JavaScript:image_popup(square2,popfont,9,9,-1,-1)" Title="Square 2">
<AREA SHAPE=RECT COORDS="3,111,105,213" A HREF="JavaScript:image_popup(square3,popfont,9,9,-1,-1)" Title="Square 3">
<AREA SHAPE=RECT COORDS="114,113,211,210" A HREF="JavaScript:image_popup(square4,popfont,9,9,-1,-1)" Title="Square 4"> </MAP>
```



## Note

The &lt;A&gt; tag **TITLE** parameter is optional.

## Related topics

<dl> <dt>

[About the Script and DHTML Examples](script-and-dhtml-examples.md)
</dt> </dl>

 

 




