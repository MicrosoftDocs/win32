---
title: MsftSil\_GuestData class
description: Deprecated. Exposes Software Inventory Logging data collected from a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8d7dba1b-8ae6-42c9-8239-41d569f663e4
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MsftSil_GuestData class Software Inventory Logging
- MsftSil_GuestData class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- MsftSil_GuestData
- MsftSil_GuestData.Item
- MsftSil_GuestData.VmGuid
api_location:
- SILProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsftSil\_GuestData class

This class has been deprecated starting with Windows Server 2016.

**Windows Server 2012 R2:** The **MsftSil\_GuestData** WMI class exposes Software Inventory Logging data collected from a virtual machine.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MsftSil_GuestData
{
  object Item;
  string VmGuid;
};
```

## Members

The **MsftSil\_GuestData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftSil\_GuestData** class has these properties.

<dl> <dt>

**Item**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the object that contains the Software Inventory Logging data.

</dd> <dt>

**VmGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the **GUID** of the virtual machine.

</dd> </dl>

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

 

 





