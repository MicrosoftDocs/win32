---
title: SILO\_DRIVER\_CAPABILITIES structure
description: This structure is used to specify the capabilities and support for IOCTL redirection of a storage silo driver. SILO\_DRIVER\_CAPABILITIES is included in the system buffer of an IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES request.
ms.assetid: E2CD35A6-0FF2-4ABA-850E-12683C5F0D8D
keywords:
- SILO_DRIVER_CAPABILITIES structure Storage Devices
- PSILO_DRIVER_CAPABILITIES structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SILO_DRIVER_CAPABILITIES
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SILO\_DRIVER\_CAPABILITIES structure

This structure is used to specify the capabilities and support for IOCTL redirection of a storage silo driver. **SILO\_DRIVER\_CAPABILITIES** is included in the system buffer of an [**IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES**](ioctl-ehstor-driver-report-capabilities.md) request.

## Syntax


```C++
typedef struct _SILO_DRIVER_CAPABILITIES {
  ULONG StructSize;
  ULONG Capabilities;
  ULONG MaxLbaFilterCount;
  ULONG RedirectedIoctlListCount;
  ULONG RedirectedIoctlListOffset;
} SILO_DRIVER_CAPABILITIES, *PSILO_DRIVER_CAPABILITIES;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of this structure. This is set to **sizeof**(SILO\_DRIVER\_CAPABILITIES).

</dd> <dt>

**Capabilities**
</dt> <dd>

Capability flags for the silo driver. This is a bitwise OR combination of the following.



| Value                                                                                                                                                                                                        | Meaning                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <span id="CAP_ON_DEMAND_AUTHENTICATION"></span><span id="cap_on_demand_authentication"></span><dl> <dt>**CAP\_ON\_DEMAND\_AUTHENTICATION**</dt> </dl> | The silo driver supports on-demand authentication and unauthentication.<br/> |
| <span id="CAP_BANDING_SUPPORT"></span><span id="cap_banding_support"></span><dl> <dt>**CAP\_BANDING\_SUPPORT**</dt> </dl>                             | The silo driver supports banding of LBA ranges.<br/>                         |



 

</dd> <dt>

**MaxLbaFilterCount**
</dt> <dd>

Maximum number of LBA filter entries the silo driver can provide in a [**IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE**](ioctl-ehstor-driver-update-lba-filter-table.md) request.

</dd> <dt>

**RedirectedIoctlListCount**
</dt> <dd>

The number of redirected IOCTLs in the list following this structure.

</dd> <dt>

**RedirectedIoctlListOffset**
</dt> <dd>

The offset of the redirected IOCTL list from the beginning of this structure. This will typically be **sizeof**(SILO\_DRIVER\_CAPABILITIES).

</dd> </dl>

## Remarks

To support receiving [**IOCTL\_EHSTOR\_DRIVER\_PERFORM\_AUTHZ**](ioctl-ehstor-driver-perform-authz.md) from the enhanced storage class driver, a silo driver must set **CAP\_ON\_DEMAND\_AUTHENTICATION** in **Capabilities**. Also, to support sending [**IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE**](ioctl-ehstor-driver-update-lba-filter-table.md), a silo driver must set **CAP\_BANDING\_SUPPORT** in **Capabilities**.

To receive band management requests from the enhanced storage class driver, a silo driver must register a list of IOCTL codes it wants to receive. The redirected IOCTL list is an array of **ULONG** IOCTL codes with a length of **RedirectedIoctlListCount**. This list is included with the **SILO\_DRIVER\_CAPABILITIES** structure in the system buffer. The list is located in the system buffer following **SILO\_DRIVER\_CAPABILITIES** at the offset indicated by **RedirectedIoctlListOffset**.

## Requirements



|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                     |
| Header<br/>  | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_DRIVER\_PERFORM\_AUTHZ**](ioctl-ehstor-driver-perform-authz.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES**](ioctl-ehstor-driver-report-capabilities.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE**](ioctl-ehstor-driver-update-lba-filter-table.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SILO_DRIVER_CAPABILITIES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






