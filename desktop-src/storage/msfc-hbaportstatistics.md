---
title: MSFC\_HBAPortStatistics structure
description: The MSFC\_HBAPortStatistics structure contains statistics information about a port.
ms.assetid: 0274b3c7-c17e-45bf-867f-2b0f741b2ecb
keywords:
- MSFC_HBAPortStatistics structure Storage Devices
- PMSFC_HBAPortStatistics structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSFC_HBAPortStatistics
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

# MSFC\_HBAPortStatistics structure

The MSFC\_HBAPortStatistics structure contains statistics information about a port.

## Syntax


```C++
typedef struct _MSFC_HBAPortStatistics {
  LONGLONG SecondsSinceLastReset;
  LONGLONG TxFrames;
  LONGLONG TxWords;
  LONGLONG RxFrames;
  LONGLONG RxWords;
  LONGLONG LIPCount;
  LONGLONG NOSCount;
  LONGLONG ErrorFrames;
  LONGLONG DumpedFrames;
  LONGLONG LinkFailureCount;
  LONGLONG LossOfSyncCount;
  LONGLONG LossOfSignalCount;
  LONGLONG PrimitiveSeqProtocolErrCount;
  LONGLONG InvalidTxWordCount;
  LONGLONG InvalidCRCCount;
} MSFC_HBAPortStatistics, *PMSFC_HBAPortStatistics;
```



## Members

<dl> <dt>

**SecondsSinceLastReset**
</dt> <dd>

Contains the number of seconds since the statistics were last reset.

</dd> <dt>

**TxFrames**
</dt> <dd>

Contains the number of total transmitted fibre channel frames across all protocols and classes.

</dd> <dt>

**TxWords**
</dt> <dd>

Contains the number of total transmitted fibre channel words across all protocols and classes.

</dd> <dt>

**RxFrames**
</dt> <dd>

Contains the number of received fibre channel frames across all protocols and classes.

</dd> <dt>

**RxWords**
</dt> <dd>

Contains the number of received fibre channel words across all protocols and classes.

</dd> <dt>

**LIPCount**
</dt> <dd>

Contains the number of loop initialization primitive sequence (LIP) events that have occurred on a arbitrated loop.

</dd> <dt>

**NOSCount**
</dt> <dd>

Contains the number of nonoperational state primitive sequence (NOS) events that have occurred on the switched fabric.

</dd> <dt>

**ErrorFrames**
</dt> <dd>

Contains the number of frames that have been received in error.

</dd> <dt>

**DumpedFrames**
</dt> <dd>

Contains the number of frames that were lost due to a lack of host buffers available.

</dd> <dt>

**LinkFailureCount**
</dt> <dd>

Contains the link failure count.

</dd> <dt>

**LossOfSyncCount**
</dt> <dd>

Contains the loss of synchronization count.

</dd> <dt>

**LossOfSignalCount**
</dt> <dd>

Contains the loss of signal count.

</dd> <dt>

**PrimitiveSeqProtocolErrCount**
</dt> <dd>

Contains the primitive sequence protocol error count.

</dd> <dt>

**InvalidTxWordCount**
</dt> <dd>

Contains a count of the number of invalid transmissions.

</dd> <dt>

**InvalidCRCCount**
</dt> <dd>

Contains a count of the number frames with invalid cyclic redundancy checksums.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[MSFC\_HBAPortStatistics WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562513)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_HBAPortStatistics%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






