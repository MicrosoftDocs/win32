---
description: The Reset method of the CIM\_VideoController class requests a reset of the logical device.
ms.assetid: 4dab954d-ed0f-4620-b5a8-7e55185d0b7b
ms.tgt_platform: multiple
title: Reset method of the CIM_VideoController class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VideoController.Reset
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Reset method of the CIM\_VideoController class

The **Reset** method of the CIM\_VideoController class requests a reset of the logical device. This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

## Return value

Returns 0 (zero) if the request was successfully executed, 1 (one) if the request is not supported, and some other value if an error occurred.

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

[CIM\_VideoController](reset-method-in-class-cim-videocontroller.md)
</dt> <dt>

[**CIM\_VideoController**](cim-videocontroller.md)
</dt> </dl>

 

 




