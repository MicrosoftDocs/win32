---
description: The LINETRANSLATEOPTION\_ bit-flag constant describes an option used by address translation.
ms.assetid: 3f5e9952-945e-42b8-8536-b52a0c833282
title: LINETRANSLATEOPTION_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINETRANSLATEOPTION\_ Constants

The **LINETRANSLATEOPTION\_** bit-flag constant describes an option used by address translation.

<dl> <dt>

<span id="LINETRANSLATEOPTION_CANCELCALLWAITING"></span><span id="linetranslateoption_cancelcallwaiting"></span>**LINETRANSLATEOPTION\_CANCELCALLWAITING**
</dt> <dd> <dl> <dt>



If a Cancel Call Waiting string is defined for the location, setting this bit will cause that string to be inserted at the beginning of the dialable string. This is commonly used by data modem and fax applications to prevent interruption of calls by call waiting beeps. If no Cancel Call Waiting string is defined for the location, this bit has no affect. Note that applications using this bit are advised to also set the LINECALLPARAMFLAGS\_SECURE bit in the **dwCallParamFlags** member of the [**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams) structure passed in to [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall) through the *lpCallParams* parameter, so that if the line device uses a mechanism other than dialable digits to suppress call interrupts then that mechanism will be invoked.


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATEOPTION_CARDOVERRIDE"></span><span id="linetranslateoption_cardoverride"></span>**LINETRANSLATEOPTION\_CARDOVERRIDE**
</dt> <dd> <dl> <dt>



The default calling card is to be overridden with a specified one.


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATEOPTION_FORCELD"></span><span id="linetranslateoption_forceld"></span>**LINETRANSLATEOPTION\_FORCELD**
</dt> <dd> <dl> <dt>



This option forces the address (number) to be translated as long distance.


</dt> </dl> </dd> <dt>

<span id="LINETRANSLATEOPTION_FORCELOCAL"></span><span id="linetranslateoption_forcelocal"></span>**LINETRANSLATEOPTION\_FORCELOCAL**
</dt> <dd> <dl> <dt>



This option forces the number (address) to be translated as local.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams)
</dt> <dt>

[**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall)
</dt> <dt>

[**LINETRANSLATEOUTPUT**](/windows/desktop/api/Tapi/ns-tapi-linetranslateoutput)
</dt> </dl>

 

 




