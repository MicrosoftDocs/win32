---
title: UpdateConfiguration method of the MDM\_WNSConfiguration class
description: Updates the Windows Notification Service (WNS) configuration.
ms.assetid: aa768e18-3867-4366-96f1-7bf3060dfd6d
keywords:
- UpdateConfiguration method MDM Settings
- UpdateConfiguration method MDM Settings , MDM_WNSConfiguration class
- MDM_WNSConfiguration class MDM Settings , UpdateConfiguration method
topic_type:
- apiref
api_name:
- MDM_WNSConfiguration.UpdateConfiguration
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

# UpdateConfiguration method of the MDM\_WNSConfiguration class

Updates the Windows Notification Service (WNS) configuration.

## Syntax


```mof
uint32 UpdateConfiguration(
  [in] string ConfigString
);
```



## Parameters

<dl> <dt>

*ConfigString* \[in\]
</dt> <dd>

The WNS configuration string in the format *&lt;AppId&gt;*;*&lt;WNS Package Family Name&gt;*.

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

[**MDM\_WNSConfiguration**](https://msdn.microsoft.com/library/dn610400)
</dt> </dl>

 

 





