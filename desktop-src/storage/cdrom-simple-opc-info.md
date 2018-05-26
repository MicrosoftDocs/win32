---
title: CDROM\_SIMPLE\_OPC\_INFO structure
description: The CDROM\_SIMPLE\_OPC\_INFO structure is the only input for the IOCTL\_CDROM\_SEND\_OPC\_INFORMATION I/O control code.
ms.assetid: CE6D2C98-C4C3-4D76-B49E-1B9344B88666
keywords:
- CDROM_SIMPLE_OPC_INFO structure Storage Devices
- PCDROM_SIMPLE_OPC_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_SIMPLE_OPC_INFO
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDROM\_SIMPLE\_OPC\_INFO structure

The **CDROM\_SIMPLE\_OPC\_INFO** structure is the only input for the [**IOCTL\_CDROM\_SEND\_OPC\_INFORMATION**](ioctl-cdrom-send-opc-information.md) I/O control code.

## Syntax


```C++
typedef struct _CDROM_SIMPLE_OPC_INFO {
   CDROM_OPC_INFO_TYPE    RequestType;
  BOOLEAN                 Exclude0;
  BOOLEAN                 Exclude1;
} CDROM_SIMPLE_OPC_INFO, *PCDROM_SIMPLE_OPC_INFO;
```



## Members

<dl> <dt>

**RequestType**
</dt> <dd>

The request type defined in the [**CDROM\_OPC\_INFO\_TYPE**](cdrom-opc-info-type.md) enumeration.

</dd> <dt>

**Exclude0**
</dt> <dd>

Exclude layer 0 from OPC.

</dd> <dt>

**Exclude1**
</dt> <dd>

Exclude layer 1 from OPC.

</dd> </dl>

## Remarks

The [**IOCTL\_CDROM\_SEND\_OPC\_INFORMATION**](ioctl-cdrom-send-opc-information.md) IOCTL is a wrapper for the SEND OPC INFORMATION command of the Multimedia Commands (MMC) specification. The **Exclude0** and **Exclude1** fields of the **CDROM\_SIMPLE\_OPC\_INFO** structure map directly to the corresponding SEND OPC INFORMATION fields.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_SEND\_OPC\_INFORMATION**](ioctl-cdrom-send-opc-information.md)
</dt> <dt>

[**CDROM\_OPC\_INFO\_TYPE**](cdrom-opc-info-type.md)
</dt> <dt>

[**CDROM\_SIMPLE\_OPC\_INFO**](cdrom-simple-opc-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_SIMPLE_OPC_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






