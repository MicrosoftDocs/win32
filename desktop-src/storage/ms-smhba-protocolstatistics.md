---
title: MS\_SMHBA\_PROTOCOLSTATISTICS structure
description: The MS\_SMHBA\_PROTOCOLSTATISTICS structure is used to report protocol traffic statistics on a port.
ms.assetid: eb992a5e-41fe-4bb3-9f53-785135af8a32
keywords:
- MS_SMHBA_PROTOCOLSTATISTICS structure Storage Devices
- PMS_SMHBA_PROTOCOLSTATISTICS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MS_SMHBA_PROTOCOLSTATISTICS
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

# MS\_SMHBA\_PROTOCOLSTATISTICS structure

The MS\_SMHBA\_PROTOCOLSTATISTICS structure is used to report protocol traffic statistics on a port.

## Syntax


```C++
typedef struct _MS_SMHBA_PROTOCOLSTATISTICS {
  LONGLONG SecondsSinceLastReset;
  LONGLONG InputRequests;
  LONGLONG OutputRequests;
  LONGLONG ControlRequests;
  LONGLONG InputMegabytes;
  LONGLONG OutputMegabytes;
} MS_SMHBA_PROTOCOLSTATISTICS, *PMS_SMHBA_PROTOCOLSTATISTICS;
```



## Members

<dl> <dt>

**SecondsSinceLastReset**
</dt> <dd>

The number of seconds since the statistics were last reset.

</dd> <dt>

**InputRequests**
</dt> <dd>

The number of input requests.

</dd> <dt>

**OutputRequests**
</dt> <dd>

The number of output requests.

</dd> <dt>

**ControlRequests**
</dt> <dd>

The number of control requests.

</dd> <dt>

**InputMegabytes**
</dt> <dd>

The number of megabytes of data that has been input.

</dd> <dt>

**OutputMegabytes**
</dt> <dd>

The number of megabytes of data that has been output.

</dd> </dl>

## Remarks

The statistics counters whose values are reported in the members of this structure are 64-bit signed integers that wrap to zero on exceeding 2\*\*63-1. The statistics counters are not reset during normal operation. Therefore, traffic rates can be determined by the difference of counter values that are derived from two successive calls, with appropriate adjustments made for counter wrap. If an HBA does not support a specific statistic, it returns the value of -1 for the corresponding counter.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MS_SMHBA_PROTOCOLSTATISTICS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





