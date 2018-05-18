---
title: Msft\_MiQuery class
description: The Msft\_MiQuery WMI class represents a data stream that encapsulates a query request from a Software Inventory Logging data provider, and exposes the query data in the stream.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd9c2d891-4de9-48cd-a947-d2f235711247'
ms.prod: 'windows-server-dev'
ms.technology:
- 'software-inventory-logging'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msft_MiQuery class Software Inventory Logging", "Msft_MiQuery class Software Inventory Logging , described"]
topic_type:
- apiref
api_name:
- Msft_MiQuery
- Msft_MiQuery.NamespaceName
- Msft_MiQuery.Dialect
- Msft_MiQuery.Expression
api_location:
- MiStreamProv.dll
api_type:
- DllExport
---

# Msft\_MiQuery class

The **Msft\_MiQuery** WMI class represents a data stream that encapsulates a query request from a Software Inventory Logging data provider, and exposes the query data in the stream.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), AMENDMENT]
class Msft_MiQuery : Msft_MiStream
{
  string NamespaceName;
  string Dialect;
  string Expression;
};
```

## Members

The **Msft\_MiQuery** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msft\_MiQuery** class has these properties.

<dl> <dt>

**Dialect**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the query language in the request.

</dd> <dt>

**Expression**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the query expression in the request.

</dd> <dt>

**NamespaceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the namespace of the data provider.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                           |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                           |
| MOF<br/>                      | <dl> <dt>MiStreamProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MiStreamProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msft\_MiStream**](msft-mistream.md)
</dt> <dt>

[Software Inventory Logging WMI Stream Provider Classes](software-inventory-logging-wmi-stream-provider-classes.md)
</dt> </dl>

 

 





