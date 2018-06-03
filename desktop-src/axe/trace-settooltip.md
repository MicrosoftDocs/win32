---
title: Trace SetTooltip method
description: Sets the tooltip of the Trace.
ms.assetid: D9A23EC7-BE2C-49FA-87EC-A650E580A263
keywords:
- SetTooltip method Access Execution Engine
- SetTooltip method Access Execution Engine , Trace interface
- Trace interface Access Execution Engine , SetTooltip method
topic_type:
- apiref
api_name:
- Trace.SetTooltip
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

# Trace::SetTooltip method

Sets the tooltip of the **Trace**.

## Syntax


```C++
virtual HRESULT SetTooltip(
  [in] LPCWSTR tooltip
) = 0;
```



## Parameters

<dl> <dt>

*tooltip* \[in\]
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

 

 





