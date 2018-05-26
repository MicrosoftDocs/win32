---
title: Msft\_MiMerge class
description: The Msft\_MiMerge WMI class represents a merged data stream. A merged data stream contains a Msft\_MiQuery object and a Msft\_MiCommand object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 108e3516-d394-42ac-80be-b06e43c67c41
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msft_MiMerge class Software Inventory Logging
- Msft_MiMerge class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- Msft_MiMerge
- Msft_MiMerge.NamespaceName
- Msft_MiMerge.Streams
- Msft_MiMerge.Inputs
api_location:
- MiStreamProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msft\_MiMerge class

The **Msft\_MiMerge** WMI class represents a merged data stream. A merged data stream contains a [**Msft\_MiQuery**](msft-miquery.md) object and a [**Msft\_MiCommand**](msft-micommand.md) object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), AMENDMENT]
class Msft_MiMerge : Msft_MiStream
{
  string        NamespaceName;
  Msft_MiStream Streams[];
  Msft_MiStream Inputs[];
};
```

## Members

The **Msft\_MiMerge** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msft\_MiMerge** class has these properties.

<dl> <dt>

**Inputs**
</dt> <dd> <dl> <dt>

Data type: **Msft\_MiStream** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**Msft\_MiStream**](msft-mistream.md)")
</dt> </dl>

The list of streams to merge.

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> <dt>

**NamespaceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property has been removed.

**Windows Server 2012 R2:** The namespace of the data provider.

This property is inherited from [**Msft\_MiStream**](msft-mistream.md).

</dd> <dt>

**Streams**
</dt> <dd> <dl> <dt>

Data type: **Msft\_MiStream** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property has been removed.

**Windows Server 2012 R2:  **

The list of embedded [**Msft\_MiStream**](msft-mistream.md) instances containing the data streams.

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

[**Msft\_MiStream**](msft-mistream.md)
</dt> <dt>

[Software Inventory Logging WMI Stream Provider Classes](software-inventory-logging-wmi-stream-provider-classes.md)
</dt> </dl>

 

 





