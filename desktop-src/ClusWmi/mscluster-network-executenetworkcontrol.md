---
title: ExecuteNetworkControl method of the MSCluster\_Network class
description: Executes a control code on the network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a3313db6-40db-41b8-a01c-2405806cf656
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExecuteNetworkControl method
- ExecuteNetworkControl method, MSCluster_Network class
- MSCluster_Network class, ExecuteNetworkControl method
topic_type:
- apiref
api_name:
- MSCluster_Network.ExecuteNetworkControl
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExecuteNetworkControl method of the MSCluster\_Network class

Executes a control code on the network.

## Syntax


```mof
void ExecuteNetworkControl(
  [in]  sint32 ControlCode,
  [in]  uint8  InputBuffer[],
  [out] uint8  OutputBuffer[],
  [out] sint32 OutputBufferSize
);
```



## Parameters

<dl> <dt>

*ControlCode* \[in\]
</dt> <dd>

A cluster control code specifying the operation to be performed. For a list of network control codes, see [Network Control Codes](https://msdn.microsoft.com/library/aa371518).

This corresponds to the *dwControlCode* parameter to the [**ClusterNetworkControl**](https://msdn.microsoft.com/library/aa368967) function listed on the network control code reference pages.

</dd> <dt>

*InputBuffer* \[in\]
</dt> <dd>

An input buffer containing information needed for the operation, or **NULL** if no information is needed.

This corresponds to the *lpInBuffer* parameter to the [**ClusterNetworkControl**](https://msdn.microsoft.com/library/aa368967) function listed on the network control code reference pages.

</dd> <dt>

*OutputBuffer* \[out\]
</dt> <dd>

An output buffer to receive the data resulting from the operation, or **NULL** if no data will be returned.

This corresponds to the *lpOutBuffer* parameter to the [**ClusterNetworkControl**](https://msdn.microsoft.com/library/aa368967) function listed on the network control code reference pages.

</dd> <dt>

*OutputBufferSize* \[out\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

This corresponds to the *cbOutBufferSize* parameter to the [**ClusterNetworkControl**](https://msdn.microsoft.com/library/aa368967) function listed on the network control code reference pages.

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

[**MSCluster\_Network**](mscluster-network.md)
</dt> <dt>

[**ClusterNetworkControl**](https://msdn.microsoft.com/library/aa368967)
</dt> <dt>

[Network Control Codes](https://msdn.microsoft.com/library/aa371518)
</dt> </dl>

 

 





