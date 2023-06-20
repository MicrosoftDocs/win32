---
title: POPUP Element
description: POPUP Element
ms.assetid: f2c46e91-eef4-42d4-842b-73105831e7e2
keywords:
- Windows Media Player skins,POPUP element
- skins,POPUP element
- POPUP element
- reference for skins,POPUP element
- elements,POPUP
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# POPUP Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **POPUP** element provides a way for users to select items from a list. These items can be specified by using **ITEM** elements as children of the **POPUP** element. The **POPUP** element is identical to the **LISTBOX** element except the default value of the **popUp** attribute is true. When **popUp** is set to true, the control is displayed only when the **show** method is called, and its width is set to the width of the content (the ambient **width** attribute is ignored). The control is hidden automatically when the user selects an item from the list or when the **dismiss** method is called.

> [!Note]  
> This element requires Windows Media Player for Windows XP or later.

 

## Related topics

<dl> <dt>

[**LISTBOX Element**](listbox-element.md)
</dt> <dt>

[**LISTBOX.dismiss**](listbox-dismiss.md)
</dt> <dt>

[**LISTBOX.popUp**](listbox-popup.md)
</dt> <dt>

[**LISTBOX.show**](listbox-show.md)
</dt> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




