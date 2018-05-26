---
title: WcsSetCalibrationManagementState function
description: Enables or disables system management of the display calibration state.
ms.assetid: 64646448-c5a8-48a6-923e-fccf1cf63855
keywords:
- WcsSetCalibrationManagementState function Windows Color System
topic_type:
- apiref
api_name:
- WcsSetCalibrationManagementState
api_location:
- mscms.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WcsSetCalibrationManagementState function

Enables or disables system management of the display calibration state.

## Syntax


```C++
BOOL WcsSetCalibrationManagementState(
  _In_ BOOL bIsEnabled
);
```



## Parameters

<dl> <dt>

*bIsEnabled* \[in\]
</dt> <dd>

**TRUE** to enable system management of the display calibration state. **FALSE** to disable system management of the display calibration state.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**.

## Remarks

This function must be called with elevated permissions for it to succeed.

## Requirements



|                    |                                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/> | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Mscms.dll</dt> </dl> |



 

 





