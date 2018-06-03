---
title: ResetUserPassword method of the MDM\_Client class
description: Resets the user's password.
ms.assetid: abd82873-6360-4801-83ec-160b5d9fd249
keywords:
- ResetUserPassword method MDM Settings
- ResetUserPassword method MDM Settings , MDM_Client class
- MDM_Client class MDM Settings , ResetUserPassword method
topic_type:
- apiref
api_name:
- MDM_Client.ResetUserPassword
api_location:
- MDMSettingsProv.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ResetUserPassword method of the MDM\_Client class

Resets the user's password.

**Windows 8.1:** This method is supported beginning with Windows 8.1 Update.

## Syntax


```mof
uint32 ResetUserPassword(
  [in] string ConfigString
);
```



## Parameters

<dl> <dt>

*ConfigString* \[in\]
</dt> <dd>

The username/password pair. For example, "*User@Company.com*;*pwd1*".

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_Client**](https://msdn.microsoft.com/library/dn610387)
</dt> </dl>

 

 





