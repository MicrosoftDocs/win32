---
title: DhcpServerVersion class
description: Returns the software version of the DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '918b2e2c-33eb-4a94-88d2-95f5a9918f67'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerVersion class", "DhcpServerVersion class, described"]
topic_type:
- apiref
api_name:
- DhcpServerVersion
- DhcpServerVersion.MajorVersion
- DhcpServerVersion.MinorVersion
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerVersion class

Returns the software version of the DHCP Server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerVersion
{
  uint32 MajorVersion;
  uint32 MinorVersion;
};
```

## Members

The **DhcpServerVersion** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerVersion** class has these properties.

<dl> <dt>

**MajorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Major Version of Dhcp server.

</dd> <dt>

**MinorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Minor Version of Dhcp server.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





