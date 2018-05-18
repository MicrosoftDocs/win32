---
title: DAMultiSite class
description: DirectAccess Multi Site Settings class.
audience: developer
ms.assetid: 'edc68ab3-ca0a-4829-9192-5b32cb6fb123'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DAMultiSite class", "DAMultiSite class, described"]
topic_type:
- apiref
api_name:
- DAMultiSite
- DAMultiSite.EnterpriseName
- DAMultiSite.GslbFqdn
- DAMultiSite.ManualEntryPointSelectionAllowed
- DAMultiSite.DAEntryPoints
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# DAMultiSite class

DirectAccess Multi Site Settings class

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAMultiSite
{
  string           EnterpriseName;
  string           GslbFqdn;
  string           ManualEntryPointSelectionAllowed;
  DAEntryPointBase DAEntryPoints[];
};
```

## Members

The **DAMultiSite** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAMultiSite** class has these properties.

<dl> <dt>

**DAEntryPoints**
</dt> <dd> <dl> <dt>

Data type: **DAEntryPointBase** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAEntryPointBase**](daentrypointbase.md)")
</dt> </dl>

An array of [**DAEntryPointBase**](daentrypointbase.md) embedded instances

</dd> <dt>

**EnterpriseName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Multisite deployment name

</dd> <dt>

**GslbFqdn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Global load balancing FQDN.

</dd> <dt>

**ManualEntryPointSelectionAllowed**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Manual selection of entry point enabled

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





