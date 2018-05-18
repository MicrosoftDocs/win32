---
title: Msft\_MiPipeline class
description: The Msft\_MiPipeline WMI class represents a pipeline that transports data streams throughout the Software Inventory Logging stream provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1474a69d-85d0-48f6-ba1a-6febb82da2a8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'software-inventory-logging'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msft_MiPipeline class Software Inventory Logging", "Msft_MiPipeline class Software Inventory Logging , described"]
topic_type:
- apiref
api_name:
- Msft_MiPipeline
- Msft_MiPipeline.NamespaceName
- Msft_MiPipeline.Streams
api_location:
- MiStreamProv.dll
api_type:
- DllExport
---

# Msft\_MiPipeline class

The **Msft\_MiPipeline** WMI class represents a pipeline that transports data streams throughout the Software Inventory Logging stream provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Msft_MiPipeline : Msft_MiStream
{
  string        NamespaceName;
  Msft_MiStream Streams[];
};
```

## Members

The **Msft\_MiPipeline** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msft\_MiPipeline** class has these properties.

<dl> <dt>

**NamespaceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The namespace of the data provider.

This property is inherited from [**Msft\_MiStream**](msft-mistream.md).

</dd> <dt>

**Streams**
</dt> <dd> <dl> <dt>

Data type: **Msft\_MiStream** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

On success, returns a list of embedded [**Msft\_MiStream**](msft-mistream.md) instances containing the data streams.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                           |
| End of client support<br/>    | None supported<br/>                                                                   |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                           |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                           |
| MOF<br/>                      | <dl> <dt>MiStreamProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MiStreamProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msft\_MiStream**](https://msdn.microsoft.com/library/dn440656)
</dt> <dt>

[Software Inventory Logging WMI Stream Provider Classes](software-inventory-logging-wmi-stream-provider-classes.md)
</dt> </dl>

 

 





