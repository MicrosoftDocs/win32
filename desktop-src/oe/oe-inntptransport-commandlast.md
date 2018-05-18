---
title: INNTPTransport CommandLAST method
description: Issues the LAST command to the server.
ms.assetid: '27fb9051-8217-46df-a79e-8ff55ef630a0'
keywords: ["CommandLAST method Windows Mail (formerly Outlook Express)", "CommandLAST method Windows Mail (formerly Outlook Express) , INNTPTransport interface", "INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandLAST method"]
topic_type:
- apiref
api_name:
- INNTPTransport.CommandLAST
api_location:
- Inetcomm.dll
api_type:
- COM
---

# INNTPTransport::CommandLAST method

\[**INNTPTransport::CommandLAST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Issues the `LAST` command to the server. This has the effect of moving the current article pointer to the article immediately preceding the current article pointer in the newsgroup. This command is only valid if a `GROUP` command has been issued previously. The article number and message-id pointed to by the new current article pointer are returned in [**OnResponse**](oe-inntpcallback-onresponse.md).

## Syntax


```C++
HRESULT CommandLAST();
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
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





