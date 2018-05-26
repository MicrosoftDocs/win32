---
title: INNTPTransport CommandLIST method
description: Sends a LIST command to the news server.
ms.assetid: d575c99e-2b23-4faf-a074-743205310336
keywords:
- CommandLIST method Windows Mail (formerly Outlook Express)
- CommandLIST method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandLIST method
topic_type:
- apiref
api_name:
- INNTPTransport.CommandLIST
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

# INNTPTransport::CommandLIST method

\[**INNTPTransport::CommandLIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends a `LIST` command to the news server. If *pszArgs* is **NULL**, then the command retrieves a list of newsgroups available on the news server. The *pszArgs* parameter can be used to issue one of the various extensions to the `LIST` command, ie. LIST NEWSGROUPS, LIST ACTIVE, LIST OVERVIEW.FMT, or LIST SUBSCRIPTIONS. See RFC 977 at http://ds.internic.net/rfc/rfc977.txt for a full list of extensions.

## Syntax


```C++
HRESULT CommandLIST(
  [in] LPSTR pszArgs
);
```



## Parameters

<dl> <dt>

*pszArgs* \[in\]
</dt> <dd>

Type: **LPSTR**

Any optional parameters that the user wants to send with the LIST command.

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



 

 





