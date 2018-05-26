---
title: KS\_CC\_SUBSTREAM
description: The KS\_CC\_SUBSTREAM constants specify the various services that are available on line 21 of the vertical blanking interval (VBI).
ms.assetid: 1a55a9b1-6784-4a29-93aa-95aadaf6fb7e
topic_type:
- apiref
api_name:
- KS_CC_SUBSTREAM_SERVICE_CC1
- KS_CC_SUBSTREAM_SERVICE_CC2
- KS_CC_SUBSTREAM_SERVICE_T1
- KS_CC_SUBSTREAM_SERVICE_T2
- KS_CC_SUBSTREAM_SERVICE_CC3
- KS_CC_SUBSTREAM_SERVICE_CC4
- KS_CC_SUBSTREAM_SERVICE_T3
- KS_CC_SUBSTREAM_SERVICE_T4
- KS_CC_SUBSTREAM_SERVICE_XDS
- KS_CC_SUBSTREAM_FIELD1_MASK
- KS_CC_SUBSTREAM_FIELD2_MASK
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# KS\_CC\_SUBSTREAM

The **KS\_CC\_SUBSTREAM** constants specify the various services that are available on line 21 of the vertical blanking interval (VBI).



| Constant/value                                                                                                                                                                                                                                                         | Description                                      |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------|
| <span id="KS_CC_SUBSTREAM_SERVICE_CC1"></span><span id="ks_cc_substream_service_cc1"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_SERVICE\_CC1**</dt> <dt>0x0001</dt> </dl> | CC1 (caption channel)<br/>                 |
| <span id="KS_CC_SUBSTREAM_SERVICE_CC2"></span><span id="ks_cc_substream_service_cc2"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_SERVICE\_CC2**</dt> <dt>0x0002</dt> </dl> | CC2 (caption channel)<br/>                 |
| <span id="KS_CC_SUBSTREAM_SERVICE_T1"></span><span id="ks_cc_substream_service_t1"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_SERVICE\_T1**</dt> <dt>0x0004</dt> </dl>    | T1 (text channel)<br/>                     |
| <span id="KS_CC_SUBSTREAM_SERVICE_T2"></span><span id="ks_cc_substream_service_t2"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_SERVICE\_T2**</dt> <dt>0x0008</dt> </dl>    | T2 (text channel)<br/>                     |
| <span id="KS_CC_SUBSTREAM_SERVICE_CC3"></span><span id="ks_cc_substream_service_cc3"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_SERVICE\_CC3**</dt> <dt>0x0100</dt> </dl> | CC3 (caption channel)<br/>                 |
| <span id="KS_CC_SUBSTREAM_SERVICE_CC4"></span><span id="ks_cc_substream_service_cc4"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_SERVICE\_CC4**</dt> <dt>0x0200</dt> </dl> | CC4 (caption channel)<br/>                 |
| <span id="KS_CC_SUBSTREAM_SERVICE_T3"></span><span id="ks_cc_substream_service_t3"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_SERVICE\_T3**</dt> <dt>0x0400</dt> </dl>    | T3 (text channel)<br/>                     |
| <span id="KS_CC_SUBSTREAM_SERVICE_T4"></span><span id="ks_cc_substream_service_t4"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_SERVICE\_T4**</dt> <dt>0x0800</dt> </dl>    | T4 (text channel)<br/>                     |
| <span id="KS_CC_SUBSTREAM_SERVICE_XDS"></span><span id="ks_cc_substream_service_xds"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_SERVICE\_XDS**</dt> <dt>0x1000</dt> </dl> | Extended Data Services (XDS)<br/>          |
| <span id="KS_CC_SUBSTREAM_FIELD1_MASK"></span><span id="ks_cc_substream_field1_mask"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_FIELD1\_MASK**</dt> <dt>0x000F</dt> </dl> | Bitmask to filter field 1 substreams.<br/> |
| <span id="KS_CC_SUBSTREAM_FIELD2_MASK"></span><span id="ks_cc_substream_field2_mask"></span><dl> <dt>**KS\_CC\_SUBSTREAM\_FIELD2\_MASK**</dt> <dt>0x1F00</dt> </dl> | Bitmask to filter field 2 substreams<br/>  |



## Remarks

Include Ks.h before Ksmedia.h.

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ksmedia.h</dt> </dl> |



## See also

<dl> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





