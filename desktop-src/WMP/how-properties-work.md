---
title: How Properties Work
description: How Properties Work
ms.assetid: 469af852-593c-4b54-8dc3-b76ad460fa77
keywords:
- Windows Media Player plug-ins,Echo sample properties
- plug-ins,Echo sample properties
- digital signal processing plug-ins,Echo sample properties
- DSP plug-ins,Echo sample properties
- Echo DSP plug-in sample,properties
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How Properties Work

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Property values are stored in member variables.

Properties are made accessible by method pairs. One method provides the implementation to specify the property value; its name starts with put\_. The other method provides the implementation to retrieve the property value; its name starts with get\_. The interface definition is in Echo.idl. The property method prototypes are in Echo.h. They are implemented in Echo.cpp.

The next three sections will show you how to modify the existing property methods to suit your needs and how to add the methods for an additional property.

-   [Variables to Store Properties](variables-to-store-properties.md)
-   [Modifying the Scale Property](modifying-the-scale-property.md)
-   [Adding the Wet Mix Property](adding-the-wet-mix-property.md)

## Related topics

<dl> <dt>

[**Echo Sample Properties**](echo-sample-properties.md)
</dt> </dl>

 

 




