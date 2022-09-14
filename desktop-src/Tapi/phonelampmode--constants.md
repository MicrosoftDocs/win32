---
description: The PHONELAMPMODE bit-flag constants describe various ways in which a phones lamp can be lit.
ms.assetid: 4f6ed2fa-32c9-44b4-bfb5-2c1446ea84fe
title: PHONELAMPMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONELAMPMODE_ Constants

The **PHONELAMPMODE_** bit-flag constants describe various ways in which a phone's lamp can be lit.

<dl> <dt>

<span id="PHONELAMPMODE_DUMMY"></span><span id="phonelampmode_dummy"></span>**PHONELAMPMODE_DUMMY**
</dt> <dd> <dl> <dt>



This value is used to describe a button/lamp position that has no corresponding lamp.


</dt> </dl> </dd> <dt>

<span id="PHONELAMPMODE_BROKENFLUTTER"></span><span id="phonelampmode_brokenflutter"></span>**PHONELAMPMODE_BROKENFLUTTER**
</dt> <dd> <dl> <dt>



Broken flutter is the superposition of flash and flutter.


</dt> </dl> </dd> <dt>

<span id="PHONELAMPMODE_FLASH"></span><span id="phonelampmode_flash"></span>**PHONELAMPMODE_FLASH**
</dt> <dd> <dl> <dt>



Flash means slow on and off.


</dt> </dl> </dd> <dt>

<span id="PHONELAMPMODE_FLUTTER"></span><span id="phonelampmode_flutter"></span>**PHONELAMPMODE_FLUTTER**
</dt> <dd> <dl> <dt>



Flutter means fast on and off.


</dt> </dl> </dd> <dt>

<span id="PHONELAMPMODE_OFF"></span><span id="phonelampmode_off"></span>**PHONELAMPMODE_OFF**
</dt> <dd> <dl> <dt>



The lamp is off.


</dt> </dl> </dd> <dt>

<span id="PHONELAMPMODE_STEADY"></span><span id="phonelampmode_steady"></span>**PHONELAMPMODE_STEADY**
</dt> <dd> <dl> <dt>



Steady means the lamp is continuously lit.


</dt> </dl> </dd> <dt>

<span id="PHONELAMPMODE_UNKNOWN"></span><span id="phonelampmode_unknown"></span>**PHONELAMPMODE_UNKNOWN**
</dt> <dd> <dl> <dt>



The lamp mode is currently unknown.


</dt> </dl> </dd> <dt>

<span id="PHONELAMPMODE_WINK"></span><span id="phonelampmode_wink"></span>**PHONELAMPMODE_WINK**
</dt> <dd> <dl> <dt>



Wink means normal rate on and off.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 16 bits can be assigned for device-specific extensions. The low-order 16 bits are reserved.

Where the exact on and off cadences can differ across phone sets from different vendors, mapping of actual lamp lighting patterns for most phones onto the values listed above should be straightforward.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




