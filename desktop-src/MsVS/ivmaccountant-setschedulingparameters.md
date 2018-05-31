---
error-parsing-yaml: 
---

# IVMAccountant::SetSchedulingParameters method

The **SetSchedulingParameters** method sets the scheduling parameters for a virtual machine.

## Syntax


```C++
HRESULT SetSchedulingParameters(
  [in] VARIANT reservedSystemCapacity,
  [in] VARIANT maxSystemCapacity,
  [in] long    relativeWeight
);
```



## Parameters

<dl> <dt>

*reservedSystemCapacity* \[in\]
</dt> <dd>

Minimum percentage of system capacity that will always be available to this virtual machine. The minimum value for this parameter is 0, the maximum value depends on the number of host processors. This argument is treated as a floating-point value (that is, VARIANT of type VT\_R8).

</dd> <dt>

*maxSystemCapacity* \[in\]
</dt> <dd>

Maximum percentage of system capacity that can be used by this virtual machine. The minimum value for this parameter is 1, the maximum value depends on the number of host processors. This argument is treated as a floating-point value (that is, VARIANT of type VT\_R8).

</dd> <dt>

*relativeWeight* \[in\]
</dt> <dd>

Number between 1 and 10,000 representing priority of this virtual machine relative to other virtual machines. A higher number indicates a higher priority.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                         | Description                              |
|-----------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt> **E\_INVALIDARG** </dt> </dl>      | A parameter was out of range.<br/> |
| <dl> <dt> **VM\_E\_VM\_UNKNOWN** </dt> </dl> | Unknown virtual machine.<br/>      |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unexpected error occurred.<br/> |



 

## Remarks

The maximum values for *reservedSystemCapacity* and *maxSystemCapacity* depend on the number of processors on the host. For one host processor, the maximum percentage is 100. For two host processors, the maximum percentage is 50. For four host processors, the maximum percentage is 25. The reserve system capacity must be less than or equal to the *maxSystemCapacity*.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccountant**](ivmaccountant.md)
</dt> </dl>

 

 





