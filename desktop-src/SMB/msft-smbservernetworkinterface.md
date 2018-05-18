---
title: MSFT\_SmbServerNetworkInterface class
description: Represents an SMB server network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c0a56b52-c9ec-4fe0-8c3f-81d6d67e6afb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SmbServerNetworkInterface class SMB", "MSFT_SmbServerNetworkInterface class SMB , described"]
topic_type:
- apiref
api_name:
- MSFT_SmbServerNetworkInterface
- MSFT_SmbServerNetworkInterface.InterfaceIndex
- MSFT_SmbServerNetworkInterface.ScopeName
- MSFT_SmbServerNetworkInterface.IpAddress
- MSFT_SmbServerNetworkInterface.FriendlyName
- MSFT_SmbServerNetworkInterface.LinkSpeed
- MSFT_SmbServerNetworkInterface.RdmaCapable
- MSFT_SmbServerNetworkInterface.RssCapable
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
---

# MSFT\_SmbServerNetworkInterface class

Represents an SMB server network interface.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("7")]
class MSFT_SmbServerNetworkInterface
{
  uint32  InterfaceIndex;
  string  ScopeName;
  string  IpAddress;
  string  FriendlyName;
  uint64  LinkSpeed;
  boolean RdmaCapable;
  boolean RssCapable;
};
```

## Members

The **MSFT\_SmbServerNetworkInterface** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SmbServerNetworkInterface** class has these properties.

<dl> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Friendly name of the network interface.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Index value that uniquely identifies the server network interface.

</dd> <dt>

**IpAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The server's IP address.

</dd> <dt>

**LinkSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Speed of the network interface.

</dd> <dt>

**RdmaCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the network interface is RDMA capable.

</dd> <dt>

**RssCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the network interface is RSS capable.

</dd> <dt>

**ScopeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Scope name of this interface. It can be \* (meaning no scope) or a file server resource name (if the server is part of a cluster).

</dd> </dl>

## Remarks

Server network interfaces are network interfaces used by the SMB Server, including the details used by SMB2 Multichannel.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





