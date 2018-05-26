---
title: MsftSil\_WindowsUpdate class
description: The MsftSil\_WindowsUpdate WMI class retrieves a list of the Quick Fix Engineering (QFE) updates installed on a server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b215c053-13e9-4aff-baf6-3e74303fd031
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MsftSil_WindowsUpdate class Software Inventory Logging
- MsftSil_WindowsUpdate class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- MsftSil_WindowsUpdate
- MsftSil_WindowsUpdate.ID
- MsftSil_WindowsUpdate.InstallDate
api_location:
- SILProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MsftSil\_WindowsUpdate class

The **MsftSil\_WindowsUpdate** WMI class retrieves a list of the Quick Fix Engineering (QFE) updates installed on a server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("silprovider"), AMENDMENT]
class MsftSil_WindowsUpdate : MsftSil_Data
{
  string   ID;
  datetime InstallDate;
};
```

## Members

The **MsftSil\_WindowsUpdate** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftSil\_WindowsUpdate** class has these properties.

<dl> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the software id, which is a unique identifier of the software.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the date and time that the update was installed.

</dd> </dl>

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

[**MsftSil\_Data**](msftsil-data.md)
</dt> <dt>

[Software Inventory Logging WMI Data Provider Classes](software-inventory-logging-wmi-data-provider-classes.md)
</dt> </dl>

 

 





