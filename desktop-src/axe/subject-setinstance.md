---
title: Subject SetInstance method
description: Sets the instance name of the Subject.
ms.assetid: 'CBE2D890-86BF-4B0E-A046-94853A5C9C46'
keywords: ["SetInstance method Access Execution Engine", "SetInstance method Access Execution Engine , Subject interface", "Subject interface Access Execution Engine , SetInstance method"]
topic_type:
- apiref
api_name:
- Subject.SetInstance
api_location:
- AxeCore.dll
api_type:
- COM
---

# Subject::SetInstance method

Sets the instance name of the **Subject**.

## Syntax


```C++
virtual HRESULT SetInstance(
  [in] LPCWSTR name
) = 0;
```



## Parameters

<dl> <dt>

*name* \[in\]
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

 

 





