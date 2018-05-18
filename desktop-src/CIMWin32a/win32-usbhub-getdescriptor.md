---
title: GetDescriptor method of the Win32\_USBHub class
description: The GetDescriptor method returns the USB hub descriptor as specified by the input parameters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4df2821c-686c-466d-9323-7e42243a4296'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetDescriptor method", "GetDescriptor method, Win32_USBHub class", "Win32_USBHub class, GetDescriptor method"]
topic_type:
- apiref
api_name:
- Win32_USBHub.GetDescriptor
api_location:
- CIMWin32.dll
api_type:
- COM
---

# GetDescriptor method of the Win32\_USBHub class

The [**GetDescriptor**](https://msdn.microsoft.com/library/aa390443) method returns the USB hub descriptor as specified by the input parameters.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetDescriptor(
  [in]      uint8  RequestType,
  [in]      uint16 RequestValue,
  [in]      uint16 RequestIndex,
  [in, out] uint16 RequestLength,
  [out]     uint8  Buffer[]
);
```



## Parameters

<dl> <dt>

*RequestType* \[in\]
</dt> <dd>

Bit-mapped identifier for the type of descriptor request and the recipient. For the appropriate values for each bit, see the USB specification.

</dd> <dt>

*RequestValue* \[in\]
</dt> <dd>

Contains the descriptor type in the high byte and the descriptor index (for example, index or offset into the descriptor array) in the low byte. For more information, see the USB specification.

</dd> <dt>

*RequestIndex* \[in\]
</dt> <dd>

Specifies the 2-byte language identifier code used by the USB device when returning string descriptor data. The parameter is typically 0 (zero) for nonstring descriptors. For more information, see the USB specification.

</dd> <dt>

*RequestLength* \[in, out\]
</dt> <dd>

On input, the length (in octets) of the descriptor that should be returned. If this value is less than the actual length of the descriptor, only the requested length is returned. If it is more than the actual length, the actual length is returned.

On output, the length (in octets) of the buffer being returned. If the requested descriptor does not exist, the contents of this parameter are undefined.

</dd> <dt>

*Buffer* \[out\]
</dt> <dd>

Buffer returns the requested descriptor information. If the descriptor does not exist, the contents of the buffer are undefined.

</dd> </dl>

## Return value

Returns a value of 0 (zero) if the USB descriptor is successfully returned, 1 (one) if the request is not supported, and any other number to indicate an error. In a subclass, the set of possible return codes could be specified by using a **ValueMap** qualifier on the method. The strings to which the **mofqualifier** contents are translated can also be specified in the subclass as a **Values** array qualifier.

## Remarks

This method is currently not implemented by WMI. To use this method, you must implement it in your own provider. For more information, see [Providing Data to WMI](https://msdn.microsoft.com/library/aa392893).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_USBHub**](https://msdn.microsoft.com/library/aa388650)
</dt> <dt>

[**Win32\_USBHub**](win32-usbhub.md)
</dt> </dl>

 

 





