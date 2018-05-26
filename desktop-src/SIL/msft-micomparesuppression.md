---
title: Msft\_MiCompareSuppression class
description: The Msft\_MiCompareSuppression WMI class represents the output instance produced when the input of the output stream is suppressed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1bd6be88-bcf9-4597-9f1f-6e7f8376bd19
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msft_MiCompareSuppression class Software Inventory Logging
- Msft_MiCompareSuppression class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- Msft_MiCompareSuppression
- Msft_MiCompareSuppression.Timestamp
- Msft_MiCompareSuppression.SuppressionSignal
api_location:
- MiStreamProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msft\_MiCompareSuppression class

The **Msft\_MiCompareSuppression** WMI class represents the output instance produced when the input of the output stream is suppressed.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), AMENDMENT]
class Msft_MiCompareSuppression
{
  datetime Timestamp;
  object   SuppressionSignal[];
};
```

## Members

The **Msft\_MiCompareSuppression** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msft\_MiCompareSuppression** class has these properties.

<dl> <dt>

**SuppressionSignal**
</dt> <dd> <dl> <dt>

Data type: **object** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **EmbeddedObject**
</dt> </dl>

Gets a list of embedded objects that signals an output suppression by the stream.

</dd> <dt>

**Timestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the timestamp indicating when the output was suppressed.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                           |
| MOF<br/>                      | <dl> <dt>MiStreamProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MiStreamProv.dll</dt> </dl> |



 

 





