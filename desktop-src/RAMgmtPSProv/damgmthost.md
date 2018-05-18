---
title: DAMgmtHost class
description: Host information.
audience: developer
ms.assetid: '45e02a53-66b2-4512-ab95-fb54065af1de'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DAMgmtHost class", "DAMgmtHost class, described"]
topic_type:
- apiref
api_name:
- DAMgmtHost
- DAMgmtHost.Host
- DAMgmtHost.IPAddresses
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# DAMgmtHost class

Host information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAMgmtHost
{
  string Host;
  string IPAddresses[];
};
```

## Members

The **DAMgmtHost** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAMgmtHost** class has these properties.

<dl> <dt>

**Host**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name or IP address

</dd> <dt>

**IPAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP Addresses

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





