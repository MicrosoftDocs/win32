---
title: KEYARRAY (Mmsystem.h)
description: KEYARRAY specifies a type used to define an array of keys.
ms.assetid: af1a1d2f-4558-4374-93ab-5a705fc879ca
keywords:
- KEYARRAY MIDIPATCHSIZE
ms.topic: reference
ms.date: 05/31/2018
---

# KEYARRAY

KEYARRAY specifies a type used to define an array of keys.


```C++
typedef WORD KEYARRAY[MIDIPATCHSIZE];
```



<dl> <dt>

**KEYARRAY\[MIDIPATCHSIZE\]**
</dt> <dd>

Each element in the array corresponds to a key-based percussion patch with each of the 16 bits representing one of the 16 MIDI channels. Bits are set for each of the channels that use that particular patch. For example, if the percussion patch for key number 60 is used by physical MIDI channels 9 and 15, element 60 of the array should be set to 0x8200.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Version<br/>                  | Musical Instrument Digital Interface (MIDI), MIDI Types<br/>                                        |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[MIDI Types](midi-event-types.md)
</dt> </dl>

 

 





