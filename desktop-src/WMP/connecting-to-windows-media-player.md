---
title: Connecting to Windows Media Player
description: Connecting to Windows Media Player
ms.assetid: c6afbd95-bcf8-438a-b854-776c543a5d51
keywords:
- Windows Media Player plug-ins,registry entries
- plug-ins,registry entries
- Windows Media Player plug-ins,connecting
- plug-ins,connecting
- digital signal processing plug-ins,connecting
- DSP plug-ins,connecting
- digital signal processing plug-ins,registry entries
- DSP plug-ins,registry entries
- registry,DSP plug-ins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Connecting to Windows Media Player

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player automatically connects to DSP plug-ins that have been installed and properly registered. DSP plug-ins must call [IWMPMediaPluginRegistrar::WMPRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpregisterplayerplugin) to create the registry entries necessary to allow Windows Media Player to recognize the plug-in and to list it on the **Plug-ins** tab of the Options dialog box. To remove the registry entries created by **IWMPMediaPluginRegistrar::WMPRegisterPlayerPlugin**, the plug-in calls [IWMPMediaPluginRegistrar::WMPUnRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpunregisterplayerplugin).

## Related topics

<dl> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> </dl>

 

 




