---
title: TransmissionMode enumeration
description: Specifies the transmission mode.
ms.assetid: b5722904-24a4-491f-8563-bfb2d5695d86
keywords:
- TransmissionMode enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- TransmissionMode
api_location:
- bdatypes.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TransmissionMode enumeration

Specifies the transmission mode.

## Syntax


```C++
typedef enum TransmissionMode { 
  BDA_XMIT_MODE_NOT_SET         = -1,
  BDA_XMIT_MODE_NOT_DEFINED     = 0,
  BDA_XMIT_MODE_2K,
  BDA_XMIT_MODE_8K,
  BDA_XMIT_MODE_4K,
  BDA_XMIT_MODE_2K_INTERLEAVED,
  BDA_XMIT_MODE_4K_INTERLEAVED,
  BDA_XMIT_MODE_1K,
  BDA_XMIT_MODE_16K,
  BDA_XMIT_MODE_32K,
  BDA_XMIT_MODE_MAX
} TransmissionMode;
```



## Constants

<dl> <dt>

<span id="BDA_XMIT_MODE_NOT_SET"></span><span id="bda_xmit_mode_not_set"></span>**BDA\_XMIT\_MODE\_NOT\_SET**
</dt> <dd>

Transmission mode is not set.

</dd> <dt>

<span id="BDA_XMIT_MODE_NOT_DEFINED"></span><span id="bda_xmit_mode_not_defined"></span>**BDA\_XMIT\_MODE\_NOT\_DEFINED**
</dt> <dd>

Transmission mode is not defined.

</dd> <dt>

<span id="BDA_XMIT_MODE_2K"></span><span id="bda_xmit_mode_2k"></span>**BDA\_XMIT\_MODE\_2K**
</dt> <dd>

Transmission uses 1705 carriers (use a 2K FFT).

</dd> <dt>

<span id="BDA_XMIT_MODE_8K"></span><span id="bda_xmit_mode_8k"></span>**BDA\_XMIT\_MODE\_8K**
</dt> <dd>

Transmission uses 6817 carriers (use an 8K FFT).

</dd> <dt>

<span id="BDA_XMIT_MODE_4K"></span><span id="bda_xmit_mode_4k"></span>**BDA\_XMIT\_MODE\_4K**
</dt> <dd>

Transmission uses "4K" mode. See ETSI EN 300 744, Annex F.

</dd> <dt>

<span id="BDA_XMIT_MODE_2K_INTERLEAVED"></span><span id="bda_xmit_mode_2k_interleaved"></span>**BDA\_XMIT\_MODE\_2K\_INTERLEAVED**
</dt> <dd>

Transmission uses "interleaved 2K" mode.

</dd> <dt>

<span id="BDA_XMIT_MODE_4K_INTERLEAVED"></span><span id="bda_xmit_mode_4k_interleaved"></span>**BDA\_XMIT\_MODE\_4K\_INTERLEAVED**
</dt> <dd>

Transmission uses "interleaved 4K" mode.

</dd> <dt>

<span id="BDA_XMIT_MODE_1K"></span><span id="bda_xmit_mode_1k"></span>**BDA\_XMIT\_MODE\_1K**
</dt> <dd>

Transmission uses a 1K FFT.

</dd> <dt>

<span id="BDA_XMIT_MODE_16K"></span><span id="bda_xmit_mode_16k"></span>**BDA\_XMIT\_MODE\_16K**
</dt> <dd>

Transmission uses a 16K FFT.

</dd> <dt>

<span id="BDA_XMIT_MODE_32K"></span><span id="bda_xmit_mode_32k"></span>**BDA\_XMIT\_MODE\_32K**
</dt> <dd>

Transmission uses a 32K FFT.

</dd> <dt>

<span id="BDA_XMIT_MODE_MAX"></span><span id="bda_xmit_mode_max"></span>**BDA\_XMIT\_MODE\_MAX**
</dt> <dd>

Reserved; do not use.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDVBTLocator::get\_Mode**](/windows/previous-versions/tuner/nf-tuner-idvbtlocator-get_mode?branch=master)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





