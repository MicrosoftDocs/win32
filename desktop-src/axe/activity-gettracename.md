---
title: Activity GetTraceName method
description: Returns the trace name of the Activity.
ms.assetid: 5E71E7D6-108A-414E-A2D3-0D2379498C47
keywords:
- GetTraceName method Access Execution Engine
- GetTraceName method Access Execution Engine , Activity interface
- Activity interface Access Execution Engine , GetTraceName method
topic_type:
- apiref
api_name:
- Activity.GetTraceName
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

# Activity::GetTraceName method

Returns the trace name of the **Activity**.

## Syntax


```C++
virtual HRESULT GetTraceName(
  [out] LPCWSTR *traceName
) const = 0;
```



## Parameters

<dl> <dt>

*traceName* \[out\]
</dt> <dd>

The trace name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

The trace name is the value of element **Activity/Trace/Description/Name**.

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

 

 





