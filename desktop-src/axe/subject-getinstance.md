---
title: Subject GetInstance method
description: Returns the instance name of the Subject.
ms.assetid: '6A30B0DF-5855-41F1-92E7-0CB9343EBB31'
keywords: ["GetInstance method Access Execution Engine", "GetInstance method Access Execution Engine , Subject interface", "Subject interface Access Execution Engine , GetInstance method"]
topic_type:
- apiref
api_name:
- Subject.GetInstance
api_location:
- AxeCore.dll
api_type:
- COM
---

# Subject::GetInstance method

Returns the instance name of the **Subject**.

## Syntax


```C++
virtual HRESULT GetInstance(
  [out] LPCWSTR *name
) const = 0;
```



## Parameters

<dl> <dt>

*name* \[out\]
</dt> <dd>

The instance name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Subject** objects hold information from the **Iteration/TestCases/TestCase/Subject** elements.

The instance name is the value of element **Subject/Instance/ProgrammaticName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Subject**](subject.md)
</dt> </dl>

 

 





