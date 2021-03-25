---
description: The LINELOCATIONOPTION\_ constants define values used in the dwOptions member of the LINELOCATIONENTRY structure returned as part of the LINETRANSLATECAPS structure returned by lineGetTranslateCaps.
ms.assetid: 3b185c16-2535-4a90-855b-29e52828ea4c
title: LINELOCATIONOPTION_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINELOCATIONOPTION\_ Constants

The **LINELOCATIONOPTION\_** constants define values used in the **dwOptions** member of the [**LINELOCATIONENTRY**](/windows/desktop/api/Tapi/ns-tapi-linelocationentry) structure returned as part of the [**LINETRANSLATECAPS**](/windows/desktop/api/Tapi/ns-tapi-linetranslatecaps) structure returned by [**lineGetTranslateCaps**](/windows/desktop/api/Tapi/nf-tapi-linegettranslatecaps).

<dl> <dt>

<span id="LINELOCATIONOPTION_PULSEDIAL"></span><span id="linelocationoption_pulsedial"></span>**LINELOCATIONOPTION\_PULSEDIAL**
</dt> <dd> <dl> <dt>



The default dialing mode at this location is pulse dialing. If this bit is set, [**lineTranslateAddress**](/windows/desktop/api/Tapi/nf-tapi-linetranslateaddress) will insert a "P" dial modifier at the beginning of the dialable string returned when this location is selected. If this bit is not set, **lineTranslateAddress** will insert a "T" dial modifier at the beginning of the dialable string.


</dt> </dl> </dd> </dl>

## Remarks

Not extensible. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




