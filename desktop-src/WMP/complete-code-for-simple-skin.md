---
title: Complete Code for Simple Skin
description: Complete Code for Simple Skin
ms.assetid: ece437d2-1a11-4096-8b3b-db2b4def8248
keywords:
- creating skins,code samples
- Windows Media Player skins,code samples
- skins,code samples
- skin definition files,code samples
- creating skins,examples
- Windows Media Player skins,examples
- skins,examples
- skin definition files,examples
ms.topic: article
ms.date: 05/31/2018
---

# Complete Code for Simple Skin

Here is the complete code for the first sample skin:


```C++
<THEME>
    <VIEW
        clippingColor = "#CCCC00"
        backgroundImage = "background.bmp"
        titleBar = "false">
         
        <BUTTONGROUP
            mappingImage = "map.bmp"
            hoverImage = "hover.bmp"> 
                
        <BUTTONELEMENT
            mappingColor = "#00FF00"
            upToolTip = "Play"
            onClick="JScript: player.URL='https://proseware.com/laure.wma';" />
                          
        <BUTTONELEMENT
            mappingColor = "#FF0000"
            upToolTip = "Close"
            onClick = "JScript: view.close(); " />
                
        </BUTTONGROUP>
    </VIEW>
</THEME>

```



Now you have all the pieces put together.

Create a compressed file with a .zip file name extension. This compressed file contains your skin definition file, bitmaps, and any digital media files you want to include. Rename the file so that it has a .wmz file name extension. Then double-clicking your compressed skin will start it playing.

You can see a similar working simple skin in the samples section of the SDK.

## Related topics

<dl> <dt>

[**Creating the Skin Definition File**](creating-the-skin-definition-file.md)
</dt> </dl>

 

 




