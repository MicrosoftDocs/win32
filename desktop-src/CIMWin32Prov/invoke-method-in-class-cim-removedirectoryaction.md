---
description: The Invoke method of the CIM\_RemoveDirectoryAction class takes a particular action. The details of how the method performs the action is implementation specific. This method is inherited from CIM\_Action.
ms.assetid: c6a7edcd-aac1-4364-8de5-a16fe2bab107
ms.tgt_platform: multiple
title: Invoke method of the CIM_RemoveDirectoryAction class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_RemoveDirectoryAction.Invoke
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Invoke method of the CIM\_RemoveDirectoryAction class

The **Invoke** method of the [**CIM\_RemoveDirectoryAction**](cim-removedirectoryaction.md) class takes a particular action. The details of how the method performs the action is implementation specific. This method is inherited from [**CIM\_Action**](cim-action.md).

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Invoke();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 (zero) on success, and any other number to indicate an error.

## Remarks

This method is currently not implemented by WMI. To use this method, you must implement it in your own provider.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[CIM\_RemoveDirectoryAction](invoke-method-in-class-cim-removedirectoryaction.md)
</dt> <dt>

[**CIM\_RemoveDirectoryAction**](cim-removedirectoryaction.md)
</dt> </dl>

 

