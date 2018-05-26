---
title: GetDescriptor method of the CIM\_USBDevice class
description: Retrieves the descriptor for a USB device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: faa4c9c1-1a71-4a31-90b6-57c01ce4dd99
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetDescriptor method
- GetDescriptor method, CIM_USBDevice class
- CIM_USBDevice class, GetDescriptor method
topic_type:
- apiref
api_name:
- CIM_USBDevice.GetDescriptor
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
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



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl>                |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_USBDevice**](cim-usbdevice.md)
</dt> </dl>

 

 





