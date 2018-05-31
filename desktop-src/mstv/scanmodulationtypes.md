---
title: ScanModulationTypes enumeration
description: The ScanModulationTypes enumeration type specifies the modulation type.
ms.assetid: 20101fa7-b943-4737-a6ec-a952bdf25196
keywords:
- ScanModulationTypes enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- ScanModulationTypes
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- Bdatypes.h
api_type:
- HeaderDef
---

# ScanModulationTypes enumeration

The **ScanModulationTypes** enumeration type specifies the modulation type.

## Syntax


```C++
typedef enum tagScanModulationTypes { 
  BDA_SCAN_MOD_16QAM                           = 0x00000001,
  BDA_SCAN_MOD_32QAM                           = 0x00000002,
  BDA_SCAN_MOD_64QAM                           = 0x00000004,
  BDA_SCAN_MOD_80QAM                           = 0x00000008,
  BDA_SCAN_MOD_96QAM                           = 0x00000010,
  BDA_SCAN_MOD_112QAM                          = 0x00000020,
  BDA_SCAN_MOD_128QAM                          = 0x00000040,
  BDA_SCAN_MOD_160QAM                          = 0x00000080,
  BDA_SCAN_MOD_192QAM                          = 0x00000100,
  BDA_SCAN_MOD_224QAM                          = 0x00000200,
  BDA_SCAN_MOD_256QAM                          = 0x00000400,
  BDA_SCAN_MOD_320QAM                          = 0x00000800,
  BDA_SCAN_MOD_384QAM                          = 0x00001000,
  BDA_SCAN_MOD_448QAM                          = 0x00002000,
  BDA_SCAN_MOD_512QAM                          = 0x00004000,
  BDA_SCAN_MOD_640QAM                          = 0x00008000,
  BDA_SCAN_MOD_768QAM                          = 0x00010000,
  BDA_SCAN_MOD_896QAM                          = 0x00020000,
  BDA_SCAN_MOD_1024QAM                         = 0x00040000,
  BDA_SCAN_MOD_QPSK                            = 0x00080000,
  BDA_MOD_BPSK                                 = 0x00100000,
  BDA_MOD_OQPSK                                = 0x00200000,
  BDA_SCAN_MOD_8VSB                            = 0x00400000,
  BDA_MOD_16VSB                                = 0x00800000,
  BDA_SCAN_MOD_AM_RADIO                        = 0x01000000,
  BDA_SCAN_MOD_FM_RADIO                        = 0x02000000,
  BDA_SCAN_MOD_8PSK                            = 0x04000000,
  BDA_SCAN_MOD_RF                              = 0x08000000,
  ScanModulationTypesMask_MCE_DigitalCable     = BDA_MOD_64QAM | BDA_MOD_256QAM,
  ScanModulationTypesMask_MCE_TerrestrialATSC  = BDA_MOD_8VSB,
  ScanModulationTypesMask_MCE_AnalogTv         = BDA_MOD_RF,
  ScanModulationTypesMask_MCE_All_TV           = 0xffffffff
} ScanModulationTypes;
```



## Constants

<dl> <dt>

<span id="BDA_SCAN_MOD_16QAM"></span><span id="bda_scan_mod_16qam"></span>**BDA\_SCAN\_MOD\_16QAM**
</dt> <dd>

16 symbol Quadrature Amplitude Modulation (QAM)

</dd> <dt>

<span id="BDA_SCAN_MOD_32QAM"></span><span id="bda_scan_mod_32qam"></span>**BDA\_SCAN\_MOD\_32QAM**
</dt> <dd>

32 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_64QAM"></span><span id="bda_scan_mod_64qam"></span>**BDA\_SCAN\_MOD\_64QAM**
</dt> <dd>

64 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_80QAM"></span><span id="bda_scan_mod_80qam"></span>**BDA\_SCAN\_MOD\_80QAM**
</dt> <dd>

80 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_96QAM"></span><span id="bda_scan_mod_96qam"></span>**BDA\_SCAN\_MOD\_96QAM**
</dt> <dd>

96 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_112QAM"></span><span id="bda_scan_mod_112qam"></span>**BDA\_SCAN\_MOD\_112QAM**
</dt> <dd>

112 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_128QAM"></span><span id="bda_scan_mod_128qam"></span>**BDA\_SCAN\_MOD\_128QAM**
</dt> <dd>

128 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_160QAM"></span><span id="bda_scan_mod_160qam"></span>**BDA\_SCAN\_MOD\_160QAM**
</dt> <dd>

160 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_192QAM"></span><span id="bda_scan_mod_192qam"></span>**BDA\_SCAN\_MOD\_192QAM**
</dt> <dd>

192 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_224QAM"></span><span id="bda_scan_mod_224qam"></span>**BDA\_SCAN\_MOD\_224QAM**
</dt> <dd>

224 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_256QAM"></span><span id="bda_scan_mod_256qam"></span>**BDA\_SCAN\_MOD\_256QAM**
</dt> <dd>

256 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_320QAM"></span><span id="bda_scan_mod_320qam"></span>**BDA\_SCAN\_MOD\_320QAM**
</dt> <dd>

320 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_384QAM"></span><span id="bda_scan_mod_384qam"></span>**BDA\_SCAN\_MOD\_384QAM**
</dt> <dd>

384 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_448QAM"></span><span id="bda_scan_mod_448qam"></span>**BDA\_SCAN\_MOD\_448QAM**
</dt> <dd>

448 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_512QAM"></span><span id="bda_scan_mod_512qam"></span>**BDA\_SCAN\_MOD\_512QAM**
</dt> <dd>

512 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_640QAM"></span><span id="bda_scan_mod_640qam"></span>**BDA\_SCAN\_MOD\_640QAM**
</dt> <dd>

640 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_768QAM"></span><span id="bda_scan_mod_768qam"></span>**BDA\_SCAN\_MOD\_768QAM**
</dt> <dd>

768 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_896QAM"></span><span id="bda_scan_mod_896qam"></span>**BDA\_SCAN\_MOD\_896QAM**
</dt> <dd>

896 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_1024QAM"></span><span id="bda_scan_mod_1024qam"></span>**BDA\_SCAN\_MOD\_1024QAM**
</dt> <dd>

1024 symbol QAM.

</dd> <dt>

<span id="BDA_SCAN_MOD_QPSK"></span><span id="bda_scan_mod_qpsk"></span>**BDA\_SCAN\_MOD\_QPSK**
</dt> <dd>

Quadrature Phase-Shift Keying (PSK) modulation.

</dd> <dt>

<span id="BDA_MOD_BPSK"></span><span id="bda_mod_bpsk"></span>**BDA\_MOD\_BPSK**
</dt> <dd>

Binary PSK modulation.

</dd> <dt>

<span id="BDA_MOD_OQPSK"></span><span id="bda_mod_oqpsk"></span>**BDA\_MOD\_OQPSK**
</dt> <dd>

Offset Q-PSK modulation.

</dd> <dt>

<span id="BDA_SCAN_MOD_8VSB"></span><span id="bda_scan_mod_8vsb"></span>**BDA\_SCAN\_MOD\_8VSB**
</dt> <dd>

8 Vestigial Side-Band modulation.

</dd> <dt>

<span id="BDA_MOD_16VSB"></span><span id="bda_mod_16vsb"></span>**BDA\_MOD\_16VSB**
</dt> <dd>

16 Vestigial Side-Band modulation.

</dd> <dt>

<span id="BDA_SCAN_MOD_AM_RADIO"></span><span id="bda_scan_mod_am_radio"></span>**BDA\_SCAN\_MOD\_AM\_RADIO**
</dt> <dd>

Analog amplitude modulation (AM radio).

</dd> <dt>

<span id="BDA_SCAN_MOD_FM_RADIO"></span><span id="bda_scan_mod_fm_radio"></span>**BDA\_SCAN\_MOD\_FM\_RADIO**
</dt> <dd>

Analog frequency modulation (FM radio).

</dd> <dt>

<span id="BDA_SCAN_MOD_8PSK"></span><span id="bda_scan_mod_8psk"></span>**BDA\_SCAN\_MOD\_8PSK**
</dt> <dd>

Eight-phase PSK (8-PSK) modulation.

</dd> <dt>

<span id="BDA_SCAN_MOD_RF"></span><span id="bda_scan_mod_rf"></span>**BDA\_SCAN\_MOD\_RF**
</dt> <dd>

Analog television.

</dd> <dt>

<span id="ScanModulationTypesMask_MCE_DigitalCable"></span><span id="scanmodulationtypesmask_mce_digitalcable"></span><span id="SCANMODULATIONTYPESMASK_MCE_DIGITALCABLE"></span>**ScanModulationTypesMask\_MCE\_DigitalCable**
</dt> <dd>

Digital cable modulation.

</dd> <dt>

<span id="ScanModulationTypesMask_MCE_TerrestrialATSC"></span><span id="scanmodulationtypesmask_mce_terrestrialatsc"></span><span id="SCANMODULATIONTYPESMASK_MCE_TERRESTRIALATSC"></span>**ScanModulationTypesMask\_MCE\_TerrestrialATSC**
</dt> <dd>

Terrestrial ATSC modulation.

</dd> <dt>

<span id="ScanModulationTypesMask_MCE_AnalogTv"></span><span id="scanmodulationtypesmask_mce_analogtv"></span><span id="SCANMODULATIONTYPESMASK_MCE_ANALOGTV"></span>**ScanModulationTypesMask\_MCE\_AnalogTv**
</dt> <dd>

Analog television modulation.

</dd> <dt>

<span id="ScanModulationTypesMask_MCE_All_TV"></span><span id="scanmodulationtypesmask_mce_all_tv"></span><span id="SCANMODULATIONTYPESMASK_MCE_ALL_TV"></span>**ScanModulationTypesMask\_MCE\_All\_TV**
</dt> <dd>

No modulation filtering.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[BDA Enumeration Types](bda-types.md)
</dt> <dt>

[**IScanningTunerEx::SetScanSignalTypeFilter**](iscanningtunerex-setscansignaltypefilter.md)
</dt> </dl>

 

 





