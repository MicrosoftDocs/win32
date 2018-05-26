---
Description: The Invoke method of the CIM\_FileAction class takes a particular action. Details of how the method performs the action are implementation specific. This method is inherited from CIM\_Action.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7514d67-4141-4d1a-bdfd-83aa062291aa
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Invoke method of the CIM\_FileAction class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Invoke method of the CIM\_FileAction class

The **Invoke** method of the [**CIM\_FileAction**](cim-fileaction.md) class takes a particular action. Details of how the method performs the action are implementation specific. This method is inherited from [**CIM\_Action**](cim-action.md).

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Invoke();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 (zero) on success, 1 (one) if the method is not supported, and any other number to indicate an error.

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

[CIM\_FileAction](invoke-method-in-class-cim-fileaction.md)
</dt> <dt>

[**CIM\_FileAction**](cim-fileaction.md)
</dt> </dl>

 

 




