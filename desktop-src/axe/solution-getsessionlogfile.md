---
title: Solution GetSessionLogFile method
description: Retrieve the name of the debugging log files that contain a record of the Axe engine execution.
ms.assetid: 9C4B5A6E-DC0F-4613-862A-3DD000165615
keywords:
- GetSessionLogFile method Access Execution Engine
- GetSessionLogFile method Access Execution Engine , Solution interface
- Solution interface Access Execution Engine , GetSessionLogFile method
topic_type:
- apiref
api_name:
- Solution.GetSessionLogFile
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

# Solution::GetSessionLogFile method

Retrieve the name of the debugging log files that contain a record of the Axe engine execution.

## Syntax


```C++
virtual HRESULT GetSessionLogFile(
  [out, optional] LPCWSTR *sessionLogFile
) const = 0;
```



## Parameters

<dl> <dt>

*sessionLogFile* \[out, optional\]
</dt> <dd>

A double pointer to receive the path to the session files.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

Managed code uses the [**Solution.SessionLogFile \| sessionLogFile**](https://www.bing.com/search?q=**Solution.SessionLogFile \| sessionLogFile**) property

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

 

 





