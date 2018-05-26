---
title: GetManifestVersion method of the PS\_NetworkControllerNode class
description: Returns the Network Controller cluster and application version defined in their template manifests.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e844e5ef-04df-4bef-8ec9-f7304c76e4c6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetManifestVersion method
- GetManifestVersion method, PS_NetworkControllerNode class
- PS_NetworkControllerNode class, GetManifestVersion method
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode.GetManifestVersion
api_location:
- NCServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetManifestVersion method of the PS\_NetworkControllerNode class

Returns the Network Controller cluster and application version defined in their template manifests.

## Syntax


```mof
uint32 GetManifestVersion(
  [out] NetworkControllerManifestVersion NCManifestVersion
);
```



## Parameters

<dl> <dt>

*NCManifestVersion* \[out\]
</dt> <dd>

On success, returns a [**NetworkControllerManifestVersion**](networkcontrollermanifestversion.md) embedded instance containing the network controller cluster manifest version.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkControllerNode**](ps-networkcontrollernode.md)
</dt> </dl>

 

 





