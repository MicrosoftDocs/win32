---
title: RULE\_TYPE enumeration
description: RULE\_TYPE is no longer available for use as of Windows Vista.
ms.assetid: 'a9f11be8-525f-4505-acf6-e4fc4f6b5482'
keywords: ["RULE_TYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Oerules.idl
api_type:
- IDLDef
---

# RULE\_TYPE enumeration

\[**RULE\_TYPE** is no longer available for use as of Windows Vista.\]

Identifies types of rules.

## Syntax


```C++
typedef enum tagRULE_TYPE { 
  RULE_TYPE_MAIL    = 0,
  RULE_TYPE_NEWS    = 1,
  RULE_TYPE_FILTER  = 2,
  RULE_TYPE_MAX     = 3
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="RULE_TYPE_MAIL"></span><span id="rule_type_mail"></span>**RULE\_TYPE\_MAIL**
</dt> <dd>

Indicates a rule for email messages.

</dd> <dt>

<span id="RULE_TYPE_NEWS"></span><span id="rule_type_news"></span>**RULE\_TYPE\_NEWS**
</dt> <dd>

Indicates a rule for newsgroups.

</dd> <dt>

<span id="RULE_TYPE_FILTER"></span><span id="rule_type_filter"></span>**RULE\_TYPE\_FILTER**
</dt> <dd>

Indicates a rule for blocking messages from certain senders.

</dd> <dt>

<span id="RULE_TYPE_MAX"></span><span id="rule_type_max"></span>**RULE\_TYPE\_MAX**
</dt> <dd>

Total number of rule types.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl> |



 

 





