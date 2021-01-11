---
description: Deprecated. Represents an instant in time, typically expressed as a date and time of day and a corresponding calendar.
ms.assetid: a714ff32-2b1f-4256-931e-324d64daf2ac
title: CALDATETIME structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CALDATETIME
api_type: 
- NA
api_location: 
---

# CALDATETIME structure

Deprecated. Represents an instant in time, typically expressed as a date and time of day and a corresponding calendar.

## Syntax


```C++
typedef struct _caldatetime {
  CALID CalId;
  UINT  Era;
  UINT  Year;
  UINT  Month;
  UINT  Day;
  UINT  DayOfWeek;
  UINT  Hour;
  UINT  Minute;
  UINT  Second;
  ULONG Tick;
} CALDATETIME, *LPCALDATETIME;
```



## Members

<dl> <dt>

**CalId**
</dt> <dd>

The [calendar identifier](calendar-identifiers.md) for the instant in time.

</dd> <dt>

**Era**
</dt> <dd>

The era information for the instant in time.

</dd> <dt>

**Year**
</dt> <dd>

The year for the instant in time.

</dd> <dt>

**Month**
</dt> <dd>

The month for the instant in time.

</dd> <dt>

**Day**
</dt> <dd>

The day for the instant in time.

</dd> <dt>

**DayOfWeek**
</dt> <dd>

The day of the week for the instant in time.

</dd> <dt>

**Hour**
</dt> <dd>

The hour for the instant in time.

</dd> <dt>

**Minute**
</dt> <dd>

The minute for the instant in time.

</dd> <dt>

**Second**
</dt> <dd>

The second for the instant in time.

</dd> <dt>

**Tick**
</dt> <dd>

The tick for the instant in time.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[National Language Support Structures](national-language-support-structures.md)
</dt> </dl>

 

 




