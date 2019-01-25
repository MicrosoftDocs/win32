---
title: Adding the Play BUTTONELEMENT
description: Adding the Play BUTTONELEMENT
ms.assetid: 895850a7-7538-4581-8348-41cbb3bc9717
keywords:
- creating skins,BUTTONELEMENT element
- Windows Media Player skins,BUTTONELEMENT element
- skins,BUTTONELEMENT element
- skin definition files,BUTTONELEMENT element
- BUTTONELEMENT element
- elements,BUTTONELEMENT
- creating skins,Play buttons
- Windows Media Player skins,Play buttons
- skins,Play buttons
- skin definition files,Play buttons
- Play buttons
ms.topic: article
ms.date: 05/31/2018
---

# Adding the Play BUTTONELEMENT

Finally, you can add the **BUTTONELEMENT** elements that connect the visual buttons on the screen to Windows Media Player actions. This is the core of your skin and you can think of it as wiring the surface of the skin to the inner machinery of Windows Media Player.

**BUTTONELEMENT**s are contained within a **BUTTONGROUP**. You must always have at least one **BUTTONELEMENT** inside each **BUTTONGROUP**.

Put the Play **BUTTONELEMENT** code after the closing angle bracket of **BUTTONGROUP**.


```C++
        <BUTTONELEMENT
            mappingColor = "#00FF00"
            upToolTip = "Play"
            onClick = "JScript: player.URL='https://proseware.com/laure.wma';" />

```



The following attributes are used to define the **BUTTONELEMENT** for the Play button:

**mappingColor**

This is the color value of a region in the mapping art file you created before. In this case it is the solid green color. This attribute is required for any **BUTTONELEMENT**. By defining this color, you are telling Windows Media Player to associate this color area with the XML code of this button.

**upToolTip**

This defines the text that will be displayed if the user hovers the mouse over the button. Do not confuse this with the hover art that will be displayed. A ToolTip is a small balloon caption that takes a moment to appear. The hover art image, however, will appear instantly in whatever color and shape you choose.

**onClick**

This defines the event that occurs when the mouse clicks on the button. The value of this event attribute is called an event handler and will be either a line of Microsoft JScript code, or a JScript function in an external text file that is loaded by the **loadScript** attribute of a **VIEW**. In this case, the JScript code calls the **URL** method of Windows Media Player, which loads and starts playing a file named "laure.wma". Note that the line ends with a semicolon inside the quotes, which is good JScript coding practice. Note also the use of single quotes inside the double quotes to set off the file name. For more information about JScript, see [Using JScript](using-jscript.md) in the About Skins section of this SDK.

Notice that there is no ending **BUTTONELEMENT** tag. If an element does not enclose another element, you can close it off with the forward slash just before the closing angle bracket. This tells XML that you are finished with that element. For example,


```C++
<BUTTONELEMENT></BUTTONELEMENT>
```



and


```C++
<BUTTONELEMENT/>
```



convey the same information in XML.

The power of skins comes from using event handlers. If the user does something with a mouse, you can handle that event with JScript. Your code can be a single line that makes Windows Media Player do something simple like play, or it can be a complete application written in JScript.

## Related topics

<dl> <dt>

[**Creating the Skin Definition File**](creating-the-skin-definition-file.md)
</dt> </dl>

 

 




