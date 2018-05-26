---
title: IMimePropertySet EnumProps method
description: Enumerates the properties in the property set.
ms.assetid: 2c1449d3-9fbe-4562-bbbb-7b8935659315
keywords:
- EnumProps method Windows Mail (formerly Outlook Express)
- EnumProps method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , EnumProps method
topic_type:
- apiref
api_name:
- IMimePropertySet.EnumProps
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimePropertySet::EnumProps method

Enumerates the properties in the property set.

## Syntax


```C++
HRESULT EnumProps(
  [in]  DWORD               dwFlags,
  [out] IMimeEnumProperties **ppEnum
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that indicates how the enumerator works.



| Value                                                                                                                                                                                                                | Meaning                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EPF_NONAME"></span><span id="epf_noname"></span><dl> <dt>**EPF\_NONAME**</dt> <dt>0x00000001</dt> </dl> | Indicates that the **pszName** field is not needed when enumerating the properties using the [**IMimeEnumProperties**](oe-imimeenumproperties.md). <br/> |



 

</dd> <dt>

*ppEnum* \[out\]
</dt> <dd>

Type: **[**IMimeEnumProperties**](oe-imimeenumproperties.md)\*\***

Receives the address of a pointer to the [**IMimeEnumProperties**](oe-imimeenumproperties.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppEnum* is **NULL**. <br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





