---
description: The get\_Event method gets a PARTICIPANT\_EVENT descriptor of the type of event that has occurred.
ms.assetid: 6b5e6358-2ba6-48b5-8d55-bc896fbb9962
title: ITParticipantEvent::get_Event method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantEvent::get\_Event method

\[**get\_Event** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_Event** method gets a [**PARTICIPANT\_EVENT**](participant-event.md) descriptor of the type of event that has occurred.

## Syntax


```C++
HRESULT get_Event(
  [out] PARTICIPANT_EVENT *pParticipantEvent
);
```



## Parameters

<dl> <dt>

*pParticipantEvent* \[out\]
</dt> <dd>

Pointer to a [**PARTICIPANT\_EVENT**](participant-event.md) descriptor of the event.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>      |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pParticipantEvent* parameter is not a valid pointer.<br/> |



 

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

[**PARTICIPANT\_EVENT**](participant-event.md)
</dt> </dl>

 

 




