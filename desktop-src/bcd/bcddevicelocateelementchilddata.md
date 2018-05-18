---
title: BcdDeviceLocateElementChildData class
description: Represents the element to locate within the virtual hard disk (VHD) and specifies the VHD file's parent device for a VPART locate device.
ms.assetid: '07e62261-ade7-4786-aa22-6b7d1b5d78f3'
keywords: ["BcdDeviceLocateElementChildData class Boot Config", "BcdDeviceLocateElementChildData class Boot Config , described"]
topic_type:
- apiref
api_name:
- BcdDeviceLocateElementChildData
- BcdDeviceLocateElementChildData.Element
- BcdDeviceLocateElementChildData.Parent
api_location:
- Root\WMI
api_type:
- Schema
---

# BcdDeviceLocateElementChildData class

Represents the element to locate within the virtual hard disk (VHD) and specifies the VHD file's parent device for a VPART locate device.

## Syntax

``` syntax
class BcdDeviceLocateElementChildData : BcdDeviceLocateData
{
  uint32        Element;
  BcdDeviceData Parent;
};
```

## Members

The **BcdDeviceLocateElementChildData** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDeviceLocateElementChildData** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The element to locate within the VHD.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **BcdDeviceData**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The VHD file's parent device.

</dd> </dl>

## Remarks

If the disk signature and partition identifier within the VHD are omitted, it is necessary to search all VHD partitions to locate the partition that contains the boot device element (the application path for a device on which a boot application resides, or the system root for a device on which an operating system resides). This is a referred to as a *VPART locate device*. To specify a locate device, use the [**SetVhdDeviceElement**](setvhddeviceelement-bcdobject.md) method.

A VHD file's parent device is always a [**BcdDeviceFileData**](bcddevicefiledata.md) element, which has either a [**BcdDevicePartitionData**](bcddevicepartitiondata.md) or a [**BcdDeviceLocateStringData**](bcddevicelocatestringdata.md) element as its parent.

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

 

 





