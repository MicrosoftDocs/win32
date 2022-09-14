---
description: The LINECARDOPTION\_constants define values used in the dwOptions member of the LINECARDENTRY structure returned as part of the LINETRANSLATECAPS structure returned by lineGetTranslateCaps.
ms.assetid: 36c67fbf-e5ca-4ec4-a03a-0b828667abcc
title: LINECARDOPTION_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECARDOPTION\_ Constants

The **LINECARDOPTION\_constants** define values used in the **dwOptions** member of the [**LINECARDENTRY**](/windows/desktop/api/Tapi/ns-tapi-linecardentry) structure returned as part of the [**LINETRANSLATECAPS**](/windows/desktop/api/Tapi/ns-tapi-linetranslatecaps) structure returned by [**lineGetTranslateCaps**](/windows/desktop/api/Tapi/nf-tapi-linegettranslatecaps). The **LINECARDOPTION\_constants**t has the following values:

<dl> <dt>

<span id="LINECARDOPTION_HIDDEN"></span><span id="linecardoption_hidden"></span>**LINECARDOPTION\_HIDDEN**
</dt> <dd> <dl> <dt>



This calling card has been hidden by the user. It is not shown by Dial Helper in the main listing of available calling cards, but will be shown in the list of cards from which dialing rules can be copied.


</dt> </dl> </dd> <dt>

<span id="LINECARDOPTION_PREDEFINED"></span><span id="linecardoption_predefined"></span>**LINECARDOPTION\_PREDEFINED**
</dt> <dd> <dl> <dt>



This calling card is one of the predefined calling card definitions included with Telephony by Microsoft. It cannot be removed entirely using Dial Helper; if the user attempts to remove it, it will become HIDDEN. It thus continues to be accessible for copying of dialing rules.


</dt> </dl> </dd> </dl>

## Remarks

Not extensible. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




