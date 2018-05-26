---
title: SetQualifiedPartitionDeviceElement method of the BcdObject class
description: Sets a qualified boot partition device.
ms.assetid: 9ae167e0-ad14-47a5-aa81-ca76da262878
keywords:
- SetQualifiedPartitionDeviceElement method Boot Config
- SetQualifiedPartitionDeviceElement method Boot Config , BcdObject class
- BcdObject class Boot Config , SetQualifiedPartitionDeviceElement method
topic_type:
- apiref
api_name:
- BcdObject.SetQualifiedPartitionDeviceElement
api_location:
- Root\WMI
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetQualifiedPartitionDeviceElement method of the BcdObject class

Sets a qualified boot partition device.

## Syntax


```mof
boolean SetQualifiedPartitionDeviceElement(
  [in] ULONG  Type,
  [in] ULONG  PartitionStyle,
  [in] PCWSTR DiskSignature,
  [in] PCWSTR PartitionIdentifier
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

*PartitionStyle* \[in\]
</dt> <dd>

The partition style. This property can be one of the following values.



| Value                                                                                                                                                                                 | Meaning                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="GPT"></span><span id="gpt"></span><dl> <dt>**GPT**</dt> <dt>1</dt> </dl> | The partition is described in a GUID partition table (GPT).<br/> |
| <span id="MBR"></span><span id="mbr"></span><dl> <dt>**MBR**</dt> <dt>0</dt> </dl> | The partition is described in a master boot record (MBR).<br/>   |



 

</dd> <dt>

*DiskSignature* \[in\]
</dt> <dd>

If the **PartitionStyle** parameter is GPT, the **DiskSignature** parameter is the disk signature as a GUID in string format (for example, "{7c69a706-eda5-11dd-bc09-001e4ce28b8f}"). If the **PartitionStyle** parameter is MBR, the **DiskSignature** parameter is the decimal MBR disk signature in string format (for example, "402653184" for 0x18000000).

</dd> <dt>

*PartitionIdentifier* \[in\]
</dt> <dd>

If the **PartitionStyle** parameter is GPT, the **PartitionIdentifier** parameter is the partition signature as a GUID in string format (for example, "{6efb52bf-1766-41db-a6b3-0ee5eff72bd7}" ). If the **PartitionStyle** parameter is MBR, the **PartitionIdentifier** parameter is the decimal MBR partition offset in string format (for example, "82837504" for 0x4F00000).

</dd> </dl>

## Remarks

The [**BcdDeviceQualifiedPartitionData**](bcddevicequalifiedpartitiondata.md) data type uniquely identifies a boot partition device by its type, disk signature, and partition identifier. An application can enumerate a qualified partition by using the [**GetElementWithFlags**](getelementwithflags-bcdobject.md) method with the *Flags* parameter set to **Qualified** (1).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdDeviceQualifiedPartitionData**](bcddevicequalifiedpartitiondata.md)
</dt> <dt>

[**BcdObject**](bcdobject.md)
</dt> <dt>

[**GetElementWithFlags**](getelementwithflags-bcdobject.md)
</dt> </dl>

 

 





