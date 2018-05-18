---
title: IMimePropertySet Clone method
description: Clones the current IMimePropertySet object. The new property set is an exact replica of the original and has no association with the original property set.
ms.assetid: '85f9371a-775a-45c6-a5f7-ccda8daf9dd2'
keywords: ["Clone method Windows Mail (formerly Outlook Express)", "Clone method Windows Mail (formerly Outlook Express) , IMimePropertySet interface", "IMimePropertySet interface Windows Mail (formerly Outlook Express) , Clone method"]
topic_type:
- apiref
api_name:
- IMimePropertySet.Clone
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimePropertySet::Clone method

Clones the current [**IMimePropertySet**](oe-imimepropertyset.md) object. The new property set is an exact replica of the original and has no association with the original property set.

## Syntax


```C++
HRESULT Clone(
  [out] IMimePropertySet **ppPropertySet
);
```



## Parameters

<dl> <dt>

*ppPropertySet* \[out\]
</dt> <dd>

Type: **[**IMimePropertySet**](oe-imimepropertyset.md)\*\***

Receives the address of a pointer to the new [**IMimePropertySet**](oe-imimepropertyset.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppPropertySet* is **NULL**. <br/>         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





