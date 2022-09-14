---
description: PNRP uses the WSASetService function to register or remove peer names.
ms.assetid: ea7941cd-2b3c-42d1-a291-759cbc32db0c
title: PNRP and WSASetService
ms.topic: article
ms.date: 05/31/2018
---

# PNRP and WSASetService

PNRP uses the [**WSASetService**](winsock-nsp-reference-links.md) function to register or remove [peer names](peer-names.md).

## Registering a Name

Registration includes a peer name and set of endpoints where a service can be contacted. A registration is specific to a PNRP cloud. After a peer is registered, there is a delay between the registration and the propagation of the registration information to other nodes. During this time, other nodes may not be able to resolve a newly registered peer.

Service registration is not persistent.

-   If a client process that registers a peer name exits or calls [**WSACleanup**](winsock-nsp-reference-links.md), then the peer name is unregistered.
-   If a specified peer name is already registered in the same cloud by the current process, it is replaced with new registration values.

When registering a peer name, the following parameter values must be indicated:

-   *essOperation* parameter must have a value of **RNRSERVICE\_REGISTER**.
-   *dwControlFlags* parameter must be zero (0).

When registering a peer name, the [**LPWSAQUERYSET**](pnrp-and-wsaqueryset.md) structure referenced by the *lpqsRegInfo* parameter must contain the following values:

<dl> <dt>

<span id="dwSize"></span><span id="dwsize"></span><span id="DWSIZE"></span>**dwSize**
</dt> <dd>

Specifies the size of this structure.

</dd> <dt>

<span id="lpszServiceInstanceName"></span><span id="lpszserviceinstancename"></span><span id="LPSZSERVICEINSTANCENAME"></span>**lpszServiceInstanceName**
</dt> <dd>

Specifies a peer name to register. If the [peer name](peer-names.md) is unsecured, then the identity is optional. If the identity is specified as **NULL**, PNRP uses the machine local identity—by default.

</dd> <dt>

<span id="lpServiceClassID"></span><span id="lpserviceclassid"></span><span id="LPSERVICECLASSID"></span>**lpServiceClassID**
</dt> <dd>

Must be SVCID\_PNRPNAME.

</dd> <dt>

<span id="lpVersion"></span><span id="lpversion"></span><span id="LPVERSION"></span>**lpVersion**
</dt> <dd>

Ignored. Set to **NULL**.

</dd> <dt>

<span id="lpszComment"></span><span id="lpszcomment"></span><span id="LPSZCOMMENT"></span>**lpszComment**
</dt> <dd>

Ignored. However, the string is still required to be fewer than 40 characters, including the **NULL** terminator.

</dd> <dt>

<span id="dwNameSpace"></span><span id="dwnamespace"></span><span id="DWNAMESPACE"></span>**dwNameSpace**
</dt> <dd>

Must be either **NS\_PNRPNAME** or **NS\_ALL**.

</dd> <dt>

<span id="lpNSProviderID"></span><span id="lpnsproviderid"></span><span id="LPNSPROVIDERID"></span>**lpNSProviderID**
</dt> <dd>

Must be either **NS\_PROVIDER\_PNRPNAME** or **NULL**.

</dd> <dt>

<span id="lpszContext"></span><span id="lpszcontext"></span><span id="LPSZCONTEXT"></span>**lpszContext**
</dt> <dd>

Must be a cloud name, an empty string, or **NULL**. If this value is **NULL** or an empty string, the default cloud, "Global", is used. Otherwise, it must point to a valid cloud name.

</dd> <dt>

<span id="dwNumberOfProtocols"></span><span id="dwnumberofprotocols"></span><span id="DWNUMBEROFPROTOCOLS"></span>**dwNumberOfProtocols**
</dt> <dd>

Ignored. Set to zero (0).

</dd> <dt>

<span id="lpszQueryString"></span><span id="lpszquerystring"></span><span id="LPSZQUERYSTRING"></span>**lpszQueryString**
</dt> <dd>

Ignored. Set to **NULL**.

</dd> <dt>

<span id="dwNumberOfCsAddrs"></span><span id="dwnumberofcsaddrs"></span><span id="DWNUMBEROFCSADDRS"></span>**dwNumberOfCsAddrs**
</dt> <dd>

Specifies the number of addresses registered by a service. The maximum number of addresses that can be registered for a single name is 10.

</dd> <dt>

<span id="lpcsaBuffer"></span><span id="lpcsabuffer"></span><span id="LPCSABUFFER"></span>**lpcsaBuffer**
</dt> <dd>

Pointer to a list of addresses to register.

</dd> <dt>

<span id="dwOutputFlags"></span><span id="dwoutputflags"></span><span id="DWOUTPUTFLAGS"></span>**dwOutputFlags**
</dt> <dd>

Ignored. Set to zero (0).

</dd> <dt>

<span id="lpBlob"></span><span id="lpblob"></span><span id="LPBLOB"></span>**lpBlob**
</dt> <dd>

Pointer to a [**BLOB**](winsock-nsp-reference-links.md) structure that points to a [**PNRPINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpinfo_v1) structure. Specific parameters in the **PNRPINFO** structure must be set. For more information, see the following **PNRPINFO** structure section.

</dd> </dl>

## PNRPINFO Structure

If the **lpBlob** member of the [**LPWSAQUERYSET**](pnrp-and-wsaqueryset.md) structure is set, the following members of the [**PNRPINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpinfo_v1) structure must be set:

<dl> <dt>

<span id="dwSize"></span><span id="dwsize"></span><span id="DWSIZE"></span>**dwSize**
</dt> <dd>

Specifies the size of this structure.

</dd> <dt>

<span id="lpwszIdentity"></span><span id="lpwszidentity"></span><span id="LPWSZIDENTITY"></span>**lpwszIdentity**
</dt> <dd>

Specifies the identity of the peer name that is created by using [**PeerIdentityCreate**](/windows/desktop/api/P2P/nf-p2p-peeridentitycreate). If a peer name is unsecured, then the identity is optional. If the identity is specified as **NULL**, PNRP uses the computer local identity—by default.

</dd> <dt>

<span id="nMaxResolve"></span><span id="nmaxresolve"></span><span id="NMAXRESOLVE"></span>**nMaxResolve**
</dt> <dd>

Ignored. Set to zero (0).

</dd> <dt>

<span id="dwTimeout"></span><span id="dwtimeout"></span><span id="DWTIMEOUT"></span>**dwTimeout**
</dt> <dd>

Ignored. Set to zero (0).

</dd> <dt>

<span id="dwLifetime"></span><span id="dwlifetime"></span><span id="DWLIFETIME"></span>**dwLifetime**
</dt> <dd>

Specifies the number of seconds between refresh operations.

</dd> <dt>

<span id="enResolveCriteria"></span><span id="enresolvecriteria"></span><span id="ENRESOLVECRITERIA"></span>**enResolveCriteria**
</dt> <dd>

Ignored. Set to zero (0).

</dd> <dt>

<span id="dwFlags"></span><span id="dwflags"></span><span id="DWFLAGS"></span>**dwFlags**
</dt> <dd>

Must be either zero (0) or **PNRPINFO\_HINT**. The default is zero (0). This means that the service location portion of the PNRP ID is built by using the IP address in **saHint**. Otherwise, the service location is built by using the first IP address in the first IPv6 entry of the **lpcsaBuffer** member.

</dd> <dt>

<span id="saHint"></span><span id="sahint"></span><span id="SAHINT"></span>**saHint**
</dt> <dd>

Specifies the IPv6 address for the hint.

</dd> <dt>

<span id="enNameState"></span><span id="ennamestate"></span><span id="ENNAMESTATE"></span>**enNameState**
</dt> <dd>

Ignored. Set to zero (0).

</dd> </dl>

## Unregistering a Peer Name

The following list identifies the important information about unregistering a peer name.

-   Only an application that registers a peer name can unregister it.
-   A peer name is unregistered automatically if [**WSACleanup**](winsock-nsp-reference-links.md) is called.
-   PNRP always removes the entire service name registration. It does not allow removal of individual addresses.
-   When unregistering a name, the *essOperation* parameter must have a value of **RNRSERVICE\_DELETE**.
-   PNRP does not support the value **RNRSERVICE\_DEREGISTER**.
-   The *dwControlFlags* parameter must be zero (0).

When unregistering a name, the [**LPWSAQUERYSET**](pnrp-and-wsaqueryset.md) structure that the *lpqsRegInfo* parameter references must contain the following values:

<dl> <dt>

<span id="dwSize"></span><span id="dwsize"></span><span id="DWSIZE"></span>**dwSize**
</dt> <dd>

Specifies the size of this structure.

</dd> <dt>

<span id="lpszServiceInstanceName"></span><span id="lpszserviceinstancename"></span><span id="LPSZSERVICEINSTANCENAME"></span>**lpszServiceInstanceName**
</dt> <dd>

Specifies a peer name to unregister.

</dd> <dt>

<span id="lpServiceClassID"></span><span id="lpserviceclassid"></span><span id="LPSERVICECLASSID"></span>**lpServiceClassID**
</dt> <dd>

Must be **SVCID\_PNRPNAME**.

</dd> <dt>

<span id="lpVersion"></span><span id="lpversion"></span><span id="LPVERSION"></span>**lpVersion**
</dt> <dd>

Ignored. Set to **NULL**.

</dd> <dt>

<span id="lpszComment"></span><span id="lpszcomment"></span><span id="LPSZCOMMENT"></span>**lpszComment**
</dt> <dd>

Ignored. Set to **NULL**.

</dd> <dt>

<span id="dwNameSpace"></span><span id="dwnamespace"></span><span id="DWNAMESPACE"></span>**dwNameSpace**
</dt> <dd>

Must be either **NS\_PNRPNAME** or **NS\_ALL**.

</dd> <dt>

<span id="lpNSProviderID"></span><span id="lpnsproviderid"></span><span id="LPNSPROVIDERID"></span>**lpNSProviderID**
</dt> <dd>

Must be either **NS\_PROVIDER\_PNRPNAME** or **NULL**.

</dd> <dt>

<span id="lpszContext"></span><span id="lpszcontext"></span><span id="LPSZCONTEXT"></span>**lpszContext**
</dt> <dd>

Must be a cloud name, an empty string, or **NULL**. If this value is **NULL** or an empty string, the default cloud, "Global" is used. Otherwise, it must point to a valid cloud name.

</dd> <dt>

<span id="dwNumberOfProtocols"></span><span id="dwnumberofprotocols"></span><span id="DWNUMBEROFPROTOCOLS"></span>**dwNumberOfProtocols**
</dt> <dd>

Ignored. Set to zero (0).

</dd> <dt>

<span id="lpszQueryString"></span><span id="lpszquerystring"></span><span id="LPSZQUERYSTRING"></span>**lpszQueryString**
</dt> <dd>

Ignored. Set to **NULL**.

</dd> <dt>

<span id="dwNumberOfCsAddrs"></span><span id="dwnumberofcsaddrs"></span><span id="DWNUMBEROFCSADDRS"></span>**dwNumberOfCsAddrs**
</dt> <dd>

Ignored. Set to **NULL**.

</dd> <dt>

<span id="lpcsaBuffer"></span><span id="lpcsabuffer"></span><span id="LPCSABUFFER"></span>**lpcsaBuffer**
</dt> <dd>

Ignored. Set to **NULL**.

</dd> <dt>

<span id="dwOutputFlags"></span><span id="dwoutputflags"></span><span id="DWOUTPUTFLAGS"></span>**dwOutputFlags**
</dt> <dd>

Ignored. Set to zero (0).

</dd> <dt>

<span id="lpBlob"></span><span id="lpblob"></span><span id="LPBLOB"></span>**lpBlob**
</dt> <dd>

Pointer to a [**BLOB**](winsock-nsp-reference-links.md) structure that points to a [**PNRPINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpinfo_v1) structure. The **lpszIdentity** member of the **lpBlob** structure identifies the name of the identity that is used to register a peer name. The remaining members must be set to the same values that are used when registering a name.

</dd> </dl>

## Related topics

<dl> <dt>

[PNRP and BLOB](pnrp-and-blob.md)
</dt> <dt>

[PNRP and WSAQUERYSET](pnrp-and-wsaqueryset.md)
</dt> <dt>

[**PNRPINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpinfo_v1)
</dt> <dt>

[PNRP NSP Error Codes](pnrp-nsp-error-codes.md)
</dt> <dt>

[**WSACleanup**](winsock-nsp-reference-links.md)
</dt> <dt>

**WSASetService**
</dt> </dl>

 

 



