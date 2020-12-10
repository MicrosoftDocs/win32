---
title: MPTHREAT_LOCALIZED_INFO structure (MpClient.h)
description: Localized information for a threat.
ms.assetid: 99DC9737-9A61-4407-B544-A7A979C5B556
keywords:
- MPTHREAT_LOCALIZED_INFO structure Legacy Windows Environment Features
- PMPTHREAT_LOCALIZED_INFO structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_LOCALIZED_INFO
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_LOCALIZED\_INFO structure

Localized information for a threat.

## Syntax


```C++
typedef struct tagMPTHREAT_LOCALIZED_INFO {
  MPTHREAT_ID           ThreatID;
  MP_MIDL_STRING LPWSTR CategoryName;
  MP_MIDL_STRING LPWSTR CategoryDescription;
  MP_MIDL_STRING LPWSTR SeverityName;
  MP_MIDL_STRING LPWSTR SeverityDescription;
  MP_MIDL_STRING LPWSTR ShortDescription;
  MP_MIDL_STRING LPWSTR DefaultActionName;;
  MP_MIDL_STRING LPWSTR Advice;
  MP_MIDL_STRING LPWSTR ThreatUrl;
} MPTHREAT_LOCALIZED_INFO, *PMPTHREAT_LOCALIZED_INFO;
```



## Members

<dl> <dt>

**ThreatID**
</dt> <dd>

Type: **MPTHREAT\_ID**

</dd> <dd>

Threat identifier. Upper bit is set to identify antivirus-related threats.

</dd> <dt>

**CategoryName**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Threat classification, such as a trojan or a keylogger.

</dd> <dt>

**CategoryDescription**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Description of threat category.

</dd> <dt>

**SeverityName**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Threat severity level, such as severe or moderate.

</dd> <dt>

**SeverityDescription**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Description of threat severity level.

</dd> <dt>

**ShortDescription**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Short description of threat.

</dd> <dt>

**DefaultActionName;**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Name of default action, such as remove or quarantine, suggested by engine.

</dd> <dt>

**Advice**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

Advice for the particular threat.

</dd> <dt>

**ThreatUrl**
</dt> <dd>

Type: **MP\_MIDL\_STRING LPWSTR**

</dd> <dd>

A URL to a webpage containing information about the threat.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





