---
title: DhcpServerv4Filter class
description: Dhcp Server v4 Filter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2daffbef-b69c-46c3-be81-9968415d269e
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerv4Filter class
- DhcpServerv4Filter class, described
topic_type:
- apiref
api_name:
- DhcpServerv4Filter
- DhcpServerv4Filter.List
- DhcpServerv4Filter.Description
- DhcpServerv4Filter.MacAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DhcpServerv4Filter class

Dhcp Server v4 Filter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Filter
{
  string List;
  string Description;
  string MacAddress;
};
```

## Members

The **DhcpServerv4Filter** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Filter** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description for the filter record.

</dd> <dt>

**List**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

List of allowed filter on Dhcp Server.

<dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>

**Allow** ("Allow")


</dt> <dd></dd> <dt>

<span id="Deny"></span><span id="deny"></span><span id="DENY"></span>

**Deny** ("Deny")


</dt> <dd></dd> </dl>

</dd> <dt>

**MacAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Filter pattern (hardware address) as hex string.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





