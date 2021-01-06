---
description: The Invoke method of the CIM\_Check class evaluates a particular check.
ms.assetid: cf1adeb2-f8a2-4f84-978f-e801bce104ac
ms.tgt_platform: multiple
title: Invoke method of the CIM_Check class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Check.Invoke
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Invoke method of the CIM\_Check class

The **Invoke** method of the [**CIM\_Check**](cim-check.md) class evaluates a particular check.

For more information about how the method evaluates a particular check in a CIM context, see the non-abstract [**CIM\_Check**](cim-check.md) subclasses.

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

Returns a value of 0 (zero) on success, 1 (one) if the method is not supported, and any other number to indicate an error.

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

[**CIM\_Check**](invoke-method-in-class-cim-check.md)
</dt> <dt>

[**CIM\_Check**](cim-check.md)
</dt> </dl>

 

