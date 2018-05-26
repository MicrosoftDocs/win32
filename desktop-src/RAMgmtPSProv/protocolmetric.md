---
title: ProtocolMetric class
description: Manages protocol metrics.
audience: developer
ms.assetid: 4c43da97-ccf6-4e92-ad8b-a420af8f544f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ProtocolMetric class
- ProtocolMetric class, described
topic_type:
- apiref
api_name:
- ProtocolMetric
- ProtocolMetric.Name
- ProtocolMetric.Level
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProtocolMetric class

Manages protocol metrics

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class ProtocolMetric
{
  string Name;
  uint32 Level;
};
```

## Members

The **ProtocolMetric** class has these types of members:

-   [Properties](#properties)

### Properties

The **ProtocolMetric** class has these properties.

<dl> <dt>

**Level**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The preference level of the protocol

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the protocol

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

 

 





