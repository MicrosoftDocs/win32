---
title: Updates to the DSP Plug-in Wizard for Windows Media Player 11
description: Updates to the DSP Plug-in Wizard for Windows Media Player 11
ms.assetid: 975c18d5-06d7-4db2-a558-bc6557963425
keywords:
- Windows Media Player plug-ins,plug-in wizard
- plug-ins,plug-in wizard
- digital signal processing plug-ins,plug-in wizard
- DSP plug-ins,plug-in wizard
- plug-in wizard
- Visual Studio,DSP plug-in wizard
ms.topic: article
ms.date: 05/31/2018
---

# Updates to the DSP Plug-in Wizard for Windows Media Player 11

The Windows Media Player 11 SDK introduces the following changes to the DSP plug-in wizard:

-   Plug-ins register the threading model as "Both". This enables the plug-in to run in the Media Foundation pipeline on Windows Vista. See the *projectname*.rgs file.

    -   Audio DSP plug-ins have support for the following two additional formats:

    <!-- -->

    -   WAVE\_FORMAT\_IEEE\_FLOAT
    -   WAVE\_FORMAT\_EXTENSIBLE with subformat KSDATAFORMAT\_SUBTYPE\_IEEE\_FLOAT.

    See the *projectname*.cpp file.

    1.  Video DSP plug-ins have support for the NV12 video format.
    2.  Plug-ins make additional calls to [IWMPMediaPluginRegistrar::WMPRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpregisterplayerplugin) and [IWMPMediaPluginRegistrar::WMPUnRegisterPlayerPlugin](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpmediapluginregistrar-wmpunregisterplayerplugin) with a new plug-in type: WMP\_PLUGINTYPE\_DSP\_OUTOFPROC. See the project's *projectnamedll*.cpp file.
    3.  An additional project in each solution creates a proxy/stub DLL for the property page settings custom interface. See the *projectnamePS* project.
    4.  Calls to deprecated methods have been changed to use the newest versions.
    5.  The wizard can generate a dual-mode plug-in that functions both as a DMO, by implementing **IMediaObject**, and as an MFT, by implementing **IMFTransform**.

## Related topics

<dl> <dt>

[**DSP Plug-in Wizard**](dsp-plug-in-wizard.md)
</dt> </dl>

 

 




