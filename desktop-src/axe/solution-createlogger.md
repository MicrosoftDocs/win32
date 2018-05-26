---
title: Solution CreateLogger method
description: Creates a Logging object to write information into AXE s event logging file.
ms.assetid: d501692d-53b0-447c-93cc-33d2961a3868
keywords:
- CreateLogger method Access Execution Engine
- CreateLogger method Access Execution Engine , Solution interface
- Solution interface Access Execution Engine , CreateLogger method
topic_type:
- apiref
api_name:
- Solution.CreateLogger
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

# Solution::CreateLogger method

Creates a [**Logging**](logging.md) object to write information into AXE s event logging file.

## Syntax


```C++
virtual HRESULT CreateLogger(
  [out] Logging **log
) = 0;
```



## Parameters

<dl> <dt>

*log* \[out\]
</dt> <dd>

A double pointer to receive a pointer to the newly created [**Logging**](logging.md) object.

</dd> </dl>

## Return value

If AXE creates the [**Logging**](logging.md) object successfully, this method returns **S\_OK**.

If there is insufficient memory available to create a [**Logging**](logging.md) object, this method returns **E\_OUTOFMEMORY**.

## Remarks

Manage code uses the [**Solution.CreateLogger \| createLogger**](axe-solution_createlogger_om) method.

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

 

 





