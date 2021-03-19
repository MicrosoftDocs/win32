---
description: The ITAudioSettings interface exposes methods that allow an application to get and set parameters for control of an audio device.
ms.assetid: 56607024-255d-4d1b-9ca0-6086eff7b7b2
title: ITAudioSettings interface (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITAudioSettings interface

\[ This interface is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITAudioSettings** interface exposes methods that allow an application to get and set parameters for control of an audio device.

This interface is implemented by the [IPConf MSP](ipconf-msp.md) and the [H323 MSP](h323-msp.md). It is exposed only when a call uses these service providers.

## Members

The **ITAudioSettings** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITAudioSettings** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITAudioSettings** interface has these methods.



| Method                                              | Description                                                                                                |
|:----------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**Get**](/windows/desktop/api/tapi3if/nf-tapi3if-itasrterminalevent-get_call)          | Gets the value of a given [audio setting property](audiosettingsproperty.md).<br/>                  |
| [**GetRange**](/windows/desktop/api/tapi3if/nf-tapi3if-itasrterminalevent-get_terminal) | Gets the range of valid values for a given [audio setting property](audiosettingsproperty.md).<br/> |
| [**Set**](/windows/desktop/api/tapi3if/nf-tapi3if-itasrterminalevent-get_error)         | Sets the value of a given [audio setting property](audiosettingsproperty.md).<br/>                  |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                         |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



 

