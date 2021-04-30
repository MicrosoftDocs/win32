---
description: Stores information about shared memory sections.
ms.assetid: 73a650ee-110c-43f2-a5e2-783d52fd29ee
title: SHAREDMEMORY_HEADER structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SHAREDMEMORY_HEADER
api_type: 
- NA
api_location: 
---

# SHAREDMEMORY\_HEADER structure

Stores information about shared memory sections.

## Syntax


```C++
typedef struct _SHAREDMEMORY_HEADER {
  DWORD             cbTotal;
  DWORD             cbOffsetSns;
  DWORD             idxEvent;
  DWORD             dwEvent;
  CURSOR_ID         cid;
  DWORD             sn;
  SYSTEM_EVENT      sysEvt;
  SYSTEM_EVENT_DATA sysEvtData;
  DWORD             cPackets;
  DWORD             cbPackets;
  BOOL              fSnsPresent;
} SHAREDMEMORY_HEADER, *PSHAREDMEMORY_HEADER;
```



## Members

<dl> <dt>

**cbTotal**
</dt> <dd>

The size, in bytes, of the data referenced by this header structure.

</dd> <dt>

**cbOffsetSns**
</dt> <dd>

The size, in bytes, that the serial numbers are offset from the header structure.

</dd> <dt>

**idxEvent**
</dt> <dd>

The event index. This value is incremented with successive events.

</dd> <dt>

**dwEvent**
</dt> <dd>

The event associated with this header.

</dd> <dt>

**cid**
</dt> <dd>

The cursor identifier referenced by the shared memory header.

</dd> <dt>

**sn**
</dt> <dd>

The serial number for the shared memory header.

</dd> <dt>

**sysEvt**
</dt> <dd>

The system event, prefixed SE\_\*, associated with this header. See the remarks section for more information.

</dd> <dt>

**sysEvtData**
</dt> <dd>

The [**SYSTEM\_EVENT\_DATA**](/windows/win32/api/tpcshrd/ns-tpcshrd-system_event_data) structure associated with the system event.

</dd> <dt>

**cPackets**
</dt> <dd>

A count of the packets associated with the current shared memory section.

</dd> <dt>

**cbPackets**
</dt> <dd>

The size, in bytes, of the packets associated with the current shared memory section.

</dd> <dt>

**fSnsPresent**
</dt> <dd>

A flag indicating whether serial numbers are present in the current shared memory section.

</dd> </dl>

## Remarks

The following values are defined for the **sysEvt** member.


```C++
#define SE_NONE                  0x00000000
#define SE_TAP                   0x00000010
#define SE_DBL_TAP               0x00000011
#define SE_RIGHT_TAP             0x00000012
#define SE_DRAG                  0x00000013
#define SE_RIGHT_DRAG            0x00000014
#define SE_HOLD_ENTER            0x00000015
#define SE_HOLD_LEAVE            0x00000016
#define SE_HOVER_ENTER           0x00000017
#define SE_HOVER_LEAVE           0x00000018
#define SE_FLICK                 0x0000001F
```



## See also

<dl> <dt>

[**SYSTEM\_EVENT\_DATA**](/windows/win32/api/tpcshrd/ns-tpcshrd-system_event_data)
</dt> </dl>

 

 



