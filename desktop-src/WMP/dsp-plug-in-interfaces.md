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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DSP Plug-in Interfaces

The digital signal processing (DSP) plug-in interfaces are used to manage data transfer between Windows Media Player and the plug-in. All DSP plug-ins may optionally implement the **ISpecifyPropertyPage** interface to provide a property page implementation.

The following interfaces are required for creating DSP plug-ins.



| Interface                                                | Description                                                                                                                                            |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **IMediaObject**                                         | Manages data exchange with Windows Media Player and performs digital signal processing tasks. Detailed documentation is included with the DirectX SDK. |
| [IWMPMediaPluginRegistrar](/windows/win32/wmpservices/nn-wmpservices-iwmpmediapluginregistrar?branch=master) | Manages plug-in registration.                                                                                                                          |
| [IWMPPlugin](/windows/win32/wmpservices/nn-wmpservices-iwmpplugin?branch=master)                             | Manages the connection to Windows Media Player.                                                                                                        |
| [IWMPPluginEnable](/windows/win32/wmpservices/nn-wmpservices-iwmppluginenable?branch=master)                 | Stores whether the plug-in is currently enabled by Windows Media Player.                                                                               |
| [IWMPServices](/windows/win32/wmpservices/nn-wmpservices-iwmpservices?branch=master)                         | Retrieves information from the Player about the current stream time and stream state.                                                                  |



 

## Related topics

<dl> <dt>

[**DSP Plug-ins Programming Reference**](dsp-plug-ins-programming-reference.md)
</dt> </dl>

 

 




