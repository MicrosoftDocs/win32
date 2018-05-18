---
title: Iteration GetIssues method
description: Returns the IssueCollection for the Iteration.
ms.assetid: '1D93B9EF-D13F-49E4-961D-DF57323BD72A'
keywords: ["GetIssues method Access Execution Engine", "GetIssues method Access Execution Engine , Iteration interface", "Iteration interface Access Execution Engine , GetIssues method"]
topic_type:
- apiref
api_name:
- Iteration.GetIssues
api_location:
- AxeCore.dll
api_type:
- COM
---

# Iteration::GetIssues method

Returns the [**IssueCollection**](issuecollection.md) for the **Iteration**.

## Syntax


```C++
virtual HRESULT GetIssues(
  [out] IssueCollection **issues
) = 0;
```



## Parameters

<dl> <dt>

*issues* \[out\]
</dt> <dd>

The **IssueCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **IssueCollection** holds information from element **Iteration/Issues**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





