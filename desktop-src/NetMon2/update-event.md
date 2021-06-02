---
description: The UPDATE\_EVENT structure updates events. This structure is passed back to the calling application via the event status callback procedure by the NPP.
ms.assetid: 6896be5a-f986-44ff-a18b-010f7b9858aa
title: UPDATE_EVENT structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UPDATE_EVENT
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# UPDATE\_EVENT structure

The **UPDATE\_EVENT** structure updates events. This structure is passed back to the calling application via the event status callback procedure by the NPP.

## Syntax


```C++
typedef struct _UPDATE_EVENT {
  USHORT       Event;
  DWORD        Action;
  DWORD        Status;
  DWORD        Value;
  __int64      TimeStamp;
  DWORD_PTR    lpUserContext;
  DWORD_PTR    lpReserved;
  UINT         FramesDropped;
  union {
    DWORD                        Reserved;
    LPFRAMETABLE                 lpFrameTable;
    DWORD_PTR                    lpPacketQueue;
    SECURITY_PERMISSION_RESPONSE SecurityResponse;
  };
  LPSTATISTICS lpFinalStats;
} UPDATE_EVENT, *PUPDATE_EVENT;
```



## Members

<dl> <dt>

**Event**
</dt> <dd>

Actual event being recorded.

</dd> <dt>

**Action**
</dt> <dd>

The action taken.

</dd> <dt>

**Status**
</dt> <dd>

Network status indication.

</dd> <dt>

**Value**
</dt> <dd>

Auxiliary counter variable.

</dd> <dt>

**TimeStamp**
</dt> <dd>

The marked events, in microseconds.

</dd> <dt>

**lpUserContext**
</dt> <dd>

User context given by the application.

</dd> <dt>

**lpReserved**
</dt> <dd>

Driver or NAL use.

</dd> <dt>

**FramesDropped**
</dt> <dd>

RTF frames dropped in the specified buffer.

</dd> <dt>

**Reserved**
</dt> <dd>

No data comes back with this switch option.

</dd> <dt>

**lpFrameTable**
</dt> <dd>

RTF only.

</dd> <dt>

**lpPacketQueue**
</dt> <dd>

For transmits.

</dd> <dt>

**SecurityResponse**
</dt> <dd>

Remote security monitor response.

</dd> <dt>

**lpFinalStats**
</dt> <dd>

This is only filled in on non-security related stops (for example, triggers).

</dd> </dl>

## Remarks

C++ users should note that the declaration for this callback should be in the public part of the header file:

``` syntax
static WINAPI DWORD NetworkCallback( UPDATE_EVENT events);
```

The implementation should be in the protected section of the .cpp file:

``` syntax
DWORD WINAPI ClassName::NetworkCallback( UPDATE_EVENT events) {};
```

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




