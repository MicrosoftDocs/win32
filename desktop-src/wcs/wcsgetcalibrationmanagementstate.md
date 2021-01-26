---
title: WcsGetCalibrationManagementState function
description: Determines whether system management of the display calibration state is enabled.
ms.assetid: 1c069d20-3d99-497f-bd43-613b504355d8
keywords:
- WcsGetCalibrationManagementState function Windows Color System
topic_type:
- apiref
api_name:
- WcsGetCalibrationManagementState
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# WcsGetCalibrationManagementState function

Determines whether system management of the display calibration state is enabled.

## Syntax


```C++
BOOL WcsGetCalibrationManagementState(
  _Out_ BOOL *pbIsEnabled
);
```



## Parameters

<dl> <dt>

*pbIsEnabled* \[out\]
</dt> <dd>

**TRUE** if system management of the display calibration state is enabled; otherwise **FALSE**.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**.

## Requirements



|                    |                                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/> | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Mscms.dll</dt> </dl> |



 

 





