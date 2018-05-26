---
title: CMS\_CTRL\_DECRYPT\_INFO structure
description: Do not use. A union that contains key transport message recipient information, key agreement recipient information, or mail list message recipient information.
ms.assetid: a14741a3-e604-458c-be45-3cbd1d072c05
keywords:
- CMS_CTRL_DECRYPT_INFO structure Windows Mail (formerly Outlook Express)
- PCMS_CTRL_DECRYPT_INFO structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- CMS_CTRL_DECRYPT_INFO
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMS\_CTRL\_DECRYPT\_INFO structure

\[The **CMS\_CTRL\_DECRYPT\_INFO** structure is available for use in Windows XP. It might be altered or unavailable in subsequent versions.\]

Do not use. A union that contains key transport message recipient information, key agreement recipient information, or mail list message recipient information.

## Syntax


```C++
typedef struct tagCMS_CTRL_DECRYPT_INFO {
  CMSG_CTRL_KEY_TRANS_DECRYPT_PARA trans;
  CMSG_CTRL_KEY_AGREE_DECRYPT_PARA agree;
  CMSG_CTRL_MAIL_LIST_DECRYPT_PARA maillist;
} CMS_CTRL_DECRYPT_INFO, *PCMS_CTRL_DECRYPT_INFO;
```



## Members

<dl> <dt>

**trans**
</dt> <dd>

Type: **[CMSG\_CTRL\_KEY\_TRANS\_DECRYPT\_PARA](http://msdn.microsoft.com/library/seccrypto/security/cmsg_ctrl_key_trans_decrypt_para.asp)**

</dd> <dd>

Contains a [CMSG\_CTRL\_KEY\_TRANS\_DECRYPT\_PARA](http://msdn.microsoft.com/library/seccrypto/security/cmsg_ctrl_key_trans_decrypt_para.asp) structure.

</dd> <dt>

**agree**
</dt> <dd>

Type: **[CMSG\_CTRL\_KEY\_AGREE\_DECRYPT\_PARA](http://msdn.microsoft.com/library/seccrypto/security/cmsg_ctrl_key_agree_decrypt_para.asp)**

</dd> <dd>

Contains a [CMSG\_CTRL\_KEY\_AGREE\_DECRYPT\_PARA](http://msdn.microsoft.com/library/seccrypto/security/cmsg_ctrl_key_agree_decrypt_para.asp) structure.

</dd> <dt>

**maillist**
</dt> <dd>

Type: **[CMSG\_CTRL\_MAIL\_LIST\_DECRYPT\_PARA](http://msdn.microsoft.com/library/seccrypto/security/cmsg_ctrl_mail_list_decrypt_para.asp)**

</dd> <dd>

Contains a [CMSG\_CTRL\_MAIL\_LIST\_DECRYPT\_PARA](http://msdn.microsoft.com/library/seccrypto/security/cmsg_ctrl_mail_list_decrypt_para.asp) structure.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





