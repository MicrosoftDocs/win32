---
title: MPCOMPONENT_VERSION structure (MpClient.h)
description: Version and update time for an individual component.
ms.assetid: 43468230-EE13-4630-8C09-F8DF983EF748
keywords:
- MPCOMPONENT_VERSION structure Legacy Windows Environment Features
- PMPCOMPONENT_VERSION structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPCOMPONENT_VERSION
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPCOMPONENT\_VERSION structure

Version and update time for an individual component.

## Syntax


```C++
typedef struct tagMPCOMPONENT_VERSION {
  ULONGLONG      Version;
  ULARGE_INTEGER UpdateTime;
} MPCOMPONENT_VERSION, *PMPCOMPONENT_VERSION;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Type: **ULONGLONG**

</dd> <dd>

Version field. Each **WORD** represents major, minor, build, and revision.

</dd> <dt>

**UpdateTime**
</dt> <dd>

Type: **ULARGE\_INTEGER**

</dd> <dd>

Last update time of the component, in **FILETIME** format.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





