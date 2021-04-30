---
description: The ITCallQualityControl interface exposes methods that allow an application to get and set parameters for call quality control.
ms.assetid: 8d33e3b2-6af9-4c2d-bc65-905467f4fc6a
title: ITCallQualityControl interface (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITCallQualityControl interface

\[ This interface is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITCallQualityControl** interface exposes methods that allow an application to get and set parameters for call quality control.

This interface is implemented by the [IPConf MSP](ipconf-msp.md) and the [H323 MSP](h323-msp.md). It is exposed only when a call uses these service providers.

## Members

The **ITCallQualityControl** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITCallQualityControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITCallQualityControl** interface has these methods.



| Method                                            | Description                                                                                                     |
|:--------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| [**Get**](itcallqualitycontrol-get.md)           | Gets the value of a given [call quality control property](callqualityproperty.md).<br/>                  |
| [**GetRange**](itcallqualitycontrol-getrange.md) | Gets the range of valid values for a given [call quality control property](callqualityproperty.md).<br/> |
| [**Set**](itcallqualitycontrol-set.md)           | Sets the value of a given [call quality control property](callqualityproperty.md).<br/>                  |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                         |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



 

