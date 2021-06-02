---
description: The SetUrgency method sets the desired urgency level for an alarm.
ms.assetid: ac2e7fda-1317-440a-adbd-1ef0844d124c
ms.tgt_platform: multiple
title: SetUrgency method of the CIM_AlarmDevice class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_AlarmDevice.SetUrgency
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetUrgency method of the CIM\_AlarmDevice class

The **SetUrgency** method sets the desired urgency level for an alarm.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 SetUrgency(
  [in] uint16 RequestedUrgency
);
```



## Parameters

<dl> <dt>

*RequestedUrgency* \[in\]
</dt> <dd>

Relative frequency at which the alarm flashes, vibrates, or emits audible tones. The following values are from the **Urgency** property in [**CIM\_AlarmDevice**](cim-alarmdevice.md).

<dt>

0
</dt> <dd>

Unknown.

</dd> <dt>

1
</dt> <dd>

Other.

</dd> <dt>

2
</dt> <dd>

Not supported.

</dd> <dt>

3
</dt> <dd>

Informational.

</dd> <dt>

4
</dt> <dd>

Non-critical.

</dd> <dt>

5
</dt> <dd>

Critical.

</dd> <dt>

6
</dt> <dd>

Unrecoverable.

</dd> </dl> </dd> </dl>

## Return value

Returns a value of 0 (zero) on success, 1 (one) if the requested urgency level is not supported, and any other number to indicate an error.

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

[CIM\_AlarmDevice](seturgency-method-in-class-cim-alarmdevice.md)
</dt> <dt>

[**CIM\_AlarmDevice**](cim-alarmdevice.md)
</dt> </dl>

 

