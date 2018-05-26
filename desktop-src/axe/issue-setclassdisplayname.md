---
title: Issue SetClassDisplayName method
description: Sets the display name of the class of the Issue.
ms.assetid: A11D6AA7-5CF3-4B95-8124-5E843EDD8544
keywords:
- SetClassDisplayName method Access Execution Engine
- SetClassDisplayName method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , SetClassDisplayName method
topic_type:
- apiref
api_name:
- Issue.SetClassDisplayName
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

# Issue::SetClassDisplayName method

Sets the display name of the class of the **Issue**.

## Syntax


```C++
virtual HRESULT SetClassDisplayName(
  [in] LPCWSTR classDisplayName
) = 0;
```



## Parameters

<dl> <dt>

*classDisplayName* \[in\]
</dt> <dd>

The display name of the class.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The display name of the class is the value of element **Issue/Class/DisplayName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





