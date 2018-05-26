---
title: MSFT\_FileServer class
description: Models the Windows operating systems concept of a file server.
ms.assetid: 1AF4536E-8B51-46A5-856F-9BE2482312F6
keywords:
- MSFT_FileServer class Windows Storage Management API
- MSFT_FileServer class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_FileServer
- MSFT_FileServer.FriendlyName
- MSFT_FileServer.HostNames
- MSFT_FileServer.HealthStatus
- MSFT_FileServer.OperationalStatus
- MSFT_FileServer.OtherOperationalStatusDescription
- MSFT_FileServer.SupportsFileShareCreation
- MSFT_FileServer.SupportsContinuouslyAvailableFileShare
- MSFT_FileServer.FileSharingProtocols
- MSFT_FileServer.FileSharingProtocolVersions
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_FileServer class

Models the Windows operating system's concept of a file server.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_FileServer : MSFT_StorageObject
{
  String  FriendlyName;
  String  HostNames[];
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OtherOperationalStatusDescription;
  Boolean SupportsFileShareCreation;
  Boolean SupportsContinuouslyAvailableFileShare;
  UInt16  FileSharingProtocols[];
  String  FileSharingProtocolVersions[];
};
```

## Members

The **MSFT\_FileServer** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FileServer** class has these methods.



| Method                                                     | Description                                         |
|:-----------------------------------------------------------|:----------------------------------------------------|
| [**CreateFileShare**](msft-fileserver-createfileshare.md) | Creates a file share on the file server.<br/> |
| [**DeleteObject**](msft-fileserver-deleteobject.md)       | Deletes the file server.<br/>                 |
| [**SetFriendlyName**](msft-fileserver-setproperties.md)   | Allows the file server to be renamed.<br/>    |



 

### Properties

The **MSFT\_FileServer** class has these properties.

<dl> <dt>

**FileSharingProtocols**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file sharing protocols supported by the file server.

<dl> <dt>

<span id="NFS"></span><span id="nfs"></span>**NFS** (2)
</dt> <dt>

<span id="SMB"></span><span id="smb"></span>**SMB** (3)
</dt> </dl>

</dd> <dt>

**FileSharingProtocolVersions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the file sharing protocol versions supported.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly string representing the name of the file server. Some servers may assign a default friendly name which cannot be modified by the user.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Denotes the current health status of the file server.

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

**HostNames**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Host names are semi-unique (scoped to the owning storage subsystem), human-readable strings used to identify a file server. There is a separate host name element per file sharing protocol.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

An array of values that denote the current operational status of the file server. Unlike *HealthStatus*, this field indicates the status of hardware, software, and infrastructure issues related to this server, and can contain multiple values.

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

**OtherOperationalStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the vendor-defined operational status. This field should only be set if the *OperationalStatus* array contains 1 ("Other").

</dd> <dt>

**SupportsContinuouslyAvailableFileShare**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the file server will support continuously available file shares.

</dd> <dt>

**SupportsFileShareCreation**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the server supports file share creation.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





