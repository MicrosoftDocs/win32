---
title: INNTPTransport CommandSTAT method
description: Issues a STAT command to the server.
ms.assetid: '52d0c4fd-b2b7-4778-9273-da83d5fb2dc3'
keywords: ["CommandSTAT method Windows Mail (formerly Outlook Express)", "CommandSTAT method Windows Mail (formerly Outlook Express) , INNTPTransport interface", "INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandSTAT method"]
topic_type:
- apiref
api_name:
- INNTPTransport.CommandSTAT
api_location:
- Inetcomm.dll
api_type:
- COM
---

# INNTPTransport::CommandSTAT method

\[**INNTPTransport::CommandSTAT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Issues a `STAT` command to the server. If an article is specified, then this command has the effect of moving the current article pointer to the specified message and returning the article number and message ID of the new current article. Otherwise, the function returns the article number and message ID of the current article.

## Syntax


```C++
HRESULT CommandSTAT(
  [in] LPARTICLEID pArticleId
);
```



## Parameters

<dl> <dt>

*pArticleId* \[in\]
</dt> <dd>

Type: **LPARTICLEID**

Article number or message ID of the article to retrieve status for. If a message ID is specified, the current article pointer will NOT be updated.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                           | Description                            |
|-------------------------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>          | pArticleId is not valid<br/>     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>         | An memory allocation failed<br/> |
| <dl> <dt>**IXP\_E\_NOT\_INIT**</dt> </dl>      |                                        |
| <dl> <dt>**IXP\_E\_NOT\_CONNECTED**</dt> </dl> |                                        |
| <dl> <dt>**IXP\_E\_BUSY**</dt> </dl>           |                                        |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





