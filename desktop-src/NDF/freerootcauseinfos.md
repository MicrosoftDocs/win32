---
title: FreeRootCauseInfos function
description: Deallocates the memory allocated internally to an array of RootCauseInfo structures.
ms.assetid: b45fa432-0db4-470b-80ce-ae25c33f88d6
keywords:
- FreeRootCauseInfos function NDF
topic_type:
- apiref
api_name:
- FreeRootCauseInfos
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

# FreeRootCauseInfos function

The **FreeRootCauseInfos** function deallocates the memory allocated internally to an array of [**RootCauseInfo**](/windows/win32/ndattrib/ns-ndattrib-tagrootcauseinfo?branch=master) structures. This function calls [**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722) to deallocate memory.

## Syntax


```C++
VOID FreeRootCauseInfos(
  _In_ RootCauseInfo *pInfo,
       ULONG         RootCauseCount,
       BOOL          bFreePointer
);
```



## Parameters

<dl> <dt>

*pInfo* \[in\]
</dt> <dd>

Type: **[**RootCauseInfo**](/windows/win32/ndattrib/ns-ndattrib-tagrootcauseinfo?branch=master)\***

The array of structures. The allocated memory pointed to by these structures will be freed.

</dd> <dt>

*RootCauseCount* 
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

[**RootCauseInfo**](/windows/win32/ndattrib/ns-ndattrib-tagrootcauseinfo?branch=master)
</dt> <dt>

[**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722)
</dt> </dl>

 

 





