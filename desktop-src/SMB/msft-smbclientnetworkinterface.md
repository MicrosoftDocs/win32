---
title: MSFT\_SmbClientNetworkInterface class
description: Represents a network interface used by SMB client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 16854425-54c5-4d56-9f72-2e4672a9f580
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SmbClientNetworkInterface class SMB
- MSFT_SmbClientNetworkInterface class SMB , described
topic_type:
- apiref
api_name:
- MSFT_SmbClientNetworkInterface
- MSFT_SmbClientNetworkInterface.InterfaceIndex
- MSFT_SmbClientNetworkInterface.IpAddresses
- MSFT_SmbClientNetworkInterface.FriendlyName
- MSFT_SmbClientNetworkInterface.LinkSpeed
- MSFT_SmbClientNetworkInterface.RdmaCapable
- MSFT_SmbClientNetworkInterface.RssCapable
api_location:
- SmbWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SmbClientNetworkInterface class

Represents a network interface used by SMB client.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("smbwmiv2"), ClassVersion("7")]
class MSFT_SmbClientNetworkInterface
{
  uint32  InterfaceIndex;
  string  IpAddresses[];
  string  FriendlyName;
  uint64  LinkSpeed;
  boolean RdmaCapable;
  boolean RssCapable;
};
```

## Members

The **MSFT\_SmbClientNetworkInterface** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SmbClientNetworkInterface** class has these properties.

<dl> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Friendly name of this network interface.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Index of the network interface in the system.

</dd> <dt>

**IpAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP addresses associated with this network interface.

</dd> <dt>

**LinkSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Speed of the network interface, in bits per second.

</dd> <dt>

**RdmaCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this network interface is RDMA capable.

</dd> <dt>

**RssCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this network interface is RSS capable.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



 

 





