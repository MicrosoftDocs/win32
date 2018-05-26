---
title: BinaryConvolutionCodeRate enumeration
description: Specifies the binary convolution code rate used in the forward error correction scheme.
ms.assetid: 161c963f-55b2-4a17-a537-47de3326df0e
keywords:
- BinaryConvolutionCodeRate enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- BinaryConvolutionCodeRate
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

# BinaryConvolutionCodeRate enumeration

Specifies the binary convolution code rate used in the forward error correction scheme.

## Syntax


```C++
typedef enum BinaryConvolutionCodeRate { 
  BDA_BCC_RATE_NOT_SET      = -1,
  BDA_BCC_RATE_NOT_DEFINED  = 0,
  BDA_BCC_RATE_1_2          = 1,
  BDA_BCC_RATE_2_3,
  BDA_BCC_RATE_3_4,
  BDA_BCC_RATE_3_5,
  BDA_BCC_RATE_4_5,
  BDA_BCC_RATE_5_6,
  BDA_BCC_RATE_5_11,
  BDA_BCC_RATE_7_8,
  BDA_BCC_RATE_1_4,
  BDA_BCC_RATE_1_3,
  BDA_BCC_RATE_2_5,
  BDA_BCC_RATE_6_7,
  BDA_BCC_RATE_8_9,
  BDA_BCC_RATE_9_10,
  BDA_BCC_RATE_MAX
} BinaryConvolutionCodeRate;
```



## Constants

<dl> <dt>

<span id="BDA_BCC_RATE_NOT_SET"></span><span id="bda_bcc_rate_not_set"></span>**BDA\_BCC\_RATE\_NOT\_SET**
</dt> <dd>

No rate is specified.

</dd> <dt>

<span id="BDA_BCC_RATE_NOT_DEFINED"></span><span id="bda_bcc_rate_not_defined"></span>**BDA\_BCC\_RATE\_NOT\_DEFINED**
</dt> <dd>

The rate is not defined.

</dd> <dt>

<span id="BDA_BCC_RATE_1_2"></span><span id="bda_bcc_rate_1_2"></span>**BDA\_BCC\_RATE\_1\_2**
</dt> <dd>

The rate is 1/2.

</dd> <dt>

<span id="BDA_BCC_RATE_2_3"></span><span id="bda_bcc_rate_2_3"></span>**BDA\_BCC\_RATE\_2\_3**
</dt> <dd>

The rate is 2/3.

</dd> <dt>

<span id="BDA_BCC_RATE_3_4"></span><span id="bda_bcc_rate_3_4"></span>**BDA\_BCC\_RATE\_3\_4**
</dt> <dd>

The rate is 3/4.

</dd> <dt>

<span id="BDA_BCC_RATE_3_5"></span><span id="bda_bcc_rate_3_5"></span>**BDA\_BCC\_RATE\_3\_5**
</dt> <dd>

The rate is 3/5.

</dd> <dt>

<span id="BDA_BCC_RATE_4_5"></span><span id="bda_bcc_rate_4_5"></span>**BDA\_BCC\_RATE\_4\_5**
</dt> <dd>

The rate is 4/5.

</dd> <dt>

<span id="BDA_BCC_RATE_5_6"></span><span id="bda_bcc_rate_5_6"></span>**BDA\_BCC\_RATE\_5\_6**
</dt> <dd>

The rate is 5/6.

</dd> <dt>

<span id="BDA_BCC_RATE_5_11"></span><span id="bda_bcc_rate_5_11"></span>**BDA\_BCC\_RATE\_5\_11**
</dt> <dd>

The rate is 5/11.

</dd> <dt>

<span id="BDA_BCC_RATE_7_8"></span><span id="bda_bcc_rate_7_8"></span>**BDA\_BCC\_RATE\_7\_8**
</dt> <dd>

The rate is 7/8.

</dd> <dt>

<span id="BDA_BCC_RATE_1_4"></span><span id="bda_bcc_rate_1_4"></span>**BDA\_BCC\_RATE\_1\_4**
</dt> <dd>

The rate is 1/4.

</dd> <dt>

<span id="BDA_BCC_RATE_1_3"></span><span id="bda_bcc_rate_1_3"></span>**BDA\_BCC\_RATE\_1\_3**
</dt> <dd>

The rate is 1/3.

</dd> <dt>

<span id="BDA_BCC_RATE_2_5"></span><span id="bda_bcc_rate_2_5"></span>**BDA\_BCC\_RATE\_2\_5**
</dt> <dd>

The rate is 2/5.

</dd> <dt>

<span id="BDA_BCC_RATE_6_7"></span><span id="bda_bcc_rate_6_7"></span>**BDA\_BCC\_RATE\_6\_7**
</dt> <dd>

The rate is 6/7.

</dd> <dt>

<span id="BDA_BCC_RATE_8_9"></span><span id="bda_bcc_rate_8_9"></span>**BDA\_BCC\_RATE\_8\_9**
</dt> <dd>

The rate is 8/9.

</dd> <dt>

<span id="BDA_BCC_RATE_9_10"></span><span id="bda_bcc_rate_9_10"></span>**BDA\_BCC\_RATE\_9\_10**
</dt> <dd>

The rate is 9/10.

</dd> <dt>

<span id="BDA_BCC_RATE_MAX"></span><span id="bda_bcc_rate_max"></span>**BDA\_BCC\_RATE\_MAX**
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

 

 





