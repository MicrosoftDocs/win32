---
title: SetPowerState method of the Win32\_USBHub class
description: The SetPowerState method of the CIM\_USBHub class sets the desired power state for a logical device and when a device should be put into that state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9ca54319-7226-4718-a515-3c3839bba640'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetPowerState method", "SetPowerState method, Win32_USBHub class", "Win32_USBHub class, SetPowerState method"]
topic_type:
- apiref
api_name:
- Win32_USBHub.SetPowerState
api_location:
- CIMWin32.dll
api_type:
- COM
---

# SetPowerState method of the Win32\_USBHub class

The [**SetPowerState**](https://msdn.microsoft.com/library/aa393577) method of the **CIM\_USBHub** class sets the desired power state for a logical device and when a device should be put into that state. In a subclass, the set of possible return codes should be specified by using a [**ValueMap**](https://msdn.microsoft.com/library/aa393650) qualifier on the method. The strings to which the **ValueMap** contents are translated should also be specified in the subclass as a **Values** array qualifier. This method is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

## Syntax


```mof
uint32 SetPowerState(
  [in] uint16   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

A [**ValueMap**](https://msdn.microsoft.com/library/aa393650) value that specifies the desired power state for this logical device.

<dt>

1
</dt> <dd>

Full power.

</dd> <dt>

2
</dt> <dd>

Power save — low-power mode.

</dd> <dt>

3
</dt> <dd>

Power save — standby.

</dd> <dt>

4
</dt> <dd>

Power save — other.

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

This method is currently not implemented by WMI. To use this method, you must implement it in your own provider. For more information, see [Providing Data to WMI](https://msdn.microsoft.com/library/aa392893).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_USBHub**](https://msdn.microsoft.com/library/aa388650)
</dt> <dt>

[**Win32\_USBHub**](win32-usbhub.md)
</dt> </dl>

 

 





