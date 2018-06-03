---
title: WcsGetUsePerUserProfiles function
description: Determines whether the user chose to use a per-user profile association list for the specified device.
ms.assetid: 375a9ee6-b432-424a-8671-c5a598d82342
keywords:
- WcsGetUsePerUserProfiles function Windows Color System
topic_type:
- apiref
api_name:
- WcsGetUsePerUserProfiles
api_location:
- mscms.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WcsGetUsePerUserProfiles function

Determines whether the user chose to use a per-user profile association list for the specified device.

## Syntax


```C++
BOOL WINAPI WcsGetUsePerUserProfiles(
  _In_  LPCWSTR pDeviceName,
  _In_  DWORD   dwDeviceClass,
  _Out_ BOOL    *pUsePerUserProfiles
);
```



## Parameters

<dl> <dt>

*pDeviceName* \[in\]
</dt> <dd>

A pointer to a string containing the user-friendly name of the device.

</dd> <dt>

*dwDeviceClass* \[in\]
</dt> <dd>

A flag value specifying the class of the device. This parameter must take one of the following values:



|                |                                    |
|----------------|------------------------------------|
| CLASS\_MONITOR | Specifies a display device.        |
| CLASS\_PRINTER | Specifies a printer.               |
| CLASS\_SCANNER | Specifies an image-capture device. |



 

</dd> <dt>

*pUsePerUserProfiles* \[out\]
</dt> <dd>

A pointer to a location to receive a Boolean value that is **TRUE** if the user chose to use a per-user profile association list for the specified device; otherwise **FALSE**.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function fails if *pDeviceName* points to a device that is not of the class specified by *dwDeviceClass*.

This function is executable in Least-Privileged User Account (LUA) context.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Windows Color System Schemas and Algorithms](windows-color-system-schemas-and-algorithms.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**WcsSetUsePerUserProfiles**](wcssetuseperuserprofiles.md)
</dt> </dl>

 

 





