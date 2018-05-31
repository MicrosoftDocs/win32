---
title: To write text for pop-up windows
description: To write text for pop-up windows
ms.assetid: 6296E486-11E2-4757-9009-B9FF7382F098
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To write text for pop-up windows

1.  Copy the following syntax in your HTML file:

    ```
    <SCRIPT Language=JavaScript> 
    <i>font_variable</i>="<i>Facename[, point size[, charset[, PLAIN BOLD ITALIC UNDERLINE]]]</i>" 
    <i>text_variable</i>="<i>A Pop-up Window</i>" 
    <i>text_variable2</i>="<i>Another Pop-up Window"</i> 
    </SCRIPT> 
    ```

    

    where *font\_variable* is the name of the variable that specifies the font attributes for the text, and *text\_variable* is the name of the variable that specifies the text of the pop-up window.

2.  Create one text variable (with a unique name) for each pop-up window.

## Example

The following script specifies 10 point Verdana as the font to use for the text and defines four pop-up windows:


```
<SCRIPT Language=JavaScript>
   popfont="Verdana,10,,plain"
   square1="Welcome to Square 1!"
   square2="This is Square 2!"
   square3="Welcome to Square 3!"
   square4="Square 4 welcomes you!"
</SCRIPT>
```



## Notes

-   You can place the pop-up windows anywhere within the **&lt;BODY&gt;** start and end tags of your HTML file.
-   The text for pop-up windows can also be stored in a [text file](example--to-store-text-for-pop-up-windows-in-a-text-file.md) with the .js file name extension that you reference from your HTML file.
-   For more information about specifying font attributes, see the TextPopup method.

## Related topics

<dl> <dt>

[Step 3: Add the Image to Your Project File](to-add-the-image-to-your-project-file.md)
</dt> </dl>

 

 




