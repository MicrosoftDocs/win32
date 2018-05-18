---
title: ErrorList GetErrorCount method
description: Retrieve the number of errors in the error list that have occurred while processing the job.
ms.assetid: '5E7978B7-1A9B-4E6F-9BCA-5E4B2E014EA5'
keywords: ["GetErrorCount method Access Execution Engine", "GetErrorCount method Access Execution Engine , ErrorList interface", "ErrorList interface Access Execution Engine , GetErrorCount method"]
topic_type:
- apiref
api_name:
- ErrorList.GetErrorCount
api_location:
- AxeCore.dll
api_type:
- COM
---

# ErrorList::GetErrorCount method

Retrieve the number of errors in the error list that have occurred while processing the job.

## Syntax


```C++
virtual HRESULT GetErrorCount(
  [out] UINT *count
) const = 0;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

The number of errors in the error list.

</dd> </dl>

## Return value

This method always returns **S\_OK**.

## Remarks

Managed codes uses the [**AxeException**](https://msdn.microsoft.com/library/windows/desktop/hh802908) object.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorList**](errorlist.md)
</dt> </dl>

 

 





