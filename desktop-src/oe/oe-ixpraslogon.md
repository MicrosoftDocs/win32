---
title: IXPRASLOGON structure
description: Holds connection information for establishing a Remote Access Service (RAS) session.
ms.assetid: '5a02052e-3cd7-407d-8195-881ad46dcc5d'
keywords: ["IXPRASLOGON structure Windows Mail (formerly Outlook Express)", "LPIXPRASLOGON structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- IXPRASLOGON
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# IXPRASLOGON structure

\[**IXPRASLOGON** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Holds connection information for establishing a Remote Access Service (RAS) session.

## Syntax


```C++
typedef struct tagIXPRASLOGON {
  CHAR szConnectoid[CCHMAX_CONNECTOID];
  CHAR szUserName[CCHMAX_USERNAME];
  CHAR szPassword[CCHMAX_PASSWORD];
  CHAR szDomain[CCHMAX_DOMAIN];
  CHAR szPhoneNumber[CCHMAX_PHONE_NUMBER];
  BOOL fSavePassword;
} IXPRASLOGON, *LPIXPRASLOGON;
```



## Members

<dl> <dt>

**szConnectoid**
</dt> <dd>

Type: **CHAR\[CCHMAX\_CONNECTOID\]**

</dd> <dd>

Contains a **\_\_wchar\_t** that contains the phone book entry used to establish the remote access connection.

</dd> <dt>

**szUserName**
</dt> <dd>

Type: **CHAR\[CCHMAX\_USERNAME\]**

</dd> <dd>

Contains a **\_\_wchar\_t** that contains the user ID.

</dd> <dt>

**szPassword**
</dt> <dd>

Type: **CHAR\[CCHMAX\_PASSWORD\]**

</dd> <dd>

Contains a **\_\_wchar\_t** that contains the user password.

</dd> <dt>

**szDomain**
</dt> <dd>

Type: **CHAR\[CCHMAX\_DOMAIN\]**

</dd> <dd>

Contains a **\_\_wchar\_t** that contains the domain name for the connection.

</dd> <dt>

**szPhoneNumber**
</dt> <dd>

Type: **CHAR\[CCHMAX\_PHONE\_NUMBER\]**

</dd> <dd>

Contains a **\_\_wchar\_t** that contains the dial-up number.

</dd> <dt>

**fSavePassword**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether to preserve the user password.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





