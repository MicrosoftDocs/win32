---
title: IOEEnumRules Clone method
description: IOEEnumRules Clone is no longer available for use as of Windows Vista.
ms.assetid: '828f2dca-8e1a-484d-b297-3a9acd6eedd6'
keywords: ["Clone method Windows Mail (formerly Outlook Express)", "Clone method Windows Mail (formerly Outlook Express) , IOEEnumRules interface", "IOEEnumRules interface Windows Mail (formerly Outlook Express) , Clone method"]
topic_type:
- apiref
api_name:
- IOEEnumRules.Clone
api_location:
- Msoe.dll
api_type:
- COM
---

# IOEEnumRules::Clone method

\[**IOEEnumRules::Clone** is no longer available for use as of Windows Vista.\]

Creates another enumerator that contains the same enumeration state as the current one.

## Syntax


```C++
HRESULT Clone(
  [out] IOEEnumRules **ppIEnumRules
);
```



## Parameters

<dl> <dt>

*ppIEnumRules* \[out\]
</dt> <dd>

Type: **[**IOEEnumRules**](oe-ioeenumrules.md)\*\***

Receives the address of a pointer to the new [**IOEEnumRules**](oe-ioeenumrules.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppIEnumRules* is **NULL**. <br/>          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| End of client support<br/>    | Windows XP<br/>                                                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                                             |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





