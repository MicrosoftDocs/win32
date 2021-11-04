---
description: LockMedia method of the Msvm_DisketteDrive class - Locks or releases the media.
ms.assetid: 90f7e06c-92d0-4742-a74d-68ae6bfc00bf
title: LockMedia method of the Msvm_DisketteDrive class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_DisketteDrive.LockMedia
api_type: 
- COM
api_location: 
- vmms.exe
---

# LockMedia method of the Msvm\_DisketteDrive class

Locks or releases the media.

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

Returns a 0 on success; otherwise, returns one of the following values:

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

[**Msvm\_DisketteDrive**](msvm-diskettedrive.md)
</dt> </dl>

 

 




