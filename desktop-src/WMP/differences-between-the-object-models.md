---
title: Differences Between the Object Models
description: Differences Between the Object Models
ms.assetid: a6d2a2d5-2892-461a-aa6d-7e11b504b2af
keywords:
- Windows Media Player,object model
- Windows Media Player object model,version differences
- object model,version differences
- Windows Media Player ActiveX control,version differences
- ActiveX control,version differences
- Windows Media Player Mobile ActiveX control,version differences
- Windows Media Player Mobile,object model
- migration guide,version differences
- versions of Windows Media Player,object model
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Differences Between the Object Models

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are two primary differences between the Windows Media Player 6.4 object model and the Windows Media Player 7 or later object model.

-   **CLSID** The Windows Media Player 7 or later object model is a complete departure from the version 6.4 object model. The Component Object Model (COM) specification requires that all existing interfaces must continue to function in new versions of a COM component. This means that new interfaces can be added to a COM component, but existing interfaces must never be altered, ensuring older client code will always work with the particular component it was designed to use. Therefore, the Windows Media Player 7 or later ActiveX control has a new class ID: 6BF52A52-394A-11D3-B153-00C04F79FAA6. If you want to take advantage of the new functionality of the control for this version, you must change your CLSID.
-   **Hierarchical Object Model** If you've been using the Windows Media Player 6.4 ActiveX control, you may have noticed that all the properties, methods, and events are accessed through the same object: the **Player** object. By contrast, the Windows Media Player 7 or later object model is organized as a hierarchy of objects. The **Player** object is still the root object, but functions are now accessed through a variety of child objects.

## Related topics

<dl> <dt>

[**Object Model Migration Guide**](object-model-migration-guide.md)
</dt> </dl>

 

 




