---
title: AddMountPoint method of the Win32\_Volume class
description: Adds a mount point directory for the volume.
ms.assetid: 21a33e2b-5f31-459f-8b08-b991e2edc547
keywords:
- AddMountPoint method
- AddMountPoint method, Win32_Volume class
- Win32_Volume class, AddMountPoint method
topic_type:
- apiref
api_name:
- Win32_Volume.AddMountPoint
api_location:
- Vdswmi.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddMountPoint method of the Win32\_Volume class

The **AddMountPoint** method adds a mount point directory for the volume. The result of this method is the creation of a [**Win32\_MountPoint**](win32-mountpoint.md) class associating this volume with the [**Win32\_Directory**](https://msdn.microsoft.com/library/aa394130) instance representing the directory specified in the parameter list.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 AddMountPoint(
  [in] string Directory
);
```



## Parameters

<dl> <dt>

*Directory* \[in\]
</dt> <dd>

Directory where the volume is to be mounted.

</dd> </dl>

## Return value



| Return code                                                                      | Description                                  |
|----------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**0**</dt> </dl> | Success<br/>                           |
| <dl> <dt>**1**</dt> </dl> | Access Denied<br/>                     |
| <dl> <dt>**2**</dt> </dl> | Invalid Argument<br/>                  |
| <dl> <dt>**3**</dt> </dl> | Specified Directory Not Empty<br/>     |
| <dl> <dt>**4**</dt> </dl> | Specified Directory Not Found<br/>     |
| <dl> <dt>**5**</dt> </dl> | Volume Mount Points Not Supported<br/> |
| <dl> <dt>**6**</dt> </dl> | Unknown Error<br/>                     |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vds.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vdswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Volume**](win32-volume.md)
</dt> </dl>

 

 





