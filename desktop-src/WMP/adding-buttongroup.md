---
title: Adding BUTTONGROUP
description: Adding BUTTONGROUP
ms.assetid: 07a4a347-b3da-4dcb-b3e4-bee0d002b2e2
keywords:
- creating skins,BUTTONGROUP element
- Windows Media Player skins,BUTTONGROUP element
- skins,BUTTONGROUP element
- skin definition files,BUTTONGROUP element
- BUTTONGROUP element
- elements,BUTTONGROUP
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Adding BUTTONGROUP

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This example uses the **BUTTONGROUP** element for the coding in the skin definition file. **BUTTONGROUP** creates an easy way to process mouse events without having to calculate exact locations on the screen and uses color instead of x and y-coordinates.

First you must add the **BUTTONGROUP** tags to the skin definition file you created. Put them after the **THEME** tag attributes.


```C++
        <BUTTONGROUP
            mappingImage = "map.bmp"
            hoverImage = "hover.bmp">


        </BUTTONGROUP>

```



Leave a few blank lines above the closing **BUTTONGROUP** tag for the buttons you will add next.

The following attributes are used to define **BUTTONGROUP**:

**mappingImage**

This is the file name of the mapping art file you created before, the one with the red and green circles. This attribute is required for any **BUTTONGROUP**.

**hoverImage**

This is the file name of the hover art file you created before, the one with the two yellow buttons that read "Play" and "Close". This is not required, but a hover image helps to provide feedback to the user.

## Related topics

<dl> <dt>

[**Creating the Skin Definition File**](creating-the-skin-definition-file.md)
</dt> </dl>

 

 




