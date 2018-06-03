---
title: IImnEnumAccounts GetNext method
description: Gets the next account object in the enumeration.
ms.assetid: 5387563a-6ae2-4cac-bcf6-740131ee390d
keywords:
- GetNext method Windows Mail (formerly Outlook Express)
- GetNext method Windows Mail (formerly Outlook Express) , IImnEnumAccounts interface
- IImnEnumAccounts interface Windows Mail (formerly Outlook Express) , GetNext method
topic_type:
- apiref
api_name:
- IImnEnumAccounts.GetNext
api_location:
- Msoeacct.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IImnEnumAccounts::GetNext method

\[**IImnEnumAccounts::GetNext** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the next account object in the enumeration.

## Syntax


```C++
HRESULT GetNext(
  [out] IImnAccount **ppAccount
);
```



## Parameters

<dl> <dt>

*ppAccount* \[out\]
</dt> <dd>

Type: **[**IImnAccount**](oe-iimnaccount.md)\*\***

Receives the address of a pointer to the next [**IImnAccount**](oe-iimnaccount.md) object in the enumeration. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                    | Description                                                                                                   |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>           | Indicates success.<br/>                                                                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>   | Indicates that *ppAccount* is **NULL**.<br/>                                                            |
| <dl> <dt>**E\_EnumFinished**</dt> </dl> | Indicates that the end of the enumeration has been reached and there are no more account objects. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





