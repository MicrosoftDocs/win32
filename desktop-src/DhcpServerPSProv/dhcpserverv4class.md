---
title: DhcpServerv4Class class
description: Contains information about the DHCP server class, version 4.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 26a0b4e4-9d1c-499d-b6e0-ffd7c282e69b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4Class class
- DhcpServerv4Class class, described
topic_type:
- apiref
api_name:
- DhcpServerv4Class
- DhcpServerv4Class.Name
- DhcpServerv4Class.Type
- DhcpServerv4Class.Data
- DhcpServerv4Class.Description
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerv4Class class

Contains information about the DHCP server class, version 4.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Class
{
  string Name;
  string Type;
  string Data;
  string Description;
};
```

## Members

The **DhcpServerv4Class** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Class** class has these properties.

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

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





