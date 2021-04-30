---
description: The IEnumMedia interface provides COM-standard enumeration methods for the ITMedia interface. The ITMediaCollection::get\_EnumerationIf method returns a pointer to IEnumMedia.
ms.assetid: 827f8866-2445-4b7c-88fe-eed19f48c93b
title: IEnumMedia interface (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IEnumMedia interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **IEnumMedia** interface provides COM-standard enumeration methods for the [**ITMedia**](itmedia.md) interface. The [**ITMediaCollection::get\_EnumerationIf**](itmediacollection-get-enumerationif.md) method returns a pointer to **IEnumMedia**.

## Members

The **IEnumMedia** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IEnumMedia** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumMedia** interface has these methods.



| Method                            | Description                                                                                        |
|:----------------------------------|:---------------------------------------------------------------------------------------------------|
| [**Clone**](ienummedia-clone.md) | Creates another enumerator that contains the same enumeration state as the current one.<br/> |
| [**Next**](ienummedia-next.md)   | Gets the next specified number of elements in the enumeration sequence.<br/>                 |
| [**Reset**](ienummedia-reset.md) | Resets to the beginning of the enumeration sequence.<br/>                                    |
| [**Skip**](ienummedia-skip.md)   | Skips over the next specified number of elements in the enumeration sequence.<br/>           |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



 

