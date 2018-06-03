---
title: BcdDeviceLocateData class
description: Represents the root class of all locate device data types and specifies the locate type of the device.
ms.assetid: 2bbe2054-7eb6-4cb6-9742-3ac338ebc381
keywords:
- BcdDeviceLocateData class Boot Config
- BcdDeviceLocateData class Boot Config , described
topic_type:
- apiref
api_name:
- BcdDeviceLocateData
- BcdDeviceLocateData.Type
api_location:
- Root\WMI
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BcdDeviceLocateData class

Represents the root class of all locate device data types and specifies the locate type of the device.

## Syntax

``` syntax
class BcdDeviceLocateData : BcdDeviceData
{
  uint32 Type;
};
```

## Members

The **BcdDeviceLocateData** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDeviceLocateData** class has these properties.

<dl> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The locate device type. This property can be one of the following values.



| Value                                                                                                                                                                                                                                           | Meaning                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <span id="Element"></span><span id="element"></span><span id="ELEMENT"></span><dl> <dt>**Element**</dt> <dt>0</dt> </dl>                     | This locate device type is not used. <br/> |
| <span id="String"></span><span id="string"></span><span id="STRING"></span><dl> <dt>**String**</dt> <dt>1</dt> </dl>                         | A VPART+PPART locate device. <br/>         |
| <span id="ElementChild"></span><span id="elementchild"></span><span id="ELEMENTCHILD"></span><dl> <dt>**ElementChild**</dt> <dt>2</dt> </dl> | A VPART locate device.<br/>                |



 

</dd> </dl>

## Remarks

If the disk signature and partition identifier within the virtual hard disk (VHD) are omitted, it is necessary to search all VHD partitions to locate the partition that contains the boot device element (the application path for a device on which a boot application resides, or the system root for a device on which an operating system resides). This is a referred to as a *VPART locate device*.

If the VHD file's parent disk signature and partition identifier are also omitted, it is also necessary to search all of the physical disks to locate the VHD file. This is referred to as a *VPART+PPART locate device*. A locate device can be specified by calling the [**SetVhdDeviceElement**](setvhddeviceelement-bcdobject.md) method.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdDeviceData**](bcddevicedata.md)
</dt> <dt>

[**BcdDeviceLocateElementChildData**](bcddevicelocateelementchilddata.md)
</dt> <dt>

[**BcdDeviceLocateElementData**](bcddevicelocateelementdata.md)
</dt> <dt>

[**BcdDeviceLocateStringData**](bcddevicelocatestringdata.md)
</dt> </dl>

 

 





