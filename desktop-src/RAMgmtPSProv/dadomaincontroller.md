---
title: DADomainController class
description: DirectAccess Domain Controller Settings class.
audience: developer
ms.assetid: '293e5045-f9fd-44f5-85ff-235f1324c238'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DADomainController class", "DADomainController class, described"]
topic_type:
- apiref
api_name:
- DADomainController
- DADomainController.EntryPointName
- DADomainController.DomainControllerName
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# DADomainController class

DirectAccess Domain Controller Settings class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DADomainController
{
  string EntryPointName;
  string DomainControllerName;
};
```

## Members

The **DADomainController** class has these types of members:

-   [Properties](#properties)

### Properties

The **DADomainController** class has these properties.

<dl> <dt>

**DomainControllerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Domain controller name.

</dd> <dt>

**EntryPointName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Entry point name.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





