---
title: DhcpServerv6Class class
description: Contains information about the DHCP server class, version 6.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7196092f-d8dc-4a17-9927-6911d3fbcbb9
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv6Class class
- DhcpServerv6Class class, described
topic_type:
- apiref
api_name:
- DhcpServerv6Class
- DhcpServerv6Class.Name
- DhcpServerv6Class.Type
- DhcpServerv6Class.Data
- DhcpServerv6Class.VendorId
- DhcpServerv6Class.Description
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerv6Class class

Contains information about the DHCP server class, version 6.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv6Class
{
  string Name;
  string Type;
  string Data;
  uint32 VendorId;
  string Description;
};
```

## Members

The **DhcpServerv6Class** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv6Class** class has these properties.

<dl> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DHCP server class data.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DHCP server class description.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the DHCP server class.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of the DHCP server class.

<dt>

<span id="Vendor"></span><span id="vendor"></span><span id="VENDOR"></span>

**Vendor** ("Vendor")


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** ("User")


</dt> <dd></dd> </dl>

</dd> <dt>

**VendorId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The enterprise number of the class vendor. If the DHCP server class type is "User", then this property is 0.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





