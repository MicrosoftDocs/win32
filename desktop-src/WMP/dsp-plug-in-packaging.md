---
title: DSP Plug-in Packaging
description: DSP Plug-in Packaging
ms.assetid: 5d40a39b-0fe8-4f77-9465-8e31d1f2708e
keywords:
- Windows Media Player plug-ins,Media Foundation pipeline
- plug-ins,Media Foundation pipeline
- digital signal processing plug-ins,Media Foundation pipeline
- DSP plug-ins,Media Foundation pipeline
- Media Foundation pipeline
- Windows Media Player plug-ins,DirectShow pipeline
- plug-ins,DirectShow pipeline
- digital signal processing plug-ins,DirectShow pipeline
- DSP plug-ins,DirectShow pipeline
- DirectShow pipeline
- digital signal processing plug-ins,basic
- DSP plug-ins,basic
- Windows Media Player plug-ins,basic DSP
- plug-ins,basic DSP
- basic DSP plug-ins
- Windows Media Player plug-ins,dual-mode DSP
- plug-ins,dual-mode DSP
- digital signal processing plug-ins,dual-mode
- DSP plug-ins,dual-mode
- dual-mode DSP plug-ins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DSP Plug-in Packaging

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player renders audio and video by using one of the following pipelines.

-   DirectShow
-   Media Foundation

In Microsoft Windows XP and earlier, the Player uses DirectShow. In Windows Vista, the Player sometimes uses DirectShow and sometimes uses Media Foundation.

A DSP plug-in that is designed to run in the DirectShow pipeline is called a *basic DSP plug-in*. A basic DSP plug-ins acts as a DirectX Media Object (DMO). A basic DSP plug-in can run natively in the DirectShow pipeline and can also run in the Media Foundation pipeline inside a wrapper provided by Media Foundation.

A DSP plug-in that is designed to run natively (no wrapper required) in both the DirectShow and Media Foundation pipelines is called a *dual-mode DSP plug-in*. A dual-mode DSP plug-in can act as a DMO or as a Media Foundation Transform (MFT).

A DSP plug-in is a COM object that is packaged as a self-registering .dll file. The interfaces that the plug-in implements depend on whether the plug-in is designed as a basic DSP plug-in or as a dual-mode DSP plug-in. For detailed information about the interfaces that DSP plug-ins must implement, see [Required Interfaces](required-interfaces.md).

A DSP plug-in that runs in the Media Foundation pipeline (either natively or wrapped) must register its threading model as "Both". For detailed information about registry subkeys and entries associated with DSP plug-ins, see [Registering DSP Plug-ins](registering-dsp-plug-ins.md).

A DSP plug-in that implements custom interfaces and runs in the Media Foundation pipeline (either natively or wrapped) must be paired with a proxy-stub .dll file that can marshal the custom interfaces across process boundaries. For information about the proxy-stub component, see [Updating Existing DSP Plug-ins](updating-existing-dsp-plug-ins.md) and [Updates to the DSP Plug-in Wizard for Windows Media Player 11](updates-to-the-dsp-plug-in-wizard-for-windows-media-player-11.md).

DSP plug-in objects must not be created as singletons. Windows Media Player must be able to create multiple separate instances of a particular DSP plug-in.

DSP plug-ins that run in the Windows Vista Protected Media Path (PMP) must be signed. For more information, see [Code Signing for Protected Media Components in Windows Vista](/windows-hardware/test/hlk/).

## Related topics

<dl> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> </dl>

 

 