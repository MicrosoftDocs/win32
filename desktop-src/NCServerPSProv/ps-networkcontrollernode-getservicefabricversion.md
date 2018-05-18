---
title: GetServiceFabricVersion method of the PS\_NetworkControllerNode class
description: Retrieves the Service Fabric Version.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c70b4c72-0619-4d59-814c-49664362ceab'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetServiceFabricVersion method", "GetServiceFabricVersion method, PS_NetworkControllerNode class", "PS_NetworkControllerNode class, GetServiceFabricVersion method"]
---

# GetServiceFabricVersion method of the PS\_NetworkControllerNode class

Retrieves the Service Fabric Version.

## Syntax


```mof
uint32 GetServiceFabricVersion(
  [out] ServiceFabricVersion ServiceFabricVersion
);
```



## Parameters

<dl> <dt>

*ServiceFabricVersion* \[out\]
</dt> <dd>

A [**ServiceFabricVersion**](servicefabricversion.md) that contains the service fabric version.

</dd> </dl>

## Return value

TBD

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkControllerNode**](ps-networkcontrollernode.md)
</dt> </dl>

 

 





