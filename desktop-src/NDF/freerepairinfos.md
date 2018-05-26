---
title: FreeRepairInfos function
description: Deallocates the memory allocated internally to an array of RepairInfo structures.
ms.assetid: c40f9d10-8d9e-4c79-ac0b-fa88608888f1
keywords:
- FreeRepairInfos function NDF
topic_type:
- apiref
api_name:
- FreeRepairInfos
api_location:
- ndattributils.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FreeRepairInfos function

The **FreeRepairInfos** function deallocates the memory allocated internally to an array of [**RepairInfo**](/windows/win32/ndattrib/ns-ndattrib-tagrepairinfo?branch=master) structures. This function calls [**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722) to deallocate memory.

## Syntax


```C++
VOID FreeRepairInfos(
  _In_ RepairInfo *pInfo,
       ULONG      RepairCount,
       BOOL       bFreePointer
);
```



## Parameters

<dl> <dt>

*pInfo* \[in\]
</dt> <dd>

Type: **[**RepairInfo**](/windows/win32/ndattrib/ns-ndattrib-tagrepairinfo?branch=master)\***

The array of structures. The allocated memory pointed to by these structures will be freed.

</dd> <dt>

*RepairCount* 
</dt> <dd>

Type: **ULONG**

The number of structures in the array pointed to by *pInfo*.

</dd> <dt>

*bFreePointer* 
</dt> <dd>

Type: **BOOL**

True if the array of structures should also be deleted; otherwise, false.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Ndattributils.h</dt> </dl> |



## See also

<dl> <dt>

[**RepairInfo**](/windows/win32/ndattrib/ns-ndattrib-tagrepairinfo?branch=master)
</dt> <dt>

[**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722)
</dt> </dl>

 

 





