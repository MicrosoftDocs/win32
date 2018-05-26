---
title: STORAGE\_MINIPORT\_DESCRIPTOR structure
description: Reserved for system use.
ms.assetid: 30497CA8-70B6-48F9-B5D5-45E606A3226E
keywords:
- STORAGE_MINIPORT_DESCRIPTOR structure Storage Devices
- PSTORAGE_MINIPORT_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_MINIPORT_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_MINIPORT\_DESCRIPTOR structure

Reserved for system use.

## Syntax


```C++
typedef struct _STORAGE_MINIPORT_DESCRIPTOR {
  ULONG                 Version;
  ULONG                 Size;
  STORAGE_PORT_CODE_SET Portdriver;
  BOOLEAN               LUNResetSupported;
  BOOLEAN               TargetResetSupported;
  USHORT                IoTimeoutValue;
  BOOLEAN               ExtraIoInfoSupported;
  UCHAR                 Reserved0[3];
  UCHAR                 Reserved1;
} STORAGE_MINIPORT_DESCRIPTOR, *PSTORAGE_MINIPORT_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the size of this structure, in bytes. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the data returned, in bytes. This may include data that follows this structure.

</dd> <dt>

**Portdriver**
</dt> <dd>

Type of port driver as enumerated by the [**STORAGE\_PORT\_CODE\_SET**](storage-port-code-set.md) enumeration.

</dd> <dt>

**LUNResetSupported**
</dt> <dd>

Indicates whether a LUN reset is supported.

</dd> <dt>

**TargetResetSupported**
</dt> <dd>

Indicates whether a target reset is supported.

</dd> <dt>

**IoTimeoutValue**
</dt> <dd>

**Introduced in Windows 8:** Indicates the timeout value for the device, in milliseconds (ms).

</dd> <dt>

**ExtraIoInfoSupported**
</dt> <dd>

**Introduced in Windows 8.1:** Indicates if extra I/O info is supported.

</dd> <dt>

**Reserved0**
</dt> <dd>

**Introduced in Windows 8.1:** Reserved for future use.

</dd> <dt>

**Reserved1**
</dt> <dd>

**Introduced in Windows 8.1:** Reserved for future use.

</dd> </dl>

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_MINIPORT_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





