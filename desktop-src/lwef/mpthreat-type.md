---
title: MPTHREAT_TYPE enumeration (MpClient.h)
description: Possible threat types.
ms.assetid: 56061F12-AA89-4203-BED4-99613E24002A
keywords:
- MPTHREAT_TYPE enumeration Legacy Windows Environment Features
- PMPTHREAT_TYPE enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_TYPE
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_TYPE enumeration

Possible threat types.

## Syntax


```C++
typedef enum tagMPTHREAT_TYPE { 
  MPTHREAT_TYPE_KNOWNBAD   = 0,
  MPTHREAT_TYPE_BEHAVIOR   = 1,
  MPTHREAT_TYPE_UNKNOWN    = 2,
  MPTHREAT_TYPE_KNOWNGOOD  = 3,
  MPTHREAT_TYPE_NIS        = 4,
  MPTHREAT_TYPE_MAXVALUE   = 4
} MPTHREAT_TYPE, *PMPTHREAT_TYPE;
```



## Constants

<dl> <dt>

<span id="MPTHREAT_TYPE_KNOWNBAD"></span><span id="mpthreat_type_knownbad"></span>**MPTHREAT\_TYPE\_KNOWNBAD**
</dt> <dd>

Known bad threat detected via signature.

</dd> <dt>

<span id="MPTHREAT_TYPE_BEHAVIOR"></span><span id="mpthreat_type_behavior"></span>**MPTHREAT\_TYPE\_BEHAVIOR**
</dt> <dd>

Suspicious threat detected via behavior monitoring.

</dd> <dt>

<span id="MPTHREAT_TYPE_UNKNOWN"></span><span id="mpthreat_type_unknown"></span>**MPTHREAT\_TYPE\_UNKNOWN**
</dt> <dd>

Unknown threats (unclassified).

</dd> <dt>

<span id="MPTHREAT_TYPE_KNOWNGOOD"></span><span id="mpthreat_type_knowngood"></span>**MPTHREAT\_TYPE\_KNOWNGOOD**
</dt> <dd>

Known good threat.

</dd> <dt>

<span id="MPTHREAT_TYPE_NIS"></span><span id="mpthreat_type_nis"></span>**MPTHREAT\_TYPE\_NIS**
</dt> <dd>

NIS threat detection.

</dd> <dt>

<span id="MPTHREAT_TYPE_MAXVALUE"></span><span id="mpthreat_type_maxvalue"></span>**MPTHREAT\_TYPE\_MAXVALUE**
</dt> <dd>

Maximum value possible.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





