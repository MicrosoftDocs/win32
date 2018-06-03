---
title: DRIVERSTATUS structure
description: The DRIVERSTATUS structure is used in conjunction with the SENDCMDOUTPARAMS structure and the SMART\_SEND\_DRIVE\_COMMAND request to retrieve data returned by a Self-Monitoring Analysis and Reporting Technology (SMART) command.
ms.assetid: de97322f-a756-49a8-a6e6-dab42f278388
keywords:
- DRIVERSTATUS structure Storage Devices
- PDRIVERSTATUS structure pointer Storage Devices
- LPDRIVERSTATUS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DRIVERSTATUS
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DRIVERSTATUS structure

The DRIVERSTATUS structure is used in conjunction with the [**SENDCMDOUTPARAMS**](sendcmdoutparams.md) structure and the [**SMART\_SEND\_DRIVE\_COMMAND**](smart-send-drive-command.md) request to retrieve data returned by a Self-Monitoring Analysis and Reporting Technology (SMART) command.

## Syntax


```C++
typedef struct _DRIVERSTATUS {
  UCHAR bDriverError;
  UCHAR bIDEError;
  UCHAR bReserved[2];
  ULONG dwReserved[2];
} DRIVERSTATUS, *PDRIVERSTATUS, *LPDRIVERSTATUS;
```



## Members

<dl> <dt>

**bDriverError**
</dt> <dd>

Error code from driver, or 0 if no error.

</dd> <dt>

**bIDEError**
</dt> <dd>

Contents of IDE Error register.

</dd> <dt>

**bReserved**
</dt> <dd>

Reserved.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**SENDCMDOUTPARAMS**](sendcmdoutparams.md)
</dt> <dt>

[**SMART\_SEND\_DRIVE\_COMMAND**](smart-send-drive-command.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DRIVERSTATUS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






