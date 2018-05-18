---
title: Reset method of the Win32\_USBHub class
description: The Reset method of the CIM\_USBHub class requests a reset of the logical device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8650d28e-24f3-45d3-b519-f819f2287022'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Reset method", "Reset method, Win32_USBHub class", "Win32_USBHub class, Reset method"]
topic_type:
- apiref
api_name:
- Win32_USBHub.Reset
api_location:
- CIMWin32.dll
api_type:
- COM
---

# Reset method of the Win32\_USBHub class

The [**Reset**](https://msdn.microsoft.com/library/aa393226) method of the **CIM\_USBHub** class requests a reset of the logical device. This method is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

## Return value

Returns 0 (zero) if the request was successfully executed, 1 (one) if the request is not supported, and some other value if an error occurred.

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

 

 





