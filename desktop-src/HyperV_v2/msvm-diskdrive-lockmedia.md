---
description: Locks or unlocks the media.
ms.assetid: 805efb2d-71a7-4c74-821f-942644928ff9
title: LockMedia method of the Msvm_DiskDrive class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_DiskDrive.LockMedia
api_type: 
- COM
api_location: 
- vmms.exe
---

# LockMedia method of the Msvm\_DiskDrive class

Locks or unlocks the media.

## Syntax


```mof
uint32 LockMedia(
  [in] boolean Lock
);
```



## Parameters

<dl> <dt>

*Lock* \[in\]
</dt> <dd>

**true** to lock the media; **false** to release the media.

</dd> </dl>

## Return value

This method returns one of the following values:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not supported** (1)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_DiskDrive**](msvm-diskdrive.md)
</dt> </dl>

 

 




