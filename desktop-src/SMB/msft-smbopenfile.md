---
title: MSFT\_SmbOpenFile class
description: Represents a file that is opened on an SMB server from the servers perspective.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cbdcb3ca-52a4-43d5-a445-19095b70587c
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbOpenFile class SMB
- MSFT_SmbOpenFile class SMB , described
topic_type:
- apiref
api_name:
- MSFT_SmbOpenFile
- MSFT_SmbOpenFile.FileId
- MSFT_SmbOpenFile.SmbInstance
- MSFT_SmbOpenFile.SessionId
- MSFT_SmbOpenFile.ScopeName
- MSFT_SmbOpenFile.ClusterNodeName
- MSFT_SmbOpenFile.Path
- MSFT_SmbOpenFile.ShareRelativePath
- MSFT_SmbOpenFile.ClientComputerName
- MSFT_SmbOpenFile.ClientUserName
- MSFT_SmbOpenFile.Permissions
- MSFT_SmbOpenFile.Locks
- MSFT_SmbOpenFile.ContinuouslyAvailable
- MSFT_SmbOpenFile.Encrypted
- MSFT_SmbOpenFile.Signed
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SmbOpenFile class

Represents a file that is opened on an SMB server from the server's perspective.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("30")]
class MSFT_SmbOpenFile
{
  uint64  FileId;
  uint32  SmbInstance;
  uint64  SessionId;
  string  ScopeName;
  string  ClusterNodeName;
  string  Path;
  string  ShareRelativePath;
  string  ClientComputerName;
  string  ClientUserName;
  uint32  Permissions;
  uint32  Locks;
  boolean ContinuouslyAvailable;
  boolean Encrypted;
  boolean Signed;
};
```

## Members

The **MSFT\_SmbOpenFile** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbOpenFile** class has these methods.



| Method                                            | Description                                                                                            |
|:--------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| [**ForceClose**](forceclose-msft-smbopenfile.md) | Forcibly closes a file that is open on behalf of an SMB client. Unsaved data might be lost.<br/> |



 

### Properties

The **MSFT\_SmbOpenFile** class has these properties.

<dl> <dt>

**ClientComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the computer from which the file handle was opened.

</dd> <dt>

**ClientUserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the user that opened the file handle.

</dd> <dt>

**ClusterNodeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer that is actually serving this handle. This is meaningful when the server is part of a cluster and the scope of the session might be served by several servers in the cluster.

</dd> <dt>

**ContinuouslyAvailable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this handle supports continuous availability. Continuously available handles will survive server failovers without any interruption to the client application.

</dd> <dt>

**Encrypted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the SMB connection is encrypted. For more information, see [SMB Encryption](https://technet.microsoft.com/library/dn551363.aspx#bkmk-smbencryption).

</dd> <dt>

**FileId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

An identifier that uniquely identifies the open file handle.

</dd> <dt>

**Locks**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of locks held on this handle.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specified the server-local path to the opened file.

</dd> <dt>

**Permissions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The access mask for this handle.

</dd> <dt>

**ScopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scope name of this handle. It can be \* (meaning no scope) or a file server resource name (if the server is part of a cluster). *ScopeName* should match the scope name of the associated session.

</dd> <dt>

**SessionId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An identifier that identifies the session in which this file handle was opened.

</dd> <dt>

**ShareRelativePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the share-relative path to the opened file.

</dd> <dt>

**Signed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the SMB connection is encrypted. If the SMB connection is encrypted (the **Encrypted** property is **True**) then the **Signed** property will be set to **False**, even though an encrypted connection is also signed. For more information, see [Require SMB Security Signatures](https://technet.microsoft.com/library/cc731957.aspx).

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

**SmbInstance**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifier of the SMB server instance that hosts the shares.

**Windows Server 2012 and Windows 8:** This property is not supported before Windows Server 2012 R2 and Windows 8.1.

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (0)


</dt> <dd></dd> <dt>

<span id="CSV"></span><span id="csv"></span>

<span id="CSV"></span><span id="csv"></span>**CSV** (1)


</dt> <dd>

Represents a Cluster Shared Volume (CSV).

**Windows 10 and Windows 8.1:** Cluster Shared Volumes are only supported on Windows Server systems.

</dd> <dt>

<span id="SBL"></span><span id="sbl"></span>

<span id="SBL"></span><span id="sbl"></span>**SBL** (2)


</dt> <dd>

Represents a Software Storage Bus used in Storage Spaces Direct.

**Windows Server 2012 R2:** This value is not supported before Windows Server 2016.

**Windows 10 and Windows 8.1:** Storage Spaces Direct is only supported on Windows Server systems.

</dd> <dt>

<span id="SR"></span><span id="sr"></span>

<span id="SR"></span><span id="sr"></span>**SR** (2)


</dt> <dd>

Represents a Storage Replica (SR).

**Windows Server 2012 R2:** This value is not supported before Windows Server 2016.

**Windows 10 and Windows 8.1:** Storage Replica is only supported on Windows Server systems.

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





