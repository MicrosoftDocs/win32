---
description: The LINESPECIALINFO\_ bit-flag constants describes special information signals that the network can use to report various reporting and network observation operations.
ms.assetid: b94f8a6f-b84d-4976-b4d4-10dee5a1a4d8
title: LINESPECIALINFO_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINESPECIALINFO\_ Constants

The **LINESPECIALINFO\_** bit-flag constants describes special information signals that the network can use to report various reporting and network observation operations. They are special coded tone sequences transmitted at the beginning of network advisory recorded announcements.

<dl> <dt>

<span id="LINESPECIALINFO_CUSTIRREG"></span><span id="linespecialinfo_custirreg"></span>**LINESPECIALINFO\_CUSTIRREG**
</dt> <dd> <dl> <dt>



This special information tone precedes a vacant number, AIS, Centrex number change and nonworking station, access code not dialed or dialed in error, or manual intercept operator message (customer irregularity category). LINESPECIALINFO\_CUSTIRREG is also reported when billing information is rejected and when the dialed address is blocked at the switch.


</dt> </dl> </dd> <dt>

<span id="LINESPECIALINFO_NOCIRCUIT"></span><span id="linespecialinfo_nocircuit"></span>**LINESPECIALINFO\_NOCIRCUIT**
</dt> <dd> <dl> <dt>



This special information tone precedes a no circuit or an emergency announcement (trunk blockage category).


</dt> </dl> </dd> <dt>

<span id="LINESPECIALINFO_REORDER"></span><span id="linespecialinfo_reorder"></span>**LINESPECIALINFO\_REORDER**
</dt> <dd> <dl> <dt>



This special information tone precedes a reorder announcement (equipment irregularity category). LINESPECIALINFO\_REORDER is also reported when the telephone is kept offhook too long.


</dt> </dl> </dd> <dt>

<span id="LINESPECIALINFO_UNAVAIL"></span><span id="linespecialinfo_unavail"></span>**LINESPECIALINFO\_UNAVAIL**
</dt> <dd> <dl> <dt>



Specifics about the special information tone are unavailable and will not become known.


</dt> </dl> </dd> <dt>

<span id="LINESPECIALINFO_UNKNOWN"></span><span id="linespecialinfo_unknown"></span>**LINESPECIALINFO\_UNKNOWN**
</dt> <dd> <dl> <dt>



Specifics about the special information tone are currently unknown but may become known later.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 16 bits can be assigned for device-specific extensions. The low-order 16 bits are reserved.

Special information tones are defined for advisory messages and are not normally used for billing or supervisory purpose.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




