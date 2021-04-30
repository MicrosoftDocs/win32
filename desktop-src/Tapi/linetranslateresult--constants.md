---
description: The LINETRANSLATERESULT\_ bit-flag constants describe various results of an address translation.
ms.assetid: 7b834c57-d862-4fe6-828c-9e8fa20f3ec7
title: LINETRANSLATERESULT_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINETRANSLATERESULT\_ Constants

The **LINETRANSLATERESULT\_** bit-flag constants describe various results of an address translation.

<dl> <dt>

<span id="LINETRANSLATERESULT_CANONICAL"></span><span id="linetranslateresult_canonical"></span>**LINETRANSLATERESULT\_CANONICAL**
</dt> <dd> <dl> <dt>



Indicates that the input string was in valid canonical format.


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_DIALBILLING"></span><span id="linetranslateresult_dialbilling"></span>**LINETRANSLATERESULT\_DIALBILLING**
</dt> <dd> <dl> <dt>



Indicates that the returned address contains a "$".


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_DIALDIALTONE"></span><span id="linetranslateresult_dialdialtone"></span>**LINETRANSLATERESULT\_DIALDIALTONE**
</dt> <dd> <dl> <dt>



Indicates that the returned address contains a "W".


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_DIALPROMPT"></span><span id="linetranslateresult_dialprompt"></span>**LINETRANSLATERESULT\_DIALPROMPT**
</dt> <dd> <dl> <dt>



Indicates that the returned address contains a "?".


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_DIALQUIET"></span><span id="linetranslateresult_dialquiet"></span>**LINETRANSLATERESULT\_DIALQUIET**
</dt> <dd> <dl> <dt>



Indicates that the returned address contain a "@".


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_INTERNATIONAL"></span><span id="linetranslateresult_international"></span>**LINETRANSLATERESULT\_INTERNATIONAL**
</dt> <dd> <dl> <dt>



Indicates that the call is being treated as an international call (country or region code specified in the destination address is different from the country or region code specified for the **CurrentLocation**).


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_INTOLLLIST"></span><span id="linetranslateresult_intolllist"></span>**LINETRANSLATERESULT\_INTOLLLIST**
</dt> <dd> <dl> <dt>



Indicates that the local call is being dialed as long distance because the country or region has toll calling and the prefix appears in the **TollPrefixList** of the **CurrentLocation**.


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_LOCAL"></span><span id="linetranslateresult_local"></span>**LINETRANSLATERESULT\_LOCAL**
</dt> <dd> <dl> <dt>



Indicates that the call is being treated as a local call (country or region code and area code specified in the destination address are the same as those specified for the **CurrentLocation**).


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_LONGDISTANCE"></span><span id="linetranslateresult_longdistance"></span>**LINETRANSLATERESULT\_LONGDISTANCE**
</dt> <dd> <dl> <dt>



Indicates that the call is being treated as a long distance call (country or region code specified in the destination address is the same but area code is different from those specified for the **CurrentLocation**).


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_NOTINTOLLLIST"></span><span id="linetranslateresult_notintolllist"></span>**LINETRANSLATERESULT\_NOTINTOLLLIST**
</dt> <dd> <dl> <dt>



Indicates that the country or region supports toll calling but the prefix does not appear in the **TollPrefixList**, so the call is dialed as a local call. Note that if both INTOLLIST and NOTINTOLLIST are off, the current country or region does not support toll prefixes, and user-interface elements related to toll prefixes should not be presented to the user; if either such bit is on, the country or region does support toll lists, and the related user-interface elements should be enabled.


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_NOTRANSLATION"></span><span id="linetranslateresult_notranslation"></span>**LINETRANSLATERESULT\_NOTRANSLATION**
</dt> <dd> <dl> <dt>



Indicates that address translation is not available. This element is exposed only to applications that negotiate a TAPI version of 3.0 or higher.


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATERESULT_VOICEDETECT"></span><span id="linetranslateresult_voicedetect"></span>**LINETRANSLATERESULT\_VOICEDETECT**
</dt> <dd> <dl> <dt>



Indicates that the returned dialable address contains a ":". This element is exposed only to applications that negotiate a TAPI version of 2.0 or higher.

> [!Note]  
> The ":" (colon) character will be added to the list of characters that can be embedded in a dialable string and passed into destination addresses. Attempting to pass it from an application to a line device that supports an API version earlier than 2.0 will most likely result in LINEERR\_INVALADDRESS, or possibly in the character being ignored entirely. The meaning of this character is "Pause until a voice prompt is detected, then continue dialing"; it is intended for use when automatically dialing into systems that give voice prompts, such as long distance calling card processors.

 


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




