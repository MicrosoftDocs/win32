---
title: ModulationType enumeration
description: Specifies the modulation type.
ms.assetid: 0f00553f-c0b1-4ff5-9c92-fe3a1990ef20
keywords:
- ModulationType enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- ModulationType
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- bdatypes.h
api_type:
- HeaderDef
---

# ModulationType enumeration

Specifies the modulation type.

## Syntax


```C++
typedef enum ModulationType { 
  BDA_MOD_NOT_SET           = -1,
  BDA_MOD_NOT_DEFINED       = 0,
  BDA_MOD_16QAM             = 1,
  BDA_MOD_32QAM,
  BDA_MOD_64QAM,
  BDA_MOD_80QAM,
  BDA_MOD_96QAM,
  BDA_MOD_112QAM,
  BDA_MOD_128QAM,
  BDA_MOD_160QAM,
  BDA_MOD_192QAM,
  BDA_MOD_224QAM,
  BDA_MOD_256QAM,
  BDA_MOD_320QAM,
  BDA_MOD_384QAM,
  BDA_MOD_448QAM,
  BDA_MOD_512QAM,
  BDA_MOD_640QAM,
  BDA_MOD_768QAM,
  BDA_MOD_896QAM,
  BDA_MOD_1024QAM,
  BDA_MOD_QPSK,
  BDA_MOD_BPSK,
  BDA_MOD_OQPSK,
  BDA_MOD_8VSB,
  BDA_MOD_16VSB,
  BDA_MOD_ANALOG_AMPLITUDE,
  BDA_MOD_ANALOG_FREQUENCY,
  BDA_MOD_8PSK,
  BDA_MOD_RF,
  BDA_MOD_16APSK,
  BDA_MOD_32APSK,
  BDA_MOD_NBC_QPSK,
  BDA_MOD_NBC_8PSK,
  BDA_MOD_DIRECTV,
  BDA_MOD_ISDB_T_TMCC,
  BDA_MOD_ISDB_S_TMCC,
  BDA_MOD_MAX
} ModulationType;
```



## Constants

<dl> <dt>

<span id="BDA_MOD_NOT_SET"></span><span id="bda_mod_not_set"></span>**BDA\_MOD\_NOT\_SET**
</dt> <dd>

Modulation not set.

</dd> <dt>

<span id="BDA_MOD_NOT_DEFINED"></span><span id="bda_mod_not_defined"></span>**BDA\_MOD\_NOT\_DEFINED**
</dt> <dd>

Modulation not defined.

</dd> <dt>

<span id="BDA_MOD_16QAM"></span><span id="bda_mod_16qam"></span>**BDA\_MOD\_16QAM**
</dt> <dd>

16 symbol Quadrature Amplitude Modulation (QAM)

</dd> <dt>

<span id="BDA_MOD_32QAM"></span><span id="bda_mod_32qam"></span>**BDA\_MOD\_32QAM**
</dt> <dd>

32 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_64QAM"></span><span id="bda_mod_64qam"></span>**BDA\_MOD\_64QAM**
</dt> <dd>

64 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_80QAM"></span><span id="bda_mod_80qam"></span>**BDA\_MOD\_80QAM**
</dt> <dd>

80 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_96QAM"></span><span id="bda_mod_96qam"></span>**BDA\_MOD\_96QAM**
</dt> <dd>

96 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_112QAM"></span><span id="bda_mod_112qam"></span>**BDA\_MOD\_112QAM**
</dt> <dd>

112 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_128QAM"></span><span id="bda_mod_128qam"></span>**BDA\_MOD\_128QAM**
</dt> <dd>

128 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_160QAM"></span><span id="bda_mod_160qam"></span>**BDA\_MOD\_160QAM**
</dt> <dd>

160 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_192QAM"></span><span id="bda_mod_192qam"></span>**BDA\_MOD\_192QAM**
</dt> <dd>

192 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_224QAM"></span><span id="bda_mod_224qam"></span>**BDA\_MOD\_224QAM**
</dt> <dd>

224 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_256QAM"></span><span id="bda_mod_256qam"></span>**BDA\_MOD\_256QAM**
</dt> <dd>

256 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_320QAM"></span><span id="bda_mod_320qam"></span>**BDA\_MOD\_320QAM**
</dt> <dd>

320 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_384QAM"></span><span id="bda_mod_384qam"></span>**BDA\_MOD\_384QAM**
</dt> <dd>

384 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_448QAM"></span><span id="bda_mod_448qam"></span>**BDA\_MOD\_448QAM**
</dt> <dd>

448 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_512QAM"></span><span id="bda_mod_512qam"></span>**BDA\_MOD\_512QAM**
</dt> <dd>

512 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_640QAM"></span><span id="bda_mod_640qam"></span>**BDA\_MOD\_640QAM**
</dt> <dd>

640 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_768QAM"></span><span id="bda_mod_768qam"></span>**BDA\_MOD\_768QAM**
</dt> <dd>

768 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_896QAM"></span><span id="bda_mod_896qam"></span>**BDA\_MOD\_896QAM**
</dt> <dd>

896 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_1024QAM"></span><span id="bda_mod_1024qam"></span>**BDA\_MOD\_1024QAM**
</dt> <dd>

1024 symbol QAM.

</dd> <dt>

<span id="BDA_MOD_QPSK"></span><span id="bda_mod_qpsk"></span>**BDA\_MOD\_QPSK**
</dt> <dd>

Quadrature Phase-Shift Keying (QPSK) modulation.

</dd> <dt>

<span id="BDA_MOD_BPSK"></span><span id="bda_mod_bpsk"></span>**BDA\_MOD\_BPSK**
</dt> <dd>

Binary Phase Shift Keying modulation.

</dd> <dt>

<span id="BDA_MOD_OQPSK"></span><span id="bda_mod_oqpsk"></span>**BDA\_MOD\_OQPSK**
</dt> <dd>

Offset QPSK modulation.

</dd> <dt>

<span id="BDA_MOD_8VSB"></span><span id="bda_mod_8vsb"></span>**BDA\_MOD\_8VSB**
</dt> <dd>

8 Vestigial Side-Band modulation.

</dd> <dt>

<span id="BDA_MOD_16VSB"></span><span id="bda_mod_16vsb"></span>**BDA\_MOD\_16VSB**
</dt> <dd>

16 Vestigial Side-Band modulation.

</dd> <dt>

<span id="BDA_MOD_ANALOG_AMPLITUDE"></span><span id="bda_mod_analog_amplitude"></span>**BDA\_MOD\_ANALOG\_AMPLITUDE**
</dt> <dd>

Analog amplitude modulation (AM).

</dd> <dt>

<span id="BDA_MOD_ANALOG_FREQUENCY"></span><span id="bda_mod_analog_frequency"></span>**BDA\_MOD\_ANALOG\_FREQUENCY**
</dt> <dd>

Analog frequency modulation (FM).

</dd> <dt>

<span id="BDA_MOD_8PSK"></span><span id="bda_mod_8psk"></span>**BDA\_MOD\_8PSK**
</dt> <dd>

8-Phase shift keying, including backwards compatible mode.

</dd> <dt>

<span id="BDA_MOD_RF"></span><span id="bda_mod_rf"></span>**BDA\_MOD\_RF**
</dt> <dd>

Analog TV (video standards such as NTSC, PAL, and SECAM).

</dd> <dt>

<span id="BDA_MOD_16APSK"></span><span id="bda_mod_16apsk"></span>**BDA\_MOD\_16APSK**
</dt> <dd>

DVB-S2 modulation 16-level APSK

</dd> <dt>

<span id="BDA_MOD_32APSK"></span><span id="bda_mod_32apsk"></span>**BDA\_MOD\_32APSK**
</dt> <dd>

DVB-S2 modulation 32-level APSK

</dd> <dt>

<span id="BDA_MOD_NBC_QPSK"></span><span id="bda_mod_nbc_qpsk"></span>**BDA\_MOD\_NBC\_QPSK**
</dt> <dd>

Non-backwards compatible QPSK.

</dd> <dt>

<span id="BDA_MOD_NBC_8PSK"></span><span id="bda_mod_nbc_8psk"></span>**BDA\_MOD\_NBC\_8PSK**
</dt> <dd>

Non-backwards compatible 8-phase shift keying.

</dd> <dt>

<span id="BDA_MOD_DIRECTV"></span><span id="bda_mod_directv"></span>**BDA\_MOD\_DIRECTV**
</dt> <dd>

DIRECTV DSS.

</dd> <dt>

<span id="BDA_MOD_ISDB_T_TMCC"></span><span id="bda_mod_isdb_t_tmcc"></span>**BDA\_MOD\_ISDB\_T\_TMCC**
</dt> <dd>

Automatic demodulation by Transmission and Multiplexing Configuration Control (TMCC) signal for ISDB-T.

</dd> <dt>

<span id="BDA_MOD_ISDB_S_TMCC"></span><span id="bda_mod_isdb_s_tmcc"></span>**BDA\_MOD\_ISDB\_S\_TMCC**
</dt> <dd>

Automatic demodulation by TMCC signal for ISDB-S.

</dd> <dt>

<span id="BDA_MOD_MAX"></span><span id="bda_mod_max"></span>**BDA\_MOD\_MAX**
</dt> <dd>

Reserved; do not use.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[**ILocator::get\_Modulation**](ilocator-get-modulation.md)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





