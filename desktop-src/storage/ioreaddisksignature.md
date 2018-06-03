---
title: IoReadDiskSignature routine
description: The IoReadDiskSignature routine reads the disk signature information for the partition table of a disk.
ms.assetid: c56d767f-598c-46b8-bab1-ce4de0780076
keywords:
- IoReadDiskSignature routine Storage Devices
topic_type:
- apiref
api_name:
- IoReadDiskSignature
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IoReadDiskSignature routine

The **IoReadDiskSignature** routine reads the disk signature information for the partition table of a disk.

## Syntax


```C++
NTSTATUS IoReadDiskSignature(
  _In_  PDEVICE_OBJECT  DeviceObject,
  _In_  ULONG           BytesPerSector,
  _Out_ PDISK_SIGNATURE Signature
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Specifies the device object for the disk to read.

</dd> <dt>

*BytesPerSector* \[in\]
</dt> <dd>

Specifies the number of bytes per sector of the disk.

</dd> <dt>

*Signature* \[out\]
</dt> <dd>

Pointer to a [**DISK\_SIGNATURE**](disk-signature.md) structure the routine uses to return the disk signature information.

</dd> </dl>

## Return value

The routine returns STATUS\_SUCCESS on success, or the appropriate error code on failure. The routine returns STATUS\_DISK\_CORRUPT\_ERROR if it detects that the disk partition table is corrupted.

## Remarks

**IoReadDiskSignature** must only be used by disk drivers. Other drivers should use the [**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX**](ioctl-disk-get-drive-geometry-ex.md) I/O request instead.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | This routine is only available on Windows XP and later.<br/>                                                                      |
| Header<br/>          | <dl> <dt>Ntddk.h (include Ntddk.h)</dt> </dl>                                    |
| Library<br/>         | <dl> <dt>NtosKrnl.lib</dt> </dl>                                                 |
| DLL<br/>             | <dl> <dt>NtosKrnl.exe</dt> </dl>                                                 |



## See also

<dl> <dt>

[**DISK\_SIGNATURE**](disk-signature.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX**](ioctl-disk-get-drive-geometry-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IoReadDiskSignature%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






