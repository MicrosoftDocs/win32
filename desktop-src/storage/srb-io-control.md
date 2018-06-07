---
title: SRB\_IO\_CONTROL structure
description: SRB\_IO\_CONTROL structure
ms.assetid: 754d2a4c-6a22-4c25-87e2-e30e87b9c1ba
keywords:
- SRB_IO_CONTROL structure Storage Devices
- PSRB_IO_CONTROL structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SRB_IO_CONTROL
api_location:
- ntddscsi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SRB\_IO\_CONTROL structure

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SRB_IO_CONTROL {
  ULONG HeaderLength;
  UCHAR Signature[8];
  ULONG Timeout;
  ULONG ControlCode;
  ULONG ReturnCode;
  ULONG Length;
} SRB_IO_CONTROL, *PSRB_IO_CONTROL;
```



## Members

<dl> <dt>

**HeaderLength**
</dt> <dd>

Is **sizeof**(SRB\_IO\_CONTROL).

</dd> <dt>

**Signature**
</dt> <dd>

Identifies the application-dedicated, target HBA for this request. This signature is used to prevent conflicts in **ControlCode** values between vendors. It should be a string of ASCII characters. If a miniport driver does not recognize the input **Signature** value, it must complete the request with a status of SRB\_STATUS\_INVALID\_REQUEST.

</dd> <dt>

**Timeout**
</dt> <dd>

Indicates the interval in seconds that the request can execute before the OS-specific port driver might consider it timed out. Miniport drivers should be enforcing timeouts for SRB\_IO\_CONTROL, especially for any privately defined SRB\_IO\_CONTROL.

</dd> <dt>

**ControlCode**
</dt> <dd>

Indicates the operation to be performed. There are no system-defined operations. Values must be defined by the driver as a set of private I/O control codes with which the application can make requests by calling the Win32 [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function. For more information about defining private I/O control codes for device control requests, see [Using I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565406).

</dd> <dt>

**ReturnCode**
</dt> <dd>

Returns a status code for examination by the requesting application.

</dd> <dt>

**Length**
</dt> <dd>

Indicates the size in bytes of the immediately following data area. This area can be divided for the particular operation into input and output areas. For input requests, the contents of the DataBuffer will be copied to the requester up to the returned value of DataTransferLength.

</dd> </dl>

## Remarks

This structure is used by applications to send requests directly to an application-dedicated HBA. Note that such an application also must set up requests to program its dedicated HBA.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[SCSI Port I/O Control Codes](scsi-port-i-o-control-codes.md)
</dt> <dt>

SCSI Port I/O Control Codes
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SRB_IO_CONTROL%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






