---
title: Subject GetClass method
description: Returns the class name of the Subject.
ms.assetid: 'F47A8555-FD2A-41BE-B38A-AF086074E6EB'
keywords: ["GetClass method Access Execution Engine", "GetClass method Access Execution Engine , Subject interface", "Subject interface Access Execution Engine , GetClass method"]
topic_type:
- apiref
api_name:
- Subject.GetClass
api_location:
- AxeCore.dll
api_type:
- COM
---

# Subject::GetClass method

Returns the class name of the **Subject**.

## Syntax


```C++
virtual HRESULT GetClass(
  [out] LPCWSTR *name
) const = 0;
```



## Parameters

<dl> <dt>

*name* \[out\]
</dt> <dd>

The class name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Subject** objects hold information from the **Iteration/TestCases/TestCase/Subject** elements.

The class name is the value of element **Subject/Class/ProgrammaticName**.

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

 

 





