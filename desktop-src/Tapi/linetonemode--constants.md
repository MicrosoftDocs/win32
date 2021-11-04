---
description: The LINETONEMODE\_ constants describe different selections that are used when generating line tones.
ms.assetid: 7bfc7d4e-2ab3-44ec-a936-f2d7dcfce263
title: LINETONEMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINETONEMODE\_ Constants

The **LINETONEMODE\_ constants** describe different selections that are used when generating line tones.

<dl> <dt>

<span id="LINETONEMODE_BEEP"></span><span id="linetonemode_beep"></span>**LINETONEMODE\_BEEP**
</dt> <dd> <dl> <dt>



The tone is a beep, such as that used to announce the beginning of a recording. Exact definition is service-provider defined.


</dt> </dl> </dd> <dt>

<span id="LINETONEMODE_BILLING"></span><span id="linetonemode_billing"></span>**LINETONEMODE\_BILLING**
</dt> <dd> <dl> <dt>



The tone is a billing information tone such as a credit card prompt tone. Exact definition is service-provider defined.


</dt> </dl> </dd> <dt>

<span id="LINETONEMODE_BUSY"></span><span id="linetonemode_busy"></span>**LINETONEMODE\_BUSY**
</dt> <dd> <dl> <dt>



The tone is a busy tone. Exact definition is service-provider defined.


</dt> </dl> </dd> <dt>

<span id="LINETONEMODE_CUSTOM"></span><span id="linetonemode_custom"></span>**LINETONEMODE\_CUSTOM**
</dt> <dd> <dl> <dt>



The tone is a custom tone defined by its component frequencies, of type [**LINEGENERATETONE**](/windows/desktop/api/Tapi/ns-tapi-linegeneratetone).


</dt> </dl> </dd> <dt>

<span id="LINETONEMODE_RINGBACK"></span><span id="linetonemode_ringback"></span>**LINETONEMODE\_RINGBACK**
</dt> <dd> <dl> <dt>



The tone is ringback tone. Exact definition is service-provider defined.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 16 bits can be assigned for device-specific extensions. The low-order 16 bits are reserved.

These constants are used to define tones to be generated inband over a call to the remote party. Note that tone detection of non-custom tones does not use these constants.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




