---
title: DAEntryPoint class
description: DirectAccess Entry Point Settings class.
audience: developer
ms.assetid: 67390648-c647-4b9b-b4a4-1f45efb76897
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DAEntryPoint class
- DAEntryPoint class, described
topic_type:
- apiref
api_name:
- DAEntryPoint
- DAEntryPoint.EntryPointName
- DAEntryPoint.Servers
- DAEntryPoint.GslbIp
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DAEntryPoint class

DirectAccess Entry Point Settings class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAEntryPoint : DAEntryPointBase
{
  string EntryPointName;
  string Servers[];
  string GslbIp;
};
```

## Members

The **DAEntryPoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAEntryPoint** class has these properties.

<dl> <dt>

**EntryPointName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The entry point name

This property is inherited from [**DAEntryPointBase**](daentrypointbase.md).

</dd> <dt>

**GslbIp**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Global load balancing IP address

</dd> <dt>

**Servers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The names of the servers

This property is inherited from [**DAEntryPointBase**](daentrypointbase.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





