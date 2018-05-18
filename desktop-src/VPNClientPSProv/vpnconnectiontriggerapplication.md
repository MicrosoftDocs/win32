---
title: VpnConnectionTriggerApplication class
description: The VpnConnectionTriggerApplication class represents an application that auto-triggers a VPN connection.
audience: developer
ms.assetid: '47794659-6EC9-4375-A86F-BB385DCAD561'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VpnConnectionTriggerApplication class", "VpnConnectionTriggerApplication class, described"]
topic_type:
- apiref
api_name:
- VpnConnectionTriggerApplication
- VpnConnectionTriggerApplication.ConnectionName
- VpnConnectionTriggerApplication.ApplicationID
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
---

# VpnConnectionTriggerApplication class

The **VpnConnectionTriggerApplication** class represents an application that auto-triggers a VPN connection.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class VpnConnectionTriggerApplication
{
  string ConnectionName;
  string ApplicationID[];
};
```

## Members

The **VpnConnectionTriggerApplication** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnConnectionTriggerApplication** class has these properties.

<dl> <dt>

**ApplicationID**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The identifiers of the auto-trigger applications.

</dd> <dt>

**ConnectionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the current VPN connection profile.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





