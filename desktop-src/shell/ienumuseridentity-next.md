---
description: IEnumUserIdentity::Next is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: 2c8dfe36-c1bb-49f8-8847-f355cfab2984
title: IEnumUserIdentity::Next method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumUserIdentity.Next
api_type: 
- COM
api_location: 
- Msident.dll
---

# IEnumUserIdentity::Next method

\[**IEnumUserIdentity::Next** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Deprecated. Retrieves an array of user identity interfaces from the enumeration.

## Syntax


```C++
HRESULT Next(
  [in]  ULONG    celt,
  [out] IUnknown **rgelt,
  [out] ULONG    *pceltFetched
);
```



## Parameters

<dl> <dt>

*celt* \[in\]
</dt> <dd>

Type: **ULONG**

A **ULONG** value that represents the number of interfaces to retrieve.

</dd> <dt>

*rgelt* \[out\]
</dt> <dd>

Type: **[**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown)\*\***

The address of a pointer that receives the interfaces.

</dd> <dt>

*pceltFetched* \[out\]
</dt> <dd>

Type: **ULONG\***

The address of a pointer that receives the number of interfaces successfully retrieved.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

[**IEnumUserIdentity**](ienumuseridentity.md) keeps an internal count that specifies which interface is next to be retrieved. Multiple calls to this method will not reset this count. To reset the count, call [**IEnumUserIdentity::Reset**](ienumuseridentity-reset.md). To increment the count without retrieving interfaces, call [**IEnumUserIdentity::Skip**](ienumuseridentity-skip.md).

The value of *celt* should not exceed the value returned by [**IEnumUserIdentity::GetCount**](ienumuseridentity-getcount.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msident.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msident.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msident.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumUserIdentity**](ienumuseridentity.md)
</dt> <dt>

[**IEnumUserIdentity::Skip**](ienumuseridentity-skip.md)
</dt> <dt>

[**IEnumUserIdentity::Reset**](ienumuseridentity-reset.md)
</dt> <dt>

[**IEnumUserIdentity::GetCount**](ienumuseridentity-getcount.md)
</dt> </dl>

 

 
