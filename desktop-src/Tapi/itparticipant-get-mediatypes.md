---
description: The get\_MediaTypes method gets the media types associated with a participant.
ms.assetid: a2323d16-8eec-4c17-b5f2-b6fbd910ba60
title: ITParticipant::get_MediaTypes method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipant::get\_MediaTypes method

\[**get\_MediaTypes** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_MediaTypes** method gets the [**media types**](tapimediatype--constants.md) associated with a participant.

## Syntax


```C++
HRESULT get_MediaTypes(
  [out] long *plMediaType
);
```



## Parameters

<dl> <dt>

*plMediaType* \[out\]
</dt> <dd>

Pointer to media type flags, such as TAPIMEDIATYPE\_VIDEO.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *plMediaType* parameter is not a valid pointer.<br/>  |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITParticipant**](itparticipant.md)
</dt> <dt>

[**media types**](tapimediatype--constants.md)
</dt> </dl>

 

 




