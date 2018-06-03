---
title: Support ManageSystemState method
description: Retrieves a SystemState interface that is bound to a file use to save and restore the system configuration.
ms.assetid: F206930D-98C0-40C0-BFA5-CEFAB5FF935E
keywords:
- ManageSystemState method Access Execution Engine
- ManageSystemState method Access Execution Engine , Support interface
- Support interface Access Execution Engine , ManageSystemState method
topic_type:
- apiref
api_name:
- Support.ManageSystemState
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

# Support::ManageSystemState method

Retrieves a [**SystemState**](systemstate.md) interface that is bound to a file use to save and restore the system configuration.

## Syntax


```C++
virtual HRESULT ManageSystemState(
  [in]  LPCWSTR     fileName,
  [out] SystemState **state
) = 0;
```



## Parameters

<dl> <dt>

*fileName* \[in\]
</dt> <dd>

The name of the file used to save system settings modified through a call to [**SetBoolean**](systemstate-setboolean.md).

</dd> <dt>

*state* \[out\]
</dt> <dd>

A double pointer to receive the object that implements the [**SystemState**](systemstate.md) interface.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The [**SystemSetting**](systemsetting.md) enumeration defines items on a system that may be used by assessments. These settings can be read and modified. The original values of modified settings are saved in the *fileName* file. The system state can be restored by calling [**RestoreAll**](systemstate-restoreall.md) to reverse any configuration changes made through [**SetBoolean**](systemstate-setboolean.md). Any changes made by manually modifying underlying OS structures are not stored. This method binds the [**SystemState**](systemstate.md) interface to a specific filename where the modified settings will be stored.

Managed code uses the [**Support.ManageSystemState**](https://www.bing.com/search?q=**Support.ManageSystemState**) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





