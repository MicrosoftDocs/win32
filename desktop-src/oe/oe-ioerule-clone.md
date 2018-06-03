---
title: IOERule Clone method
description: IOERule Clone is no longer available for use as of Windows Vista.
ms.assetid: a396b666-2ccb-437a-8a39-d3c678d1d7cd
keywords:
- Clone method Windows Mail (formerly Outlook Express)
- Clone method Windows Mail (formerly Outlook Express) , IOERule interface
- IOERule interface Windows Mail (formerly Outlook Express) , Clone method
topic_type:
- apiref
api_name:
- IOERule.Clone
api_location:
- Msoe.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOERule::Clone method

\[**IOERule::Clone** is no longer available for use as of Windows Vista.\]

Makes a duplicate rule object.

## Syntax


```C++
HRESULT Clone(
  [out] IOERule **ppIRule
);
```



## Parameters

<dl> <dt>

*ppIRule* \[out\]
</dt> <dd>

Type: **[**IOERule**](oe-ioerule.md)\*\***

Receives the address of a pointer to the new [**IOERule**](oe-ioerule.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppIRule* is **NULL**. <br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| End of client support<br/>    | Windows XP<br/>                                                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                                             |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





