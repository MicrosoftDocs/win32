---
title: TunerLockType enumeration
description: The TunerLockType enumeration type specifies how well a television tuner has locked onto a signal.
ms.assetid: '657dfd46-b01c-41aa-af0c-0d07235f15fc'
keywords: ["TunerLockType enumeration Microsoft TV Technologies"]
topic_type:
- apiref
api_name:
- TunerLockType
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# TunerLockType enumeration

The **TunerLockType** enumeration type specifies how well a television tuner has locked onto a signal.

## Syntax


```C++
typedef enum _TunerDecoderLockType { 
  Tuner_LockType_None                       = 0x00,
  Tuner_LockType_Within_Scan_Sensing_Range  = 0x01,
  Tuner_LockType_Locked                     = 0x02
} TunerLockType;
```



## Constants

<dl> <dt>

<span id="Tuner_LockType_None"></span><span id="tuner_locktype_none"></span><span id="TUNER_LOCKTYPE_NONE"></span>**Tuner\_LockType\_None**
</dt> <dd>

The tuner is not locked onto a signal. If this value is returned at the end of a scan, it means the tuner was not able to lock onto a signal anywhere within the scanning range.

</dd> <dt>

<span id="Tuner_LockType_Within_Scan_Sensing_Range"></span><span id="tuner_locktype_within_scan_sensing_range"></span><span id="TUNER_LOCKTYPE_WITHIN_SCAN_SENSING_RANGE"></span>**Tuner\_LockType\_Within\_Scan\_Sensing\_Range**
</dt> <dd>

The tuner found a signal in the vicinity but could establish the exact frequency.

</dd> <dt>

<span id="Tuner_LockType_Locked"></span><span id="tuner_locktype_locked"></span><span id="TUNER_LOCKTYPE_LOCKED"></span>**Tuner\_LockType\_Locked**
</dt> <dd>

The tuner locked onto an exact frequency. This value indicates that the tuner was able to fine tune to a frequency.

</dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ksmedia.h</dt> </dl> |



## See also

<dl> <dt>

[BDA Enumeration Types](bda-types.md)
</dt> </dl>

 

 





