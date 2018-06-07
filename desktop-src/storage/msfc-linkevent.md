---
title: MSFC\_LinkEvent structure
description: A WMI provider uses the MSFC\_LinkEvent structure to report link events for the indicated adapter.
ms.assetid: 35fb3397-2e45-4d32-8cb1-1050199b2209
keywords:
- MSFC_LinkEvent structure Storage Devices
- PMSFC_LinkEvent structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSFC_LinkEvent
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MSFC\_LinkEvent structure

A WMI provider uses the MSFC\_LinkEvent structure to report link events for the indicated adapter.

## Syntax


```C++
typedef struct _MSFC_LinkEvent {
  ULONG EventType;
  UCHAR AdapterWWN[8];
  ULONG RLIRBufferSize;
  UCHAR RLIRBuffer[1];
} MSFC_LinkEvent, *PMSFC_LinkEvent;
```



## Members

<dl> <dt>

**EventType**
</dt> <dd>

Indicates the type of the event. The values that can be assigned to this member are defined by the [EVENT\_TYPE\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff553764) WMI class qualifier.

</dd> <dt>

**AdapterWWN**
</dt> <dd>

Contains a worldwide name that indicates the adapter for which the event occurred.

</dd> <dt>

**RLIRBufferSize**
</dt> <dd>

Indicates the size of the buffer at **RLIRBuffer**.

</dd> <dt>

**RLIRBuffer**
</dt> <dd>

Contains the data associated with a register link incident request (RLIR).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[EVENT\_TYPE\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff553764)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_LinkEvent%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






