---
description: The get\_Status method returns a VARIANT\_BOOL indicating participant status.
ms.assetid: 03ad763b-5223-41b5-b0cf-1f13c761f5c2
title: ITParticipant::get_Status method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipant::get\_Status method

\[**get\_Status** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_Status** method returns a VARIANT\_BOOL indicating participant status.

## Syntax


```C++
HRESULT get_Status(
  [in]  ITStream     *pITStream,
  [out] VARIANT_BOOL *pStatus
);
```



## Parameters

<dl> <dt>

*pITStream* \[in\]
</dt> <dd>

Pointer to [**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream) interface.

</dd> <dt>

*pStatus* \[out\]
</dt> <dd>

VARIANT\_TRUE if the participant is enabled on the stream, VARIANT\_FALSE if it is disabled.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                               |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                              |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | Method not implemented.<br/>                                        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>           |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pITStream* parameter is not a valid pointer.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pITStream* parameter does not point to a valid interface.<br/> |



 

## Remarks

Enabling or disabling a participant's status on a stream allows an application to essentially mute a given participant.

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

[**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream)
</dt> <dt>

[**put\_Status**](itparticipant-put-status.md)
</dt> </dl>

 

