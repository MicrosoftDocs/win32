---
description: The ResetCounter method resets the error and warning counters.
ms.assetid: 5bc6c939-cd97-40ca-a16c-5227e7f27c76
ms.tgt_platform: multiple
title: ResetCounter method of the CIM_DeviceErrorCounts class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_DeviceErrorCounts.ResetCounter
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# ResetCounter method of the CIM\_DeviceErrorCounts class

The **ResetCounter** method resets the error and warning counters. A method is used so that the logical device's instrumentation, which tabulates the errors and warnings, can also reset its internal processing and counters. In a subclass, the set of possible return codes can be specified using a **ValueMap** qualifier on the method. The strings to which the **ValueMap** contents are translated can also be specified in the subclass as a **Values** array qualifier.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 ResetCounter(
  [in] uint16 SelectedCounter
);
```



## Parameters

<dl> <dt>

*SelectedCounter* \[in\]
</dt> <dd>

Error counter to reset.

<dt>

<span id="All"></span><span id="all"></span><span id="ALL"></span>

**All** (0)


</dt> <dd></dd> <dt>

<span id="Indeterminate_Error_Counter"></span><span id="indeterminate_error_counter"></span><span id="INDETERMINATE_ERROR_COUNTER"></span>

**Indeterminate Error Counter** (1)


</dt> <dd></dd> <dt>

<span id="Critical_Error_Counter"></span><span id="critical_error_counter"></span><span id="CRITICAL_ERROR_COUNTER"></span>

**Critical Error Counter** (2)


</dt> <dd></dd> <dt>

<span id="Major_Error_Counter"></span><span id="major_error_counter"></span><span id="MAJOR_ERROR_COUNTER"></span>

**Major Error Counter** (3)


</dt> <dd></dd> <dt>

<span id="Minor_Error_Counter"></span><span id="minor_error_counter"></span><span id="MINOR_ERROR_COUNTER"></span>

**Minor Error Counter** (4)


</dt> <dd></dd> <dt>

<span id="Warning_Counter"></span><span id="warning_counter"></span><span id="WARNING_COUNTER"></span>

**Warning Counter** (5)


</dt> <dd></dd> </dl> </dd> </dl>

## Return value

Returns 0 (zero) if successful, 1 (one) if not supported, and any other value if an error occurred.

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

[CIM\_DeviceErrorCounts](resetcounter-method-in-class-cim-deviceerrorcounts.md)
</dt> <dt>

[**CIM\_DeviceErrorCounts**](cim-deviceerrorcounts.md)
</dt> </dl>

 

