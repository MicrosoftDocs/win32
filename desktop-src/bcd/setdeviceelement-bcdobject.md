---
title: SetDeviceElement method of the BcdObject class
description: Sets the specified device element.
ms.assetid: 'dc077fb0-a0d5-4989-a9bf-d50b81a9f36a'
keywords: ["SetDeviceElement method Boot Config", "SetDeviceElement method Boot Config , BcdObject class", "BcdObject class Boot Config , SetDeviceElement method"]
topic_type:
- apiref
api_name:
- BcdObject.SetDeviceElement
api_location:
- Root\WMI
api_type:
- COM
---

# SetDeviceElement method of the BcdObject class

Sets the specified device element.

## Syntax


```mof
boolean SetDeviceElement(
  [in] uint32 Type,
  [in] uint32 DeviceType,
  [in] string AdditionalOptions
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

[**BcdDeviceElement**](bcddeviceelement.md)
</dt> <dt>

[**BcdObject**](bcdobject.md)
</dt> </dl>

 

 





