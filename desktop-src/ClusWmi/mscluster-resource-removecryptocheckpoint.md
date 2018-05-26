---
title: RemoveCryptoCheckpoint method of the MSCluster\_Resource class
description: Removes a crypto key from the list of keys being checkpointed for the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3adf218d-3bb7-48df-83de-10588aae80a3
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveCryptoCheckpoint method
- RemoveCryptoCheckpoint method, MSCluster_Resource class
- MSCluster_Resource class, RemoveCryptoCheckpoint method
topic_type:
- apiref
api_name:
- MSCluster_Resource.RemoveCryptoCheckpoint
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveCryptoCheckpoint method of the MSCluster\_Resource class

Removes a crypto key from the list of keys being checkpointed for the [resource](https://msdn.microsoft.com/library/aa372152).

## Syntax


```mof
void RemoveCryptoCheckpoint(
  [in] string CheckpointName
);
```



## Parameters

<dl> <dt>

*CheckpointName* \[in\]
</dt> <dd>

The Cryptographic Service Provider (CSP) key container to be replicated. The CSP key container must first be created with the CryptoAPI, and the keys in the container must be exportable. The string must specify the CSP provider type, provider name, and key container name using the following syntax:

*Type*\\*Name*\\*Key*

Note that the values must be separated by a backslash (\). The provider type should specify the decimal value of the type, not the constant that represents the value. For example, instead of "PROV\_RSA\_FULL", use "1". The provider name is optional; if the provider name is omitted, the default CSP provider name associated with the specified provider type will be used.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





