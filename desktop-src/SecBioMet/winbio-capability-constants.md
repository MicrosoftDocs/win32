---
title: WINBIO_CAPABILITY Constants (Winbio\_types.h)
description: Fingerprint sensor sub types.
ms.assetid: D447273E-2A02-484E-B0E4-69FEADD15797
topic_type:
- apiref
api_name:
- WINBIO_CAPABILITY_SENSOR
- WINBIO_CAPABILITY_MATCHING
- WINBIO_CAPABILITY_DATABASE
- WINBIO_CAPABILITY_PROCESSING
- WINBIO_CAPABILITY_ENCRYPTION
- WINBIO_CAPABILITY_NAVIGATION
- WINBIO_CAPABILITY_INDICATOR
- WINBIO_CAPABILITY_VIRTUAL_SENSOR
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_CAPABILITY Constants

The following fingerprint sensor sub types are **WINBIO\_CAPABILITIES** values that can be used as a bitmask for the *Capabilities* parameter of the [**WINBIO\_UNIT\_SCHEMA**](winbio-unit-schema.md) structure. These refer to the onboard sensor capabilities.




| Constant/value | Description | 
|----------------|-------------|
| <span id="WINBIO_CAPABILITY_SENSOR"></span><span id="winbio_capability_sensor"></span><dl><dt><strong>WINBIO_CAPABILITY_SENSOR</strong></dt><dt>0x00000001</dt></dl> | The sensor can capture biometric data.<br /> | 
| <span id="WINBIO_CAPABILITY_MATCHING"></span><span id="winbio_capability_matching"></span><dl><dt><strong>WINBIO_CAPABILITY_MATCHING</strong></dt><dt>0x00000002</dt></dl> | The sensor can match biometric data to an identity.<br /> | 
| <span id="WINBIO_CAPABILITY_DATABASE"></span><span id="winbio_capability_database"></span><dl><dt><strong>WINBIO_CAPABILITY_DATABASE</strong></dt><dt>0x00000004</dt></dl> | The sensor contains an onboard database.<br /> | 
| <span id="WINBIO_CAPABILITY_PROCESSING"></span><span id="winbio_capability_processing"></span><dl><dt><strong>WINBIO_CAPABILITY_PROCESSING</strong></dt><dt>0x00000008</dt></dl> | The sensor can perform biometric processing.<br /> | 
| <span id="WINBIO_CAPABILITY_ENCRYPTION"></span><span id="winbio_capability_encryption"></span><dl><dt><strong>WINBIO_CAPABILITY_ENCRYPTION</strong></dt><dt>0x00000010</dt></dl> | The sensor can encrypt biometric data.<br /> | 
| <span id="WINBIO_CAPABILITY_NAVIGATION"></span><span id="winbio_capability_navigation"></span><dl><dt><strong>WINBIO_CAPABILITY_NAVIGATION</strong></dt><dt>0x00000020</dt></dl> | The sensor can act as a mouse pad. This is currently not supported.<br /> | 
| <span id="WINBIO_CAPABILITY_INDICATOR"></span><span id="winbio_capability_indicator"></span><dl><dt><strong>WINBIO_CAPABILITY_INDICATOR</strong></dt><dt>0x00000040</dt></dl> | The sensor contains an indicator light.<br /> | 
| <span id="WINBIO_CAPABILITY_VIRTUAL_SENSOR"></span><span id="winbio_capability_virtual_sensor"></span><dl><dt><strong>WINBIO_CAPABILITY_VIRTUAL_SENSOR</strong></dt><dt>0x00000080</dt></dl> | The sensor adapter manages its own connection to the biometric hardware.<br /><blockquote>[!Note]<br />This constant applies only for Windows 10 and later.</blockquote><br /> | 




## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                                                                                  |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h for client applications or Winbio\_adapters.h for adapters)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Constants](client-application-constants.md)
</dt> <dt>

[**WINBIO\_UNIT\_SCHEMA**](winbio-unit-schema.md)
</dt> </dl>

 

 





