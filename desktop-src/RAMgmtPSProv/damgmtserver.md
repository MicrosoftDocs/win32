---
title: DAMgmtServer class
description: Management server class.
audience: developer
ms.assetid: 'f35e6054-c7f6-4914-adc1-a4e5f1b402e1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DAMgmtServer class", "DAMgmtServer class, described"]
topic_type:
- apiref
api_name:
- DAMgmtServer
- DAMgmtServer.Summary
- DAMgmtServer.Servers
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# DAMgmtServer class

Management server class

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAMgmtServer
{
  string            Summary;
  DAMgmtChangedHost Servers[];
};
```

## Members

The **DAMgmtServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAMgmtServer** class has these properties.

<dl> <dt>

**Servers**
</dt> <dd> <dl> <dt>

Data type: **DAMgmtChangedHost** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DAMgmtChangedHost**](damgmtchangedhost.md)")
</dt> </dl>

An array of [**DAMgmtChangedHost**](damgmtchangedhost.md) embedded instances

</dd> <dt>

**Summary**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Summary

The possible values are.

<dt>

<span id="NoChangeDetected"></span><span id="nochangedetected"></span><span id="NOCHANGEDETECTED"></span>

**NoChangeDetected** ("NoChangeDetected")


</dt> <dd></dd> <dt>

<span id="ChangesDetected"></span><span id="changesdetected"></span><span id="CHANGESDETECTED"></span>

**ChangesDetected** ("ChangesDetected")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





