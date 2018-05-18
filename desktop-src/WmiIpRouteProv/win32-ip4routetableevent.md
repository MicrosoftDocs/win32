---
title: Win32\_IP4RouteTableEvent class
description: The Win32\_IP4RouteTableEvent \ 32; WMI class represents IP route change events resulting from the addition, removal, or modification of IP routes on the computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a700467b-4535-4197-8aed-bae7e84e7962'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_IP4RouteTableEvent class", "Win32_IP4RouteTableEvent class, described"]
topic_type:
- apiref
api_name:
- Win32_IP4RouteTableEvent
- Win32_IP4RouteTableEvent.SECURITY_DESCRIPTOR
- Win32_IP4RouteTableEvent.TIME_CREATED
api_location:
- Wmipiprt.dll
api_type:
- DllExport
---

# Win32\_IP4RouteTableEvent class

The **Win32\_IP4RouteTableEvent** [WMI class](https://msdn.microsoft.com/library/aa393244) represents IP route change events resulting from the addition, removal, or modification of IP routes on the computer system.

This class is only applicable to IP4 and does not return IPX or IP6 data. For more information, see [IPv6 and IPv4 Support in WMI](https://msdn.microsoft.com/library/aa822883).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{1C385E29-A5B4-40F0-96CF-929FC00958B}"), AMENDMENT]
class Win32_IP4RouteTableEvent : __ExtrinsicEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
};
```

## Members

The **Win32\_IP4RouteTableEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_IP4RouteTableEvent** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634). For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> </dl>

## Remarks

The **Win32\_IP4RouteTableEvent** class is derived from the WMI [**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646) system class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipiprt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipiprt.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





