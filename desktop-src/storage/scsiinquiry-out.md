---
title: ScsiInquiry\_OUT structure
description: The ScsiInquiry\_OUT structure holds the output data for the ScsiInquiry method.
ms.assetid: ac3ec079-61a5-42fe-a1c0-b7626e5f32d2
keywords:
- ScsiInquiry_OUT structure Storage Devices
- PScsiInquiry_OUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ScsiInquiry_OUT
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ScsiInquiry\_OUT structure

The ScsiInquiry\_OUT structure holds the output data for the [**ScsiInquiry**](https://msdn.microsoft.com/library/windows/hardware/ff564585) method.

## Syntax


```C++
typedef struct _ScsiInquiry_OUT {
  ULONG Status;
  ULONG ResponseBufferSize;
  UCHAR ScsiStatus;
  UCHAR SenseBuffer[18];
  UCHAR ResponseBuffer[1];
} ScsiInquiry_OUT, *PScsiInquiry_OUT;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

The status of the **ScsiInquiry** operation. This member will contain 0 if the INQUIRY operation succeeds and ISDSC\_SCSI\_REQUEST\_FAILED if the operation fails. If the INQUIRY operation fails, **ScsiStatus** will contain the SCSI status of the SCSI command. SCSI status qualifiers are documented in the *SCSI Primary Commands* specification. For a list of status qualifiers, see [ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568).

</dd> <dt>

**ResponseBufferSize**
</dt> <dd>

The response buffer size, in bytes*.*

</dd> <dt>

**ScsiStatus**
</dt> <dd>

The status of the SCSI INQUIRY command.

</dd> <dt>

**SenseBuffer**
</dt> <dd>

A buffer that holds the SCSI sense data that the SCSI INQUIRY command received.

</dd> <dt>

**ResponseBuffer**
</dt> <dd>

A buffer that holds the response data that the SCSI INQUIRY command received.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568)
</dt> <dt>

[**ScsiInquiry**](https://msdn.microsoft.com/library/windows/hardware/ff564585)
</dt> <dt>

[**ScsiInquiry\_IN**](scsiinquiry-in.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiInquiry_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






