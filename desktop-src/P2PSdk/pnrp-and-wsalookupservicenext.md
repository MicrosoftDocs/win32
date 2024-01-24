---
description: PNRP uses the WSALookupServiceNext function to match queries specified in a previous call to WSALookupServiceBegin.
ms.assetid: b3e1abf4-ff59-481d-b96e-f8916a47cd52
title: PNRP and WSALookupServiceNext
ms.topic: article
ms.date: 05/31/2018
---

# PNRP and WSALookupServiceNext

PNRP uses the [**WSALookupServiceNext**](winsock-nsp-reference-links.md) function to match queries specified in a previous call to **WSALookupServiceBegin**. The results of the **WSALookupServiceNext** function are determined by settings in the **WSAQUERYSET** structure passed in the initial **WSALookupServiceBegin** function call. This function is used to perform the following two functions:

-   Resolving a peer name to a list of addresses
-   Enumerating network clouds

By using [**WSANSPIoctl**](winsock-nsp-reference-links.md), the lookup service can be used asynchronously. For information about using the lookup service functions asynchronously, see [PNRP and WSANSPIoctl](pnrp-and-wsanspioctl.md).

The [**WSALookupServiceNext**](winsock-nsp-reference-links.md) function blocks even if **WSANSPIoctl** is called. Before calling **WSALookupServiceNext**, an application must wait until it receives a notification—if blocking is an issue.

## Resolving a Peer Name to a List of Addresses

When resolving a peer name to a list of addresses, the [**LPWSAQUERYSET**](pnrp-and-wsaqueryset.md) structure returned in the *lpqsResults* parameter contains the following values:

<dl> <dt>

<span id="dwSize"></span><span id="dwsize"></span><span id="DWSIZE"></span>**dwSize**
</dt> <dd>

Returns the size of the structure.

</dd> <dt>

<span id="lpszServiceInstanceName"></span><span id="lpszserviceinstancename"></span><span id="LPSZSERVICEINSTANCENAME"></span>**lpszServiceInstanceName**
</dt> <dd>

Returns a peer name—if **LUP\_RETURN\_NAME**, **LUP\_RETURN\_ALL**, or **NULL** are specified.

</dd> <dt>

<span id="lpServiceClassID"></span><span id="lpserviceclassid"></span><span id="LPSERVICECLASSID"></span>**lpServiceClassID**
</dt> <dd>

Returns **SVCID\_PNRPNAME**.

</dd> <dt>

<span id="lpVersion"></span><span id="lpversion"></span><span id="LPVERSION"></span>**lpVersion**
</dt> <dd>

Returns **NULL**.

</dd> <dt>

<span id="lpszComment"></span><span id="lpszcomment"></span><span id="LPSZCOMMENT"></span>**lpszComment**
</dt> <dd>

Returns a comment—if **LUP\_RETURN\_COMMENT**, **LUP\_RETURN\_ALL**, or **NULL** are specified.

</dd> <dt>

<span id="dwNameSpace"></span><span id="dwnamespace"></span><span id="DWNAMESPACE"></span>**dwNameSpace**
</dt> <dd>

Returns **NS\_PNRPNAME**.

</dd> <dt>

<span id="lpNSProviderID"></span><span id="lpnsproviderid"></span><span id="LPNSPROVIDERID"></span>**lpNSProviderID**
</dt> <dd>

Returns **NS\_PROVIDER\_PNRPNAME**.

</dd> <dt>

<span id="lpszContext"></span><span id="lpszcontext"></span><span id="LPSZCONTEXT"></span>**lpszContext**
</dt> <dd>

Returns the cloud name if **LUP\_RETURN\_NAME**, **LUP\_RETURN\_ALL**, or **NULL** are specified.

</dd> <dt>

<span id="dwNumberOfProtocols"></span><span id="dwnumberofprotocols"></span><span id="DWNUMBEROFPROTOCOLS"></span>**dwNumberOfProtocols**
</dt> <dd>

Returns zero (0).

</dd> <dt>

<span id="lpszQueryString"></span><span id="lpszquerystring"></span><span id="LPSZQUERYSTRING"></span>**lpszQueryString**
</dt> <dd>

Returns **NULL**.

</dd> <dt>

<span id="dwNumberOfCsAddrs"></span><span id="dwnumberofcsaddrs"></span><span id="DWNUMBEROFCSADDRS"></span>**dwNumberOfCsAddrs**
</dt> <dd>

Returns the number of entries in the CSADDR\_INFO array if **LUP\_RETURN\_ADDR**, **LUP\_RETURN\_ALL**, or **NULL** are specified. This value and the information in **lpcsaBuffer** are the key bits of information returned in this structure.

</dd> <dt>

<span id="lpcsaBuffer"></span><span id="lpcsabuffer"></span><span id="LPCSABUFFER"></span>**lpcsaBuffer**
</dt> <dd>

Returns a pointer to an array of CSADDR\_INFO structures if **LUP\_RETURN\_ADDR**, **LUP\_RETURN\_ALL**, or **NULL** are specified. This buffer and the value in **dwNumberOfCsAddrs** are the key information bits returned in this structure.

</dd> <dt>

<span id="dwOutputFlags"></span><span id="dwoutputflags"></span><span id="DWOUTPUTFLAGS"></span>**dwOutputFlags**
</dt> <dd>

Returns zero (0).

</dd> <dt>

<span id="lpBlob"></span><span id="lpblob"></span><span id="LPBLOB"></span>**lpBlob**
</dt> <dd>

Returns **NULL**.

</dd> </dl>

## Enumerating Network Clouds

When enumerating clouds, the [**LPWSAQUERYSET**](pnrp-and-wsaqueryset.md) structure returned in the *lpqsResults* parameter contains the following values:

<dl> <dt>

<span id="dwSize"></span><span id="dwsize"></span><span id="DWSIZE"></span>**dwSize**
</dt> <dd>

Returns the size of the structure.

</dd> <dt>

<span id="lpszServiceInstanceName"></span><span id="lpszserviceinstancename"></span><span id="LPSZSERVICEINSTANCENAME"></span>**lpszServiceInstanceName**
</dt> <dd>

Returns a cloud name—if **LUP\_RETURN\_NAME**, **LUP\_RETURN\_ALL**, or **NULL** are specified.

</dd> <dt>

<span id="lpServiceClassID"></span><span id="lpserviceclassid"></span><span id="LPSERVICECLASSID"></span>**lpServiceClassID**
</dt> <dd>

Returns **SVCID\_PNRPCLOUD**.

</dd> <dt>

<span id="lpVersion"></span><span id="lpversion"></span><span id="LPVERSION"></span>**lpVersion**
</dt> <dd>

Returns **NULL**.

</dd> <dt>

<span id="lpszComment"></span><span id="lpszcomment"></span><span id="LPSZCOMMENT"></span>**lpszComment**
</dt> <dd>

Returns **NULL**.

</dd> <dt>

<span id="dwNameSpace"></span><span id="dwnamespace"></span><span id="DWNAMESPACE"></span>**dwNameSpace**
</dt> <dd>

Returns **NS\_PNRPCLOUD**.

</dd> <dt>

<span id="lpNSProviderID"></span><span id="lpnsproviderid"></span><span id="LPNSPROVIDERID"></span>**lpNSProviderID**
</dt> <dd>

Returns **NS\_PROVIDER\_PNRPCLOUD**.

</dd> <dt>

<span id="lpszContext"></span><span id="lpszcontext"></span><span id="LPSZCONTEXT"></span>**lpszContext**
</dt> <dd>

Returns **NULL**.

</dd> <dt>

<span id="dwNumberOfProtocols"></span><span id="dwnumberofprotocols"></span><span id="DWNUMBEROFPROTOCOLS"></span>**dwNumberOfProtocols**
</dt> <dd>

Returns zero (0).

</dd> <dt>

<span id="lpszQueryString"></span><span id="lpszquerystring"></span><span id="LPSZQUERYSTRING"></span>**lpszQueryString**
</dt> <dd>

Returns **NULL**.

</dd> <dt>

<span id="dwNumberOfCsAddrs"></span><span id="dwnumberofcsaddrs"></span><span id="DWNUMBEROFCSADDRS"></span>**dwNumberOfCsAddrs**
</dt> <dd>

Returns zero (0).

</dd> <dt>

<span id="lpcsaBuffer"></span><span id="lpcsabuffer"></span><span id="LPCSABUFFER"></span>**lpcsaBuffer**
</dt> <dd>

Returns **NULL**.

</dd> <dt>

<span id="dwOutputFlags"></span><span id="dwoutputflags"></span><span id="DWOUTPUTFLAGS"></span>**dwOutputFlags**
</dt> <dd>

Returns zero (0).

</dd> <dt>

<span id="lpBlob"></span><span id="lpblob"></span><span id="LPBLOB"></span>**lpBlob**
</dt> <dd>

Returns a pointer to a [**BLOB**](winsock-nsp-reference-links.md) structure that points to a [**PNRPCLOUDINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpcloudinfo) structure—if **LUP\_RETURN\_BLOB**, **LUP\_RETURN\_ALL**, or **NULL** are specified.

</dd> </dl>

## PNRPCLOUDINFO Structure

When enumerating cloud names, the following values are returned in the [**PNRPCLOUDINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpcloudinfo) structure:

<dl> <dt>

<span id="dwSize"></span><span id="dwsize"></span><span id="DWSIZE"></span>**dwSize**
</dt> <dd>

The size of this structure.

</dd> <dt>

<span id="Cloud"></span><span id="cloud"></span><span id="CLOUD"></span>**Cloud**
</dt> <dd>

The actual cloud value.

</dd> <dt>

<span id="enCloudState"></span><span id="encloudstate"></span><span id="ENCLOUDSTATE"></span>**enCloudState**
</dt> <dd>

The current state of a cloud. [**PNRP\_CLOUD\_STATE**](/windows/desktop/api/Pnrpdef/ne-pnrpdef-pnrp_cloud_state) specifies the valid values.

</dd> <dt>

<span id="enCloudFlags"></span><span id="encloudflags"></span><span id="ENCLOUDFLAGS"></span>**enCloudFlags**
</dt> <dd>

Indicates that a cloud name is valid on a network, or only valid on a current computer. [**PNRP\_CLOUD\_FLAGS**](/windows/desktop/api/Pnrpdef/ne-pnrpdef-pnrp_cloud_flags) specifies the valid values. Some cloud names are valid on any computer on the same network. Other cloud names are valid only on a current computer, and may be valid only for a period of time.

-   If **enCloudFlags** is set to **PNRP\_CLOUD\_NAME\_LOCAL,** the name is only valid locally.
-   If **enCloudFlags** is not set, then the cloud name can be transferred to other computers.

</dd> </dl>

## Related topics

<dl> <dt>

[PNRP and BLOB](pnrp-and-blob.md)
</dt> <dt>

[PNRP and WSALookupServiceEnd](pnrp-and-wsalookupserviceend.md)
</dt> <dt>

[PNRP and WSANSPIoctl](pnrp-and-wsanspioctl.md)
</dt> <dt>

[PNRP and WSAQUERYSET](pnrp-and-wsaqueryset.md)
</dt> <dt>

[**PNRPCLOUDINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpcloudinfo)
</dt> <dt>

[**PNRPINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpinfo_v1)
</dt> <dt>

[PNRP NSP Error Codes](pnrp-nsp-error-codes.md)
</dt> <dt>

[**WSALookupServiceBegin**](winsock-nsp-reference-links.md)
</dt> </dl>

 

 



