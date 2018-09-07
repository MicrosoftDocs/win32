---
Description: The StartService method puts the service in a started state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0f2880ed-1643-4211-8684-12493711b1f8
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: StartService method of the CIM_Service class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Service.StartService
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# StartService method of the CIM\_Service class

The **StartService** method puts the service in a started state.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 StartService();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 (zero) on success, and any other number to indicate an error. In a subclass, the set of possible return codes can be specified by using a **ValueMap** qualifier on the method. The strings to which the **ValueMap** contents are translated can also be specified in the subclass as a **Values** array qualifier.

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

[CIM\_Service](startservice-method-in-class-cim-service.md)
</dt> <dt>

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

 




