---
title: SystemState RestoreAll method
description: Restores all system settings originally modified through SetBoolean back to their original values.
ms.assetid: BC630F4B-DFC9-4AF8-B412-AC6FF947037F
keywords:
- RestoreAll method Access Execution Engine
- RestoreAll method Access Execution Engine , SystemState interface
- SystemState interface Access Execution Engine , RestoreAll method
topic_type:
- apiref
api_name:
- SystemState.RestoreAll
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

# SystemState::RestoreAll method

Restores all system settings originally modified through [**SetBoolean**](systemstate-setboolean.md) back to their original values.

## Syntax


```C++
virtual HRESULT RestoreAll() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

When an assessment calls [**ManageSystemState**](support-managesystemstate.md) a state file is created that stores any [**SystemSetting**](systemsetting.md) values that are modified by [**SetBoolean**](systemstate-setboolean.md). This method restores the original settings as stored in the state file. If an assessment modifies a system setting manually, without using **SetBoolean**, this method will not restore the original value because it will not have been stored in the state file.

Managed code uses [**SystemState.RestoreAll**](axe-systemstate_restoreall_om) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**SystemState**](systemstate.md)
</dt> </dl>

 

 





