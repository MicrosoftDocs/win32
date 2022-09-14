---
description: Contains information about a processor.
ms.assetid: fa8c533c-3a54-4eb5-893f-649dfd8b4609
title: PROCESSOR_POWER_INFORMATION structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PROCESSOR_POWER_INFORMATION
api_type: 
- NA
api_location: 
---

# PROCESSOR\_POWER\_INFORMATION structure

Contains information about a processor.

## Syntax


```C++
typedef struct _PROCESSOR_POWER_INFORMATION {
  ULONG Number;
  ULONG MaxMhz;
  ULONG CurrentMhz;
  ULONG MhzLimit;
  ULONG MaxIdleState;
  ULONG CurrentIdleState;
} PROCESSOR_POWER_INFORMATION, *PPROCESSOR_POWER_INFORMATION;
```



## Members

<dl> <dt>

**Number**
</dt> <dd>

The system processor number.

</dd> <dt>

**MaxMhz**
</dt> <dd>

The maximum specified clock frequency of the system processor, in megahertz.

</dd> <dt>

**CurrentMhz**
</dt> <dd>

The processor clock frequency, in megahertz. This number is the maximum specified processor clock frequency multiplied by the current processor throttle.

</dd> <dt>

**MhzLimit**
</dt> <dd>

The limit on the processor clock frequency, in megahertz. This number is the maximum specified processor clock frequency multiplied by the current processor thermal throttle limit.

</dd> <dt>

**MaxIdleState**
</dt> <dd>

The maximum idle state of this processor.

</dd> <dt>

**CurrentIdleState**
</dt> <dd>

The current idle state of this processor.

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

 

 




