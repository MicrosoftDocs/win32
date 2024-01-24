---
title: Object Model Migration Guide
description: Object Model Migration Guide
ms.assetid: 2fd4f7ec-36b0-49da-9a11-546dd41c7a98
keywords:
- Windows Media Player,object model
- Windows Media Player,migration guide
- Windows Media Player object model,migration guide
- object model,migration guide
- Windows Media Player ActiveX control,migration guide
- ActiveX control,migration guide
- Windows Media Player Mobile ActiveX control,migration guide
- Windows Media Player Mobile,object model
- Windows Media Player Mobile,migration guide
- migration guide,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Object Model Migration Guide

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player 7 introduced a new object model that offers a rich new set of functionality that you can use to enhance your webpages. Subsequent versions have extended the version 7 object model with additional properties, methods, and events. However, the new object model differs substantially from the Windows Media Player 6.4 object model, so you need to understand how to update your existing code if you want to support Windows Media Player 7 and later in your projects.

For a sample that demonstrates how to detect the user's Windows Media Player version and current browser, see the sample named "detection" that is installed with this SDK. For more information about samples, see [Samples](samples.md).

This guide refers to the new object model as the Windows Media Player 7 or later object model. For details about which functionality is available in each version of Windows Media Player, see [Object Model Reference for Scripting](object-model-reference-for-scripting.md).

These object model issues are covered by the following topics:

-   [Differences Between the Object Models](differences-between-the-object-models.md)
-   [Using the Windows Media Player 7 or Later Object Model](using-the-windows-media-player-7-or-later-object-model.md)
-   [Error Handling](error-handling.md)
-   [Playlists](playlists.md)
-   [Closed Captioning](closed-captioning.md)
-   [DVD](dvd.md)
-   [Detailed Object Model Comparison](detailed-object-model-comparison.md)

## Related topics

<dl> <dt>

[**Player Control Guide**](player-control-guide.md)
</dt> </dl>

 

 




