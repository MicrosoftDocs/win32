---
title: Unmount method of the Msvm\_MountedStorageImage class
description: Unmounts the storage image.
ms.assetid: 'b59ad612-b0a3-4d6a-8669-d07a50675f1c'
keywords: ["Unmount method Hyper-V", "Unmount method Hyper-V , Msvm_MountedStorageImage class", "Msvm_MountedStorageImage class Hyper-V , Unmount method"]
topic_type:
- apiref
api_name:
- Msvm_MountedStorageImage.Unmount
api_location:
- Root\Virtualization
api_type:
- COM
---

# Unmount method of the Msvm\_MountedStorageImage class

Unmounts the storage image.

## Syntax


```mof
uint32 Unmount();
```



## Parameters

This method has no parameters.

## Return value

Type: **uint32**

This method can return one of the following values.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Failed** (1)
</dt> </dl>

## Remarks

Access to the [**Msvm\_MountedStorageImage**](msvm-mountedstorageimage.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_MountedStorageImage**](msvm-mountedstorageimage.md)
</dt> </dl>

 

 





