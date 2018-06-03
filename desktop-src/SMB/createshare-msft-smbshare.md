---
title: CreateShare method of the MSFT\_SmbShare class
description: Creates a new share and allows the creator to specify initial access rights that determine who can and can t access the newly created share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d411f1f-e167-4bb6-aaf9-22ced0e43508
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateShare method SMB
- CreateShare method SMB , MSFT_SmbShare class
- MSFT_SmbShare class SMB , CreateShare method
topic_type:
- apiref
api_name:
- MSFT_SmbShare.CreateShare
api_location:
- SmbWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateShare method of the MSFT\_SmbShare class

Creates a new share and allows the creator to specify initial access rights that determine who can and can t access the newly created share.

## Syntax


```mof
uint32 CreateShare(
  [in]  string        Name,
  [in]  string        ScopeName,
  [in]  string        Path,
  [in]  string        Description,
  [in]  uint32        ConcurrentUserLimit,
  [in]  uint32        FolderEnumerationMode,
  [in]  uint32        CachingMode,
  [in]  boolean       Temporary,
  [in]  boolean       ContinuouslyAvailable,
  [in]  uint32        CATimeout,
  [in]  boolean       EncryptData,
  [in]  string        FullAccess[],
  [in]  string        ChangeAccess[],
  [in]  string        ReadAccess[],
  [in]  string        NoAccess[],
  [in]  string        SecurityDescriptor,
  [out] MSFT_SmbShare CreatedShare
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the share.

</dd> <dt>

*ScopeName* \[in\]
</dt> <dd>

Name of the endpoint to which the share is scoped.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

Absolute path to the file system directory that is shared. **Null** if the share is not a file share.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Optional description of the share.

</dd> <dt>

*ConcurrentUserLimit* \[in\]
</dt> <dd>

Maximum number of users that may concurrently access the share. If this property is zero, there is no limit.

</dd> <dt>

*FolderEnumerationMode* \[in\]
</dt> <dd>

The enumeration mode that is enabled for the share.

<dt>

<span id="AccessBased"></span><span id="accessbased"></span><span id="ACCESSBASED"></span>

<span id="AccessBased"></span><span id="accessbased"></span><span id="ACCESSBASED"></span>**AccessBased** (0)


</dt> <dd>

Access-based

</dd> <dt>

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>**Unrestricted** (1)


</dt> <dd>

Unrestricted

</dd> </dl> </dd> <dt>

*CachingMode* \[in\]
</dt> <dd>

The caching policy for the share.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>

**Manual** (1)


</dt> <dd></dd> <dt>

<span id="Documents"></span><span id="documents"></span><span id="DOCUMENTS"></span>

**Documents** (2)


</dt> <dd></dd> <dt>

<span id="Programs"></span><span id="programs"></span><span id="PROGRAMS"></span>

**Programs** (3)


</dt> <dd></dd> <dt>

<span id="BranchCache"></span><span id="branchcache"></span><span id="BRANCHCACHE"></span>

**BranchCache** (4)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (5)


</dt> <dd></dd> </dl> </dd> <dt>

*Temporary* \[in\]
</dt> <dd>

Indicates whether this is a temporary share.

</dd> <dt>

*ContinuouslyAvailable* \[in\]
</dt> <dd>

Indicates whether the share supports continuous availability.

</dd> <dt>

*CATimeout* \[in\]
</dt> <dd>

In case of a failover, the number of seconds the client will wait before failing the operation.

</dd> <dt>

*EncryptData* \[in\]
</dt> <dd>

Indicates whether the data on the share should be encrypted.

</dd> <dt>

*FullAccess* \[in\]
</dt> <dd>

An array of strings containing the account names of users to be granted full access to the share.

</dd> <dt>

*ChangeAccess* \[in\]
</dt> <dd>

An array of strings containing the account names of users to be granted change access to the share.

</dd> <dt>

*ReadAccess* \[in\]
</dt> <dd>

An array of strings containing the account names of users to be granted read-only access to the share.

</dd> <dt>

*NoAccess* \[in\]
</dt> <dd>

An array of strings containing the account names of users to be granted no access to the share.

</dd> <dt>

*SecurityDescriptor* \[in\]
</dt> <dd>

The name of the security descriptor of the share.

**Windows Server 2012 and Windows 8:** This parameter is not supported before Windows Server 2012 R2 and Windows 8.1.

</dd> <dt>

*CreatedShare* \[out\]
</dt> <dd>

An instance of the [**MSFT\_SmbShare**](msft-smbshare.md) class that represents the share.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                    |
| Header<br/>                   | <dl> <dt>Shobjidl\_core.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_SmbShare**](msft-smbshare.md)
</dt> <dt>

[**NetShareAdd**](https://msdn.microsoft.com/library/windows/desktop/bb525384)
</dt> </dl>

 

 





