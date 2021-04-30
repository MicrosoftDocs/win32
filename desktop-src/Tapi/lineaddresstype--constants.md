---
description: The address type identifies address format, such as standard phone number or e-mail address. Only applications that negotiate TAPI version 3.0 or higher can use address types.
ms.assetid: 2c32eda1-e510-40eb-ae75-fc7b9e9953cd
title: LINEADDRESSTYPE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEADDRESSTYPE\_ Constants

The address type identifies address format, such as standard phone number or e-mail address. Only applications that negotiate TAPI version 3.0 or higher can use address types.

<dl> <dt>

<span id="LINEADDRESSTYPE_PHONENUMBER"></span><span id="lineaddresstype_phonenumber"></span>**LINEADDRESSTYPE\_PHONENUMBER**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



Address type is a standard phone number.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSTYPE_SDP"></span><span id="lineaddresstype_sdp"></span>**LINEADDRESSTYPE\_SDP**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



Address type is Session Description Protocol (SDP) conference.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSTYPE_EMAILNAME"></span><span id="lineaddresstype_emailname"></span>**LINEADDRESSTYPE\_EMAILNAME**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



Address type is an e-mail name.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSTYPE_DOMAINNAME"></span><span id="lineaddresstype_domainname"></span>**LINEADDRESSTYPE\_DOMAINNAME**
</dt> <dd> <dl> <dt>

0x00000008
</dt> <dt>



Address type is a domain name.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSTYPE_IPADDRESS"></span><span id="lineaddresstype_ipaddress"></span>**LINEADDRESSTYPE\_IPADDRESS**
</dt> <dd> <dl> <dt>

0x00000010
</dt> <dt>



Address type is an IP address.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




