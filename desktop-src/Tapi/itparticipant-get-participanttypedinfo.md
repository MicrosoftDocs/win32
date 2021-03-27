---
description: The get\_ParticipantTypedInfo method gets a BSTR representation of the type of information needed, such as PTI\_EMAILADDRESS.
ms.assetid: 8dcc6182-ad3c-47f2-b4a0-e18a3c9f6888
title: ITParticipant::get_ParticipantTypedInfo method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipant::get\_ParticipantTypedInfo method

\[**get\_ParticipantTypedInfo** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_ParticipantTypedInfo** method gets a **BSTR** representation of the type of information needed, such as PTI\_EMAILADDRESS.

## Syntax


```C++
HRESULT get_ParticipantTypedInfo(
  [in]  PARTICIPANT_TYPED_INFO InfoType,
  [out] BSTR                   *ppInfo
);
```



## Parameters

<dl> <dt>

*InfoType* \[in\]
</dt> <dd>

[**PARTICIPANT\_TYPED\_INFO**](participant-typed-info.md) descriptor of the type of information needed.

</dd> <dt>

*ppInfo* \[out\]
</dt> <dd>

Pointer to **BSTR** representation of the information needed.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                    | Description                                                     |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>           | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>         | Storage of information into *ppInfo* failed.<br/>         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>   | The *InfoType* parameter is not valid.<br/>               |
| <dl> <dt>**E\_POINTER**</dt> </dl>      | The *ppInfo* parameter is not a valid pointer.<br/>       |
| <dl> <dt>**TAPI\_E\_NOITEM**</dt> </dl> | TAPI has no information on the specified type.<br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>  | Insufficient memory exists to perform the operation.<br/> |



 

## Remarks

The application must use [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory allocated for the *ppInfo* parameter.

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

[**PARTICIPANT\_TYPED\_INFO**](participant-typed-info.md)
</dt> <dt>

[**media types**](tapimediatype--constants.md)
</dt> </dl>

 

