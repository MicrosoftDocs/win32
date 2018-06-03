---
title: SetDefaults method of the MicrosoftNLB\_ClusterSetting class
description: Resets all of the properties of the MicrosoftNLB\_ClusterSetting class to their default values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ee90e0ae-5ccb-40bd-874e-e5c93a222af7
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetDefaults method
- SetDefaults method, MicrosoftNLB_ClusterSetting class
- MicrosoftNLB_ClusterSetting class, SetDefaults method
topic_type:
- apiref
api_name:
- MicrosoftNLB_ClusterSetting.SetDefaults
api_location:
- WlbsProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetDefaults method of the MicrosoftNLB\_ClusterSetting class

Resets all of the properties of the [**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md) class to their default values.

## Syntax


```mof
void SetDefaults();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Use the [**LoadAllSettings**](https://msdn.microsoft.com/library/aa371012) method to commit the setting changes to the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> </dl>

 

 





