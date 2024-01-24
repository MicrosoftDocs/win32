---
description: The LINECALLFEATURE2\_ constants list the supplemental features available for conferencing, transferring, and parking calls.
ms.assetid: 67a3b587-dd5b-4ccf-ab69-2137604706b8
title: LINECALLFEATURE2_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLFEATURE2\_ Constants

The **LINECALLFEATURE2\_** constants list the supplemental features available for conferencing, transferring, and parking calls.

<dl> <dt>

<span id="LINECALLFEATURE2_COMPLCALLBACK"></span><span id="linecallfeature2_complcallback"></span>**LINECALLFEATURE2\_COMPLCALLBACK**
</dt> <dd> <dl> <dt>



If this bit is on, the "callback" feature can be invoked by using the LINECOMPLMODE\_CALLBACK option with [**lineCompleteCall**](/windows/desktop/api/Tapi/nf-tapi-linecompletecall). The LINECALLFEATURE\_COMPLETECALL bit will also be on in the **dwCallFeatures** member.


</dt> </dl> </dd> <dt>

<span id="LINECALLFEATURE2_COMPLCAMPON"></span><span id="linecallfeature2_complcampon"></span>**LINECALLFEATURE2\_COMPLCAMPON**
</dt> <dd> <dl> <dt>



If this bit is on, the "camp on" feature can be invoked by using the LINECOMPLMODE\_CAMPON option with [**lineCompleteCall**](/windows/desktop/api/Tapi/nf-tapi-linecompletecall). The LINECALLFEATURE\_COMPLETECALL bit will also be on in the **dwCallFeatures** member.


</dt> </dl> </dd> <dt>

<span id="LINECALLFEATURE2_COMPLINTRUDE"></span><span id="linecallfeature2_complintrude"></span>**LINECALLFEATURE2\_COMPLINTRUDE**
</dt> <dd> <dl> <dt>



If this bit is on, the "intrude" feature can be invoked by using the LINECOMPLMODE\_INTRUDE option with [**lineCompleteCall**](/windows/desktop/api/Tapi/nf-tapi-linecompletecall). The LINECALLFEATURE\_COMPLETECALL bit will also be on in the **dwCallFeatures** member.


</dt> </dl> </dd> <dt>

<span id="LINECALLFEATURE2_COMPLMESSAGE"></span><span id="linecallfeature2_complmessage"></span>**LINECALLFEATURE2\_COMPLMESSAGE**
</dt> <dd> <dl> <dt>



If this bit is on, the "leave message" feature can be invoked by using the LINECOMPLMODE\_MESSAGE option with [**lineCompleteCall**](/windows/desktop/api/Tapi/nf-tapi-linecompletecall). The LINECALLFEATURE\_COMPLETECALL bit will also be on in the **dwCallFeatures** member.


</dt> </dl> </dd> <dt>

<span id="LINECALLFEATURE2_NOHOLDCONFERENCE"></span><span id="linecallfeature2_noholdconference"></span>**LINECALLFEATURE2\_NOHOLDCONFERENCE**
</dt> <dd> <dl> <dt>



If this bit is on, a "no hold conference" can be created by using the LINECALLPARAMFLAGS\_NOHOLDCONFERENCE option with [**lineSetupConference**](/windows/desktop/api/Tapi/nf-tapi-linesetupconference). The LINECALLFEATURE\_SETUPCONF bit will also be on in the **dwCallFeatures** member.


</dt> </dl> </dd> <dt>

<span id="LINECALLFEATURE2_ONESTEPTRANSFER"></span><span id="linecallfeature2_onesteptransfer"></span>**LINECALLFEATURE2\_ONESTEPTRANSFER**
</dt> <dd> <dl> <dt>



If this bit is on, "one step transfer" can be created by using the LINECALLPARAMFLAGS\_ONESTEPTRANSFER option with [**lineSetupTransfer**](/windows/desktop/api/Tapi/nf-tapi-linesetuptransfer). The LINECALLFEATURE\_SETUPTRANSFER bit will also be on in the **dwCallFeatures** member.

> [!Note]  
> If none of the "COMPL" bits is specified in the **dwCallFeatures2** member in [**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus) but LINECALLFEATURE\_COMPLETECALL is specified, then it is possible that any of them will work, but the service provider has not specified which.

 


</dt> </dl> </dd> <dt>

<span id="LINECALLFEATURE2_TRANSFERCONF"></span><span id="linecallfeature2_transferconf"></span>**LINECALLFEATURE2\_TRANSFERCONF**
</dt> <dd> <dl> <dt>



If this bit is on, the [**lineCompleteTransfer**](/windows/desktop/api/Tapi/nf-tapi-linecompletetransfer) function can be used to resolve the transfer as a three-way conference. The LINECALLFEATURE\_COMPLETETRANSF bit will also be on in the **dwCallFeatures** member.


</dt> </dl> </dd> <dt>

<span id="LINECALLFEATURE2_TRANSFERNORM"></span><span id="linecallfeature2_transfernorm"></span>**LINECALLFEATURE2\_TRANSFERNORM**
</dt> <dd> <dl> <dt>



If this bit is on, the [**lineCompleteTransfer**](/windows/desktop/api/Tapi/nf-tapi-linecompletetransfer) function can be used to resolve the transfer as a normal transfer. The LINECALLFEATURE\_COMPLETETRANSF bit will also be on in the **dwCallFeatures** member.

> [!Note]  
> If neither TRANSFERNORM nor TRANSFERCONF is specified in the **dwCallFeatures2** member in [**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus) but LINECALLFEATURE\_COMPLETETRANSF is specified, then it is possible that either will work, but the service provider has not specified which.

 


</dt> </dl> </dd> <dt>

<span id="LINECALLFEATURE2_PARKDIRECT"></span><span id="linecallfeature2_parkdirect"></span>**LINECALLFEATURE2\_PARKDIRECT**
</dt> <dd> <dl> <dt>



If this bit is on, the "directed park" feature can be invoked by using the LINEPARKMODE\_DIRECTED option with [**linePark**](/windows/desktop/api/Tapi/nf-tapi-linepark). The LINECALLFEATURE\_PARK bit will also be on in the **dwCallFeatures** member.


</dt> </dl> </dd> <dt>

<span id="LINECALLFEATURE2_PARKNONDIRECT"></span><span id="linecallfeature2_parknondirect"></span>**LINECALLFEATURE2\_PARKNONDIRECT**
</dt> <dd> <dl> <dt>



If this bit is on, the "non-directed park" feature can be invoked by using the LINEPARKMODE\_NONDIRECTED option with [**linePark**](/windows/desktop/api/Tapi/nf-tapi-linepark). The LINECALLFEATURE\_PARK bit will also be on in the **dwCallFeatures** member.

> [!Note]  
> If neither PARKDIRECT nor PARKNONDIRECT is specified in the **dwCallFeatures2** member in [**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus) but LINECALLFEATURE\_PARK is specified, then it is possible that either will work, but the service provider has not specified which.

 


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus)
</dt> <dt>

[**lineCompleteCall**](/windows/desktop/api/Tapi/nf-tapi-linecompletecall)
</dt> <dt>

[**lineCompleteTransfer**](/windows/desktop/api/Tapi/nf-tapi-linecompletetransfer)
</dt> <dt>

[**linePark**](/windows/desktop/api/Tapi/nf-tapi-linepark)
</dt> <dt>

[**lineSetupConference**](/windows/desktop/api/Tapi/nf-tapi-linesetupconference)
</dt> <dt>

[**lineSetupTransfer**](/windows/desktop/api/Tapi/nf-tapi-linesetuptransfer)
</dt> </dl>

 

 




