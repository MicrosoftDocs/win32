---
title: MSiSCSI\_NICPerformance structure
description: The MSiSCSI\_NICPerformance structure can be used by an iSCSI initiator to report statistics for a network interface card (NIC) port.
ms.assetid: 921e6e44-adc2-4257-b11e-941121f5bfd7
keywords:
- MSiSCSI_NICPerformance structure Storage Devices
- PMSiSCSI_NICPerformance structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_NICPerformance
api_location:
- iscsiprf.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MSiSCSI\_NICPerformance structure

The MSiSCSI\_NICPerformance structure can be used by an iSCSI initiator to report statistics for a network interface card (NIC) port.

## Syntax


```C++
typedef struct _MSiSCSI_NICPerformance {
  ULONG BytesTransmitted;
  ULONG BytesReceived;
  ULONG PDUTransmitted;
  ULONG PDUReceived;
} MSiSCSI_NICPerformance, *PMSiSCSI_NICPerformance;
```



## Members

<dl> <dt>

**BytesTransmitted**
</dt> <dd>

The number of bytes that are transmitted through the Ethernet port.

</dd> <dt>

**BytesReceived**
</dt> <dd>

The number of bytes that are received through the Ethernet port.

</dd> <dt>

**PDUTransmitted**
</dt> <dd>

The number of PDUs that are transmitted through the Ethernet port.

</dd> <dt>

**PDUReceived**
</dt> <dd>

The number of PDUs that are received through the Ethernet port.

</dd> </dl>

## Remarks

It is optional that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiprf.h (include Iscsiprf.h)</dt> </dl> |



## See also

<dl> <dt>

[MSiSCSI\_NICPerformance WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563089)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_NICPerformance%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






