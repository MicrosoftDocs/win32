---
description: Specifies whether an XPS print job is in the spooling or the rendering phase.
ms.assetid: 14871d29-59e4-45a2-9697-12550c58396c
title: EPrintXPSJobOperation enumeration (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EPrintXPSJobOperation
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# EPrintXPSJobOperation enumeration

Specifies whether an XPS print job is in the spooling or the rendering phase.

## Syntax


```C++
typedef enum tagEPrintXPSJobOperation { 
  kJobProduction,
  kJobConsumption
} EPrintXPSJobOperation;
```



## Constants

<dl> <dt>

<span id="kJobProduction"></span><span id="kjobproduction"></span><span id="KJOBPRODUCTION"></span>**kJobProduction**
</dt> <dd>

The XPS job is spooling.

</dd> <dt>

<span id="kJobConsumption"></span><span id="kjobconsumption"></span><span id="KJOBCONSUMPTION"></span>**kJobConsumption**
</dt> <dd>

The XPS job is rendering.

</dd> </dl>

## Remarks

This enumeration is primarily used as a parameter for the [**ReportJobProcessingProgress**](reportjobprocessingprogress.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |



 

 




