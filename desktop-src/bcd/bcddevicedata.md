---
title: BcdDeviceData class
description: The root class of all device data types.
ms.assetid: f07d06f0-dfd4-4bb2-8539-9329dade0b2d
keywords:
- BcdDeviceData class Boot Config
- BcdDeviceData class Boot Config , described
topic_type:
- apiref
api_name:
- BcdDeviceData
- BcdDeviceData.DeviceType
- BcdDeviceData.AdditionalOptions
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

# BcdDeviceData class

The root class of all device data types.

## Syntax

``` syntax
class BcdDeviceData
{
  uint32 DeviceType;
  string AdditionalOptions;
};
```

## Members

The **BcdDeviceData** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDeviceData** class has these properties.

<dl> <dt>

**AdditionalOptions**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional options for the specified element. This property can be either a GUID in string form with surrounding curly braces that represents another object in the store, or the empty string ("").

</dd> <dt>

**DeviceType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device type. This property can be one of the following values.



| Value                                                                                                                                                                                                                                                                   | Meaning                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <span id="BootDevice"></span><span id="bootdevice"></span><span id="BOOTDEVICE"></span><dl> <dt>**BootDevice**</dt> <dt>1</dt> </dl>                                 | Device that initiated the boot.<br/>                                     |
| <span id="FileDevice"></span><span id="filedevice"></span><span id="FILEDEVICE"></span><dl> <dt>**FileDevice**</dt> <dt>3</dt> </dl>                                 | File that contains file system metadata and is treated as a device.<br/> |
| <span id="LocateDevice"></span><span id="locatedevice"></span><span id="LOCATEDEVICE"></span><dl> <dt>**LocateDevice**</dt> <dt>7</dt> </dl>                         | This value is not used.<br/>                                             |
| <span id="LocateExDevice"></span><span id="locateexdevice"></span><span id="LOCATEEXDEVICE"></span><dl> <dt>**LocateExDevice**</dt> <dt>8</dt> </dl>                 | Locate device.<br/>                                                      |
| <span id="PartitionDevice"></span><span id="partitiondevice"></span><span id="PARTITIONDEVICE"></span><dl> <dt>**PartitionDevice**</dt> <dt>2</dt> </dl>             | Disk partition.<br/>                                                     |
| <span id="QualifiedPartition"></span><span id="qualifiedpartition"></span><span id="QUALIFIEDPARTITION"></span><dl> <dt>**QualifiedPartition**</dt> <dt>6</dt> </dl> | Qualified disk partition.<br/>                                           |
| <span id="RamdiskDevice"></span><span id="ramdiskdevice"></span><span id="RAMDISKDEVICE"></span><dl> <dt>**RamdiskDevice**</dt> <dt>4</dt> </dl>                     | Ramdisk.<br/>                                                            |
| <span id="UnknownDevice"></span><span id="unknowndevice"></span><span id="UNKNOWNDEVICE"></span><dl> <dt>**UnknownDevice**</dt> <dt>5</dt> </dl>                     | Unknown.<br/>                                                            |



 

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



 

 





