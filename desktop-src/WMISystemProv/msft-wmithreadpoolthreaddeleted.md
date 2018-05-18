---
title: MSFT\_WmiThreadPoolThreadDeleted class
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a3930d1d-5c80-439f-a81f-030ca2c7d3a4'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WmiThreadPoolThreadDeleted class", "MSFT_WmiThreadPoolThreadDeleted class, described"]
topic_type:
- apiref
api_name:
- MSFT_WmiThreadPoolThreadDeleted
- MSFT_WmiThreadPoolThreadDeleted.SECURITY_DESCRIPTOR
- MSFT_WmiThreadPoolThreadDeleted.TIME_CREATED
- MSFT_WmiThreadPoolThreadDeleted.ThreadID
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
---

# MSFT\_WmiThreadPoolThreadDeleted class

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_WmiThreadPoolThreadDeleted : MSFT_WmiThreadPoolEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 ThreadID;
};
```

## Members

The **MSFT\_WmiThreadPoolThreadDeleted** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiThreadPoolThreadDeleted** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor that the event provider uses to determine which users can receive the event. For more information, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

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

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\cimv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WmiThreadPoolEvent**](msft-wmithreadpoolevent.md)
</dt> </dl>

 

 





