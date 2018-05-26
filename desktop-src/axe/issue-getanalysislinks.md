---
title: Issue GetAnalysisLinks method
description: Returns the analysis LinkCollection of the Issue.
ms.assetid: D2A5CA5A-97E5-4DBF-A3F8-0C603FE94A0B
keywords:
- GetAnalysisLinks method Access Execution Engine
- GetAnalysisLinks method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetAnalysisLinks method
topic_type:
- apiref
api_name:
- Issue.GetAnalysisLinks
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

# Issue::GetAnalysisLinks method

Returns the analysis [**LinkCollection**](linkcollection.md) of the **Issue**.

## Syntax


```C++
virtual HRESULT GetAnalysisLinks(
  [out] LinkCollection **analysisLinks
) = 0;
```



## Parameters

<dl> <dt>

*analysisLinks* \[out\]
</dt> <dd>

The analysis **LinkCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The analysis **LinkCollection** holds data from element **Issue/AnalysisLinks**.

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

 

 





