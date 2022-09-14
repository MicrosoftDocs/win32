---
title: MPSCAN_TYPE enumeration (MpClient.h)
description: Type of scan performed.
ms.assetid: 980A80FD-FF02-4338-B7FB-DAA141F65E89
keywords:
- MPSCAN_TYPE enumeration Legacy Windows Environment Features
- PMPSCAN_TYPE enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPSCAN_TYPE
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPSCAN\_TYPE enumeration

Type of scan performed.

## Syntax


```C++
typedef enum tagMPSCAN_TYPE { 
  MPSCAN_TYPE_UNKNOWN   = 0,
  MPSCAN_TYPE_QUICK     = 1,
  MPSCAN_TYPE_FULL      = 2,
  MPSCAN_TYPE_RESOURCE  = 3,
  MPSCAN_TYPE_MAXVALUE  = 3
} MPSCAN_TYPE, *PMPSCAN_TYPE;
```



## Constants

<dl> <dt>

<span id="MPSCAN_TYPE_UNKNOWN"></span><span id="mpscan_type_unknown"></span>**MPSCAN\_TYPE\_UNKNOWN**
</dt> <dd>

Internal use only.

</dd> <dt>

<span id="MPSCAN_TYPE_QUICK"></span><span id="mpscan_type_quick"></span>**MPSCAN\_TYPE\_QUICK**
</dt> <dd>

Scans running processes and various ASEP points in the system where malware typically hides.

</dd> <dt>

<span id="MPSCAN_TYPE_FULL"></span><span id="mpscan_type_full"></span>**MPSCAN\_TYPE\_FULL**
</dt> <dd>

Performs a quick scan followed by scan of all fixed drives of the system.

</dd> <dt>

<span id="MPSCAN_TYPE_RESOURCE"></span><span id="mpscan_type_resource"></span>**MPSCAN\_TYPE\_RESOURCE**
</dt> <dd>

Scans specific resources, such as files or folders.

</dd> <dt>

<span id="MPSCAN_TYPE_MAXVALUE"></span><span id="mpscan_type_maxvalue"></span>**MPSCAN\_TYPE\_MAXVALUE**
</dt> <dd>

Maximum value possible.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





