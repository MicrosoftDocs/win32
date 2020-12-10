---
title: PATCHARRAY (Mmsystem.h)
description: PATCHARRAY is a type used to define an array of MIDI patches.
ms.assetid: f48ee0d2-224a-4530-ac28-ae63160316cc
keywords:
- PATCHARRAY MIDIPATCHSIZE
ms.topic: reference
ms.date: 05/31/2018
---

# PATCHARRAY

PATCHARRAY is a type used to define an array of MIDI patches.


```C++
typedef WORD PATCHARRAY[MIDIPATCHSIZE];
```



<dl> <dt>

**PATCHARRAY\[MIDIPATCHSIZE\]**
</dt> <dd>

Each element in the array corresponds to a patch with each of the 16 bits representing one of the 16 MIDI channels. Bits are set for each of the channels that use that particular patch. For example, if patch number 0 is used by physical MIDI channels 0 and 8, element 0 of the array should be set to 0x0101.

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

 

 





