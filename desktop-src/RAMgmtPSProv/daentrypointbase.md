---
title: DAEntryPointBase class
description: DirectAccess Entry Point Base Settings object.
audience: developer
ms.assetid: 688cc48d-37e9-4b0e-b145-db42d2bbfcca
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAEntryPointBase class
- DAEntryPointBase class, described
topic_type:
- apiref
api_name:
- DAEntryPointBase
- DAEntryPointBase.EntryPointName
- DAEntryPointBase.Servers
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DAEntryPointBase class

DirectAccess Entry Point Base Settings object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAEntryPointBase
{
  string EntryPointName;
  string Servers[];
};
```

## Members

The **DAEntryPointBase** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAEntryPointBase** class has these properties.

<dl> <dt>

**EntryPointName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The entry point name

</dd> <dt>

**Servers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The names of the servers

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





