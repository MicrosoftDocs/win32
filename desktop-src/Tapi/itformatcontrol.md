---
description: The ITFormatControl interface exposes methods that allow an application to retrieve information concerning the format of a receive or transmit stream for a call.
ms.assetid: a3d15561-229e-4eb6-a0ac-2d69f170bced
title: ITFormatControl interface (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITFormatControl interface

\[ This interface is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITFormatControl** interface exposes methods that allow an application to retrieve information concerning the format of a receive or transmit stream for a call.

This interface is implemented by the [H323 MSP](h323-msp.md) and is exposed only when a call uses this service provider.

## Members

The **ITFormatControl** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITFormatControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITFormatControl** interface has these methods.



| Method                                                                     | Description                                                                    |
|:---------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**GetCurrentFormat**](itformatcontrol-getcurrentformat.md)               | Gets the media format of the current stream.<br/>                        |
| [**GetNumberOfCapabilities**](itformatcontrol-getnumberofcapabilities.md) | Gets the number of capabilities associated with the current format.<br/> |
| [**GetStreamCaps**](itformatcontrol-getstreamcaps.md)                     | Gets the capabilities associated with a given format index.<br/>         |
| [**ReleaseFormat**](itformatcontrol-releaseformat.md)                     | Releases the structure associated with the format.<br/>                  |
| [**ReOrderCapabilities**](itformatcontrol-reordercapabilities.md)         | Sets a new order for format capabilities.<br/>                           |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                         |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



 

