---
title: GetDescriptor method of the CIM\_USBDevice class
description: Retrieves the descriptor for a USB device.
ms.assetid: a3ac2065-bc7c-4a3c-95ec-3b5014be3917
keywords:
- GetDescriptor method Hyper-V
- GetDescriptor method Hyper-V , CIM_USBDevice class
- CIM_USBDevice class Hyper-V , GetDescriptor method
topic_type:
- apiref
api_name:
- CIM_USBDevice.GetDescriptor
api_location:
- Root\virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetDescriptor method of the CIM\_USBDevice class

Retrieves the descriptor for a USB device.

> [!Note]  
> For more information on USB descriptors, see the *USB Specification*.

 

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

A bitmap that identifies the type of descriptor request and the recipient. The type of request can be standard, class or vendor-specific. The recipient may be device, interface, endpoint or other. See the *USB Specification* for the appropriate values for each bit.

</dd> <dt>

*RequestValue* \[in\]
</dt> <dd>

The descriptor type in the high byte, and the descriptor index, in the low byte. See the *USB Specification* for more information on this parameter.

</dd> <dt>

*RequestIndex* \[in\]
</dt> <dd>

The 2 byte language ID code used by the USB device when returning string descriptor data. The parameter is typically "0" for non-string descriptors. Refer to the USB specification for more information.

</dd> <dt>

*RequestLength* \[in, out\]
</dt> <dd>

The length, in octets, of the descriptor to return. If this value is less than the actual length of the descriptor, only the requested length is returned. If it is more than the actual length, the actual length is returned.

When this method returns, this parameter contains the length, in octets, of the **Buffer** parameter. f the requested Descriptor does not exist, the contents of **RequestLength** are undefined.

</dd> <dt>

*Buffer* \[out\]
</dt> <dd>

A buffer that returns the requested descriptor information. If the descriptor does not exist, the contents of the buffer are undefined.

</dd> </dl>

## Return value

Returns "0" on success, "1" if the request is not supported. Otherwise, returns a WMI error code.

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_USBDevice**](cim-usbdevice.md)
</dt> </dl>

 

 





