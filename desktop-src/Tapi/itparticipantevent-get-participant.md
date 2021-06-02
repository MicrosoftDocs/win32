---
description: The get\_Participant method gets a pointer to an array of ITParticipant interfaces representing the participants involved in the event.
ms.assetid: 3c650715-b1c3-4f84-976a-2cb0f7f19f52
title: ITParticipantEvent::get_Participant method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantEvent::get\_Participant method

\[**get\_Participant** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_Participant** method gets a pointer to an array of [**ITParticipant**](itparticipant.md) interfaces representing the participants involved in the event.

## Syntax


```C++
HRESULT get_Participant(
  [out] ITParticipant **ppParticipant
);
```



## Parameters

<dl> <dt>

*ppParticipant* \[out\]
</dt> <dd>

Pointer to array of [**ITParticipant**](itparticipant.md) interfaces.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                           | Meaning                                                          |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>            | Method succeeded.<br/>                                     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>   | Insufficient memory exists to perform the operation.<br/>  |
| <dl> <dt>**TAPI\_E\_NOITEMS**</dt> </dl> | There are no participants associated with the event.<br/>  |
| <dl> <dt>**E\_POINTER**</dt> </dl>       | The *ppParticipant* parameter is not a valid pointer.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITParticipantEvent**](itparticipantevent.md)
</dt> <dt>

[**ITParticipant**](itparticipant.md)
</dt> </dl>

 

 




