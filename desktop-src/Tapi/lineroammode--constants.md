---
description: The LINEROAMMODE\_ bit-flag constants describe the roaming status of a line device.
ms.assetid: af0eb263-8deb-44ab-8acb-00e4ff7930ab
title: LINEROAMMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEROAMMODE\_ Constants

The **LINEROAMMODE\_** bit-flag constants describe the roaming status of a line device.

<dl> <dt>

<span id="LINEROAMMODE_HOME"></span><span id="lineroammode_home"></span>**LINEROAMMODE\_HOME**
</dt> <dd> <dl> <dt>



The line is connected to the home network node.


</dt> </dl> </dd> <dt>

<span id="LINEROAMMODE_ROAMA"></span><span id="lineroammode_roama"></span>**LINEROAMMODE\_ROAMA**
</dt> <dd> <dl> <dt>



The line is connected to the Roam-A carrier and calls are charged accordingly.


</dt> </dl> </dd> <dt>

<span id="LINEROAMMODE_ROAMB"></span><span id="lineroammode_roamb"></span>**LINEROAMMODE\_ROAMB**
</dt> <dd> <dl> <dt>



The line is connected to the Roam-B carrier and calls are charged accordingly.


</dt> </dl> </dd> <dt>

<span id="LINEROAMMODE_UNAVAIL"></span><span id="lineroammode_unavail"></span>**LINEROAMMODE\_UNAVAIL**
</dt> <dd> <dl> <dt>



The roam mode is unavailable and will not be known.


</dt> </dl> </dd> <dt>

<span id="LINEROAMMODE_UNKNOWN"></span><span id="lineroammode_unknown"></span>**LINEROAMMODE\_UNKNOWN**
</dt> <dd> <dl> <dt>



The roam mode is currently unknown but may become known later.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




