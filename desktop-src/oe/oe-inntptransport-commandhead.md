---
title: INNTPTransport CommandHEAD method
description: Retrieves just the header for the requested article.
ms.assetid: 8064e31a-ca55-4c1e-abf3-c1f5ccbcad88
keywords:
- CommandHEAD method Windows Mail (formerly Outlook Express)
- CommandHEAD method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandHEAD method
topic_type:
- apiref
api_name:
- INNTPTransport.CommandHEAD
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

# INNTPTransport::CommandHEAD method

\[**INNTPTransport::CommandHEAD** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves just the header for the requested article. If the caller has previously issued a `GROUP` command, then the article can be specified by either article number or message-id. Otherwise, the article must be requested by message-id. The provided stream will be filled and returned to the caller in [**OnResponse**](oe-inntpcallback-onresponse.md).

## Syntax


```C++
HRESULT CommandHEAD(
  [in] LPARTICLEID pArticleId
);
```



## Parameters

<dl> <dt>

*pArticleId* \[in\]
</dt> <dd>

Type: **LPARTICLEID**

Structure specifying the article to retrieve the header for.

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



 

 





