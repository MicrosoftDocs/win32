---
title: INNTPTransport CommandNEXT method
description: Issues the NEXT command to the server.
ms.assetid: 0870c0e9-5b14-4e9c-a841-4252b55241ab
keywords:
- CommandNEXT method Windows Mail (formerly Outlook Express)
- CommandNEXT method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandNEXT method
topic_type:
- apiref
api_name:
- INNTPTransport.CommandNEXT
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

# INNTPTransport::CommandNEXT method

\[**INNTPTransport::CommandNEXT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Issues the `NEXT` command to the server. This has the effect of moving the current article pointer to the article immediately after the current article pointer in the newsgroup. This command is only valid if a `GROUP` command has been issued previously. The article number and message-id pointed to by the new current article pointer are returned in [**OnResponse**](oe-inntpcallback-onresponse.md).

## Syntax


```C++
HRESULT CommandNEXT();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.

<dl> <dt>

**S\_OK**
</dt> <dt>

**E\_OUTOFMEMORY**
</dt> <dt>

**IXP\_E\_NOT\_INIT**
</dt> <dt>

**IXP\_E\_NOT\_CONNECTED**
</dt> <dt>

**IXP\_E\_BUSY**
</dt> </dl>

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





