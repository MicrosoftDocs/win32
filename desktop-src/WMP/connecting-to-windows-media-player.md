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
ms.date: 05/31/2018
---

# Connecting to Windows Media Player

Windows Media Player automatically connects to DSP plug-ins that have been installed and properly registered. DSP plug-ins must call [IWMPMediaPluginRegistrar::WMPRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpregisterplayerplugin) to create the registry entries necessary to allow Windows Media Player to recognize the plug-in and to list it on the **Plug-ins** tab of the Options dialog box. To remove the registry entries created by **IWMPMediaPluginRegistrar::WMPRegisterPlayerPlugin**, the plug-in calls [IWMPMediaPluginRegistrar::WMPUnRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpunregisterplayerplugin).

## Related topics

<dl> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> </dl>

 

 




