---
title: Msft\_MiCommand class
description: The Msft\_MiCommand WMI class encapsulates a command request from a Software Inventory Logging data provider, and exposes the method data in the request.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3ba53532-f13d-4fd8-ad93-735a99cf047a
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msft_MiCommand class Software Inventory Logging
- Msft_MiCommand class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- Msft_MiCommand
- Msft_MiCommand.NamespaceName
- Msft_MiCommand.ClassName
- Msft_MiCommand.MethodName
- Msft_MiCommand.Input
- Msft_MiCommand.Parameters
api_location:
- MiStreamProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msft\_MiCommand class

The **Msft\_MiCommand** WMI class encapsulates a command request from a Software Inventory Logging data provider, and exposes the method data in the request.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), AMENDMENT]
class Msft_MiCommand : Msft_MiStream
{
  string NamespaceName;
  string ClassName;
  string MethodName;
  object Input;
  object Parameters;
};
```

## Members

The **Msft\_MiCommand** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msft\_MiCommand** class has these properties.

<dl> <dt>

**ClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the class of method in the command request.

</dd> <dt>

**Input**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **EmbeddedObject**
</dt> </dl>

Gets the arguments for the method in the command request.

</dd> <dt>

**MethodName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the method in the command request.

</dd> <dt>

**NamespaceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

The namespace of the data provider.

</dd> <dt>

**Parameters**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **EmbeddedObject**
</dt> </dl>

Gets the parameters for the method in the command request.

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

 

 





