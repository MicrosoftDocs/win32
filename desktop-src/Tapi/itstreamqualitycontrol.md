---
description: The ITStreamQualityControl exposes methods that allow an application to get and set parameters for stream quality control.
ms.assetid: b9ecf24a-c87e-44a6-9e20-aa7bf7619314
title: ITStreamQualityControl interface (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITStreamQualityControl interface

\[ This interface is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITStreamQualityControl** exposes methods that allow an application to get and set parameters for stream quality control.

This interface is implemented by the [IPConf MSP](ipconf-msp.md) and the [H323 MSP](h323-msp.md). It is exposed only when a call uses these service providers.

## Members

The **ITStreamQualityControl** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITStreamQualityControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITStreamQualityControl** interface has these methods.



| Method                                              | Description                                                                                                 |
|:----------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**Get**](itstreamqualitycontrol-get.md)           | Gets the value of a given [stream quality property](streamqualityproperty.md).<br/>                  |
| [**GetRange**](itstreamqualitycontrol-getrange.md) | Gets the range of valid values for a given [stream quality property](streamqualityproperty.md).<br/> |
| [**Set**](itstreamqualitycontrol-set.md)           | Sets the value of a given [stream quality property](streamqualityproperty.md).<br/>                  |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                         |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



 

