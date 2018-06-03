---
title: Solution CreateEngine method
description: Create an Engine object for running AXE jobs.
ms.assetid: b1251e91-5479-43b3-854e-a05cc37a3292
keywords:
- CreateEngine method Access Execution Engine
- CreateEngine method Access Execution Engine , Solution interface
- Solution interface Access Execution Engine , CreateEngine method
topic_type:
- apiref
api_name:
- Solution.CreateEngine
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

# Solution::CreateEngine method

Create an [**Engine**](engine-if.md) object for running AXE jobs.

## Syntax


```C++
virtual HRESULT CreateEngine(
  [out] Engine **engine
) = 0;
```



## Parameters

<dl> <dt>

*engine* \[out\]
</dt> <dd>

A double pointer to receive a pointer to the newly created [**Engine**](engine-if.md) object.

</dd> </dl>

## Return value

If successful, this method returns **S\_OK**.

If there is insufficient memory available to create an [**Engine**](engine-if.md) object, this method returns **E\_OUTOFMEMORY**.

## Remarks

Managed code uses the [**Solution.CreateEngine \| createEngine**](https://www.bing.com/search?q=**Solution.CreateEngine \| createEngine**) method.

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

 

 





