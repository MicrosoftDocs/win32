---
title: Subject GetClassDisplay method
description: Returns the class display name of the Subject.
ms.assetid: '2E1072CE-B5F3-4F27-8D32-5E2945009AD9'
keywords: ["GetClassDisplay method Access Execution Engine", "GetClassDisplay method Access Execution Engine , Subject interface", "Subject interface Access Execution Engine , GetClassDisplay method"]
topic_type:
- apiref
api_name:
- Subject.GetClassDisplay
api_location:
- AxeCore.dll
api_type:
- COM
---

# Subject::GetClassDisplay method

Returns the class display name of the **Subject**.

## Syntax


```C++
virtual HRESULT GetClassDisplay(
  [out] LPCWSTR *name
) const = 0;
```



## Parameters

<dl> <dt>

*name* \[out\]
</dt> <dd>

The class display name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Subject** objects hold information from the **Iteration/TestCases/TestCase/Subject** elements.

The class display name is the value of element **Subject/Class/DisplayName**.

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

 

 





