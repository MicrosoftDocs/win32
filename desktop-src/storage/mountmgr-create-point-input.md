---
title: MOUNTMGR\_CREATE\_POINT\_INPUT structure
description: The MOUNTMGR\_CREATE\_POINT\_INPUT structure is used by the mount manager to send a symbolic link name to a client that has requested symbolic link name by means of an IOCTL\_MOUNTMGR\_CREATE\_POINT request.
ms.assetid: 'b53d5163-612d-4bfb-89f4-21457629e365'
keywords: ["MOUNTMGR_CREATE_POINT_INPUT structure Storage Devices", "PMOUNTMGR_CREATE_POINT_INPUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MOUNTMGR_CREATE_POINT_INPUT
api_location:
- mountmgr.h
api_type:
- HeaderDef
---

# MOUNTMGR\_CREATE\_POINT\_INPUT structure

The MOUNTMGR\_CREATE\_POINT\_INPUT structure is used by the mount manager to send a symbolic link name to a client that has requested symbolic link name by means of an [**IOCTL\_MOUNTMGR\_CREATE\_POINT**](ioctl-mountmgr-create-point.md) request.

## Syntax


```C++
typedef struct _MOUNTMGR_CREATE_POINT_INPUT {
  USHORT SymbolicLinkNameOffset;
  USHORT SymbolicLinkNameLength;
  USHORT DeviceNameOffset;
  USHORT DeviceNameLength;
} MOUNTMGR_CREATE_POINT_INPUT, *PMOUNTMGR_CREATE_POINT_INPUT;
```



## Members

<dl> <dt>

**SymbolicLinkNameOffset**
</dt> <dd>

Contains an offset in bytes into the output buffer where the symbolic link name is located.

</dd> <dt>

**SymbolicLinkNameLength**
</dt> <dd>

Contains the length in bytes of the symbolic link name stored in the output buffer.

</dd> <dt>

**DeviceNameOffset**
</dt> <dd>

Contains an offset in bytes into the output buffer where the nonpersistent (target) device name is located.

</dd> <dt>

**DeviceNameLength**
</dt> <dd>

Contains the length in bytes of the nonpersistent (target) device name.

</dd> </dl>

## Remarks

The name given for purposes of identifying the volume can be of any type: a unique volume name, a symbolic link name, or a nonpersistent device name. For a discussion of the difference between symbolic link names and nonpersistent target device names, see [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTMGR\_CREATE\_POINT**](ioctl-mountmgr-create-point.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MOUNTMGR_CREATE_POINT_INPUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






