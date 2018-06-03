---
title: Trace GetTooltip method
description: Returns the tooltip of the Trace.
ms.assetid: 41829876-6826-43F4-962F-EF6A3830A9CB
keywords:
- GetTooltip method Access Execution Engine
- GetTooltip method Access Execution Engine , Trace interface
- Trace interface Access Execution Engine , GetTooltip method
topic_type:
- apiref
api_name:
- Trace.GetTooltip
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

# Trace::GetTooltip method

Returns the tooltip of the **Trace**.

## Syntax


```C++
virtual HRESULT GetTooltip(
  [out] LPCWSTR *tooltip
) const = 0;
```



## Parameters

<dl> <dt>

*tooltip* \[out\]
</dt> <dd>

The tooltip.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

**Trace** objects hold data from **AssessmentResult/Traces/Trace**, **Iteration/Trace** and **Activity/Trace** elements.

The tooltip is the value of element **Trace/Description/ToolTip**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Trace**](trace-struct.md)
</dt> </dl>

 

 





