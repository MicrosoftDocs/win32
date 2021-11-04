---
description: The LINETRANSFERMODE\_ bit-flag constants describe different ways of resolving call transfer requests.
ms.assetid: 0a01131f-b63c-45ef-a0a9-17d69a0dacf9
title: LINETRANSFERMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINETRANSFERMODE\_ Constants

The **LINETRANSFERMODE\_** bit-flag constants describe different ways of resolving call transfer requests.

<dl> <dt>

<span id="LINETRANSFERMODE_CONFERENCE"></span><span id="linetransfermode_conference"></span>**LINETRANSFERMODE\_CONFERENCE**
</dt> <dd> <dl> <dt>



The transfer is resolved by establishing a three-way conference between the application, the party connected to the initial call, and the party connected to the consultation call. A conference call is created when this option is selected.


</dt> </dl> </dd> <dt>

<span id="LINETRANSFERMODE_TRANSFER"></span><span id="linetransfermode_transfer"></span>**LINETRANSFERMODE\_TRANSFER**
</dt> <dd> <dl> <dt>



The transfer is resolved by transferring the initial call to the consultation call. Both calls will become idle to the application.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




