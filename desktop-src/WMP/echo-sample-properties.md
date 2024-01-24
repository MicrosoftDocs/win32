---
title: Echo Sample Properties
description: Echo Sample Properties
ms.assetid: 16f6f963-d746-42dc-872f-6f4db296cab9
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

# Echo Sample Properties

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Echo sample exposes two properties: the delay time and the effect level (wet mix). The value for the dry signal level (dry mix) is always derived from the wet mix value. You need to modify existing code and add some new code to make these properties accessible.

The following sections explain how to modify the properties code:

-   [How Properties Work](how-properties-work.md)
-   [Variables to Store Properties](variables-to-store-properties.md)
-   [Modifying the Scale Property](modifying-the-scale-property.md)
-   [Adding the Wet Mix Property](adding-the-wet-mix-property.md)

## Related topics

<dl> <dt>

[**The Echo Sample**](the-echo-sample.md)
</dt> </dl>

 

 




