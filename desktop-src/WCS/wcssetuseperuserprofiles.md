---
title: WcsSetUsePerUserProfiles function
description: Enables a user to specify whether or not to use a per-user profile association list for the specified device.
ms.assetid: c108fbb2-e9f3-41fe-af36-99114df1507e
keywords:
- WcsSetUsePerUserProfiles function Windows Color System
topic_type:
- apiref
api_name:
- WcsSetUsePerUserProfiles
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

# WcsSetUsePerUserProfiles function

Enables a user to specify whether or not to use a per-user profile association list for the specified device.

## Syntax


```C++
BOOL WINAPI WcsSetUsePerUserProfiles(
  _In_ LPCWSTR pDeviceName,
  _In_ DWORD   dwDeviceClass,
  _In_ BOOL    usePerUserProfiles
);
```



## Parameters

<dl> <dt>

*pDeviceName* \[in\]
</dt> <dd>

A pointer to a string that contains the user-friendly name of the device.

</dd> <dt>

*dwDeviceClass* \[in\]
</dt> <dd>

A flag value that specifies the class of the device. This parameter must take one of the following values:



|                |                                    |
|----------------|------------------------------------|
| CLASS\_MONITOR | Specifies a display device.        |
| CLASS\_PRINTER | Specifies a printer.               |
| CLASS\_SCANNER | Specifies an image capture device. |



 

</dd> <dt>

*usePerUserProfiles* \[in\]
</dt> <dd>

A Boolean value that is TRUE if the user wants to use a per-user profile association list for the specified device; otherwise **FALSE**.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If *usePerUserProfiles* is **TRUE**, and the user is not already using a per-user profile association list for *pDeviceName*, then the per-user profile association list is initialized by making a copy of the system-wide profile association list for the same device. From then on, changes to the system-wide list are not included in the per-user list.

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

[**WcsGetUsePerUserProfiles**](wcsgetuseperuserprofiles.md)
</dt> </dl>

 

 





