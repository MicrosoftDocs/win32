---
title: SetVhdDeviceElement method of the BcdObject class
description: Creates a virtual hard disk (VHD) boot device element.
ms.assetid: b39c0117-ede1-4eea-a784-0312c259cdc7
keywords:
- SetVhdDeviceElement method Boot Config
- SetVhdDeviceElement method Boot Config , BcdObject class
- BcdObject class Boot Config , SetVhdDeviceElement method
topic_type:
- apiref
api_name:
- BcdObject.SetVhdDeviceElement
api_location:
- Root\WMI
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetVhdDeviceElement method of the BcdObject class

Creates a virtual hard disk (VHD) boot device element.

## Syntax


```mof
boolean SetVhdDeviceElement(
  [in] ULONG  Type,
  [in] PCWSTR Path,
  [in] ULONG  ParentDeviceType,
  [in] PCWSTR ParentAdditionalOptions,
  [in] PCWSTR ParentPath,
  [in] ULONG  CustomLocate
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the values from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

The path to the VHD file.

</dd> <dt>

*ParentDeviceType* \[in\]
</dt> <dd>

The device type. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                       | Meaning                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <span id="BootDevice"></span><span id="bootdevice"></span><span id="BOOTDEVICE"></span><dl> <dt>**BootDevice**</dt> <dt>1</dt> </dl>                     | Device that initiated the boot.<br/>                                            |
| <span id="FileDevice"></span><span id="filedevice"></span><span id="FILEDEVICE"></span><dl> <dt>**FileDevice**</dt> <dt>3</dt> </dl>                     | File that contains file system metadata. This file is treated as a device.<br/> |
| <span id="LocateDevice"></span><span id="locatedevice"></span><span id="LOCATEDEVICE"></span><dl> <dt>**LocateDevice**</dt> <dt>8</dt> </dl>             | Locate device. The *ParentPath* parameter is not used.<br/>                     |
| <span id="PartitionDevice"></span><span id="partitiondevice"></span><span id="PARTITIONDEVICE"></span><dl> <dt>**PartitionDevice**</dt> <dt>2</dt> </dl> | Disk partition.<br/>                                                            |
| <span id="RamdiskDevice"></span><span id="ramdiskdevice"></span><span id="RAMDISKDEVICE"></span><dl> <dt>**RamdiskDevice**</dt> <dt>4</dt> </dl>         | Ramdisk.<br/>                                                                   |
| <span id="UnknownDevice"></span><span id="unknowndevice"></span><span id="UNKNOWNDEVICE"></span><dl> <dt>**UnknownDevice**</dt> <dt>5</dt> </dl>         | Unknown.<br/>                                                                   |



 

</dd> <dt>

*ParentAdditionalOptions* \[in\]
</dt> <dd>

Either a GUID in string form with surrounding braces that represents another object in the store, or the empty string ("").

</dd> <dt>

*ParentPath* \[in\]
</dt> <dd>

The path to the physical partition that contains the VHD file. If the *ParentDeviceType* parameter is **Locate**, this parameter is not used.

</dd> <dt>

*CustomLocate* \[in\]
</dt> <dd>

A BCD element that overrides the default locate heuristics for a VHD device.

If this parameter is zero, the application path (for example, \\Windows\\System32\\winload.exe) is used to locate a boot device and the system root element (\\Windows) is used to locate an operating system device.

</dd> </dl>

## Remarks

A native VHD boot device element is identified by its VHD file name and a parent device that describes the physical partition that contains the VHD file. This kind of VHD device element also specifies a partition within the VHD and is the only VHD boot device that supports multi-boot scenarios within a single VHD. A native VHD boot device element provides the fastest performance because it is fully qualified; however, its entry in the BCD store is not portable and cannot be used in a BCD store that will be imported to a different system. To create native VHD boot device elements for mounted VHDs, use the [**SetPartitionDeviceElement**](setpartitiondeviceelement-bcdobject.md) method.

A VPART+PPART locate VHD device element is identified by its VHD file name only, and the parent device is not specified. The system resolves the VPART to the first VHD partition that contains the specified element and resolves the PPART to the first physical partition that contains the VHD file. A VPART+PPART locate VHD device element is slower and cannot be used for multi-boot scenarios, but its entry in the BCD store is portable. Use this kind of locate VHD device entry in a BCD store that will be imported on a different system.

A VPART locate VHD device element is identified by its VHD file name and its corresponding parent physical partition device. A VPART locate VHD device element has better performance than a VPART+PPART locate VHD device element, but its entry in the BCD store is not portable. The VPART locate device is the best choice for most applications because it provides reasonable performance and can be created without having to mount the VHD.

To enumerate a VHD boot device, use the locate data types [**BcdDeviceLocateData**](bcddevicelocatedata.md), [**BcdDeviceLocateElementChildData**](bcddevicelocateelementchilddata.md), [**BcdDeviceLocateElementData**](bcddevicelocateelementdata.md), and [**BcdDeviceLocateStringData**](bcddevicelocatestringdata.md).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdDeviceLocateData**](bcddevicelocatedata.md)
</dt> <dt>

[**BcdDeviceLocateElementChildData**](bcddevicelocateelementchilddata.md)
</dt> <dt>

[**BcdDeviceLocateElementData**](bcddevicelocateelementdata.md)
</dt> <dt>

[**BcdDeviceLocateStringData**](bcddevicelocatestringdata.md)
</dt> <dt>

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





