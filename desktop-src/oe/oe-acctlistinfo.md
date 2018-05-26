---
title: ACCTLISTINFO structure
description: Contains information about an account list for display in a dialog box.
ms.assetid: dd86931f-57cb-474c-9076-cfe4c707ffa9
keywords:
- ACCTLISTINFO structure Windows Mail (formerly Outlook Express)
- ACCESSTYPE structure Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnact.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ACCTLISTINFO structure

\[**ACCTLISTINFO** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains information about an account list for display in a dialog box.

## Syntax


```C++
typedef struct tagACCTLISTINFO {
  DWORD    cbSize;
  ACCTTYPE AcctTypeInit;
  DWORD    dwAcctFlags;
  DWORD    dwFlags;
} ACCESSTYPE;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that indicates the size of the account list.

</dd> <dt>

**AcctTypeInit**
</dt> <dd>

Type: **[**ACCTTYPE**](oe-accttype.md)**

</dd> <dd>

Contains a [**ACCTTYPE**](oe-accttype.md) value that indicates the account list type.

</dd> <dt>

**dwAcctFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that indicates the account type flag.

<dl><span id="ACCT_FLAG_NEWS"></span><span id="acct_flag_news"></span><dt>

**ACCT\_FLAG\_NEWS**
</dt><span id="ACCT_FLAG_MAIL"></span><span id="acct_flag_mail"></span><dt>

**ACCT\_FLAG\_MAIL**
</dt><span id="ACCT_FLAG_DIR_SERV"></span><span id="acct_flag_dir_serv"></span><dt>

**ACCT\_FLAG\_DIR\_SERV**
</dt> </dl> </dd> <dt>

**dwFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains dialog initialization information.

<dl> <dt>

<span id="ACCTDLG_NO_IMAP"></span><span id="acctdlg_no_imap"></span>**ACCTDLG\_NO\_IMAP** (0x0001)
</dt> <dt>

<span id="ACCTDLG_NO_REMOVEDELETE"></span><span id="acctdlg_no_removedelete"></span>**ACCTDLG\_NO\_REMOVEDELETE** (0x0002)
</dt> <dt>

<span id="ACCTDLG_NO_BREAKMESSAGES"></span><span id="acctdlg_no_breakmessages"></span>**ACCTDLG\_NO\_BREAKMESSAGES** (0x0004)
</dt> <dt>

<span id="ACCTDLG_NO_REMOVEAFTER"></span><span id="acctdlg_no_removeafter"></span>**ACCTDLG\_NO\_REMOVEAFTER** (0x0008)
</dt> <dt>

<span id="ACCTDLG_NO_SENDRECEIVE"></span><span id="acctdlg_no_sendreceive"></span>**ACCTDLG\_NO\_SENDRECEIVE** (0x0010)
</dt> <dt>

<span id="ACCTDLG_NO_NEWSPOLL"></span><span id="acctdlg_no_newspoll"></span>**ACCTDLG\_NO\_NEWSPOLL** (0x0020)
</dt> <dt>

<span id="ACCTDLG_NO_SECURITY"></span><span id="acctdlg_no_security"></span>**ACCTDLG\_NO\_SECURITY** (0x0040)
</dt> <dt>

<span id="ACCTDLG_BACKUP_CONNECT"></span><span id="acctdlg_backup_connect"></span>**ACCTDLG\_BACKUP\_CONNECT** (0x0080)
</dt> <dt>

<span id="ACCTDLG_NO_IMAPPOLL"></span><span id="acctdlg_no_imappoll"></span>**ACCTDLG\_NO\_IMAPPOLL** (0x0100)
</dt> <dt>

<span id="ACCTDLG_NO_NEW_POP"></span><span id="acctdlg_no_new_pop"></span>**ACCTDLG\_NO\_NEW\_POP** (0x0200)
</dt> <dt>

<span id="ACCTDLG_SHOWIMAPSPECIAL"></span><span id="acctdlg_showimapspecial"></span>**ACCTDLG\_SHOWIMAPSPECIAL** (0x0400)
</dt> <dt>

<span id="ACCTDLG_INTERNETCONNECTION"></span><span id="acctdlg_internetconnection"></span>**ACCTDLG\_INTERNETCONNECTION** (0x0800)
</dt> <dt>

<span id="ACCTDLG_HTTPMAIL"></span><span id="acctdlg_httpmail"></span>**ACCTDLG\_HTTPMAIL** (0x1000)
</dt> <dt>

<span id="ACCTDLG_REVOCATION"></span><span id="acctdlg_revocation"></span>**ACCTDLG\_REVOCATION** (0x2000)
</dt> <dt>

<span id="ACCTDLG_OE"></span><span id="acctdlg_oe"></span>**ACCTDLG\_OE** (0x4000)
</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





