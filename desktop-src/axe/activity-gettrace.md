---
title: Activity GetTrace method
description: Returns the Trace of the Activity.
ms.assetid: 4AF5A2DA-CC32-455F-8FED-B16B5A12FA06
keywords:
- GetTrace method Access Execution Engine
- GetTrace method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetTrace method
topic_type:
- apiref
api_name:
- Activity.GetTrace
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Activity::GetTrace method

Returns the [**Trace**](trace-struct.md) of the **Activity**.

## Syntax


```C++
virtual HRESULT GetTrace(
  [out] Trace **trace
) = 0;
```



## Parameters

<dl> <dt>

*trace* \[out\]
</dt> <dd>

The **Trace**.

</dd> </dl>

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

 

 





