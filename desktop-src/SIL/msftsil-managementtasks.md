---
title: MsftSil\_ManagementTasks class
description: The MsftSil\_ManagementTasks WMI class retrieves and configures settings for Software Inventory Logging.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a66c4ca8-0e8d-40b9-b626-f546ef7e11d9
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MsftSil_ManagementTasks class Software Inventory Logging
- MsftSil_ManagementTasks class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- MsftSil_ManagementTasks
api_location:
- SILProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MsftSil\_ManagementTasks class

The **MsftSil\_ManagementTasks** WMI class retrieves and configures settings for Software Inventory Logging.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("silprovider"), AMENDMENT]
class MsftSil_ManagementTasks
{
};
```

## Members

The **MsftSil\_ManagementTasks** class has these types of members:

-   [Methods](#methods)

### Methods

The **MsftSil\_ManagementTasks** class has these methods.



| Method                                                             | Description                                                                                                                        |
|:-------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**GetLoggingState**](getloggingstate-msftsil-managementtasks.md) | Verifies whether Software Inventory Logging is enabled, and optionally enables or disables the feature.<br/>                 |
| [**GetLoggingTime**](getloggingtime-msftsil-managementtasks.md)   | Gets the start time in which the Software Inventory Logging engine collects data.<br/>                                       |
| [**GetTargetUri**](gettargeturi-msftsil-managementtasks.md)       | Retrieves and optionally specifies the resource to which the Software Inventory Logging stream provider publishes data.<br/> |
| [**SetLoggingState**](setloggingstate-msftsil-managementtasks.md) | Enables or disables Software Inventory Logging.<br/>                                                                         |
| [**SetLoggingTime**](setloggingtime-msftsil-managementtasks.md)   | Configures the start time in which the Software Inventory Logging engine collects data.<br/>                                 |
| [**SetTargetUri**](settargeturi-msftsil-managementtasks.md)       | Specifies the resource to which the Software Inventory Logging stream provider publishes data.<br/>                          |



 

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                          |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                          |
| MOF<br/>                      | <dl> <dt>SILProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SILProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[Software Inventory Logging WMI Data Provider Classes](software-inventory-logging-wmi-data-provider-classes.md)
</dt> </dl>

 

 





