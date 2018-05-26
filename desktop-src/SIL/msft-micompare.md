---
title: Msft\_MiCompare class
description: The Msft\_MiCompare WMI class compares the current output of a stream identified by the given ID with the previous output of the input stream and, if identical, suppress the current output.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4996e07c-716a-4944-bd16-833e41b76f2d
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msft_MiCompare class Software Inventory Logging
- Msft_MiCompare class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- Msft_MiCompare
- Msft_MiCompare.OnlyUpdateSnapshot
- Msft_MiCompare.SuppressionHint
- Msft_MiCompare.Input
api_location:
- MiStreamProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msft\_MiCompare class

The **Msft\_MiCompare** WMI class compares the current output of a stream identified by the given ID with the previous output of the input stream and, if identical, suppress the current output.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), AMENDMENT]
class Msft_MiCompare : Msft_MiStream
{
  boolean                   OnlyUpdateSnapshot;
  Msft_MiCompareSuppression SuppressionHint;
  Msft_MiStream             Input;
};
```

## Members

The **Msft\_MiCompare** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msft\_MiCompare** class has these properties.

<dl> <dt>

**Input**
</dt> <dd> <dl> <dt>

Data type: **Msft\_MiStream**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**Msft\_MiStream**](msft-mistream.md)")
</dt> </dl>

A [**Msft\_MiStream**](msft-mistream.md) containing the input stream.

</dd> <dt>

**OnlyUpdateSnapshot**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** to only update the last known snapshot; **false** to also suppress the output based on that snapshot.

</dd> <dt>

**SuppressionHint**
</dt> <dd> <dl> <dt>

Data type: **Msft\_MiCompareSuppression**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**Msft\_MiCompareSuppression**](msft-micomparesuppression.md)")
</dt> </dl>

The [**Msft\_MiCompareSuppression**](msft-micomparesuppression.md) instance to produce if the output of the input stream was suppressed.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                           |
| MOF<br/>                      | <dl> <dt>MiStreamProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MiStreamProv.dll</dt> </dl> |



 

 





