---
title: IOEEnumRules Next method
description: IOEEnumRules Next is no longer available for use as of Windows Vista.
ms.assetid: 1ef5d50f-db1b-472b-ba74-10e7f916f02a
keywords:
- Next method Windows Mail (formerly Outlook Express)
- Next method Windows Mail (formerly Outlook Express) , IOEEnumRules interface
- IOEEnumRules interface Windows Mail (formerly Outlook Express) , Next method
topic_type:
- apiref
api_name:
- IOEEnumRules.Next
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

# IOEEnumRules::Next method

\[**IOEEnumRules::Next** is no longer available for use as of Windows Vista.\]

Retrieves the next specified number of elements in the enumeration sequence.

## Syntax


```C++
HRESULT Next(
  [in]  ULONG   cpIRule,
  [out] IOERule **rgpIRule,
  [out] ULONG   *pcpIRuleFetched
);
```



## Parameters

<dl> <dt>

*cpIRule* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that indicates the number of requested elements.

</dd> <dt>

*rgpIRule* \[out\]
</dt> <dd>

Type: **[**IOERule**](oe-ioerule.md)\*\***

Receives the address of a pointer to the array of retrieved [**IOERule**](oe-ioerule.md) objects. The client is responsible for releasing these objects.

</dd> <dt>

*pcpIRuleFetched* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of elements that were retrieved.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates that the method retrieved the number of elements specified by *cpIRule*. <br/>           |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates that the method retrieved fewer than the number of elements specified by *cpIRule*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                                          |



 

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



 

 





