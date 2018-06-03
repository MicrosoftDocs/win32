---
title: IMAPADDR structure
description: Contains various fields inside the parentheses of an Internet Message Access Protocol (IMAP) address defined in the \ 0034;Formal Syntax \ 0034; section of RFC 2060.
ms.assetid: 98c5db50-cb50-45a1-a526-3b87eb42a9e3
keywords:
- IMAPADDR structure Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- IMAPADDR
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IMAPADDR structure

\[**IMAPADDR** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains various fields inside the parentheses of an Internet Message Access Protocol (IMAP) address defined in the "Formal Syntax" section of [RFC 2060](http://www.ietf.org/rfc/rfc2060.txt).

## Syntax


```C++
typedef struct tagIMAPADDR {
  LPSTR    pszName;
  LPSTR    pszADL;
  LPSTR    pszMailbox;
  LPSTR    pszHost;
  IMAPADDR *pNext;
} IMAPADDR;
```



## Members

<dl> <dt>

**pszName**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the addr\_name string defined in the "Formal Syntax" section of [RFC 2060](http://www.ietf.org/rfc/rfc2060.txt).

</dd> <dt>

**pszADL**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the addr\_adl string defined in the "Formal Syntax" section of [RFC 2060](http://www.ietf.org/rfc/rfc2060.txt).

</dd> <dt>

**pszMailbox**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the addr\_mailbox string defined in the "Formal Syntax" section of [RFC 2060](http://www.ietf.org/rfc/rfc2060.txt).

</dd> <dt>

**pszHost**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the addr\_host string defined in the "Formal Syntax" section of [RFC 2060](http://www.ietf.org/rfc/rfc2060.txt).

</dd> <dt>

**pNext**
</dt> <dd>

Type: ****IMAPADDR**\***

</dd> <dd>

Contains a pointer to the next **IMAPADDR** structure in the chain.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





