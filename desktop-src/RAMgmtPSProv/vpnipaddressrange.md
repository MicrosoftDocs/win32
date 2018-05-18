---
title: VpnIPAddressRange class
description: Virtual Private Network (VPN) IP address range object.
audience: developer
ms.assetid: '4a6f4363-4b62-454b-90a2-c461ed3621fb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VpnIPAddressRange class", "VpnIPAddressRange class, described"]
topic_type:
- apiref
api_name:
- VpnIPAddressRange
- VpnIPAddressRange.StartIPAddress
- VpnIPAddressRange.EndIPAddress
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# VpnIPAddressRange class

Virtual Private Network (VPN) IP address range object

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnIPAddressRange
{
  string StartIPAddress;
  string EndIPAddress;
};
```

## Members

The **VpnIPAddressRange** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnIPAddressRange** class has these properties.

<dl> <dt>

**EndIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

End IP address of the Range

</dd> <dt>

**StartIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Start IP address of the Range

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





