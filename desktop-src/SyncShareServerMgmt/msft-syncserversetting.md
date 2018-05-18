---
Description: 'Retrieves and updates settings for Work Folders Sync Share server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'b6c4247e-9246-455a-af42-3f002d0c9567'
ms.prod: 'windows-server-dev'
ms.technology:
- 'work-folders'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Msft\_SyncServerSetting class'
---

# Msft\_SyncServerSetting class

Retrieves and updates settings for Work Folders Sync Share server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("SyncShareServerWmiProvider")]
class Msft_SyncServerSetting
{
  string  Server;
  string  Description;
  string  AdministratorEmail;
  string  ADFSUrl;
  string  SuspendedUser[];
  uint32  MinimumChangeDetectionMins;
  boolean SSLCertificateEnabled;
};
```

## Members

The **Msft\_SyncServerSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msft\_SyncServerSetting** class has these properties.

<dl> <dt>

**ADFSUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets the URL of the Active Directory Federation Services (ADFS) for authentication. If this property is empty then the default Windows authentication is used.

</dd> <dt>

**AdministratorEmail**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Semicolon-separated list of email addresses of the administrators of the Sync Share server. The Sync Share Server sends the email addressed to the client so the client can contact the administrator to report issues and to receive help troubleshooting the issues.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets the description of the server.

</dd> <dt>

**MinimumChangeDetectionMins**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the time, in minutes, before the Sync Share server detects changes on devices and syncs the client and server. The default value is 5. The minimum value that you can set is 1. The Sync Share server synchronizes with multiple devices for potentially many users. Increasing the frequency that Sync Share detects changes on devices and syncs the client and server results in fresher data on the devices of users. However, this increases the load on the Sync Share server and can affect the performance of the synchronization, particularly for users who make frequent changes to the files directly on the server and who have many devices.

</dd> <dt>

**Server**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the name of the server.

</dd> <dt>

**SSLCertificateEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a value that indicates whether SSL certificates are enabled on the server. **TRUE** if SSL certificates are enabled; otherwise **FALSE**. On a cluster, the value is returned for the current node where the query is executed.

</dd> <dt>

**SuspendedUser**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets or sets a user that is not permitted to synchronize on the server.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                           |
| Namespace<br/>                | Root\\Microsoft\\Windows\\SyncShareServer<br/>                                        |
| MOF<br/>                      | <dl> <dt>ECSServer.Mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>SyncShareSvc.dll</dt> </dl> |



## See also

<dl> <dt>

[Work Folders Management Classes](sync-share-server-management-classes.md)
</dt> </dl>

 

 




