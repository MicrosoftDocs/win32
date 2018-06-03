---
title: MsftSil\_GuestTasks class
description: This class has been removed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 250034b3-4a27-4161-ba0e-50b5420ea8a9
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MsftSil_GuestTasks class Software Inventory Logging
- MsftSil_GuestTasks class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- MsftSil_GuestTasks
api_location:
- SILProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsftSil\_GuestTasks class

This class has been removed.

**Windows Server 2012 R2:** The **MsftSil\_GuestTasks** WMI class retrieves Software Inventory Logging data from a virtual machine, and then returns it as a [**MsftSil\_GuestData**](msftsil-guestdata.md) object.

## Syntax

``` syntax
[Dynamic]
class MsftSil_GuestTasks
{
};
```

## Members

The **MsftSil\_GuestTasks** class has these types of members:

-   [Methods](#methods)

### Methods

The **MsftSil\_GuestTasks** class has these methods.



| Method                                                        | Description                                                                                                                   |
|:--------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**GetDataByFqdn**](getdatabyfqdn-msftsil-guesttasks.md)     | Retrieves Software Inventory Logging data from the virtual machine with the specified fully qualified domain name.<br/> |
| [**GetDataByVmGuid**](getdatabyvmguid-msftsil-guesttasks.md) | Retrieves Software Inventory Logging data from the virtual machine with the specified virtual machine **GUID**.<br/>    |



 

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                          |
| End of client support<br/>    | None supported<br/>                                                                  |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                          |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                          |
| MOF<br/>                      | <dl> <dt>SILProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SILProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[Software Inventory Logging WMI Data Provider Classes](software-inventory-logging-wmi-data-provider-classes.md)
</dt> </dl>

 

 





