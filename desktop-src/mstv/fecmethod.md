---
title: FECMethod enumeration
description: Specifies the type of forward error correction being used by the provider.
ms.assetid: 6910c51d-4176-49a3-be6b-6b072ad03fc1
keywords:
- FECMethod enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- FECMethod
api_location:
- bdatypes.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# FECMethod enumeration

Specifies the type of forward error correction being used by the provider.

## Syntax


```C++
typedef enum FECMethod { 
  BDA_FEC_METHOD_NOT_SET      = -1,
  BDA_FEC_METHOD_NOT_DEFINED  = 0,
  BDA_FEC_VITERBI             = 1,
  BDA_FEC_RS_204_188          = 2,
  BDA_FEC_LDPC,
  BDA_FEC_BCH,
  BDA_FEC_RS_147_130,
  BDA_FEC_MAX                 = 3
} FECMethod;
```



## Constants

<dl> <dt>

<span id="BDA_FEC_METHOD_NOT_SET"></span><span id="bda_fec_method_not_set"></span>**BDA\_FEC\_METHOD\_NOT\_SET**
</dt> <dd>

The FEC method is not set.

</dd> <dt>

<span id="BDA_FEC_METHOD_NOT_DEFINED"></span><span id="bda_fec_method_not_defined"></span>**BDA\_FEC\_METHOD\_NOT\_DEFINED**
</dt> <dd>

The FEC method is not defined.

</dd> <dt>

<span id="BDA_FEC_VITERBI"></span><span id="bda_fec_viterbi"></span>**BDA\_FEC\_VITERBI**
</dt> <dd>

The FEC is a Viterbi Binary Convolution.

</dd> <dt>

<span id="BDA_FEC_RS_204_188"></span><span id="bda_fec_rs_204_188"></span>**BDA\_FEC\_RS\_204\_188**
</dt> <dd>

The FEC is Reed-Solomon 204/188 (outer FEC).

</dd> <dt>

<span id="BDA_FEC_LDPC"></span><span id="bda_fec_ldpc"></span>**BDA\_FEC\_LDPC**
</dt> <dd>

The FEC is Low Density Parity Check (LDPC) error correction code.

</dd> <dt>

<span id="BDA_FEC_BCH"></span><span id="bda_fec_bch"></span>**BDA\_FEC\_BCH**
</dt> <dd>

The FEC is Bose-Chaudhuri-Hocquenghem (BCH) multiple error correction binary block code.

</dd> <dt>

<span id="BDA_FEC_RS_147_130"></span><span id="bda_fec_rs_147_130"></span>**BDA\_FEC\_RS\_147\_130**
</dt> <dd>

The FEC is Reed-Solomon 147/130 (outer FEC).

</dd> <dt>

<span id="BDA_FEC_MAX"></span><span id="bda_fec_max"></span>**BDA\_FEC\_MAX**
</dt> <dd>

Reserved; do not use.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





