---
Description: Begins the task completion.
ms.assetid: 75C84DD9-D815-45C2-A28E-EAE437EAFF89
title: TaskCompletionClient::ApplyTaskCompletion method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TaskCompletionClient::ApplyTaskCompletion method

Begins the task completion.

## Syntax


```C++
HRESULT ApplyTaskCompletion(
    UINT32   ptcfCategory
);
```



## Parameters

<dl> <dt>

*ptcfCategory* 
</dt> <dd>

A value indicating the category of the task.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The only supported value for *ptcfCategory* is 0x08000000.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                           |
| DLL<br/>                      | <dl> <dt>ExecModelClient.dll</dt> </dl> |



## See also

<dl> <dt>

[**TaskCompletionClient**](taskcompletionclient.md)
</dt> </dl>

 

 




