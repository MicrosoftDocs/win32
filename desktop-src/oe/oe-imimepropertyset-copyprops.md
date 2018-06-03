---
title: IMimePropertySet CopyProps method
description: Copies a set of properties to another IMimePropertySet object.
ms.assetid: 17378dbb-973e-4b19-ba97-1c562bac60a6
keywords:
- CopyProps method Windows Mail (formerly Outlook Express)
- CopyProps method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , CopyProps method
topic_type:
- apiref
api_name:
- IMimePropertySet.CopyProps
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimePropertySet::CopyProps method

Copies a set of properties to another [**IMimePropertySet**](oe-imimepropertyset.md) object.

## Syntax


```C++
HRESULT CopyProps(
  [in] ULONG            cNames,
  [in] LPCSTR           *prgszName,
  [in] IMimePropertySet *pPropertySet
);
```



## Parameters

<dl> <dt>

*cNames* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the number of elements in the *prgszName* array. A client can pass 0 for this parameter and **NULL** for *prgszName* to copy all properties to *pPropertySet*.

</dd> <dt>

*prgszName* \[in\]
</dt> <dd>

Type: **LPCSTR\***

Specifies a pointer to an array of property names or property IDs to copy. If an entry in this array is **NULL**, the property is skipped without the method failing.

</dd> <dt>

*pPropertySet* \[in\]
</dt> <dd>

Type: **[**IMimePropertySet**](oe-imimepropertyset.md)\***

Specifies a pointer to the destination [**IMimePropertySet**](oe-imimepropertyset.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                                                                                                                                           |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>                                                                                                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *cNames* is equal to zero and *prgszName* is not **NULL** or *cNames* is greater than zero and *prgszName* is **NULL**. It may also indicate that *pPropertySet* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





