---
Description: Brings a new computer system into a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 26d9428e-99de-4dcb-96ed-d773f28e015a
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: AddNode method of the CIM\_ClusteringService class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddNode method of the CIM\_ClusteringService class

The **AddNode** method brings a new computer system into a cluster. The node to be added is specified as a parameter to the method.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 AddNode(
  [in] CIM_ComputerSystem REF CS
);
```



## Parameters

<dl> <dt>

*CS* \[in\]
</dt> <dd>

Reference to the computer system to add to the cluster.

</dd> </dl>

## Return value

Returns a value of 0 (zero) on success, 1 (one) if the operation is not supported, and any other number to indicate an error.

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

[**CIM\_ClusteringService**](addnode-method-in-class-cim-clusteringservice.md)
</dt> <dt>

[**CIM\_ClusteringService**](cim-clusteringservice.md)
</dt> </dl>

 

 




