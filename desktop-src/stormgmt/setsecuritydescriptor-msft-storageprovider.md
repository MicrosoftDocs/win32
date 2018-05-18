---
title: SetSecurityDescriptor method of the MSFT\_StorageProvider class
description: Sets the security descriptor that controls access to the storage provider object instance.
ms.assetid: 'B8C903EE-96CA-4854-971A-C7A914F91BB5'
keywords: ["SetSecurityDescriptor method Windows Storage Management API", "SetSecurityDescriptor method Windows Storage Management API , MSFT_StorageProvider class", "MSFT_StorageProvider class Windows Storage Management API , SetSecurityDescriptor method"]
topic_type:
- apiref
api_name:
- MSFT_StorageProvider.SetSecurityDescriptor
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetSecurityDescriptor method of the MSFT\_StorageProvider class

Sets the security descriptor that controls access to the storage provider object instance.

## Syntax


```mof
UInt32 SetSecurityDescriptor(
  [in]  String SecurityDescriptor,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*SecurityDescriptor* \[in\]
</dt> <dd>

A Security Descriptor Definition Language (SDDL) formatted string describing the access control list of the object.

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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageProvider**](msft-storageprovider.md)
</dt> </dl>

 

 





