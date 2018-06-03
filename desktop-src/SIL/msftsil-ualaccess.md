---
title: MsftSil\_UalAccess class
description: The MsftSil\_UalAccess WMI class aggregates User Access Logging (UAL) data from a server, and then returns information about the number of unique users and devices that accessed a software product.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ca4e35b7-bcce-4217-83cb-5c5bd4955c6e
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MsftSil_UalAccess class Software Inventory Logging
- MsftSil_UalAccess class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- MsftSil_UalAccess
- MsftSil_UalAccess.ProductName
- MsftSil_UalAccess.RoleGuid
- MsftSil_UalAccess.RoleName
- MsftSil_UalAccess.SampleDate
- MsftSil_UalAccess.UniqueDeviceAccessCount
- MsftSil_UalAccess.UniqueUserAccessCount
api_location:
- SILProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsftSil\_UalAccess class

The **MsftSil\_UalAccess** WMI class aggregates [User Access Logging](https://msdn.microsoft.com/library/hh437528) (UAL) data from a server, and then returns information about the number of unique users and devices that accessed a software product.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("silprovider"), AMENDMENT]
class MsftSil_UalAccess : MsftSil_Data
{
  string   ProductName;
  string   RoleGuid;
  string   RoleName;
  datetime SampleDate;
  uint32   UniqueDeviceAccessCount;
  uint32   UniqueUserAccessCount;
};
```

## Members

The **MsftSil\_UalAccess** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftSil\_UalAccess** class has these properties.

<dl> <dt>

**ProductName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the name of the software product.

</dd> <dt>

**RoleGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Retrieves the **GUID** that represents the role or minor product name associated with a UAL session.

</dd> <dt>

**RoleName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the name of the role of the software product.

</dd> <dt>

**SampleDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the date the user accessed the product.

</dd> <dt>

**UniqueDeviceAccessCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the number of unique devices that accessed the product role.

</dd> <dt>

**UniqueUserAccessCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the number of unique users that accessed the product role.

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

 

 





