---
title: Subject SetInstanceDisplay method
description: Sets the instance display name of the Subject.
ms.assetid: 4C48F87C-DCFA-4507-86A2-43A40B5A3FDE
keywords:
- SetInstanceDisplay method Access Execution Engine
- SetInstanceDisplay method Access Execution Engine , Subject interface
- Subject interface Access Execution Engine , SetInstanceDisplay method
topic_type:
- apiref
api_name:
- Subject.SetInstanceDisplay
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

# Subject::SetInstanceDisplay method

Sets the instance display name of the **Subject**.

## Syntax


```C++
virtual HRESULT SetInstanceDisplay(
  [in] LPCWSTR name
) = 0;
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

The instance display name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Subject** objects hold information from the **Iteration/TestCases/TestCase/Subject** elements.

The instance display name is the value of element **Subject/Instance/DisplayName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Subject**](subject.md)
</dt> </dl>

 

 





