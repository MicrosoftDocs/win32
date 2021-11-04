---
description: The put\_LocalParticipantTypedInfo method sets participant information.
ms.assetid: c4afd1d3-6fe4-4e5b-a9bf-81b7dffa9914
title: ITLocalParticipant::put_LocalParticipantTypedInfo method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITLocalParticipant::put\_LocalParticipantTypedInfo method

The **put\_LocalParticipantTypedInfo** method sets participant information.

## Syntax


```C++
HRESULT put_LocalParticipantTypedInfo(
  [in] PARTICIPANT_TYPED_INFO InfoType,
  [in] BSTR                   ppInfo
);
```



## Parameters

<dl> <dt>

*InfoType* \[in\]
</dt> <dd>

[**PARTICIPANT\_TYPED\_INFO**](participant-typed-info.md) identifier of the type of information required.

</dd> <dt>

*ppInfo* \[in\]
</dt> <dd>

**BSTR** containing the required new value for the information.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The application must use [SysAllocString](/windows/win32/api/oleauto/nf-oleauto-sysallocstring) to allocate memory for the *ppInfo* parameter and use [SysFreeString](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) to free the memory when the variable is no longer needed.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITLocalParticipant**](itlocalparticipant.md)
</dt> <dt>

[**PARTICIPANT\_TYPED\_INFO**](participant-typed-info.md)
</dt> </dl>

 

