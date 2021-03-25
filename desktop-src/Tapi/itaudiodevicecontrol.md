---
description: The ITAudioDeviceControl interface exposes methods that enable an application to get and set parameters for control of an audio device.
ms.assetid: 9a557cb2-acad-406c-9a87-18cbe96e8a9f
title: ITAudioDeviceControl interface (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITAudioDeviceControl interface

\[ This interface is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITAudioDeviceControl** interface exposes methods that enable an application to get and set parameters for control of an audio device.

This interface is implemented by the [IPConf MSP](ipconf-msp.md) and the [H323 MSP](h323-msp.md). It is exposed when a call uses these service providers or a third party service provider that implements this interface. To obtain a pointer to the **ITAudioDeviceControl** interface, call **QueryInterface** on the [**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream) interface that controls the audio device corresponding to the stream. The media type of the **ITStream** interface must be audio for the **ITAudioDeviceControl** interface to be exposed.

## Members

The **ITAudioDeviceControl** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITAudioDeviceControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITAudioDeviceControl** interface has these methods.



| Method                                              | Description                                                                                             |
|:----------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**Get**](/windows/desktop/api/tapi3if/nf-tapi3if-itasrterminalevent-get_call)          | Gets the value of a given [audio device property](audiodeviceproperty.md).<br/>                  |
| [**GetRange**](/windows/desktop/api/tapi3if/nf-tapi3if-itasrterminalevent-get_terminal) | Gets the range of valid values for a given [audio device property](audiodeviceproperty.md).<br/> |
| [**Set**](/windows/desktop/api/tapi3if/nf-tapi3if-itasrterminalevent-get_error)         | Sets the value of a given [audio device property](audiodeviceproperty.md).<br/>                  |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                         |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



## See also

<dl> <dt>

[IPConf MSP](ipconf-msp.md)
</dt> </dl>

 

