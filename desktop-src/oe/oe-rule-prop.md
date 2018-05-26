---
title: RULE\_PROP enumeration
description: RULE\_PROP is no longer available for use as of Windows Vista.
ms.assetid: 5f2eadfd-033b-4bf6-963b-e996b8521754
keywords:
- RULE_PROP enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Oerules.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RULE\_PROP enumeration

\[**RULE\_PROP** is no longer available for use as of Windows Vista.\]

Identifies the various properties of message rules.

## Syntax


```C++
typedef enum tagRULE_PROP { 
  RULE_PROP_NAME       = 0,
  RULE_PROP_DISABLED   = 1,
  RULE_PROP_CRITERIA   = 2,
  RULE_PROP_ACTIONS    = 3,
  RULE_PROP_STATE      = 4,
  RULE_PROP_VERSION    = 5,
  RULE_PROP_READONLY   = 6,
  RULE_PROP_JUNKPCT    = 7,
  RULE_PROP_EXCPT_WAB  = 8,
  RULE_PROP_MAX        = 9
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="RULE_PROP_NAME"></span><span id="rule_prop_name"></span>**RULE\_PROP\_NAME**
</dt> <dd>

Indicates the name of a rule.

</dd> <dt>

<span id="RULE_PROP_DISABLED"></span><span id="rule_prop_disabled"></span>**RULE\_PROP\_DISABLED**
</dt> <dd>

Indicates the enabled state of a rule.

</dd> <dt>

<span id="RULE_PROP_CRITERIA"></span><span id="rule_prop_criteria"></span>**RULE\_PROP\_CRITERIA**
</dt> <dd>

Indicates the conditions under which a rule applies.

</dd> <dt>

<span id="RULE_PROP_ACTIONS"></span><span id="rule_prop_actions"></span>**RULE\_PROP\_ACTIONS**
</dt> <dd>

Indicates the actions a rule executes.

</dd> <dt>

<span id="RULE_PROP_STATE"></span><span id="rule_prop_state"></span>**RULE\_PROP\_STATE**
</dt> <dd>

Indicates the state of a rule.

</dd> <dt>

<span id="RULE_PROP_VERSION"></span><span id="rule_prop_version"></span>**RULE\_PROP\_VERSION**
</dt> <dd>

Indicates the version number of a copied rule.

</dd> <dt>

<span id="RULE_PROP_READONLY"></span><span id="rule_prop_readonly"></span>**RULE\_PROP\_READONLY**
</dt> <dd>

Indicates the read/write state of a rule.

</dd> <dt>

<span id="RULE_PROP_JUNKPCT"></span><span id="rule_prop_junkpct"></span>**RULE\_PROP\_JUNKPCT**
</dt> <dd>

Indicates the percentage of blocked senders.

</dd> <dt>

<span id="RULE_PROP_EXCPT_WAB"></span><span id="rule_prop_excpt_wab"></span>**RULE\_PROP\_EXCPT\_WAB**
</dt> <dd>

Indicates WAB usage.

</dd> <dt>

<span id="RULE_PROP_MAX"></span><span id="rule_prop_max"></span>**RULE\_PROP\_MAX**
</dt> <dd>

Indicates the total number of values in this enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Oerules.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl> |



 

 





