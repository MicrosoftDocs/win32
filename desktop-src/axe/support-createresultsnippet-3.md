---
title: Support CreateResultSnippet method
description: Creates a result snippet.
ms.assetid: 'C64FF4DD-41C0-4249-A6D2-092D0137407E'
keywords: ["CreateResultSnippet method Access Execution Engine", "CreateResultSnippet method Access Execution Engine , Support interface", "Support interface Access Execution Engine , CreateResultSnippet method"]
topic_type:
- apiref
api_name:
- Support.CreateResultSnippet
api_location:
- AxeCore.dll
api_type:
- COM
---

# Support::CreateResultSnippet method

Creates a result snippet.

## Syntax


```C++
virtual HRESULT CreateResultSnippet(
  [in]  LPCWSTR       resultsFile,
  [out] ResultSnippet **resultsFile
) = 0;
```



## Parameters

<dl> <dt>

*resultsFile* \[in\]
</dt> <dd>

The name of the results file.

</dd> <dt>

*resultsFile* \[out\]
</dt> <dd>

A double pointer to receive the new results snippet.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





