---
title: HBA\_PortStatistics structure
description: The HBA\_PortStatistics structure contains statistical information about a port.
ms.assetid: 3a0d6633-b4a6-4864-96ae-4f91de11daa1
keywords:
- HBA_PortStatistics structure Storage Devices
- HBA_PORTSTATISTICS structure Storage Devices
- PHBA_PORTSTATISTICS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- HBA_PORTSTATISTICS
api_location:
- hbaapi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# HBA\_PortStatistics structure

The HBA\_PortStatistics structure contains statistical information about a port.

## Syntax


```C++
typedef struct HBA_PortStatistics {
  HBA_INT64 SecondsSinceLastReset;
  HBA_INT64 TxFrames;
  HBA_INT64 TxWords;
  HBA_INT64 RxFrames;
  HBA_INT64 RxWords;
  HBA_INT64 LIPCount;
  HBA_INT64 NOSCount;
  HBA_INT64 ErrorFrames;
  HBA_INT64 DumpedFrames;
  HBA_INT64 LinkFailureCount;
  HBA_INT64 LossOfSyncCount;
  HBA_INT64 LossOfSignalCount;
  HBA_INT64 PrimitiveSeqProtocolErrCount;
  HBA_INT64 InvalidTxWordCount;
  HBA_INT64 InvalidCRCCount;
} HBA_PORTSTATISTICS, *PHBA_PORTSTATISTICS;
```



## Members

<dl> <dt>

**SecondsSinceLastReset**
</dt> <dd>

Reports the number of seconds since the statistics were last reset.

</dd> <dt>

**TxFrames**
</dt> <dd>

Reports the number of fibre channel frames transmitted for all protocols and classes.

</dd> <dt>

**TxWords**
</dt> <dd>

Reports the number of fibre channel words transmitted for all protocols and classes.

</dd> <dt>

**RxFrames**
</dt> <dd>

Reports the number of fibre channel frames received for all protocols and classes.

</dd> <dt>

**RxWords**
</dt> <dd>

Reports the number of fibre channel words received for all protocols and classes.

</dd> <dt>

**LIPCount**
</dt> <dd>

Reports the number of LIP events that have occurred on a arbitrated loop.

</dd> <dt>

**NOSCount**
</dt> <dd>

Reports the number of NOS events that have occurred on the switched fabric.

</dd> <dt>

**ErrorFrames**
</dt> <dd>

Reports the number of frames that have been received in error.

</dd> <dt>

**DumpedFrames**
</dt> <dd>

Reports the number of frames that were lost due to a lack of host buffers available.

</dd> <dt>

**LinkFailureCount**
</dt> <dd>

Reports the link failure count field of the error status block for the port.

</dd> <dt>

**LossOfSyncCount**
</dt> <dd>

Reports the value of the loss of synchronization count field of the link error status block for the port.

</dd> <dt>

**LossOfSignalCount**
</dt> <dd>

Reports the value of the loss of signal count field of the link error status block for the specified port.

</dd> <dt>

**PrimitiveSeqProtocolErrCount**
</dt> <dd>

Reports the value of the primitive sequence protocol error field of the link error status block for the port.

</dd> <dt>

**InvalidTxWordCount**
</dt> <dd>

Reports the value of the invalid transmission word field of the link error status block for the specified port.

</dd> <dt>

**InvalidCRCCount**
</dt> <dd>

Reports the value of the invalid CRC count field of the link error status block for the specified port.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_GetPortStatistics**](hba-getportstatistics.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_PortStatistics%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






