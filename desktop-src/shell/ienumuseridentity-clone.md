---
description: IEnumUserIdentity::Clone is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: dde9afca-db8d-41ba-afa0-94eadecb695b
title: IEnumUserIdentity::Clone method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumUserIdentity.Clone
api_type: 
- COM
api_location: 
- Msident.dll
---

# IEnumUserIdentity::Clone method

\[**IEnumUserIdentity::Clone** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Gets a copy of the current enumeration.

## Syntax


```C++
HRESULT Clone(
  [out] IEnumUserIdentity **ppenum
);
```



## Parameters

<dl> <dt>

*ppenum* \[out\]
</dt> <dd>

Type: **[**IEnumUserIdentity**](ienumuseridentity.md)\*\***

The address of a pointer that receives a copy of this enumeration.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

[**IEnumUserIdentity**](ienumuseridentity.md) keeps an internal count that specifies which interface is next to be retrieved. The value of this count will be applied to the interface received by *ppenum*. To reset the count, call [**IEnumUserIdentity::Reset**](ienumuseridentity-reset.md).

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

[**IEnumUserIdentity::Reset**](ienumuseridentity-reset.md)
</dt> </dl>

 

 




