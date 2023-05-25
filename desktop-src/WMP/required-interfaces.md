---
title: Required Interfaces (Windows Media Player SDK)
description: Learn about the required interfaces that Windows Media Player implements in DirectShow or Media Foundation.
ms.assetid: 202d5769-edff-46df-bc05-bbb630a8f3f4
keywords:
- Windows Media Player plug-ins,interfaces
- plug-ins,interfaces
- digital signal processing plug-ins,interfaces
- DSP plug-ins,interfaces
- interfaces,DSP plug-ins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Required Interfaces (Windows Media Player SDK)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player renders audio and video by using one of the following pipelines.

-   DirectShow
-   Media Foundation

In Microsoft Windows XP and earlier, the Player uses DirectShow. In Windows Vista, the Player sometimes uses DirectShow and sometimes uses Media Foundation.

A DSP plug-in implements some or all of the following interfaces:

-   **IMediaObject**
-   **IWMPPluginEnable**
-   **IMFTransform**
-   **IMFGetService**
-   **ISpecifyPropertyPages**

A plug-in that implements **IMediaObject** and **IWMPPluginEnable** can run in the DirectShow pipeline. It can also run in the Media Foundation Pipeline inside a wrapper provided by Media Foundation. A plug-in of this type is called a Microsoft DirectX Media Object (DMO). It is common to think of a DMO as being analogous to a filter object in DirectShow. The DMO documentation is in the DirectShow section of the Windows SDK.

A plug-in that implements **IMFTransform** and **IMFGetService** can run natively (no wrapper required) in the Media Foundation pipeline. A plug-in of this type is called a Media Foundation Transform (MFT). The MFT documentation is in the Media Foundation section of the Windows SDK.

A plug-in that implements **IMediaObject**, **IWMPPluginEnable**, **IMFTransform**, and **IMFGetService** can run in the DirectShow pipeline and can also run natively in the Media Foundation pipeline. This type of plug-in, which is called a *dual-mode DSP plug-in*, can play the role of a DMO or an MFT.

When Windows Media Player uses a dual-mode DSP plug-in in the Media Foundation pipeline, it first queries for the **IMFTransform** interface. If that query fails, Windows Media Player queries for the **IMediaObject** interface. If the **IMediaObject** query is successful, the plug-in is wrapped and added to the Media Foundation pipeline.

Regardless of the pipeline, any DSP plug-in that allows the user to set properties must implement **ISpecifyPropertyPages**.

## Related topics

<dl> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> <dt>

[**DSP Plug-in Interfaces**](dsp-plug-in-interfaces.md)
</dt> <dt>

[**DSP Plug-in Packaging**](dsp-plug-in-packaging.md)
</dt> </dl>

 

 




