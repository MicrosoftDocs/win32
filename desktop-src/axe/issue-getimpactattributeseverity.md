---
title: Issue GetImpactAttributeSeverity method
description: Returns the impact severity of the Issue.
ms.assetid: ACDD5D11-BDA8-4D60-B5BF-FB69ED66587D
keywords:
- GetImpactAttributeSeverity method Access Execution Engine
- GetImpactAttributeSeverity method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetImpactAttributeSeverity method
topic_type:
- apiref
api_name:
- Issue.GetImpactAttributeSeverity
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

# Issue::GetImpactAttributeSeverity method

Returns the impact severity of the **Issue**.

## Syntax


```C++
virtual HRESULT GetImpactAttributeSeverity(
  [out] UINT *impactAttributeSeverity
) const = 0;
```



## Parameters

<dl> <dt>

*impactAttributeSeverity* \[out\]
</dt> <dd>

The impact severity.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The impact severity is the value of attribute **Severity** of element **Issue/Impact**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





