---
title: SetPartitionDeviceElementWithFlags method of the BcdObject class
description: Sets the specified partition device element. This method is identical to SetPartitionDeviceElement except it takes additional flags.
ms.assetid: 'be7a88a3-f684-4155-a8c7-638f54125de0'
keywords: ["SetPartitionDeviceElementWithFlags method Boot Config", "SetPartitionDeviceElementWithFlags method Boot Config , BcdObject class", "BcdObject class Boot Config , SetPartitionDeviceElementWithFlags method"]
topic_type:
- apiref
api_name:
- BcdObject.SetPartitionDeviceElementWithFlags
api_location:
- Root\WMI
api_type:
- COM
---

# SetPartitionDeviceElementWithFlags method of the BcdObject class

Sets the specified partition device element. This method is identical to [**SetPartitionDeviceElement**](setpartitiondeviceelement-bcdobject.md) except it takes additional flags.

## Syntax


```mof
boolean SetPartitionDeviceElementWithFlags(
  [in] uint32 Type,
  [in] uint32 DeviceType,
  [in] string AdditionalOptions,
  [in] string Path,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The element type. This parameter is one of the Device element types from the following enumerations:

-   [**BcdBootMgrElementTypes**](bcdbootmgrelementtypes.md)
-   [**BcdDeviceObjectElementTypes**](bcddeviceobjectelementtypes.md)
-   [**BcdLibraryElementTypes**](bcdlibraryelementtypes.md)
-   [**BcdMemDiagElementTypes**](bcdmemdiagelementtypes.md)
-   [**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)

It can also be a custom element type created for your own use.

</dd> <dt>

*DeviceType* \[in\]
</dt> <dd>

The device type. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                       | Meaning                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <span id="BootDevice"></span><span id="bootdevice"></span><span id="BOOTDEVICE"></span><dl> <dt>**BootDevice**</dt> <dt>1</dt> </dl>                     | Device that initiated the boot.<br/>                                     |
| <span id="FileDevice"></span><span id="filedevice"></span><span id="FILEDEVICE"></span><dl> <dt>**FileDevice**</dt> <dt>3</dt> </dl>                     | File that contains file system metadata and is treated as a device.<br/> |
| <span id="PartitionDevice"></span><span id="partitiondevice"></span><span id="PARTITIONDEVICE"></span><dl> <dt>**PartitionDevice**</dt> <dt>2</dt> </dl> | Disk partition.<br/>                                                     |
| <span id="RamdiskDevice"></span><span id="ramdiskdevice"></span><span id="RAMDISKDEVICE"></span><dl> <dt>**RamdiskDevice**</dt> <dt>4</dt> </dl>         | Ramdisk.<br/>                                                            |
| <span id="UnknownDevice"></span><span id="unknowndevice"></span><span id="UNKNOWNDEVICE"></span><dl> <dt>**UnknownDevice**</dt> <dt>5</dt> </dl>         | Unknown.<br/>                                                            |



 

</dd> <dt>

*AdditionalOptions* \[in\]
</dt> <dd>

A GUID in string form with surrounding braces that represents another object in the store, or the empty string ("").

</dd> <dt>

*Path* \[in\]
</dt> <dd>

The path to the partition that contains the element to set.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter can be zero or the following value.



| Value                                                                                                                                                                                                                                                                                                | Meaning                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <span id="DisableVhdDeviceDetection"></span><span id="disablevhddevicedetection"></span><span id="DISABLEVHDDEVICEDETECTION"></span><dl> <dt>**DisableVhdDeviceDetection**</dt> <dt>32</dt> </dl> | Disable virtual hard disk (VHD) detection. Specify this flag if the partition will be used to boot a virtual machine. <br/> |



 

If this parameter is zero, VHD detection is enabled. For more information, see Remarks.

</dd> </dl>

## Remarks

By default, the [**SetPartitionDeviceElementWithFlags**](setpartitiondeviceelement-bcdobject.md) method detects whether the specified device path is backed by a VHD. If so, it creates a boot device using the VHD file information so that the device can be mounted on a physical machine at boot time. However, this type of VHD boot device is not compatible with a virtual machine. To suppress automatic VHD detection, specify the **DisableVhdDeviceDetection** flag when creating boot devices that will be used by the boot process of a virtual machine.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdObject**](bcdobject.md)
</dt> <dt>

[**SetPartitionDeviceElement**](setpartitiondeviceelement-bcdobject.md)
</dt> </dl>

 

 





