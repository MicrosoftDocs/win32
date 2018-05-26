---
title: FreeRepairInfoExs function
description: Deallocates the memory allocated internally to an array of RepairInfoEx structures.
ms.assetid: b4e3e758-88cd-4ce2-b1a4-5b47889aae9b
keywords:
- FreeRepairInfoExs function NDF
topic_type:
- apiref
api_name:
- FreeRepairInfoExs
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

# FreeRepairInfoExs function

The **FreeRepairInfoExs** function deallocates the memory allocated internally to an array of [**RepairInfoEx**](/windows/win32/ndattrib/ns-ndattrib-tagrepairinfoex?branch=master) structures. This function calls [**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722) to deallocate memory.

## Syntax


```C++
VOID FreeRepairInfoExs(
  _In_ RepairInfoEx *pInfo,
       ULONG        RepairCount,
       BOOL         bFreePointer
);
```



## Parameters

<dl> <dt>

*pInfo* \[in\]
</dt> <dd>

Type: **[**RepairInfoEx**](/windows/win32/ndattrib/ns-ndattrib-tagrepairinfoex?branch=master)\***

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

[**RepairInfoEx**](/windows/win32/ndattrib/ns-ndattrib-tagrepairinfoex?branch=master)
</dt> <dt>

[**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722)
</dt> </dl>

 

 





