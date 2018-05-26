---
title: Solution GetSessionFolder method
description: Retrieve the folder that contains the Axe engine state files and debugging logs.
ms.assetid: 45C26178-E2DD-4FF9-8C44-55E396C73AB4
keywords:
- GetSessionFolder method Access Execution Engine
- GetSessionFolder method Access Execution Engine , Solution interface
- Solution interface Access Execution Engine , GetSessionFolder method
topic_type:
- apiref
api_name:
- Solution.GetSessionFolder
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

# Solution::GetSessionFolder method

Retrieve the folder that contains the Axe engine state files and debugging logs.

## Syntax


```C++
virtual HRESULT GetSessionFolder(
  [out, optional] LPCWSTR *sessionFolder
) const = 0;
```



## Parameters

<dl> <dt>

*sessionFolder* \[out, optional\]
</dt> <dd>

A double pointer to receive the path to the session files.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

Managed code uses the [**Solution.SessionFolder \| sessionFolder**](axe-solution_sessionfolder_om) property.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Solution**](solution-inf.md)
</dt> </dl>

 

 





