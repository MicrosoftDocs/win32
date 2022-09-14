---
description: Windows Portable Devices supports the following network association properties.
ms.assetid: 5e1b3e8d-9620-4b68-b7ef-1642404ed6ed
title: Network Association Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Network
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Network Association Properties

Windows Portable Devices supports the following network association properties.



| Property                                                  | VarType                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_NETWORK\_ASSOCIATION\_HOST\_NETWORK\_IDENTIFIERS** | **VT\_VECTOR \| VT\_UI1** | The list of EUI-64 host identifiers valid for this association.This is an array of bytes that contains an integral number of EUI-64 physical network addresses. These EUI-64 values are the physical network addresses available on the host at Network Association time. If the host has MAC-48 physical network addresses (typical of IPv4 networks), each MAC-48 address will be encoded in the EUI-64 address as the two halves of the MAC-48 address separated by FF-FF.<br/> |
| **WPD\_NETWORK\_ASSOCIATION\_X509V3SEQUENCE**             | **VT\_VECTOR \| VT\_UI1** | The sequence of X.509 v3 certificates to be provided for TLS server authentication.                                                                                                                                                                                                                                                                                                                                                                                                      |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




