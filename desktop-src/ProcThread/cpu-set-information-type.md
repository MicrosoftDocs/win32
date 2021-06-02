---
description: Represents the type of information in the SYSTEM\_CPU\_SET\_INFORMATION structure.
ms.assetid: B42CB8E8-0010-4B11-AB0D-6D196DCCC90A
title: CPU_SET_INFORMATION_TYPE enumeration (Processthreadapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPU_SET_INFORMATION_TYPE
api_type: 
- HeaderDef
api_location: 
- Processthreadapi.h
---

# CPU\_SET\_INFORMATION\_TYPE enumeration

Represents the type of information in the [**SYSTEM\_CPU\_SET\_INFORMATION**](/windows/desktop/api/winnt/ns-winnt-system_cpu_set_information) structure.

## Syntax


```C++
typedef enum _CPU_SET_INFORMATION_TYPE { 
  CpuSetInformation
} CPU_SET_INFORMATION_TYPE, *PCPU_SET_INFORMATION_TYPE;
```



## Constants

<dl> <dt>

<span id="CpuSetInformation"></span><span id="cpusetinformation"></span><span id="CPUSETINFORMATION"></span>**CpuSetInformation**
</dt> <dd>

The structure contains CPU Set information.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                              |
| Header<br/>                   | <dl> <dt>Processthreadsapi.h (include Windows.h)</dt> </dl> |



 

 




