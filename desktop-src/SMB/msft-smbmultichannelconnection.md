---
title: MSFT\_SmbMultichannelConnection class
description: Represents an SMB connection network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 07B58209-B8EF-45C0-8C66-4695F5C35C58
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbMultichannelConnection class SMB
- MSFT_SmbMultichannelConnection class SMB , described
topic_type:
- apiref
api_name:
- MSFT_SmbMultichannelConnection
- MSFT_SmbMultichannelConnection.ServerName
- MSFT_SmbMultichannelConnection.ClientInterfaceIndex
- MSFT_SmbMultichannelConnection.ServerInterfaceIndex
- MSFT_SmbMultichannelConnection.ServerIpAddress
- MSFT_SmbMultichannelConnection.ClientIpAddress
- MSFT_SmbMultichannelConnection.ClientInterfaceFriendlyName
- MSFT_SmbMultichannelConnection.Selected
- MSFT_SmbMultichannelConnection.ClientRSSCapable
- MSFT_SmbMultichannelConnection.ServerRSSCapable
- MSFT_SmbMultichannelConnection.ClientRdmaCapable
- MSFT_SmbMultichannelConnection.ServerRdmaCapable
- MSFT_SmbMultichannelConnection.ClientLinkSpeed
- MSFT_SmbMultichannelConnection.ServerLinkSpeed
- MSFT_SmbMultichannelConnection.MaxChannels
- MSFT_SmbMultichannelConnection.CurrentChannels
- MSFT_SmbMultichannelConnection.Failed
- MSFT_SmbMultichannelConnection.FailureCount
- MSFT_SmbMultichannelConnection.SmbInstance
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SmbMultichannelConnection class

Represents an SMB connection network interface.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("7")]
class MSFT_SmbMultichannelConnection
{
  string  ServerName;
  uint32  ClientInterfaceIndex;
  uint32  ServerInterfaceIndex;
  string  ServerIpAddress;
  string  ClientIpAddress;
  string  ClientInterfaceFriendlyName;
  boolean Selected;
  boolean ClientRSSCapable;
  boolean ServerRSSCapable;
  boolean ClientRdmaCapable;
  boolean ServerRdmaCapable;
  uint64  ClientLinkSpeed;
  uint64  ServerLinkSpeed;
  uint32  MaxChannels;
  uint32  CurrentChannels;
  boolean Failed;
  uint32  FailureCount;
  uint32  SmbInstance;
};
```

## Members

The **MSFT\_SmbMultichannelConnection** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SmbMultichannelConnection** class has these methods.



| Method                                                    | Description                                               |
|:----------------------------------------------------------|:----------------------------------------------------------|
| [**Refresh**](msft-smbmultichannelconnection-refresh.md) | Refreshes an SMB connection network interface.<br/> |



 

### Properties

The **MSFT\_SmbMultichannelConnection** class has these properties.

<dl> <dt>

**ClientInterfaceFriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly name for the client network interface.

</dd> <dt>

**ClientInterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Index value that uniquely identifies the client network interface.

</dd> <dt>

**ClientIpAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The client IP address.

</dd> <dt>

**ClientLinkSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Speed of the client network interface.

</dd> <dt>

**ClientRdmaCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the client network interface is RDMA capable.

</dd> <dt>

**ClientRSSCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the client network interface is RSS capable.

</dd> <dt>

**CurrentChannels**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of Multichannel connections that are currently established for this network interface pair. This could be different than **MaxChannels** when the connections are being set up or if there were errors.

</dd> <dt>

**Failed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether establishing a connection between this client network interface and server network interface have failed.

</dd> <dt>

**FailureCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the connection has failed between this client network interface and server network interface.

</dd> <dt>

**MaxChannels**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of Multichannel connections desired for this network interface pair. This could be different from **CurrentChannels** when the connections are being set up or if there were errors.

</dd> <dt>

**Selected**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if this specific network interface pair is being used by Multichannel.

</dd> <dt>

**ServerInterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Index value that uniquely identifies the server network interface.

</dd> <dt>

**ServerIpAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The server IP address.

</dd> <dt>

**ServerLinkSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Speed of the server network interface.

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the server.

</dd> <dt>

**ServerRdmaCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the server network interface is RDMA capable.

</dd> <dt>

**ServerRSSCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the server network interface is RSS capable.

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

**Windows Server 2012 R2 and Windows 8.1:** This value is not supported before Windows Server 2016 and Windows 10.

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



 

 





