---
title: CDROM\_OPC\_INFO\_TYPE enumeration
description: The CDROM\_OPC\_INFO\_TYPE enumeration is a member of the CDROM\_SIMPLE\_OPC\_INFO structure. It defines the Optimum Power Calibration (OPC) request that is used as input to the IOCTL\_CDROM\_SEND\_OPC\_INFORMATION I/O control request.
ms.assetid: 447D225C-4B73-4567-81E3-950EBC802F84
keywords:
- CDROM_OPC_INFO_TYPE enumeration Storage Devices
- PCDROM_OPC_INFO_TYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_OPC_INFO_TYPE
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# CDROM\_OPC\_INFO\_TYPE enumeration

The **CDROM\_OPC\_INFO\_TYPE** enumeration is a member of the [**CDROM\_SIMPLE\_OPC\_INFO**](cdrom-simple-opc-info.md) structure. It defines the Optimum Power Calibration (OPC) request that is used as input to the [**IOCTL\_CDROM\_SEND\_OPC\_INFORMATION**](ioctl-cdrom-send-opc-information.md) I/O control request.

## Syntax


```C++
typedef enum _CDROM_OPC_INFO_TYPE { 
  SimpleOpcInfo  = 1
} CDROM_OPC_INFO_TYPE, *PCDROM_OPC_INFO_TYPE;
```



## Constants

<dl> <dt>

<span id="SimpleOpcInfo"></span><span id="simpleopcinfo"></span><span id="SIMPLEOPCINFO"></span>**SimpleOpcInfo**
</dt> <dd>

Specifies the wrapper for the SEND OPC INFORMATION command from the Multimedia Commands (MMC) specification.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_SIMPLE\_OPC\_INFO**](cdrom-simple-opc-info.md)
</dt> <dt>

[**IOCTL\_CDROM\_SEND\_OPC\_INFORMATION**](ioctl-cdrom-send-opc-information.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_OPC_INFO_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






