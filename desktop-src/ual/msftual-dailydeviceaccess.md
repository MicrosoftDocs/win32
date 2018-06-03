---
title: MsftUal\_DailyDeviceAccess class
description: This is a class of property qualifiers that provides client device access data on a given day of the year, or range.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 611e9d43-1820-41b4-b3b6-2f73a15a5635
ms.prod: windows-server-dev
ms.technology: user-access-logging
ms.tgt_platform: multiple
keywords:
- MsftUal_DailyDeviceAccess class User Access Logging
- MsftUal_DailyDeviceAccess class User Access Logging , described
topic_type:
- apiref
api_name:
- MsftUal_DailyDeviceAccess
- MsftUal_DailyDeviceAccess.ProductName
- MsftUal_DailyDeviceAccess.RoleName
- MsftUal_DailyDeviceAccess.RoleGuid
- MsftUal_DailyDeviceAccess.IPAddress
- MsftUal_DailyDeviceAccess.AccessDate
- MsftUal_DailyDeviceAccess.AccessCount
api_location:
- UALProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsftUal\_DailyDeviceAccess class

This is a class of property qualifiers that provides client device access data on a given day of the year, or range.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1"), dynamic, provider("UAL")]
class MsftUal_DailyDeviceAccess
{
  string   ProductName;
  string   RoleName;
  string   RoleGuid;
  string   IPAddress;
  datetime AccessDate;
  uint32   AccessCount;
};
```

## Members

The **MsftUal\_DailyDeviceAccess** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftUal\_DailyDeviceAccess** class has these properties.

<dl> <dt>

**AccessCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of accesses of a role, or installed product, on the local server from a unique client device.

</dd> <dt>

**AccessDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date that a device accessed a role, or installed product, on the local server.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The IP address of a client device that accompanies the UAL payload from installed roles and products.

</dd> <dt>

**ProductName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the software parent product, or product line, that is providing User Access Logging data. This is also associated with a RoleName, and a RoleGuid.

</dd> <dt>

**RoleGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The UAL assigned, or registered, GUID representing the server role, or installed product. When a role or product reports its UAL data, this GUID accompanies the payload.

</dd> <dt>

**RoleName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the role, component, or sub-product that is providing User Access Logging data. This is also associated with a ProductName, and a RoleGuid.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\AccessLogging<br/>                                                         |
| MOF<br/>                      | <dl> <dt>Sum.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>UALProv.dll</dt> </dl> |



 

 





