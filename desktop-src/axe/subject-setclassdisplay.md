---
title: Subject SetClassDisplay method
description: Sets the class display name of the Subject.
ms.assetid: '474BD256-99A9-4E09-BBB0-5F0A0D3E40F3'
keywords: ["SetClassDisplay method Access Execution Engine", "SetClassDisplay method Access Execution Engine , Subject interface", "Subject interface Access Execution Engine , SetClassDisplay method"]
topic_type:
- apiref
api_name:
- Subject.SetClassDisplay
api_location:
- AxeCore.dll
api_type:
- COM
---

# Subject::SetClassDisplay method

Sets the class display name of the **Subject**.

## Syntax


```C++
virtual HRESULT SetClassDisplay(
  [in] LPCWSTR name
) = 0;
```



## Parameters

<dl> <dt>

*name* \[in\]
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

 

 





