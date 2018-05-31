---
title: Example To Store Text for Pop-up Windows in a Text File
description: Example To Store Text for Pop-up Windows in a Text File
ms.assetid: AAE16AB3-7D82-46d3-87DE-D86FC2F05E0A
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Example: To Store Text for Pop-up Windows in a Text File

1.  The text for pop-up windows can be stored in one text file with the .js file name extension. This enables you to store the text for all pop-up windows in your entire help system in a single location. This also enables you to globally define the font attributes to be used for pop-up windows.
2.  Create your pop-up windows using any text editor, in the following format:

    ```
    <i>popfont</i>="<i>Facename[, point size[, charset[, PLAIN BOLD ITALIC UNDERLINE]]]</i>"
    <i>Text1</i>="<i>The text for the first pop-up window.</i>"
    <i>Text2</i>="<i>The text for the second pop-up window.</i>"
    ```

    

    where *popfont* is the name of the variable that specifies the font attributes for the pop-up text and *Text1*, *Text2*, and so on, are the variables that specify the text of each pop-up window.

3.  Save the file with a .js file name extension.

4.  Copy the following code into each HTML file from which you want to open a pop-up window. Place the code between the &lt;HEAD&gt; start and end tags:

    ```
    <OBJECT
    id=HHCTRL type="application/x-oleobject"
    classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436" >
    </OBJECT>
    <SCRIPT language=javascript
    SRC="terms.js">
    </SCRIPT>
    ```

    

    where *HHCTRL* is the ID of the control that you are referencing, and *terms.js* is the name of your text file. You might want to include an error handler that is invoked if the specified text file cannot be found.

5.  Also copy this code in your HTML file to call the [TextPopup](textpopup-method.md) method of the HTML Help ActiveX control:

    ```
    <A HREF="JavaScript:HHCTRL.TextPopup(Text1,popfont,9,9,-1,-1)"
    Title="Click for pop-up definition">Word to be defined</A> 
    ```

    

## Notes

-   You must add the text file to the \[FILES\] section of your project (.hhp) file.
-   This procedure cannot be used to create context-sensitive help topics that users open through an external program.

## Related topics

<dl> <dt>

[About the Script and DHTML Examples](script-and-dhtml-examples.md)
</dt> </dl>

 

 




