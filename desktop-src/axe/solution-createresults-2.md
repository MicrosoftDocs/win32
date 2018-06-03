---
title: Solution CreateResults method
description: Create a JobResults object from a results file.
ms.assetid: DA62D3C6-CF54-4320-8706-124DA2A447CB
keywords:
- CreateResults method Access Execution Engine
- CreateResults method Access Execution Engine , Solution interface
- Solution interface Access Execution Engine , CreateResults method
topic_type:
- apiref
api_name:
- Solution.CreateResults
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

# Solution::CreateResults method

Create a [**JobResults**](jobresults.md) object from a results file.

## Syntax


```C++
HRESULT CreateResults(
  [in]  LPCWSTR    resultPath,
  [out] JobResults **newResults,
  [out] ErrorList  **errorList
);
```



## Parameters

<dl> <dt>

*resultPath* \[in\]
</dt> <dd>

The path to the result file.

</dd> <dt>

*newResults* \[out\]
</dt> <dd>

The **JobResults** object that this method creates.

</dd> <dt>

*errorList* \[out\]
</dt> <dd>

An [**ErrorList**](errorlist.md) object.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>AxeCore.lib</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Solution**](solution-inf.md)
</dt> </dl>

 

 





