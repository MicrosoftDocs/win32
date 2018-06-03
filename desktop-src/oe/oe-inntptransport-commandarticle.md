---
title: INNTPTransport CommandARTICLE method
description: This function is used to request an article from the server.
ms.assetid: bcaf0a21-af89-4088-8e7d-3e275a777d39
keywords:
- CommandARTICLE method Windows Mail (formerly Outlook Express)
- CommandARTICLE method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandARTICLE method
topic_type:
- apiref
api_name:
- INNTPTransport.CommandARTICLE
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

# INNTPTransport::CommandARTICLE method

\[**INNTPTransport::CommandARTICLE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This function is used to request an article from the server. If the caller has previously issued a `GROUP` command then the article can be specified by either article number or message-id. If the `GROUP` command has not been issued, then the article can only be requested by message-id.

## Syntax


```C++
HRESULT CommandARTICLE(
  [in] LPARTICLEID pArticleId
);
```



## Parameters

<dl> <dt>

*pArticleId* \[in\]
</dt> <dd>

Type: **LPARTICLEID**

Either the article number or message-id of the article to retrieve.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | An invalid parameter was passed in<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | A memory allocation failed<br/>         |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





