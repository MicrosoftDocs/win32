---
title: Subject GetInstanceDisplay method
description: Returns the instance display name of the Subject.
ms.assetid: 182CC705-F41B-4CD4-8E65-0CD4CB803AEE
keywords:
- GetInstanceDisplay method Access Execution Engine
- GetInstanceDisplay method Access Execution Engine , Subject interface
- Subject interface Access Execution Engine , GetInstanceDisplay method
topic_type:
- apiref
api_name:
- Subject.GetInstanceDisplay
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Subject::GetInstanceDisplay method

Returns the instance display name of the **Subject**.

## Syntax


```C++
virtual HRESULT GetInstanceDisplay(
  [out] LPCWSTR *name
) const = 0;
```



## Parameters

<dl> <dt>

*name* \[out\]
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

 

 





