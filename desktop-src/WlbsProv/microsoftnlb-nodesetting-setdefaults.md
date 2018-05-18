---
title: SetDefaults method of the MicrosoftNLB\_NodeSetting class
description: Resets all of the properties of the MicrosoftNLB\_NodeSetting class to their default values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ee964364-1c6b-4795-840b-aeb97423240d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetDefaults method", "SetDefaults method, MicrosoftNLB_NodeSetting class", "MicrosoftNLB_NodeSetting class, SetDefaults method"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_NodeSetting.SetDefaults
api_location:
- WlbsProv.dll
api_type:
- COM
---

# SetDefaults method of the MicrosoftNLB\_NodeSetting class

Resets all of the properties of the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class to their default values.

## Syntax


```mof
void SetDefaults();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Use the [**LoadAllSettings**](https://msdn.microsoft.com/library/aa371167) method to commit the setting changes to the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md)
</dt> </dl>

 

 





