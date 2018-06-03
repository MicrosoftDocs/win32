---
title: INETSERVER structure
description: Contains Internet server information.
ms.assetid: e61cd6f6-0884-4fd0-86af-2e2c96eecf9e
keywords:
- INETSERVER structure Windows Mail (formerly Outlook Express)
- LPINETSERVER structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- INETSERVER
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

# INETSERVER structure

\[**INETSERVER** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains Internet server information.

## Syntax


```C++
typedef struct INETSERVER {
  CHAR        szAccount[CCHMAX_ACCOUNT_NAME];
  CHAR        szUserName[CCHMAX_USERNAME];
  CHAR        szPassword[CCHMAX_PASSWORD];
  CHAR        szServerName[CCHMAX_SERVER_NAME];
  CHAR        szConnectoid[CCHMAX_CONNECTOID];
  RASCONNTYPE rasconntype;
  DWORD       dwPort;
  BOOL        fSSL;
  BOOL        fTrySicily;
  DWORD       dwTimeout;
  DWORD       dwFlags;
} INETSERVER, *LPINETSERVER;
```



## Members

<dl> <dt>

**szAccount**
</dt> <dd>

Type: **CHAR\[CCHMAX\_ACCOUNT\_NAME\]**

</dd> <dd>

Contains the IMN account name.

</dd> <dt>

**szUserName**
</dt> <dd>

Type: **CHAR\[CCHMAX\_USERNAME\]**

</dd> <dd>

Contains the user's connection name.

</dd> <dt>

**szPassword**
</dt> <dd>

Type: **CHAR\[CCHMAX\_PASSWORD\]**

</dd> <dd>

Contains the user's password.

</dd> <dt>

**szServerName**
</dt> <dd>

Type: **CHAR\[CCHMAX\_SERVER\_NAME\]**

</dd> <dd>

Contains the server name or IP address string.

</dd> <dt>

**szConnectoid**
</dt> <dd>

Type: **CHAR\[CCHMAX\_CONNECTOID\]**

</dd> <dd>

Contains the RAS connection name.

</dd> <dt>

**rasconntype**
</dt> <dd>

Type: **[**RASCONNTYPE**](oe-rasconntype.md)**

</dd> <dd>

Contains the RAS connection type.

</dd> <dt>

**dwPort**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the port name.

</dd> <dt>

**fSSL**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Indicates SSL usage.

</dd> <dt>

**fTrySicily**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Indicates SPA.

</dd> <dt>

**dwTimeout**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the server timeout in seconds.

</dd> <dt>

**dwFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains ISF\_*xxx* flags.



| Value                                                                                                                                                                                                   | Meaning                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ISF_SMTP_USEIPFORHELO"></span><span id="isf_smtp_useipforhelo"></span><dl> <dt>**ISF\_SMTP\_USEIPFORHELO**</dt> </dl>                  | Indicates a HELO or EHLO command. <br/>                                                                                                     |
| <span id="ISF_ALWAYSPROMPTFORPASSWORD"></span><span id="isf_alwayspromptforpassword"></span><dl> <dt>**ISF\_ALWAYSPROMPTFORPASSWORD**</dt> </dl> | Indicates that the password (Boolean) should never be saved for a HELO or EHLO command. <br/>                                               |
| <span id="ISF_SSLONSAMEPORT"></span><span id="isf_sslonsameport"></span><dl> <dt>**ISF\_SSLONSAMEPORT**</dt> </dl>                               | Indicates a starttls command for TLS (SMTP only). <br/>                                                                                     |
| <span id="ISF_QUERYDSNSUPPORT"></span><span id="isf_querydsnsupport"></span><dl> <dt>**ISF\_QUERYDSNSUPPORT**</dt> </dl>                         | Indicates that an EHLO command should be issued at connection time and that the transport should check for a DSN (SMTP only). <br/>         |
| <span id="ISF_QUERYAUTHSUPPORT"></span><span id="isf_queryauthsupport"></span><dl> <dt>**ISF\_QUERYAUTHSUPPORT**</dt> </dl>                      | Indicates that a EHLO command should be issued at connection time and that the transport should check for authentication (SMTP only). <br/> |



 

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





