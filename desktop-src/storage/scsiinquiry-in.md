---
title: ScsiInquiry\_IN structure
description: The ScsiInquiry\_IN structure holds the input data for the ScsiInquiry method, which is used to send a SCSI inquiry command.
ms.assetid: b1a73ef7-c13a-4627-8eb0-b9285567caec
keywords:
- ScsiInquiry_IN structure Storage Devices
- PScsiInquiry_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ScsiInquiry_IN
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

# ScsiInquiry\_IN structure

The ScsiInquiry\_IN structure holds the input data for the [**ScsiInquiry**](https://msdn.microsoft.com/library/windows/hardware/ff564585) method, which is used to send a SCSI inquiry command.

## Syntax


```C++
typedef struct _ScsiInquiry_IN {
  ULONGLONG UniqueSessionId;
  ULONGLONG Lun;
  UCHAR     InquiryFlags;
  UCHAR     PageCode;
} ScsiInquiry_IN, *PScsiInquiry_IN;
```



## Members

<dl> <dt>

**UniqueSessionId**
</dt> <dd>

A 64-bit integer that uniquely identifies the session. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in the *UniqueSessionId* parameter. Do not confuse this value with the values in the ISID and TSID members.

</dd> <dt>

**Lun**
</dt> <dd>

A 64-bit number that, together with the name of the target, uniquely identifies the logical unit.

</dd> <dt>

**InquiryFlags**
</dt> <dd>

The inquiry flags to set in the SCSI inquiry command. A value of 1 in the lowest order bit (0x01) indicates that the enable vital product data (EVPD) bit will be set in the inquiry command and the device server will return the optional vital product data that the page code field specifies in the inquiry command. A value of 1 in the second bit (0x02) indicates that the command support data bit will be set in the inquiry command and the device server will return the optional command support data that the operation code field specifies in the inquiry command.

</dd> <dt>

**PageCode**
</dt> <dd>

The page code field in the SCSI inquiry command.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> <dt>

[**ScsiInquiry**](https://msdn.microsoft.com/library/windows/hardware/ff564585)
</dt> <dt>

[**ScsiInquiry\_OUT**](scsiinquiry-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiInquiry_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






