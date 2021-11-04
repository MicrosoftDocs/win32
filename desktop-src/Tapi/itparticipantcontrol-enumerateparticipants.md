---
description: The EnumerateParticipants method enumerates participants associated with the current conference.
ms.assetid: 90a2b5f1-8749-42cd-92d4-f5ee4e680eae
title: ITParticipantControl::EnumerateParticipants method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantControl::EnumerateParticipants method

\[**EnumerateParticipants** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **EnumerateParticipants** method enumerates participants associated with the current conference. This method is provided for C and C++ applications. Automation client applications, such as those written in Visual Basic, must use the [**get\_Participants**](itparticipantcontrol-get-participants.md) method.

## Syntax


```C++
HRESULT EnumerateParticipants(
  [out] IEnumParticipant **ppEnumParticipants
);
```



## Parameters

<dl> <dt>

*ppEnumParticipants* \[out\]
</dt> <dd>

Pointer to [**IEnumParticipant**](ienumparticipant.md) interface.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                               |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                          |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppEnumParticipants* parameter is not a valid pointer.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>       |



 

## Remarks

TAPI calls the **AddRef** method on the [**IEnumParticipant**](ienumparticipant.md) interface returned by **ITParticipantControl::EnumerateParticipants**. The application must call **Release** on the **IEnumParticipant** interface to free resources associated with it.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITParticipantControl**](itparticipantcontrol.md)
</dt> <dt>

[**get\_Participants**](itparticipantcontrol-get-participants.md)
</dt> <dt>

[**IEnumParticipant**](ienumparticipant.md)
</dt> <dt>

[**ITParticipant**](itparticipant.md)
</dt> </dl>

 

 




