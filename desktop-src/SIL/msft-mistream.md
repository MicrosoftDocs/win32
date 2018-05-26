---
title: Msft\_MiStream class
description: The Msft\_MiStream WMI class is an abstract base class that represents a data stream of command or query data sent from a Software Inventory Logging data provider to the Software Inventory Logging stream provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d035843c-ee20-42fe-868e-659ca0403233
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msft_MiStream class Software Inventory Logging
- Msft_MiStream class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- Msft_MiStream
- Msft_MiStream.NamespaceName
api_location:
- MiStreamProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msft\_MiStream class

The **Msft\_MiStream** WMI class is an abstract base class that represents a data stream of command or query data sent from a Software Inventory Logging data provider to the Software Inventory Logging stream provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, ClassVersion("1.0.0"), AMENDMENT]
class Msft_MiStream
{
  string NamespaceName;
};
```

## Members

The **Msft\_MiStream** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msft\_MiStream** class has these properties.

<dl> <dt>

**NamespaceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows Server 2012 R2:** The namespace of the data provider.

This property has been removed.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                           |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                           |
| MOF<br/>                      | <dl> <dt>MiStreamProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MiStreamProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Software Inventory Logging WMI Stream Provider Classes](software-inventory-logging-wmi-stream-provider-classes.md)
</dt> </dl>

 

 





