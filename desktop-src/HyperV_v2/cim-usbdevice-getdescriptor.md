---
description: Returns the USBDevice descriptor as specified by the input parameters.
ms.assetid: 89bb8a49-6fca-422c-808d-70ae77aae4c3
title: GetDescriptor method of the CIM_USBDevice class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_USBDevice.GetDescriptor
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetDescriptor method of the CIM_USBDevice class (Hyper-V management)

Returns the USBDevice descriptor as specified by the input parameters.

## Syntax


```mof
uint32 GetDescriptor(
  [in]      uint8  RequestType,
  [in]      uint16 RequestValue,
  [in]      uint16 RequestIndex,
  [in, out] uint16 RequestLength,
  [out]     uint8  Buffer[]
);
```



## Parameters

<dl> <dt>

*RequestType* \[in\]
</dt> <dd>

Bit-map that identifies the type of Descriptor request and the recipient. The type of request may be 'standard', 'class' or 'vendor-specific'. The recipient may be 'device', 'interface', 'endpoint' or 'other'. Refer to the USB Specification for the appropriate values for each bit.

</dd> <dt>

*RequestValue* \[in\]
</dt> <dd>

Contains the Descriptor Type in the high byte and the Descriptor Index (for example, index or offset into the Descriptor array) in the low byte. Refer to the USB Specification for more information.

</dd> <dt>

*RequestIndex* \[in\]
</dt> <dd>

Defines the 2 byte Language ID code used by the USBDevice when returning string Descriptor data. The parameter is typically 0 for non-string Descriptors. Refer to the USB Specification for more information.

</dd> <dt>

*RequestLength* \[in, out\]
</dt> <dd>

On input, contains the length (in octets) of the Descriptor that should be returned. If this value is less than the actual length of the Descriptor, only the requested length will be returned. If it is more than the actual length, the actual length is returned. On output, this parameter is the length, in octets, of the Buffer being returned. If the requested Descriptor does not exist, the contents of this parameter are undefined.

</dd> <dt>

*Buffer* \[out\]
</dt> <dd>

Returns the requested Descriptor information. If the Descriptor does not exist, the contents of the parameter are undefined.

</dd> </dl>

## Return value

Returns a 0 on success; otherwise, returns an error.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_USBDevice**](cim-usbdevice.md)
</dt> </dl>

 

 




