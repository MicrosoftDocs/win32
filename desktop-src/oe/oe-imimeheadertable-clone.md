---
title: IMimeHeaderTable Clone method
description: Creates another header table object that is an exact replica of the current header table object. The new header table object has no association with the current header table object.
ms.assetid: e6997643-ffb0-4c18-bccb-4e30251082ab
keywords:
- Clone method Windows Mail (formerly Outlook Express)
- Clone method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , Clone method
topic_type:
- apiref
api_name:
- IMimeHeaderTable.Clone
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

# IMimeHeaderTable::Clone method

Creates another header table object that is an exact replica of the current header table object. The new header table object has no association with the current header table object.

## Syntax


```C++
HRESULT Clone(
  [out] IMimeHeaderTable **ppTable
);
```



## Parameters

<dl> <dt>

*ppTable* \[out\]
</dt> <dd>

Type: **[**IMimeHeaderTable**](oe-imimeheadertable.md)\*\***

Receives the address of a pointer to the new [**IMimeHeaderTable**](oe-imimeheadertable.md) object. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppTable* is **NULL**. <br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred.<br/>         |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





