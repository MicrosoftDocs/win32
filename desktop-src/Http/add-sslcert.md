---
title: add sslcert
description: Adds a new Secure Sockets Layer (SSL) server certificate binding and the corresponding client certificate policies for an IP address and port.
ms.assetid: 4ba3d2cb-050f-46e3-81f9-5f7e360b19fb
keywords:
- add sslcert HTTP
topic_type:
- apiref
api_name:
- add sslcert
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# add sslcert

Adds a new Secure Sockets Layer (SSL) server certificate binding and the corresponding client certificate policies for an IP address and port.

``` syntax
add sslcert [ipport=]IP Address:port
            [certhash=]string
            [appid=]GUID
            [certstorename=]string
            [verifyclientcertrevocation={enable|disable}]
            [verifyrevocationwithcachedclientcertonly={enable|disable}]
            [usagecheck={enable|disable}]
            [revocationfreshnesstime=]u-int
            [urlretrievaltimeout=]u-int
            [sslctlidentifier=]string
            [sslctlstorename=]string
            [dsmapperusage={enable|disable}]
            [clientcertnegotiation={enable|disable}]

 
```

## Parameters

<dl> <dt>

<span id="_ipport__IP_Address_port"></span><span id="_ipport__ip_address_port"></span><span id="_IPPORT__IP_ADDRESS_PORT"></span>**\[ipport=IP Address:port\]**
</dt> <dd>

Specifies the IP address and port for the binding.

</dd> <dt>

<span id="_certhash__string"></span><span id="_CERTHASH__STRING"></span>**\[certhash=string\]**
</dt> <dd>

Specifies the SHA hash of the certificate. This hash is 20 bytes long and specified as a hexadecimal string.

</dd> <dt>

<span id="_appid__GUID"></span><span id="_appid__guid"></span><span id="_APPID__GUID"></span>**\[appid=GUID\]**
</dt> <dd>

Specifies the GUID to identify the owning application.

</dd> <dt>

<span id="_certstorename__string"></span><span id="_CERTSTORENAME__STRING"></span>**\[certstorename=string\]**
</dt> <dd>

Specifies the store name for the certificate. Defaults to MY. Certificate must be stored in the local computer context.

</dd> <dt>

<span id="_verifyclientcertrevocation__enable_disable__"></span><span id="_VERIFYCLIENTCERTREVOCATION__ENABLE_DISABLE__"></span>**\[verifyclientcertrevocation={enable\|disable}\]**
</dt> <dd>

Turns on or turnsoff verification of revocation of client certificates.

</dd> <dt>

<span id="_verifyrevocationwithcachedclientcertonly__enable_disable__"></span><span id="_VERIFYREVOCATIONWITHCACHEDCLIENTCERTONLY__ENABLE_DISABLE__"></span>**\[verifyrevocationwithcachedclientcertonly={enable\|disable}\]**
</dt> <dd>

Turns on or turns off usage of only cached client certificate for revocation checking.

</dd> <dt>

<span id="_usagecheck__enable_disable__"></span><span id="_USAGECHECK__ENABLE_DISABLE__"></span>**\[usagecheck={enable\|disable}\]**
</dt> <dd>

Turns on or turns off usage check. Default is enabled.

</dd> <dt>

<span id="_revocationfreshnesstime__u-int"></span><span id="_REVOCATIONFRESHNESSTIME__U-INT"></span>**\[revocationfreshnesstime=u-int\]**
</dt> <dd>

Specifies the time interval to check for an updated certificate revocation list (CRL). If this value is 0, then the new CRL is updated only if the previous one expires (in seconds).

</dd> <dt>

<span id="_urlretrievaltimeout__u-int"></span><span id="_URLRETRIEVALTIMEOUT__U-INT"></span>**\[urlretrievaltimeout=u-int\]**
</dt> <dd>

Specifies the timeout interval on attempts to retrieve the certificate revocation list for the remote URL (in milliseconds).

</dd> <dt>

<span id="_sslctlidentifier__string"></span><span id="_SSLCTLIDENTIFIER__STRING"></span>**\[sslctlidentifier=string\]**
</dt> <dd>

Lists the certificate issuers that can be trusted. This list can be a subset of the certificate issuers that are trusted by the computer.

</dd> <dt>

<span id="_sslctlstorename__string"></span><span id="_SSLCTLSTORENAME__STRING"></span>**\[sslctlstorename=string\]**
</dt> <dd>

Specifies the store name under LOCAL\_MACHINE where SslCtlIdentifier is stored.

</dd> <dt>

<span id="_dsmapperusage__enable_disable__"></span><span id="_DSMAPPERUSAGE__ENABLE_DISABLE__"></span>**\[dsmapperusage={enable\|disable}\]**
</dt> <dd>

Turns on or turns off DS mappers. Default is disabled.

</dd> <dt>

<span id="_clientcertnegotiation__enable_disable__"></span><span id="_CLIENTCERTNEGOTIATION__ENABLE_DISABLE__"></span>**\[clientcertnegotiation={enable\|disable}\]**
</dt> <dd>

Turns on or turns off negotiation of certificate. Default is disabled.

</dd> </dl>

## Examples

**add sslcert ipport=1.1.1.1:443**

**certhash=0102030405060708090A0B0C0D0E0F1011121314**

**appid={00112233-4455-6677-8899-AABBCCDDEEFF}**

 

 




