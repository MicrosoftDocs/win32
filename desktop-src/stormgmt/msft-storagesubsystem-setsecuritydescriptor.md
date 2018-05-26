---
title: SetSecurityDescriptor method of the MSFT\_StorageSubSystem class
description: Sets the security descriptor that controls access to the storage subsystem object instance.
ms.assetid: 045CDEC1-3B2D-4BB1-BA2D-8873B589C402
keywords:
- SetSecurityDescriptor method Windows Storage Management API
- SetSecurityDescriptor method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , SetSecurityDescriptor method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.SetSecurityDescriptor
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetSecurityDescriptor method of the MSFT\_StorageSubSystem class

Sets the security descriptor that controls access to the storage subsystem object instance.

## Syntax


```mof
UInt32 SetSecurityDescriptor(
  [in]  String SecurityDescriptor,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*SecurityDescriptor* \[in\]
</dt> <dd>

A Security Descriptor Definition Language (SDDL) formatted string describing the desired access control list of the object.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> </dl>

## Remarks

The user must have sufficient privileges to set the security descriptor.

If the call is not made in the context of a user specified in the security descriptor's access control list, this method will fail with **Access Denied**.

If an empty security descriptor is passed to this method, the behavior is left to the specific implementation as long as there is some user context (typically domain administrators) that can access and administer the object.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





