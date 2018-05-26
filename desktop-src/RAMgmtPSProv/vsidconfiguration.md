---
title: VSIDConfiguration class
description: The configuration of a Virtual Subnet ID (VSID).
audience: developer
ms.assetid: 2d18b9a3-c713-413a-a3e6-79bf88598c22
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VSIDConfiguration class
- VSIDConfiguration class, described
topic_type:
- apiref
api_name:
- VSIDConfiguration
- VSIDConfiguration.VSID
- VSIDConfiguration.RDID
- VSIDConfiguration.MTNICName
- VSIDConfiguration.Ipv4TransportInfo
- VSIDConfiguration.Ipv6TransportInfo
- VSIDConfiguration.LUID
- VSIDConfiguration.InterfaceName
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VSIDConfiguration class

The configuration of a Virtual Subnet ID (VSID).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VSIDConfiguration
{
  uint32 VSID;
  string RDID;
  string MTNICName;
  uint8  Ipv4TransportInfo[];
  uint8  Ipv6TransportInfo[];
  uint64 LUID;
  string InterfaceName;
};
```

## Members

The **VSIDConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **VSIDConfiguration** class has these properties.

<dl> <dt>

**InterfaceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the VSID interface

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**Ipv4TransportInfo**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv4 transport info of the VSID

</dd> <dt>

**Ipv6TransportInfo**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv6 transport info of the VSID

</dd> <dt>

**LUID**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The LUID of the VSID

</dd> <dt>

**MTNICName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The locally unique identifier (LUID) of a multi-tenant network interface controller (NIC)

</dd> <dt>

**RDID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The ID of the routing domain

</dd> <dt>

**VSID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The ID of the VSID.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





