---
description: The SetPowerState method of the CIM\_InfraredController class sets the desired power state for a logical device and when a device should be put into that state.
ms.assetid: dce688f3-b7c2-4e43-a26f-7318ce0011b8
ms.tgt_platform: multiple
title: SetPowerState method of the CIM_InfraredController class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_InfraredController.SetPowerState
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# SetPowerState method of the CIM\_InfraredController class

The **SetPowerState** method of the CIM\_InfraredController class sets the desired power state for a logical device and when a device should be put into that state. In a subclass, the set of possible return codes should be specified by using a **ValueMap** qualifier on the method. The strings to which the **ValueMap** contents are translated should also be specified in the subclass as a **Values** array qualifier. This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

## Syntax


```mof
uint32 SetPowerState(
  [in] uint16   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

A **ValueMap** value that specifies the desired power state for the logical device.

<dt>

1
</dt> <dd>

Full power.

</dd> <dt>

2
</dt> <dd>

Power save   low-power mode.

</dd> <dt>

3
</dt> <dd>

Power save   standby.

</dd> <dt>

4
</dt> <dd>

Power save   other.

</dd> <dt>

5
</dt> <dd>

Power cycle.

</dd> <dt>

6
</dt> <dd>

Power off.

</dd> </dl> </dd> <dt>

*Time* \[in\]
</dt> <dd>

Specifies when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received). When the *PowerState* parameter is equal to 5 ("Power Cycle"), the *Time* parameter indicates when the device should power on again. Power-off is immediate.

</dd> </dl>

## Return value

Returns 0 (zero) if successful, 1 (one) if the specified *PowerState* and *Time* request is not supported, and another value if any other error occurred.

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

[CIM\_InfraredController](setpowerstate-method-in-class-cim-infraredcontroller.md)
</dt> <dt>

[**CIM\_InfraredController**](cim-infraredcontroller.md)
</dt> </dl>

 

 




