---
description: The SetSpeed method requests that the fan speed be set to the value specified in the method's input parameter.
ms.assetid: 7dd1cd57-66c5-4b50-9a73-31caf0b824e6
ms.tgt_platform: multiple
title: SetSpeed method of the CIM_Fan class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Fan.SetSpeed
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetSpeed method of the CIM\_Fan class

The **SetSpeed** method requests that the fan speed be set to the value specified in the method's input parameter.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 SetSpeed(
  [in] uint64 DesiredSpeed
);
```



## Parameters

<dl> <dt>

*DesiredSpeed* \[in\]
</dt> <dd>

Requested fan speed, in revolutions per minute.

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

[CIM\_Fan](setspeed-method-in-class-cim-fan.md)
</dt> <dt>

[**CIM\_Fan**](cim-fan.md)
</dt> </dl>

 

