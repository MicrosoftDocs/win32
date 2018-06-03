---
title: MPIO\_EventEntry structure
description: The MPIO\_EventEntry structure is used to return events that MPIO has logged.
ms.assetid: de7fd19e-e18d-4e78-963a-3abdd7921d69
keywords:
- MPIO_EventEntry structure Storage Devices
- PMPIO_EventEntry structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIO_EventEntry
api_location:
- mpiowmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MPIO\_EventEntry structure

The MPIO\_EventEntry structure is used to return events that MPIO has logged.

## Syntax


```C++
typedef struct _MPIO_EventEntry {
  ULONGLONG TimeStamp;
  ULONG     Severity;
  WCHAR     Component[63 + 1];
  WCHAR     EventDescription[63 + 1];
} MPIO_EventEntry, *PMPIO_EventEntry;
```



## Members

<dl> <dt>

**TimeStamp**
</dt> <dd>

A 64-bitfield that specifies the timestamp for the event entry.

</dd> <dt>

**Severity**
</dt> <dd>

A 32-bitfield that indicates the severity of the reported event.

</dd> <dt>

**Component**
</dt> <dd>

A string that indicates the component to which this event belongs.

</dd> <dt>

**EventDescription**
</dt> <dd>

A string that indicates the event description.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_EventEntry%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





