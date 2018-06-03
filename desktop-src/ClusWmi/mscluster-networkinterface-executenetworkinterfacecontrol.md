---
title: ExecuteNetworkInterfaceControl method of the MSCluster\_NetworkInterface class
description: Executes a control code on the network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bc48ade4-b049-435a-97c7-65d93dd72525
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExecuteNetworkInterfaceControl method
- ExecuteNetworkInterfaceControl method, MSCluster_NetworkInterface class
- MSCluster_NetworkInterface class, ExecuteNetworkInterfaceControl method
topic_type:
- apiref
api_name:
- MSCluster_NetworkInterface.ExecuteNetworkInterfaceControl
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExecuteNetworkInterfaceControl method of the MSCluster\_NetworkInterface class

Executes a control code on the network interface.

## Syntax


```mof
void ExecuteNetworkInterfaceControl(
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

A control code specifying the operation to be performed. For a list of network interface control codes, see [Network Interface Control Codes](https://msdn.microsoft.com/library/aa371723).

</dd> <dt>

*InputBuffer* \[in\]
</dt> <dd>

An input buffer containing information needed for the operation, or **NULL** if no information is needed.

This corresponds to the *lpInBuffer* parameter to the [**ClusterNetInterfaceControl**](https://msdn.microsoft.com/library/aa368846) function listed on the network interface control code reference pages.

</dd> <dt>

*OutputBuffer* \[out\]
</dt> <dd>

An output buffer to receive the data resulting from the operation, or **NULL** if no data will be returned.

This corresponds to the *lpOutBuffer* parameter to the [**ClusterNetInterfaceControl**](https://msdn.microsoft.com/library/aa368846) function listed on the network interface control code reference pages.

</dd> <dt>

*OutputBufferSize* \[out\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

This corresponds to the *cbOutBufferSize* parameter to the [**ClusterNetInterfaceControl**](https://msdn.microsoft.com/library/aa368846) function listed on the network interface control code reference pages.

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

[**MSCluster\_NetworkInterface**](mscluster-networkinterface.md)
</dt> <dt>

[**ClusterNetInterfaceControl**](https://msdn.microsoft.com/library/aa368846)
</dt> <dt>

[Network Interface Control Codes](https://msdn.microsoft.com/library/aa371723)
</dt> </dl>

 

 





