---
title: LNB\_Source enumeration
description: Specifies the Digital Satellite Equipment Control (DiSeqC) Low Noise Blocker (LNB) input source.
ms.assetid: 586bcbf7-dd7a-45d3-b35a-dba785d13970
keywords:
- LNB_Source enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- LNB_Source
api_location:
- Bdatypes.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# LNB\_Source enumeration

Specifies the Digital Satellite Equipment Control (DiSeqC) Low Noise Blocker (LNB) input source. This type is used by Digital Video Broadcast-Satellite version 2 (DBS2) tuner devices that support the [**IDVBSLocator2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbslocator2) interface.

## Syntax


```C++
typedef enum  { 
  BDA_LNB_SOURCE_NOT_SET      = -1,
  BDA_LNB_SOURCE_NOT_DEFINED  = 0,
  BDA_LNB_SOURCE_A            = 1,
  BDA_LNB_SOURCE_B            = 2,
  BDA_LNB_SOURCE_C            = 3,
  BDA_LNB_SOURCE_D            = 4,
  BDA_LNB_SOURCE_MAX          = 5
} LNB_Source;
```



## Constants

<dl> <dt>

<span id="BDA_LNB_SOURCE_NOT_SET"></span><span id="bda_lnb_source_not_set"></span>**BDA\_LNB\_SOURCE\_NOT\_SET**
</dt> <dd>

Source input value can be any predefined value, but the caller does not explicitly set it.

</dd> <dt>

<span id="BDA_LNB_SOURCE_NOT_DEFINED"></span><span id="bda_lnb_source_not_defined"></span>**BDA\_LNB\_SOURCE\_NOT\_DEFINED**
</dt> <dd>

Source input value is not one of the legal predefined values.

</dd> <dt>

<span id="BDA_LNB_SOURCE_A"></span><span id="bda_lnb_source_a"></span>**BDA\_LNB\_SOURCE\_A**
</dt> <dd>

Input source A.

</dd> <dt>

<span id="BDA_LNB_SOURCE_B"></span><span id="bda_lnb_source_b"></span>**BDA\_LNB\_SOURCE\_B**
</dt> <dd>

Input source B.

</dd> <dt>

<span id="BDA_LNB_SOURCE_C"></span><span id="bda_lnb_source_c"></span>**BDA\_LNB\_SOURCE\_C**
</dt> <dd>

Input source C.

</dd> <dt>

<span id="BDA_LNB_SOURCE_D"></span><span id="bda_lnb_source_d"></span>**BDA\_LNB\_SOURCE\_D**
</dt> <dd>

Input source D.

</dd> <dt>

<span id="BDA_LNB_SOURCE_MAX"></span><span id="bda_lnb_source_max"></span>**BDA\_LNB\_SOURCE\_MAX**
</dt> <dd>

Maximum legal value for the input source.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Header<br/>                   | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[**IDVBSLocator2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbslocator2)
</dt> </dl>

 

 





