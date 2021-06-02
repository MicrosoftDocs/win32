---
description: Contains information about the idleness of the system.
ms.assetid: f6349b7c-1835-4492-95e3-9ce142628804
title: SYSTEM_POWER_INFORMATION structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SYSTEM_POWER_INFORMATION
api_type: 
- NA
api_location: 
---

# SYSTEM\_POWER\_INFORMATION structure

Contains information about the idleness of the system.

## Syntax


```C++
typedef struct _SYSTEM_POWER_INFORMATION {
  ULONG MaxIdlenessAllowed;
  ULONG Idleness;
  ULONG TimeRemaining;
  UCHAR CoolingMode;
} SYSTEM_POWER_INFORMATION, *PSYSTEM_POWER_INFORMATION;
```



## Members

<dl> <dt>

**MaxIdlenessAllowed**
</dt> <dd>

The idleness at which the system is considered idle and the idle time-out begins counting, expressed as a percentage. Dropping below this number causes the timer to be canceled.

</dd> <dt>

**Idleness**
</dt> <dd>

The current idle level, expressed as a percentage.

</dd> <dt>

**TimeRemaining**
</dt> <dd>

The time remaining in the idle timer, in seconds.

</dd> <dt>

**CoolingMode**
</dt> <dd>

The current system cooling mode. This member must one of the following values.



| Value                                                                                                                                                                                                                                 | Meaning                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <span id="PO_TZ_ACTIVE"></span><span id="po_tz_active"></span><dl> <dt>**PO\_TZ\_ACTIVE**</dt> <dt>0</dt> </dl>                    | The system is currently in Active cooling mode.<br/>                                                |
| <span id="PO_TZ_INVALID_MODE"></span><span id="po_tz_invalid_mode"></span><dl> <dt>**PO\_TZ\_INVALID\_MODE**</dt> <dt>2</dt> </dl> | The system does not support CPU throttling, or there is no thermal zone defined in the system.<br/> |
| <span id="PO_TZ_PASSIVE"></span><span id="po_tz_passive"></span><dl> <dt>**PO\_TZ\_PASSIVE**</dt> <dt>1</dt> </dl>                 | The system is currently in Passive cooling mode.<br/>                                               |



 

</dd> </dl>

## Remarks

Note that this structure definition was accidentally omitted from WinNT.h. This error will be corrected in the future. In the meantime, to compile your application, include the structure definition contained in this topic in your source code.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**CallNtPowerInformation**](/windows/desktop/api/Powerbase/nf-powerbase-callntpowerinformation)
</dt> </dl>

 

 




