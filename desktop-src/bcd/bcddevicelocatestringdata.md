---
title: BcdDeviceLocateStringData class
description: Represents the parent of a virtual hard disk (VHD) file's parent device and specifies the string to search for a VPART+PPART locate device.
ms.assetid: 'c4af04f6-9f56-4fb7-9dfd-ba7f72753435'
keywords: ["BcdDeviceLocateStringData class Boot Config", "BcdDeviceLocateStringData class Boot Config , described"]
topic_type:
- apiref
api_name:
- BcdDeviceLocateStringData
- BcdDeviceLocateStringData.Path
api_location:
- Root\WMI
api_type:
- Schema
---

# BcdDeviceLocateStringData class

Represents the parent of a virtual hard disk (VHD) file's parent device and specifies the string to search for a VPART+PPART locate device.

## Syntax

``` syntax
class BcdDeviceLocateStringData : BcdDeviceLocateData
{
  string Path;
};
```

## Members

The **BcdDeviceLocateStringData** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDeviceLocateStringData** class has these properties.

<dl> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The string to search for a VPART+PPART locate device.

</dd> </dl>

## Remarks

If the disk signature and partition identifier within the VHD are omitted, it is necessary to search all VHD partitions to locate the partition that contains the boot device element (the application path for a device on which a boot application resides, or the system root for a device on which an operating system resides). This is a referred to as a *VPART locate device*. If the VHD file's parent disk signature and partition identifier are also omitted, it is also necessary to search all of the physical disks to locate the VHD file. This is referred to as a *VPART+PPART locate device*. To specify a locate device, use the [**SetVhdDeviceElement**](setvhddeviceelement-bcdobject.md) method.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdDeviceLocateData**](bcddevicelocatedata.md)
</dt> <dt>

[**SetVhdDeviceElement**](setvhddeviceelement-bcdobject.md)
</dt> </dl>

 

 





