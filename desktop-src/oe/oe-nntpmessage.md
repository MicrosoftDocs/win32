---
title: NNTPMESSAGE structure
description: This structure provides the information needed to post a message to the news server using the POST command.
ms.assetid: '252daac7-0601-44e3-8f55-ab29b53e8974'
keywords: ["NNTPMESSAGE structure Windows Mail (formerly Outlook Express)", "LPNNTPMESSAGE structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- NNTPMESSAGE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# NNTPMESSAGE structure

\[**NNTPMESSAGE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This structure provides the information needed to post a message to the news server using the POST command.

## Syntax


```C++
typedef struct tagNNTPMESSAGE {
  ULONG    cbSize;
  LPSTREAM pstmMsg;
} NNTPMESSAGE, *LPNNTPMESSAGE;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Size of the message in bytes

</dd> <dt>

**pstmMsg**
</dt> <dd>

Type: **LPSTREAM**

</dd> <dd>

Stream containing a ANSI MIME/rfc822/rfc1036 message stream

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





