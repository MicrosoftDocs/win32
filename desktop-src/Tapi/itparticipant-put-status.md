---
description: The put\_Status method sets the status of a participant.
ms.assetid: 8478fcf4-00b3-4b77-9859-e5a80ce24be1
title: ITParticipant::put_Status method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipant::put\_Status method

\[**put\_Status** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **put\_Status** method sets the status of a participant.

## Syntax


```C++
HRESULT put_Status(
  [in] ITStream     *pITStream,
  [in] VARIANT_BOOL fEnable
);
```



## Parameters

<dl> <dt>

*pITStream* \[in\]
</dt> <dd>

Pointer to [**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream) interface.

</dd> <dt>

*fEnable* \[in\]
</dt> <dd>

VARIANT\_TRUE if the participant is enabled on the stream, VARIANT\_FALSE if it is to be disabled.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                               |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                              |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | Method not implemented.<br/>                                        |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pITStream* parameter is not a valid pointer.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pITStream* parameter does not point to a valid interface.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/>           |



 

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

[**get\_Status**](itparticipant-get-status.md)
</dt> </dl>

 

