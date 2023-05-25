---
title: Adding the Close BUTTONELEMENT
description: Adding the Close BUTTONELEMENT
ms.assetid: 18f0ee9d-b0d4-4134-8dd6-6ece480b2818
keywords:
- creating skins,BUTTONELEMENT element
- Windows Media Player skins,BUTTONELEMENT element
- skins,BUTTONELEMENT element
- skin definition files,BUTTONELEMENT element
- BUTTONELEMENT element
- elements,BUTTONELEMENT
- creating skins,Close buttons
- Windows Media Player skins,Close buttons
- skins,Close buttons
- skin definition files,Close buttons
- Close buttons
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Adding the Close BUTTONELEMENT

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Close button is similar in concept to the Play button, but has different codes and colors.

Put the Close **BUTTONELEMENT** code after the closing angle bracket of the Play **BUTTONELEMENT**.


```C++
        <BUTTONELEMENT
            mappingColor = "#FF0000"
            upToolTip = "Close"
            onClick="JScript: view.close();" />

```



The following attributes are used to define the **BUTTONELEMENT** for the Close button:

**mappingColor**

This is the color value of the region in the mapping art file you created before. In this case it is the solid red color. This attribute is required for any **BUTTONELEMENT**. By defining this color, you are telling Windows Media Player to associate this color area with the XML code of this button.

**upToolTip**

This defines the text that will be displayed when the user hovers the mouse over the button. This is the same as the Play button except that it is labeled "Close".

**onClick**

This defines the event that occurs when the mouse clicks on the button. The value of this event attribute is called an event handler and will be either a line of Microsoft JScript code, or a JScript function in an external text file that is loaded by the **loadScript** attribute of a **VIEW**. In this case, the JScript code calls the **close** method of the **VIEW** element using the global attribute **view**, which closes the view and shuts down Windows Media Player.

## Related topics

<dl> <dt>

[**Creating the Skin Definition File**](creating-the-skin-definition-file.md)
</dt> </dl>

 

 




