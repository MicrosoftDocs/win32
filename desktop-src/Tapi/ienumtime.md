---
description: The IEnumTime interface provides COM-standard enumeration methods for the ITTime interface. The ITTimeCollection::get\_EnumerationIf method returns a pointer to IEnumTime.
ms.assetid: 395d7830-9a70-473a-8a89-4b4db48d5774
title: IEnumTime interface (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IEnumTime interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **IEnumTime** interface provides COM-standard enumeration methods for the [**ITTime**](ittime.md) interface. The [**ITTimeCollection::get\_EnumerationIf**](ittimecollection-get-enumerationif.md) method returns a pointer to **IEnumTime**.

## Members

The **IEnumTime** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IEnumTime** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumTime** interface has these methods.



| Method                           | Description                                                                                        |
|:---------------------------------|:---------------------------------------------------------------------------------------------------|
| [**Clone**](ienumtime-clone.md) | Creates another enumerator that contains the same enumeration state as the current one.<br/> |
| [**Next**](ienumtime-next.md)   | Gets the next specified number of elements in the enumeration sequence.<br/>                 |
| [**Reset**](ienumtime-reset.md) | Resets to the beginning of the enumeration sequence.<br/>                                    |
| [**Skip**](ienumtime-skip.md)   | Skips over the next specified number of elements in the enumeration sequence.<br/>           |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



 

