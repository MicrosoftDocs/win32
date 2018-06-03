---
title: IoCreateDisk routine
description: The IoCreateDisk routine initializes a raw disk by creating a new partition table.
ms.assetid: 0ad85551-a8d2-4f7f-958b-fe23111de340
keywords:
- IoCreateDisk routine Storage Devices
topic_type:
- apiref
api_name:
- IoCreateDisk
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

# IoCreateDisk routine

The **IoCreateDisk** routine initializes a raw disk by creating a new partition table.

## Syntax


```C++
NTSTATUS IoCreateDisk(
  _In_     PDEVICE_OBJECT      DeviceObject,
  _In_opt_ struct _CREATE_DISK *Disk
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Specifies the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) for the raw disk.

</dd> <dt>

*Disk* \[in, optional\]
</dt> <dd>

Pointer to a [**CREATE\_DISK**](create-disk.md) structure that specifies the type and parameters for the partition table. If *Disk* is **NULL**, the routine deletes the partition table on the disk.

</dd> </dl>

## Return value

Returns STATUS\_SUCCESS on success, or the appropriate error code on failure.

## Remarks

**IoCreateDisk** must only be used by disk drivers. Other drivers should use the [**IOCTL\_DISK\_CREATE\_DISK**](ioctl-disk-create-disk.md) I/O request instead.

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

[**CREATE\_DISK**](create-disk.md)
</dt> <dt>

[**IOCTL\_DISK\_CREATE\_DISK**](ioctl-disk-create-disk.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IoCreateDisk%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






