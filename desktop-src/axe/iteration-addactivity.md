---
title: Iteration AddActivity method
description: Creates and adds an Activity to the Iteration.
ms.assetid: A8673017-E2CC-496F-B50F-D22981A20263
keywords:
- AddActivity method Access Execution Engine
- AddActivity method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , AddActivity method
topic_type:
- apiref
api_name:
- Iteration.AddActivity
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

# Iteration::AddActivity method

Creates and adds an [**Activity**](activity-struct.md) to the **Iteration**.

## Syntax


```C++
virtual HRESULT AddActivity(
  [out] Activity **activity
) = 0;
```



## Parameters

<dl> <dt>

*activity* \[out\]
</dt> <dd>

The **Activity** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Activity** objects hold information from the **Iteration/Activities/Activity** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





