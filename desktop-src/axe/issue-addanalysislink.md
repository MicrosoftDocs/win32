---
title: Issue AddAnalysisLink method
description: Creates and adds an analysis Link to the Issue.
ms.assetid: 'A266EF53-C00B-4901-A065-4E6513C81D4D'
keywords: ["AddAnalysisLink method Access Execution Engine", "AddAnalysisLink method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , AddAnalysisLink method"]
topic_type:
- apiref
api_name:
- Issue.AddAnalysisLink
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::AddAnalysisLink method

Creates and adds an analysis [**Link**](link-struct.md) to the **Issue**.

## Syntax


```C++
virtual HRESULT AddAnalysisLink(
  [in, optional]  LPCWSTR analysisLinkTitle,
  [in, optional]  LPCWSTR analysisLinkValue,
  [out, optional] Link    **analysisLink
) = 0;
```



## Parameters

<dl> <dt>

*analysisLinkTitle* \[in, optional\]
</dt> <dd>

The analysis link title.

</dd> <dt>

*analysisLinkValue* \[in, optional\]
</dt> <dd>

The analysis link value, a URI.

</dd> <dt>

*analysisLink* \[out, optional\]
</dt> <dd>

The analysis **Link** object that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The analysis **Link** objects hold information from the **Issue/AnalysisLinks/Link** elements.

The analysis link title is the value of element **Link/LinkTitle**.

The analysis link value is the value of element **Link/LinkURI**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





