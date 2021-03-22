---
description: The IEnumParticipant interface provides COM-standard enumeration methods for the ITParticipant interface. The ITParticipantControl::EnumerateParticipants method returns a pointer to IEnumParticipant.
ms.assetid: 8534d102-06ce-4e82-8f9c-9ab9f0d14df9
title: IEnumParticipant interface (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IEnumParticipant interface

\[**IEnumParticipant** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **IEnumParticipant** interface provides COM-standard enumeration methods for the [**ITParticipant**](itparticipant.md) interface. The [**ITParticipantControl::EnumerateParticipants**](itparticipantcontrol-enumerateparticipants.md) method returns a pointer to **IEnumParticipant**.

The **IEnumParticipant** interface is hidden from Visual Basic and scripting languages.

## Members

The **IEnumParticipant** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IEnumParticipant** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumParticipant** interface has these methods.



| Method                                  | Description                                                                                        |
|:----------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**Clone**](ienumparticipant-clone.md) | Creates another enumerator that contains the same enumeration state as the current one.<br/> |
| [**Next**](ienumparticipant-next.md)   | Gets the next specified number of elements in the enumeration sequence.<br/>                 |
| [**Reset**](ienumparticipant-reset.md) | Resets to the beginning of the enumeration sequence.<br/>                                    |
| [**Skip**](ienumparticipant-skip.md)   | Skips over the next specified number of elements in the enumeration sequence.<br/>           |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITParticipant**](itparticipant.md)
</dt> </dl>

 

