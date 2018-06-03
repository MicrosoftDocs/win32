---
title: ProtocolPreference class
description: Routing protocol preference.
audience: developer
ms.assetid: 4ea2ea36-ef27-4c51-846b-16c728f738e9
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ProtocolPreference class
- ProtocolPreference class, described
topic_type:
- apiref
api_name:
- ProtocolPreference
- ProtocolPreference.ProtocolMetric
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProtocolPreference class

Routing protocol preference

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class ProtocolPreference
{
  ProtocolMetric ProtocolMetric[];
};
```

## Members

The **ProtocolPreference** class has these types of members:

-   [Properties](#properties)

### Properties

The **ProtocolPreference** class has these properties.

<dl> <dt>

**ProtocolMetric**
</dt> <dd> <dl> <dt>

Data type: **ProtocolMetric** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**ProtocolMetric**](protocolmetric.md)")
</dt> </dl>

An array of [**ProtocolMetric**](protocolmetric.md) embedded instances

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

 

 





