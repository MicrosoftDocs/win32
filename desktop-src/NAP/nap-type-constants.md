---
title: NAP Type Constants (NapTypes.h)
description: The following NAP constants are defined.
ms.assetid: 2727487c-8c6a-4cd9-b6d8-253191a7d7f6
topic_type:
- apiref
api_name:
- maxSoHAttributeCount
- maxSoHAttributeSize
- minNetworkSoHSize
- maxNetworkSoHSize
- maxDwordCountPerSoHAttribute
- maxIpv4CountPerSoHAttribute
- maxIpv6CountPerSoHAttribute
- maxStringLength
- maxStringLengthInBytes
- maxSystemHealthEntityCount
- SystemHealthEntityCount
- maxEnforcerCount
- EnforcementEntityCount
- maxPrivateDataSize
- maxConnectionCountPerEnforcer
- maxCachedSoHCount
- freshSoHRequest
- shaFixup
- failureCategoryCount
- ComponentTypeEnforcementClientSoH
- ComponentTypeEnforcementClientRp
- defaultProtocolMaxSize
- maxProtocolMaxSize
- minProtocolMaxSize
- ProtocolMaxSize
api_location:
- NapTypes.h
- NapEnforcementClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NAP Type Constants

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The following NAP constants are defined.

The following NAP constants are defined in NapTypes.h:

<dl> <dt>

<span id="maxSoHAttributeCount"></span><span id="maxsohattributecount"></span><span id="MAXSOHATTRIBUTECOUNT"></span>**maxSoHAttributeCount**
</dt> <dd> <dl> <dt>

0x64
</dt> <dt>



The maximum number of [**SoHAttribute**](/windows/win32/api/naptypes/ns-naptypes-sohattribute) type-length-value (TLV) objects associated with an [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet.


</dt> </dl> </dd> <dt>

<span id="maxSoHAttributeSize"></span><span id="maxsohattributesize"></span><span id="MAXSOHATTRIBUTESIZE"></span>**maxSoHAttributeSize**
</dt> <dd> <dl> <dt>

0xFA0
</dt> <dt>



The maximum size, in bytes, of a [**SoHAttribute**](/windows/win32/api/naptypes/ns-naptypes-sohattribute) object associated with a statement of health ([**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh)) packet.


</dt> </dl> </dd> <dt>

<span id="minNetworkSoHSize"></span><span id="minnetworksohsize"></span><span id="MINNETWORKSOHSIZE"></span>**minNetworkSoHSize**
</dt> <dd> <dl> <dt>

0xC
</dt> <dt>



The minimum size, in bytes, of an [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet.


</dt> </dl> </dd> <dt>

<span id="maxNetworkSoHSize"></span><span id="maxnetworksohsize"></span><span id="MAXNETWORKSOHSIZE"></span>**maxNetworkSoHSize**
</dt> <dd> <dl> <dt>

0xFA0
</dt> <dt>



The maximum size, in bytes, of an [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet.


</dt> </dl> </dd> <dt>

<span id="maxDwordCountPerSoHAttribute"></span><span id="maxdwordcountpersohattribute"></span><span id="MAXDWORDCOUNTPERSOHATTRIBUTE"></span>**maxDwordCountPerSoHAttribute**
</dt> <dd> <dl> <dt>

maxSoHAttributeSize / sizeof(DWORD)
</dt> <dt>



The maximum number of DWORD values associated with an [**SoHAttribute**](/windows/win32/api/naptypes/ns-naptypes-sohattribute).


</dt> </dl> </dd> <dt>

<span id="maxIpv4CountPerSoHAttribute"></span><span id="maxipv4countpersohattribute"></span><span id="MAXIPV4COUNTPERSOHATTRIBUTE"></span>**maxIpv4CountPerSoHAttribute**
</dt> <dd> <dl> <dt>

maxSoHAttributeSize / 0x4
</dt> <dt>



The maximum number of IPv4 addresses associated with an [**SoHAttribute**](/windows/win32/api/naptypes/ns-naptypes-sohattribute).


</dt> </dl> </dd> <dt>

<span id="maxIpv6CountPerSoHAttribute"></span><span id="maxipv6countpersohattribute"></span><span id="MAXIPV6COUNTPERSOHATTRIBUTE"></span>**maxIpv6CountPerSoHAttribute**
</dt> <dd> <dl> <dt>

maxSoHAttributeSize / 0x10
</dt> <dt>



The maximum number of IPv6 addresses associated with an [**SoHAttribute**](/windows/win32/api/naptypes/ns-naptypes-sohattribute).


</dt> </dl> </dd> <dt>

<span id="maxStringLength"></span><span id="maxstringlength"></span><span id="MAXSTRINGLENGTH"></span>**maxStringLength**
</dt> <dd> <dl> <dt>

0x400
</dt> <dt>



The maximum length of a string specified by the [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure.


</dt> </dl> </dd> <dt>

<span id="maxStringLengthInBytes"></span><span id="maxstringlengthinbytes"></span><span id="MAXSTRINGLENGTHINBYTES"></span>**maxStringLengthInBytes**
</dt> <dd> <dl> <dt>

(maxStringLength + 1) \* sizeof(WCHAR)
</dt> <dt>



The maximum length, in bytes, of a string specified by the [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure.


</dt> </dl> </dd> <dt>

<span id="maxSystemHealthEntityCount"></span><span id="maxsystemhealthentitycount"></span><span id="MAXSYSTEMHEALTHENTITYCOUNT"></span>**maxSystemHealthEntityCount**
</dt> <dd> <dl> <dt>

0x14
</dt> <dt>



The maximum number of system health entities, such as SHVs and SHAs.


</dt> </dl> </dd> <dt>

<span id="SystemHealthEntityCount"></span><span id="systemhealthentitycount"></span><span id="SYSTEMHEALTHENTITYCOUNT"></span>**SystemHealthEntityCount**
</dt> <dd> <dl> <dt>

\[range(0, maxSystemHealthEntityCount)\] 
</dt> <dt>



The range of possible values for the number of system health entities.


</dt> </dl> </dd> <dt>

<span id="maxEnforcerCount"></span><span id="maxenforcercount"></span><span id="MAXENFORCERCOUNT"></span>**maxEnforcerCount**
</dt> <dd> <dl> <dt>

0x14
</dt> <dt>



The maximum number of enforcement entities, such as QECs.


</dt> </dl> </dd> <dt>

<span id="EnforcementEntityCount"></span><span id="enforcemententitycount"></span><span id="ENFORCEMENTENTITYCOUNT"></span>**EnforcementEntityCount**
</dt> <dd> <dl> <dt>

\[range(0, maxEnforcerCount)\]
</dt> <dt>



The range of possible values for the number of enforcement entities.


</dt> </dl> </dd> <dt>

<span id="maxPrivateDataSize"></span><span id="maxprivatedatasize"></span><span id="MAXPRIVATEDATASIZE"></span>**maxPrivateDataSize**
</dt> <dd> <dl> <dt>

0xC8
</dt> <dt>



The maximum size, in bytes, of a [**PrivateData**](/windows/win32/api/naptypes/ns-naptypes-privatedata) structure.


</dt> </dl> </dd> <dt>

<span id="maxConnectionCountPerEnforcer"></span><span id="maxconnectioncountperenforcer"></span><span id="MAXCONNECTIONCOUNTPERENFORCER"></span>**maxConnectionCountPerEnforcer**
</dt> <dd> <dl> <dt>

0x14
</dt> <dt>



The maximum number of [**INapEnforcementClientConnection**](inapenforcementclientconnection.md) objects associated with an enforcement entity.


</dt> </dl> </dd> <dt>

<span id="maxCachedSoHCount"></span><span id="maxcachedsohcount"></span><span id="MAXCACHEDSOHCOUNT"></span>**maxCachedSoHCount**
</dt> <dd> <dl> <dt>

maxSystemHealthEntityCount \* maxEnforcerCount \* maxConnectionCountPerEnforcer
</dt> <dt>



The maximum number of cached SoH connections for all system health and enforcement entities.


</dt> </dl> </dd> <dt>

<span id="freshSoHRequest"></span><span id="freshsohrequest"></span><span id="FRESHSOHREQUEST"></span>**freshSoHRequest**
</dt> <dd> <dl> <dt>

0x1
</dt> <dt>



Specifies that an [**SoHResponse**](/windows/win32/api/naptypes/ns-naptypes-networksoh)is due to a new request, not a cached request. This flag is used by the NAP agent on an [**INapEnforcementClientConnection**](inapenforcementclientconnection.md) object.


</dt> </dl> </dd> <dt>

<span id="shaFixup"></span><span id="shafixup"></span><span id="SHAFIXUP"></span>**shaFixup**
</dt> <dd> <dl> <dt>

0x1
</dt> <dt>



Specifies that fix-up is required. This flag is used by a SHA.


</dt> </dl> </dd> <dt>

<span id="failureCategoryCount"></span><span id="failurecategorycount"></span><span id="FAILURECATEGORYCOUNT"></span>**failureCategoryCount**
</dt> <dd> <dl> <dt>

0x5
</dt> <dt>



The number of failure categories contained within a [**FailureCategoryMapping**](/windows/win32/api/naptypes/ns-naptypes-failurecategorymapping) structure.


</dt> </dl> </dd> <dt>

<span id="ComponentTypeEnforcementClientSoH"></span><span id="componenttypeenforcementclientsoh"></span><span id="COMPONENTTYPEENFORCEMENTCLIENTSOH"></span>**ComponentTypeEnforcementClientSoH**
</dt> <dd> <dl> <dt>

0x1
</dt> <dt>



The component is a quarantine enforcement client (QEC) that sends an [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet in-band during connection authentication.

> [!Note]  
> This value is not used by SHAs and SHVs.

 


</dt> </dl> </dd> <dt>

<span id="ComponentTypeEnforcementClientRp"></span><span id="componenttypeenforcementclientrp"></span><span id="COMPONENTTYPEENFORCEMENTCLIENTRP"></span>**ComponentTypeEnforcementClientRp**
</dt> <dd> <dl> <dt>

0x2
</dt> <dt>



The component is a QEC that implements [**INapCertRelyingParty**](inapcertrelyingparty.md) and must interact with the Health Certificate Server (HCS) in order to obtain a health certificate.

> [!Note]  
> This value is not used by SHAs and SHVs.

 


</dt> </dl> </dd> </dl>

The following NAP constants are defined in NapEnforcementClient.h.

<dl> <dt>

<span id="defaultProtocolMaxSize"></span><span id="defaultprotocolmaxsize"></span><span id="DEFAULTPROTOCOLMAXSIZE"></span>**defaultProtocolMaxSize**
</dt> <dd> <dl> <dt>

0x0FA0
</dt> <dt>



The default maximum size, in bytes, of an SoH packet.


</dt> </dl> </dd> <dt>

<span id="maxProtocolMaxSize"></span><span id="maxprotocolmaxsize"></span><span id="MAXPROTOCOLMAXSIZE"></span>**maxProtocolMaxSize**
</dt> <dd> <dl> <dt>

0xFFFF
</dt> <dt>



The maximum possible size, in bytes, of an SoH packet.


</dt> </dl> </dd> <dt>

<span id="minProtocolMaxSize"></span><span id="minprotocolmaxsize"></span><span id="MINPROTOCOLMAXSIZE"></span>**minProtocolMaxSize**
</dt> <dd> <dl> <dt>

0x012C
</dt> <dt>



The smallest possible maximum size, in bytes, of an SoH packet. The actual size of the SoH packet may be smaller than **minProtocolMaxSize**.


</dt> </dl> </dd> <dt>

<span id="ProtocolMaxSize"></span><span id="protocolmaxsize"></span><span id="PROTOCOLMAXSIZE"></span>**ProtocolMaxSize**
</dt> <dd> <dl> <dt>

range(minProtocolMaxSize, maxProtocolMaxSize)
</dt> <dt>



The range of possible values for the maximum size of a SoH packet.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                |
| Header<br/>                   | <dl> <dt>NapTypes.h; </dt> <dt>NapEnforcementClient.h</dt> </dl> |



## See also

<dl> <dt>

[**NAP Constants**](nap-constants.md)
</dt> </dl>

 

 





