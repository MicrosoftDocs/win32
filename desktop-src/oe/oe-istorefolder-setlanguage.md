---
title: IStoreFolder SetLanguage method
description: Sets the language codepage for a specified list of messages within the folder.
ms.assetid: cb4bae0d-1b02-4e28-8e55-36002be8f4ea
keywords:
- SetLanguage method Windows Mail (formerly Outlook Express)
- SetLanguage method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , SetLanguage method
topic_type:
- apiref
api_name:
- IStoreFolder.SetLanguage
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

# IStoreFolder::SetLanguage method

Sets the language codepage for a specified list of messages within the folder.

## Syntax


```C++
HRESULT SetLanguage(
  [in] DWORD           dwLanguage,
  [in] DWORD           dwReserved,
  [in] LPMESSAGEIDLIST pMsgIdList
);
```



## Parameters

<dl> <dt>

*dwLanguage* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the codepage to apply to each of the messages in the list.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*pMsgIdList* \[in\]
</dt> <dd>

Type: **LPMESSAGEIDLIST**

Pointer to a [**MESSAGEIDLIST**](oe-messageidlist.md) structure that specifies the list of messages that will have their language set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error value.



| Return code                                                                                  | Description                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Occurs if the value of *dwReserved* is not 0, if *pMsgIdList* is **NULL**, or if the **prgdwMsgId** member value of the structure referenced by *pMsgIdList* is **NULL**.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IStoreFolder**](oe-istorefolder.md)
</dt> <dt>

[**CODEPAGEID**](oe-codepageid-constants.md)
</dt> </dl>

 

 





