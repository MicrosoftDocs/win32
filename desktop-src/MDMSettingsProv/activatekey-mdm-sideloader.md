---
title: ActivateKey method of the MDM\_SideLoader class
description: Activates side-loading and installs the product key.
ms.assetid: 13326a90-6e33-4c3b-bca0-9f0a62431be0
keywords:
- ActivateKey method MDM Settings
- ActivateKey method MDM Settings , MDM_SideLoader class
- MDM_SideLoader class MDM Settings , ActivateKey method
topic_type:
- apiref
api_name:
- MDM_SideLoader.ActivateKey
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

# ActivateKey method of the MDM\_SideLoader class

Activates side-loading and installs the product key.

## Syntax


```mof
uint32 ActivateKey(
  [in] string ProductKey
);
```



## Parameters

<dl> <dt>

*ProductKey* \[in\]
</dt> <dd>

The side-loading key.

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

[**MDM\_SideLoader**](https://msdn.microsoft.com/library/dn610395)
</dt> </dl>

 

 





