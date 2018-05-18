---
title: SetFileDeviceElement method of the BcdObject class
description: Sets the specified file device element.
ms.assetid: '0501cf17-39bb-48fa-a581-3d6b18e24c38'
keywords: ["SetFileDeviceElement method Boot Config", "SetFileDeviceElement method Boot Config , BcdObject class", "BcdObject class Boot Config , SetFileDeviceElement method"]
topic_type:
- apiref
api_name:
- BcdObject.SetFileDeviceElement
api_location:
- Root\WMI
api_type:
- COM
---

# SetFileDeviceElement method of the BcdObject class

Sets the specified file device element.

## Syntax


```mof
boolean SetFileDeviceElement(
  [in] uint32 Type,
  [in] uint32 DeviceType,
  [in] string AdditionalOptions,
  [in] string Path,
  [in] uint32 ParentDeviceType,
  [in] string ParentAdditionalOptions,
  [in] string ParentPath
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

Either a GUID in string form with surrounding curly braces that represents another object in the store, or the empty string ("").

</dd> <dt>

*Path* \[in\]
</dt> <dd>

The file path.

</dd> <dt>

*ParentDeviceType* \[in\]
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

*ParentAdditionalOptions* \[in\]
</dt> <dd>

Either a GUID in string form with surrounding curly braces that represents another object in the store, or the empty string ("").

</dd> <dt>

*ParentPath* \[in\]
</dt> <dd>

The path of the parent. This parameter can be an empty string ("") if the parent device is of a type that does not have a path.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





