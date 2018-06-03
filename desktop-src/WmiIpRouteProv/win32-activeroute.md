---
title: Win32\_ActiveRoute class
description: The Win32\_ActiveRoute association WMI class relates the current IP4 route to the persisted IP route table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 76ece9d4-9a9e-419a-b09b-0881ae871359
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_ActiveRoute class
- Win32_ActiveRoute class, described
topic_type:
- apiref
api_name:
- Win32_ActiveRoute
- Win32_ActiveRoute.SameElement
- Win32_ActiveRoute.SystemElement
api_location:
- Wmipiprt.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ActiveRoute class

The **Win32\_ActiveRoute** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the current IP4 route to the persisted IP route table.

This class is only applicable to IP4 and does not return IPX or IP6 data. For more information, see [IPv6 and IPv4 Support in WMI](https://msdn.microsoft.com/library/aa822883).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, provider("RouteProvider"), UUID("{7BA1437A-C51C-421B-A359-2906AF2BDD9F}"), AMENDMENT]
class Win32_ActiveRoute : CIM_LogicalIdentity
{
  Win32_IP4PersistedRouteTable REF SameElement;
  Win32_IP4RouteTable          REF SystemElement;
};
```

## Members

The **Win32\_ActiveRoute** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ActiveRoute** class has these properties.

<dl> <dt>

**SameElement**
</dt> <dd> <dl> <dt>

Data type: **Win32\_IP4PersistedRouteTable**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SameElement"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("")
</dt> </dl>

Reference to the instance representing the persistent IP route in this relationship. This property is derived from [**CIM\_LogicalIdentity**](https://msdn.microsoft.com/library/aa387895).

</dd> <dt>

**SystemElement**
</dt> <dd> <dl> <dt>

Data type: **Win32\_IP4RouteTable**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SystemElement"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("")
</dt> </dl>

Reference to the instance representing the active IP route being used. This property is derived from [**CIM\_LogicalIdentity**](https://msdn.microsoft.com/library/aa387895).

</dd> </dl>

## Remarks

The **Win32\_ActiveRoute** class is derived from [**CIM\_LogicalIdentity**](https://msdn.microsoft.com/library/aa387895).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipiprt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipiprt.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalIdentity**](https://msdn.microsoft.com/library/aa387895)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





