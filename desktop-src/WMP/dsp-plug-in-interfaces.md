---
title: DSP Plug-in Interfaces
description: DSP Plug-in Interfaces
ms.assetid: 4660f928-2e92-468f-9e2b-b411931dfded
keywords:
- Windows Media Player plug-ins,DSP interfaces
- Windows Media Player plug-ins,interfaces
- plug-ins,DSP interfaces
- plug-ins,interfaces
- digital signal processing plug-ins,interfaces
- digital signal processing plug-ins,ISpecifyPropertyPage interface
- DSP plug-ins,interfaces
- DSP plug-ins,ISpecifyPropertyPage interface
- interfaces,DSP plug-ins
- ISpecifyPropertyPage
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DSP Plug-in Interfaces

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The digital signal processing (DSP) plug-in interfaces are used to manage data transfer between Windows Media Player and the plug-in. All DSP plug-ins may optionally implement the **ISpecifyPropertyPage** interface to provide a property page implementation.

The following interfaces are required for creating DSP plug-ins.



| Interface                                                | Description                                                                                                                                            |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **IMediaObject**                                         | Manages data exchange with Windows Media Player and performs digital signal processing tasks. Detailed documentation is included with the DirectX SDK. |
| [IWMPMediaPluginRegistrar](/previous-versions/windows/desktop/api/wmpservices/nn-wmpservices-iwmpmediapluginregistrar) | Manages plug-in registration.                                                                                                                          |
| [IWMPPlugin](/previous-versions/windows/desktop/api/wmpservices/nn-wmpservices-iwmpplugin)                             | Manages the connection to Windows Media Player.                                                                                                        |
| [IWMPPluginEnable](/previous-versions/windows/desktop/api/wmpservices/nn-wmpservices-iwmppluginenable)                 | Stores whether the plug-in is currently enabled by Windows Media Player.                                                                               |
| [IWMPServices](/previous-versions/windows/desktop/api/wmpservices/nn-wmpservices-iwmpservices)                         | Retrieves information from the Player about the current stream time and stream state.                                                                  |



 

## Related topics

<dl> <dt>

[**DSP Plug-ins Programming Reference**](dsp-plug-ins-programming-reference.md)
</dt> </dl>

 

 




