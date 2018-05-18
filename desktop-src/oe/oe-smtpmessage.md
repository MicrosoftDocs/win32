---
title: SMTPMESSAGE structure
description: Holds a Simple Mail Transport Protocol (SMTP) message.
ms.assetid: '175f82bc-1f14-4d25-b62a-cfc4c1346bbf'
keywords: ["SMTPMESSAGE structure Windows Mail (formerly Outlook Express)", "LPSMTPMESSAGE structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- SMTPMESSAGE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# SMTPMESSAGE structure

\[**SMTPMESSAGE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Holds a Simple Mail Transport Protocol (SMTP) message.

## Syntax


```C++
typedef struct tagSMTPMESSAGE {
  ULONG        cbSize;
  LPSTREAM     pstmMsg;
  INETADDRLIST rAddressList;
} SMTPMESSAGE, *LPSMTPMESSAGE;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains a **ULONG** that contains the size of the message in bytes.

</dd> <dt>

**pstmMsg**
</dt> <dd>

Type: **LPSTREAM**

</dd> <dd>

Contains a pointer to an [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the ANSI MIME/[RFC 822](http://www.ietf.org/rfc/rfc822.txt) message stream.

</dd> <dt>

**rAddressList**
</dt> <dd>

Type: **[**INETADDRLIST**](oe-inetaddrlist.md)**

</dd> <dd>

Contains the [**INETADDRLIST**](oe-inetaddrlist.md) that contains sender and recipients.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





