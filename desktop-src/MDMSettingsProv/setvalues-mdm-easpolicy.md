---
title: SetValues method of the MDM\_EASPolicy class
description: Sets password-related setting values.
ms.assetid: 5d72680d-c640-415b-abdd-23429eaffa75
keywords:
- SetValues method MDM Settings
- SetValues method MDM Settings , MDM_EASPolicy class
- MDM_EASPolicy class MDM Settings , SetValues method
topic_type:
- apiref
api_name:
- MDM_EASPolicy.SetValues
api_location:
- MDMSettingsProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetValues method of the MDM\_EASPolicy class

Sets password-related setting values.

## Syntax


```mof
uint32 SetValues(
  [in] string NamedValuesList
);
```



## Parameters

<dl> <dt>

*NamedValuesList* \[in\]
</dt> <dd>

The setting-name/value pairs in the form: *name1*,*value1*;*name2*,*value2*.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_EASPolicy**](https://msdn.microsoft.com/library/dn610390)
</dt> </dl>

 

 





