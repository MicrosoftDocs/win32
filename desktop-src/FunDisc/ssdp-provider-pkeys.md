---
Description: 'Defines the PKEYs associated with the SSDP Provider.'
ms.assetid: '38decada-12c4-438e-8bfe-7e2b5b8adb44'
title: SSDP Provider PKEYs
---

# SSDP Provider PKEYs

\[Function Discovery is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

SSDP services and devices are quite frequently discovered by the PnP-X Provider. SSDP devices must support many of the PnP-X PKEYs. For more information, see [**PnP-X Provider PKEYs**](pnp-x-provider-pkeys.md).

The following keys are associated with the [SSDP provider](ssdp-provider.md).

<dl> <dt>

<span id="PKEY_SSDP_AltLocationInfo"></span><span id="pkey_ssdp_altlocationinfo"></span><span id="PKEY_SSDP_ALTLOCATIONINFO"></span>**PKEY\_SSDP\_AltLocationInfo**
</dt> <dd> <dl> <dt>



An alternate device location. This value is sent in the AL header of a SSDP packet. The meaning and interpretation of this PKEY may vary by device. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> <dt>

<span id="PKEY_SSDP_DevLifeTime"></span><span id="pkey_ssdp_devlifetime"></span><span id="PKEY_SSDP_DEVLIFETIME"></span>**PKEY\_SSDP\_DevLifeTime**
</dt> <dd> <dl> <dt>



The number of seconds that the SSDP message is valid. This value is sent in the CACHE\_CONTROL header of a SSDP packet. PROPVARIANT type VT\_UI4.


</dt> </dl> </dd> <dt>

<span id="PKEY_SSDP_NetworkInterface"></span><span id="pkey_ssdp_networkinterface"></span><span id="PKEY_SSDP_NETWORKINTERFACE"></span>**PKEY\_SSDP\_NetworkInterface**
</dt> <dd> <dl> <dt>



The GUID of the network interface upon which the device was discovered. PROPVARIANT type VT\_LPWSTR.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>FunctionDiscoveryKeys.h</dt> </dl> |



## See also

<dl> <dt>

[**Key Definitions**](key-definitions.md)
</dt> <dt>

[SSDP provider](ssdp-provider.md)
</dt> </dl>

 

 




