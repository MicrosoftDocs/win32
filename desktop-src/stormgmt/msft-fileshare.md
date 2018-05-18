---
title: MSFT\_FileShare class
description: Models the Windows operating system's concept of a file share.
ms.assetid: '064B4DA4-5879-4758-A7D1-683DB77F909D'
keywords: ["MSFT_FileShare class Windows Storage Management API", "MSFT_FileShare class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_FileShare
- MSFT_FileShare.Name
- MSFT_FileShare.Description
- MSFT_FileShare.VolumeRelativePath
- MSFT_FileShare.ContinuouslyAvailable
- MSFT_FileShare.EncryptData
- MSFT_FileShare.FileSharingProtocol
- MSFT_FileShare.ShareState
- MSFT_FileShare.HealthStatus
- MSFT_FileShare.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_FileShare class

Models the Windows operating system's concept of a file share.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_FileShare : MSFT_StorageObject
{
  String  Name;
  String  Description;
  String  VolumeRelativePath;
  Boolean ContinuouslyAvailable;
  Boolean EncryptData;
  UInt16  FileSharingProtocol;
  UInt16  ShareState;
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
};
```

## Members

The **MSFT\_FileShare** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FileShare** class has these methods.



| Method                                                             | Description                                                                              |
|:-------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**BlockAccess**](msft-fileshare-blockaccess.md)                  | Denies specified users access to the file share.<br/>                              |
| [**DeleteObject**](msft-fileshare-deleteobject.md)                | Deletes the file share.<br/>                                                       |
| [**Diagnose**](msft-fileshare-diagnose.md)                        | Performs a diagnostic on the file share, returning any actionable results.<br/>    |
| [**GetAccessControlEntries**](msft-fileshare-getaccesscontrol.md) | Gets the access control entries for specified accounts.<br/>                       |
| [**GrantAccess**](msft-fileshare-grantaccess.md)                  | Grants to the specified user accounts the specified access to the file share.<br/> |
| [**RevokeAccess**](msft-fileshare-revokeaccess.md)                | Revokes access to the file share for specified users.<br/>                         |
| [**SetAttributes**](msft-fileshare-setattributes.md)              | Allows the user to update or set various attributes on the file share.<br/>        |
| [**SetDescription**](msft-fileshare-setdescription.md)            | Allows a user to set the description field of the file share.<br/>                 |
| [**UnblockAccess**](msft-fileshare-unblockaccess.md)              | Removes specified users from the denied access list for the file share.<br/>       |



 

### Properties

The **MSFT\_FileShare** class has these properties.

<dl> <dt>

**ContinuouslyAvailable**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the share is continuously available.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user settable description of the file share. This field can be used to store extra free-form information, such as notes or details about the intended usage. Some shares do not allow setting a description and will either support a default description or will not support any description.

</dd> <dt>

**EncryptData**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the share data is encrypted during transport.

</dd> <dt>

**FileSharingProtocol**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file sharing protocol used by the share.

<dl> <dt>

<span id="NFS"></span><span id="nfs"></span>**NFS** (2)
</dt> <dt>

<span id="CIFS_SMB_"></span><span id="cifs_smb_"></span>**CIFS(SMB)** (3)
</dt> </dl>

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health status of the file share.

<dl> <dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (0)
</dt> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (1)
</dt> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>**Unhealthy** (2)
</dt> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (5)
</dt> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A semi-unique (scoped to the owning file server), human-readable string used to identify and access a file share.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of values that denote the current operational status of the file share. Unlike *HealthStatus*, this field indicates the status of hardware, software, and infrastructure issues related to this share, and can contain multiple values.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="OK"></span><span id="ok"></span>**OK** (2)
</dt> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)
</dt> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)
</dt> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)
</dt> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)
</dt> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)
</dt> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)
</dt> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)
</dt> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)
</dt> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)
</dt> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)
</dt> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)
</dt> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)
</dt> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)
</dt> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)
</dt> <dt>

<span id="Power_Mode_"></span><span id="power_mode_"></span><span id="POWER_MODE_"></span>**Power Mode** (18 )
</dt> <dt>

<span id="Relocating"></span><span id="relocating"></span><span id="RELOCATING"></span>**Relocating** (19 )
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
</dt> <dt>

<span id="Read-only"></span><span id="read-only"></span><span id="READ-ONLY"></span>**Read-only** (0xD000)
</dt> <dt>

<span id="Incomplete"></span><span id="incomplete"></span><span id="INCOMPLETE"></span>**Incomplete** (0xD001)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (0xD001..)
</dt> </dl>

</dd> <dt>

**ShareState**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of the file share.

<dl> <dt>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>**Pending** (0)
</dt> <dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>**Online** (1)
</dt> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (2)
</dt> </dl>

</dd> <dt>

**VolumeRelativePath**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The volume relative path to the directory that is being shared.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





