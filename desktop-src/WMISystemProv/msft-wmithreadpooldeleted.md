---
title: MSFT\_WmiThreadPoolDeleted class
description: Provides notification when a thread is deleted in the WMI Event SubSystem (ESS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f0af3e48-dba3-49ec-8ea4-398ebe42f0d3
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiThreadPoolDeleted class
- MSFT_WmiThreadPoolDeleted class, described
topic_type:
- apiref
api_name:
- MSFT_WmiThreadPoolDeleted
- MSFT_WmiThreadPoolDeleted.SECURITY_DESCRIPTOR
- MSFT_WmiThreadPoolDeleted.ThreadID
- MSFT_WmiThreadPoolDeleted.TIME_CREATED
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WmiThreadPoolDeleted class

The **MSFT\_WmiThreadPoolDeleted** abstract [troubleshooting class](https://msdn.microsoft.com/library/aa394604) class provides notification when a thread is deleted in the WMI Event SubSystem (ESS).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSFT_WmiThreadPoolDeleted : MSFT_WmiThreadPoolEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint32 ThreadID;
  uint64 TIME_CREATED;
};
```

## Members

The **MSFT\_WmiThreadPoolDeleted** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiThreadPoolDeleted** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor that the event provider uses to determine which users can receive the event. For more information, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634)

</dd> <dt>

**ThreadID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier of the thread involved in the event.

This property is inherited from [**MSFT\_WmiThreadPoolEvent**](msft-wmithreadpoolevent.md)

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time the event is generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634)

</dd> </dl>

## Examples

For an example, see [**MSFT\_WmiThreadPoolEvent**](msft-wmithreadpoolevent.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WmiThreadPoolEvent**](msft-wmithreadpoolevent.md)
</dt> <dt>

[WMI Service Event Troubleshooting Classes](https://msdn.microsoft.com/library/aa394578)
</dt> <dt>

[WMI Troubleshooting](https://msdn.microsoft.com/library/aa394603)
</dt> <dt>

WMI Troubleshooting
</dt> <dt>

[Monitoring Events](https://msdn.microsoft.com/library/aa392396)
</dt> <dt>

[Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013)
</dt> </dl>

 

 





