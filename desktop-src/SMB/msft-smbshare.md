---
title: MSFT\_SmbShare class
description: Represents an SMB share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b6a23782-92fd-489d-af03-98ea146f8676'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SmbShare class SMB", "MSFT_SmbShare class SMB , described"]
topic_type:
- apiref
api_name:
- MSFT_SmbShare
- MSFT_SmbShare.Name
- MSFT_SmbShare.ScopeName
- MSFT_SmbShare.Scoped
- MSFT_SmbShare.ShareType
- MSFT_SmbShare.Special
- MSFT_SmbShare.Temporary
- MSFT_SmbShare.ShadowCopy
- MSFT_SmbShare.Path
- MSFT_SmbShare.Volume
- MSFT_SmbShare.Description
- MSFT_SmbShare.ConcurrentUserLimit
- MSFT_SmbShare.CurrentUsers
- MSFT_SmbShare.SecurityDescriptor
- MSFT_SmbShare.EncryptData
- MSFT_SmbShare.FolderEnumerationMode
- MSFT_SmbShare.CachingMode
- MSFT_SmbShare.ContinuouslyAvailable
- MSFT_SmbShare.CATimeout
- MSFT_SmbShare.ShareState
- MSFT_SmbShare.SmbInstance
- MSFT_SmbShare.AvailabilityType
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
---

# MSFT\_SmbShare class

Represents an SMB share.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("30"), DisplayName("Smb Share"), AMENDMENT]
class MSFT_SmbShare
{
  string  Name;
  string  ScopeName;
  boolean Scoped;
  uint32  ShareType;
  boolean Special;
  boolean Temporary;
  boolean ShadowCopy;
  string  Path;
  string  Volume;
  string  Description;
  uint32  ConcurrentUserLimit;
  uint32  CurrentUsers;
  string  SecurityDescriptor;
  boolean EncryptData;
  uint32  FolderEnumerationMode;
  uint32  CachingMode;
  boolean ContinuouslyAvailable;
  uint32  CATimeout;
  uint32  ShareState;
  uint32  SmbInstance;
  uint32  AvailabilityType;
};
```

## Members

The **MSFT\_SmbShare** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbShare** class has these methods.



| Method                                                                   | Description                                                                                                                                             |
|:-------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BlockAccess**](blockaccess-msft-smbshare.md)                         | Updates a share's security descriptor to block accounts from accessing a share.<br/>                                                              |
| [**CreateShare**](createshare-msft-smbshare.md)                         | Creates a new share and allows the creator to specify initial access rights that determine who can and can't access the newly created share.<br/> |
| [**EnumerateShares**](enumerateshares-msft-smbshare.md)                 | Enumerates the specified shares.<br/>                                                                                                             |
| [**FireShareChangeEvent**](firesharechangeevent-msft-smbshare.md)       | This method is reserved for system use.<br/>                                                                                                      |
| [**GetAccessControlEntries**](getaccesscontrolentries-msft-smbshare.md) | Retrieves the access rights that have been granted to the share.<br/>                                                                             |
| [**GetShare**](getshare-msft-smbshare.md)                               | Returns a specified share instance.<br/>                                                                                                          |
| [**GrantAccess**](grantaccess-msft-smbshare.md)                         | Updates a share's security descriptor to grant accounts permission to access a share.<br/>                                                        |
| [**RevokeAccess**](revokeaccess-msft-smbshare.md)                       | Updates a share's security descriptor to revoke permission to access a share from a set of accounts.<br/>                                         |
| [**UnblockAccess**](unblockaccess-msft-smbshare.md)                     | Updates a share's security descriptor to unblock accounts from accessing a share.<br/>                                                            |



 

### Properties

The **MSFT\_SmbShare** class has these properties.

<dl> <dt>

**AvailabilityType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The availability status of the share.

<dt>

<span id="NonClustered"></span><span id="nonclustered"></span><span id="NONCLUSTERED"></span>

**NonClustered** (0)


</dt> <dd></dd> <dt>

<span id="Clustered"></span><span id="clustered"></span><span id="CLUSTERED"></span>

**Clustered** (1)


</dt> <dd></dd> <dt>

<span id="ScaleOut"></span><span id="scaleout"></span><span id="SCALEOUT"></span>

**ScaleOut** (2)


</dt> <dd></dd> <dt>

<span id="CSV"></span><span id="csv"></span>

**CSV** (3)


</dt> <dd></dd> <dt>

<span id="DFS"></span><span id="dfs"></span>

**DFS** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**CachingMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

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


</dt> <dd></dd> </dl>

</dd> <dt>

**CATimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

In case of a failover, the number of seconds the client will wait before failing the operation.

</dd> <dt>

**ConcurrentUserLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum number of users that may concurrently access the share. If this property is zero, there is no limit.

</dd> <dt>

**ContinuouslyAvailable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the share supports continuous availability.

</dd> <dt>

**CurrentUsers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of users that are currently connected to this share.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Optional description of the share.

</dd> <dt>

**EncryptData**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the data on the share should be encrypted.

</dd> <dt>

**FolderEnumerationMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

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

</dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Name of the share.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Absolute path to the file system directory that is shared. **Null** if **ShareType** is not **File System Directory**.

</dd> <dt>

**Scoped**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the share is scoped.

</dd> <dt>

**ScopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Name of the endpoint to which the share is scoped.

</dd> <dt>

**SecurityDescriptor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

SDDL-formatted security descriptor for the share.

</dd> <dt>

**ShadowCopy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the share represents a shadow copy for Remote VSS for File Shares (RVSS).

</dd> <dt>

**ShareState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of the share.

<dt>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>

**Pending** (0)


</dt> <dd></dd> <dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>

**Online** (1)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**ShareType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the type of resource that is shared.

<dt>

<span id="File_System_Directory"></span><span id="file_system_directory"></span><span id="FILE_SYSTEM_DIRECTORY"></span>

<span id="File_System_Directory"></span><span id="file_system_directory"></span><span id="FILE_SYSTEM_DIRECTORY"></span>**File System Directory** (0)


</dt> <dd>

File share

</dd> <dt>

<span id="Print_Queue"></span><span id="print_queue"></span><span id="PRINT_QUEUE"></span>

<span id="Print_Queue"></span><span id="print_queue"></span><span id="PRINT_QUEUE"></span>**Print Queue** (1)


</dt> <dd>

Print queue

</dd> <dt>

<span id="Communication_Device"></span><span id="communication_device"></span><span id="COMMUNICATION_DEVICE"></span>

<span id="Communication_Device"></span><span id="communication_device"></span><span id="COMMUNICATION_DEVICE"></span>**Communication Device** (2)


</dt> <dd>

Communication device

</dd> <dt>

<span id="Interprocess_Communication"></span><span id="interprocess_communication"></span><span id="INTERPROCESS_COMMUNICATION"></span>

<span id="Interprocess_Communication"></span><span id="interprocess_communication"></span><span id="INTERPROCESS_COMMUNICATION"></span>**Interprocess Communication** (3)


</dt> <dd>

Interprocess communication (IPC) mechanism

</dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (4)


</dt> <dd>

Unknown

</dd> </dl>

</dd> <dt>

**SmbInstance**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifier of the SMB server instance that hosts the shares.

**Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2012 R2 and Windows 8.1.

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (0)


</dt> <dd></dd> <dt>

<span id="CSV"></span><span id="csv"></span>

<span id="CSV"></span><span id="csv"></span>**CSV** (1)


</dt> <dd>

Represents a Cluster Shared Volume (CSV).

**Windows 10 and Windows 8.1:** Cluster Shared Volumes are only supported on Windows Server systems.

</dd> <dt>

<span id="SBL"></span><span id="sbl"></span>

<span id="SBL"></span><span id="sbl"></span>**SBL** (2)


</dt> <dd>

Represents a Software Storage Bus used in Storage Spaces Direct.

**Windows Server 2012 R2 and Windows 8.1:** This value is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

<span id="SR"></span><span id="sr"></span>

<span id="SR"></span><span id="sr"></span>**SR** (3)


</dt> <dd>

Represents a Storage Replica (SR).

**Windows Server 2012 R2:** This value is not supported before Windows Server 2016.

**Windows 10 and Windows 8.1:** Storage Replica is only supported on Windows Server systems.

</dd> </dl>

</dd> <dt>

**Special**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this is a special share.

</dd> <dt>

**Temporary**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this is a temporary share.

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the volume that hosts the directory specified by **Path**. This name can be a volume mount point. For more information, see [Naming a Volume](https://msdn.microsoft.com/library/windows/desktop/aa365248).

**NullShareType** is not **File System Directory**.

</dd> </dl>

## Remarks

There will be one instance of this class per existing share on the system.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





