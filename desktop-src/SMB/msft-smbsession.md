---
title: MSFT\_SmbSession class
description: Represents a session on an SMB server from the server's perspective.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e7a7fa39-0558-4d41-9097-9f13bf0f0a18'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SmbSession class SMB", "MSFT_SmbSession class SMB , described"]
topic_type:
- apiref
api_name:
- MSFT_SmbSession
- MSFT_SmbSession.SessionId
- MSFT_SmbSession.ScopeName
- MSFT_SmbSession.ClusterNodeName
- MSFT_SmbSession.ClientComputerName
- MSFT_SmbSession.ClientUserName
- MSFT_SmbSession.NumOpens
- MSFT_SmbSession.SecondsIdle
- MSFT_SmbSession.SecondsExists
- MSFT_SmbSession.Dialect
- MSFT_SmbSession.TransportName
- MSFT_SmbSession.SmbInstance
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
---

# MSFT\_SmbSession class

Represents a session on an SMB server from the server's perspective.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("30")]
class MSFT_SmbSession
{
  uint64 SessionId;
  string ScopeName;
  string ClusterNodeName;
  string ClientComputerName;
  string ClientUserName;
  uint64 NumOpens;
  uint32 SecondsIdle;
  uint32 SecondsExists;
  string Dialect;
  string TransportName;
  uint32 SmbInstance;
};
```

## Members

The **MSFT\_SmbSession** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbSession** class has these methods.



| Method                                           | Description                                                                         |
|:-------------------------------------------------|:------------------------------------------------------------------------------------|
| [**ForceClose**](forceclose-msft-smbsession.md) | Closes all handles opened by the session. Any unsaved data will be lost.<br/> |



 

### Properties

The **MSFT\_SmbSession** class has these properties.

<dl> <dt>

**ClientComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the client computer from which the session was established.

</dd> <dt>

**ClientUserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the user that established the session.

</dd> <dt>

**ClusterNodeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer that is actually serving this session. This is meaningful when the server is part of a cluster and the scope of the session might be served by several servers in the cluster.

</dd> <dt>

**Dialect**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SMB protocol dialect of this session. Depends on the versions of SMB Client and server.

</dd> <dt>

**NumOpens**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of file opens that are currently active in the session.

</dd> <dt>

**ScopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scope name of this session. It can be \* (meaning no scope) or a file server resource name (if the server is part of a cluster).

</dd> <dt>

**SecondsExists**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of seconds that have elapsed since the session was created.

</dd> <dt>

**SecondsIdle**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of seconds since the last request was received in the session.

</dd> <dt>

**SessionId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

ID that uniquely identifies the session.

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

**Windows Server 2012 R2:** This value is not supported before Windows Server 2016.

**Windows 10 and Windows 8.1:** Storage Spaces Direct is only supported on Windows Server systems.

</dd> <dt>

<span id="SR"></span><span id="sr"></span>

<span id="SR"></span><span id="sr"></span>**SR** (2)


</dt> <dd>

Represents a Storage Replica (SR).

**Windows Server 2012 R2:** This value is not supported before Windows Server 2016.

**Windows 10 and Windows 8.1:** Storage Replica is only supported on Windows Server systems.

</dd> </dl>

</dd> <dt>

**TransportName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the transport that is being used for the session.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





