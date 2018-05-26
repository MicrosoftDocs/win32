---
title: Activity ClearTrace method
description: Clears the Trace settings of the Activity.
ms.assetid: 89B4DF86-7B84-45F6-99E2-863BE70BFCC0
keywords:
- ClearTrace method Access Execution Engine
- ClearTrace method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , ClearTrace method
topic_type:
- apiref
api_name:
- Activity.ClearTrace
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Activity::ClearTrace method

Clears the [**Trace**](trace-struct.md) settings of the **Activity**.

## Syntax


```C++
virtual HRESULT ClearTrace() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The **Trace** holds data from element **Activity/Trace**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





