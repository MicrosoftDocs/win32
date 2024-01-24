---
description: Verifies whether the referenced physical chassis can be contained by, or inserted into, the physical package.
ms.assetid: 9a1aa1b7-2b95-4887-9d14-e416ff69f9df
ms.tgt_platform: multiple
title: IsCompatible method of the CIM_Chassis class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Chassis.IsCompatible
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# IsCompatible method of the CIM\_Chassis class

The **IsCompatible** method verifies whether the referenced physical chassis can be contained by, or inserted into, the physical package. In a subclass, the set of possible return codes can be specified by using a [**ValueMap**](/windows/desktop/WmiSdk/standard-qualifiers) qualifier on the method. The strings to which the **ValueMap** contents are translated can also be specified in the subclass as a **Values** array qualifier. This method is inherited from [**CIM\_PhysicalPackage**](cim-physicalpackage.md).

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 IsCompatible(
  [in] CIM_PhysicalElement REF ElementToCheck
);
```



## Parameters

<dl> <dt>

*ElementToCheck* \[in\]
</dt> <dd>

Reference to the physical element for which to check compatibility.

</dd> </dl>

## Return value

Returns a value of 0 (zero) on success, 1 (one) if the request is not supported, and any other number to indicate an error.

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

[**CIM\_Chassis**](iscompatible-method-in-class-cim-chassis.md)
</dt> <dt>

[**CIM\_Chassis**](cim-chassis.md)
</dt> </dl>

 

