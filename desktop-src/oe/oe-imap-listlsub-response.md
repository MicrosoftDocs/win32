---
title: IMAP\_LISTLSUB\_RESPONSE structure
description: Returns the results of a LIST or LSUB response.
ms.assetid: 'ea012336-c773-4bfd-8d05-d9500e354bcb'
keywords: ["IMAP_LISTLSUB_RESPONSE structure Windows Mail (formerly Outlook Express)", "IMAPADDR structure Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- IMAPADDR
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# IMAP\_LISTLSUB\_RESPONSE structure

\[**IMAP\_LISTLSUB\_RESPONSE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the results of a LIST or LSUB response.

## Syntax


```C++
typedef struct tagIMAP_LISTLSUB_RESPONSE {
  LPSTR          pszMailboxName;
  IMAP_MBOXFLAGS imfMboxFlags;
  char           cHierarchyChar;
} IMAPADDR;
```



## Members

<dl> <dt>

**pszMailboxName**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the multibyte mailbox name.

</dd> <dt>

**imfMboxFlags**
</dt> <dd>

Type: **[**IMAP\_MBOXFLAGS**](oe-imap-mboxflags-constants.md)**

</dd> <dd>

Contains one or more values from the [**IMAP\_MBOXFLAGS**](oe-imap-mboxflags-constants.md) enumeration.

</dd> <dt>

**cHierarchyChar**
</dt> <dd>

Type: **char**

</dd> <dd>

Contains a **CHAR** that indicates the hierarchy delimiter used in the mailbox name. Contains a null character ("\\0") when the response returns "NIL" to indicate a flat tree mailbox structure.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





