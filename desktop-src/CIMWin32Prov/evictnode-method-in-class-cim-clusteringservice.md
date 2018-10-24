---
Description: The EvictNode method removes a computer system from a cluster. The node to be evicted is specified as a parameter to the method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4691d536-ade3-4a02-bc28-e31ebaf5d9e4
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: EvictNode method of the CIM_ClusteringService class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ClusteringService.EvictNode
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# EvictNode method of the CIM\_ClusteringService class

The **EvictNode** method removes a computer system from a cluster. The node to be evicted is specified as a parameter to the method.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 EvictNode(
  [in] CIM_ComputerSystem REF CS
);
```



## Parameters

<dl> <dt>

*CS* \[in\]
</dt> <dd>

Reference to the computer system to remove from the cluster.

</dd> </dl>

## Return value

Returns 0 (zero) if the computer system is successfully evicted, 1 (one) if the method is not supported, and any other number if an error occurred.

## Remarks

This method is currently not implemented by WMI. To use this method, you must implement it in your own provider.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ClusteringService**](evictnode-method-in-class-cim-clusteringservice.md)
</dt> <dt>

[**CIM\_ClusteringService**](cim-clusteringservice.md)
</dt> </dl>

 

 




