---
title: BAND\_MANAGEMENT\_CAPABILITIES structure
description: The BAND\_MANAGEMENT\_CAPABILITIES structure contains the security capabilities available for a storage device. This structure is returned in the system buffer by the IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES request.
ms.assetid: 102C7CEC-B1DD-49F6-AB7F-0CE0A22EBE54
keywords:
- BAND_MANAGEMENT_CAPABILITIES structure Storage Devices
- PBAND_MANAGEMENT_CAPABILITIES structure pointer Storage Devices
topic_type:
- apiref
api_name:
- BAND_MANAGEMENT_CAPABILITIES
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BAND\_MANAGEMENT\_CAPABILITIES structure

The **BAND\_MANAGEMENT\_CAPABILITIES** structure contains the security capabilities available for a storage device. This structure is returned in the system buffer by the [**IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES**](ioctl-ehstor-bandmgmt-query-capabilities.md) request.

## Syntax


```C++
typedef struct _BAND_MANAGEMENT_CAPABILITIES {
  ULONG     StructSize;
  ULONG     Capabilities;
  ULONGLONG KeyProtectionMechanism;
  ULONG     MinAuthKeyLength;
  ULONG     MaxAuthKeyLength;
  ULONG     MaxBandCount;
  ULONG     MaxSimultaneousReencryptionCount;
  ULONG     BandMetadataSize;
} BAND_MANAGEMENT_CAPABILITIES, *PBAND_MANAGEMENT_CAPABILITIES;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of this structure in bytes. Set to **sizeof**(BAND\_MANAGEMENT\_CAPABILITIES).

</dd> <dt>

**Capabilities**
</dt> <dd>

Security capability flags for a storage device. This is a bitwise OR value of the following flags.



| Value                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPS_ACTIVATED"></span><span id="caps_activated"></span><dl> <dt>**CAPS\_ACTIVATED**</dt> </dl>                                         | If set, the capability members of this structure are available. Otherwise, the remaining members of this structure are not valid.<br/>                                                               |
| <span id="CAPS_BANDCROSSING_SUPPORTED"></span><span id="caps_bandcrossing_supported"></span><dl> <dt>**CAPS\_BANDCROSSING\_SUPPORTED**</dt> </dl> | The storage device supports reads and writes across multiple bands. If this flag is not set, single reads or writes spanning multiple bands are divided into multiple IO requests for a device.<br/> |
| <span id="CAPS_SID_SECURED"></span><span id="caps_sid_secured"></span><dl> <dt>**CAPS\_SID\_SECURED**</dt> </dl>                                  | SID authority is secured. If set, the default SID pin cannot be used to modify the security configuration of the storage device.<br/>                                                                |



 

</dd> <dt>

**KeyProtectionMechanism**
</dt> <dd>

The mechanism used to protect the media keys. This member is set to one of the following.



| Value                                                                                                                                                                                                                      | Meaning                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl>                                                                                                                       | Keys are not protected.<br/>                                                                                                                                |
| <span id="MEDIAKEY_PROTECTEDBY_VENDORSCHEME"></span><span id="mediakey_protectedby_vendorscheme"></span><dl> <dt>**MEDIAKEY\_PROTECTEDBY\_VENDORSCHEME**</dt> </dl> | Keys are protected by a vendor-supplied method. Do not use. This option is not supported.<br/>                                                              |
| <span id="MEDIAKEY_PROTECTEDBY_AUTHKEY"></span><span id="mediakey_protectedby_authkey"></span><dl> <dt>**MEDIAKEY\_PROTECTEDBY\_AUTHKEY**</dt> </dl>                | Keys are encrypted by keys derived from band authentication keys. Key derivation results in negligible entropy loss from the band authentication data.<br/> |



 

</dd> <dt>

**MinAuthKeyLength**
</dt> <dd>

The minimum length, in bytes, of the band authentication or erase keys accepted by the storage device.

</dd> <dt>

**MaxAuthKeyLength**
</dt> <dd>

The maximum length, in bytes, of the band authentication or erase keys accepted by the storage device.

</dd> <dt>

**MaxBandCount**
</dt> <dd>

The maximum number of simultaneous bands configured in the storage device. This includes the global band.

</dd> <dt>

**MaxSimultaneousReencryptionCount**
</dt> <dd>

The number of simultaneous band re-encryptions the hardware on the device supports. If this member is 0, hardware-driven band re-encryptions are not supported.

</dd> <dt>

**BandMetadataSize**
</dt> <dd>

The size, in bytes, of the per band metadata store.

</dd> </dl>

## Remarks

If **CAPS\_ACTIVATED** is not set in **Capabilities**, security functionality can be activated with the [**IOCTL\_EHSTOR\_BANDMGMT\_ACTIVATE**](ioctl-ehstor-bandmgmt-activate.md) request.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_ACTIVATE**](ioctl-ehstor-bandmgmt-activate.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES**](ioctl-ehstor-bandmgmt-query-capabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20BAND_MANAGEMENT_CAPABILITIES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






