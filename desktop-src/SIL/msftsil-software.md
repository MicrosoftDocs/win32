---
title: MsftSil\_Software class
description: The MsftSil\_Software WMI class retrieves installation data about the software installed on a server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a3450def-b3ef-462e-a85b-4e0bb936539b
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MsftSil_Software class Software Inventory Logging
- MsftSil_Software class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- MsftSil_Software
- MsftSil_Software.ID
- MsftSil_Software.InstallDate
- MsftSil_Software.Name
- MsftSil_Software.Publisher
- MsftSil_Software.Version
api_location:
- SILProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsftSil\_Software class

The **MsftSil\_Software** WMI class retrieves installation data about the software installed on a server.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("silprovider"), AMENDMENT]
class MsftSil_Software : MsftSil_Data
{
  string   ID;
  datetime InstallDate;
  string   Name;
  string   Publisher;
  string   Version;
};
```

## Members

The **MsftSil\_Software** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftSil\_Software** class has these properties.

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

Gets the date and time that the software was installed.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the product name of the software.

</dd> <dt>

**Publisher**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the organization that published the software.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the revision identifier of the software release.

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

 

 





