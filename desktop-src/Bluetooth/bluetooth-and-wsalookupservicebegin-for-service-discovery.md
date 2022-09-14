---
title: Bluetooth and WSALookupServiceBegin for Service Discovery
description: To discover the existence of a particular service on a Bluetooth server, clients use the WSALookupServiceBegin, WSALookupServiceNext, and WSALookupServiceEnd functions.
ms.assetid: d9961600-cdca-42ec-92eb-118b8186ed2e
keywords:
- Bluetooth and WSALookupServiceBegin for Service Discovery Bluetooth
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and WSALookupServiceBegin for Service Discovery

To discover the existence of a particular service on a Bluetooth server, clients use the [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina), [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta), and [**WSALookupServiceEnd**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupserviceend) functions. Queries can be performed for local and remote addresses, but connections can only be established with remote addresses. Service handles discovered during this operation cannot be used to delete the service via [**WSASetService**](/windows/desktop/api/winsock2/nf-winsock2-wsasetservicea). Loopback is not supported by RFCOMM.

Two basic types of service discovery queries can be performed:

-   Queries for one or more services on the local device
-   Queries for one or more services on a specified peer device

The [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) function receives a [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure in its *lpqsRestrictions* parameter. **WSALookupServiceBegin** performs a client query based on the set of search restrictions that the **WSAQUERYSET** contains. Bluetooth clients must specify the restrictions, listed in the following table, in the **WSAQUERYSET** structure when using the **WSALookupServiceBegin** function to query for services.



| WSAQUERYSET member    | Restriction                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **dwSize**            | Set to **sizeof**([**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw)).                                                                                                                                                                                                                                                                                                                    |
| **lpServiceClassId**  | Set to the most specific Bluetooth UUID that can be used to determine the scope of the query. For example, setting **lpServiceClassId** to the UUID of the L2CAP protocol results in all L2CAP services returned, essentially enumerating all SD records on the target. Setting the UUID to a specific service, however, returns only the instances of that service.<br/> |
| **dwNameSpace**       | Set to **NS\_BTH**.                                                                                                                                                                                                                                                                                                                                                             |
| **dwNumberOfCsAddrs** | Set to 0.                                                                                                                                                                                                                                                                                                                                                                       |
| **lpszContext**       | Set to the Bluetooth Device Address with which to establish an SDP connection to perform the query of services. This member must be a string that is converted by using the [**WSAAddressToString**](/windows/desktop/api/winsock2/nf-winsock2-wsaaddresstostringa) function. If the local radio address is supplied, the local SDP records are searched.<br/>                                             |
| Other members         | All other members of the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure are ignored.                                                                                                                                                                                                                                                                                        |



 

The SDP connection to the remote device does not remain active after the [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) function completes a service query; the connection is terminated before **WSALookupServiceBegin** returns. Applications that require the SDP connection to remain active after a service query completes should specify the service class UUID to which to connect by using the **serviceClassId** member of the [**SOCKADDR\_BTH**](/windows/desktop/api/Ws2bth/ns-ws2bth-sockaddr_bth) structure when issuing the Windows Sockets [**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect) function call.

The flags, listed in the following table, are used in the *dwControlFlags* parameter of the [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) and [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) functions to control the query results. The **LUP\_CONTAINERS** and **LUP\_FLUSHCACHE** flags are used by the **WSALookupServiceBegin** function; the rest of the flags are used in calls to the **WSALookupServiceNext** function.


| Flag | Result | 
|------|--------|
| <strong>LUP_CONTAINERS</strong> | Must not be set. | 
| <strong>LUP_FLUSHCACHE</strong> | Applications should generally specify <strong>LUP_FLUSHCACHE</strong>. This flag instructs the system to ignore any cached information and establish an over-the-air SDP connection to the specified device to perform the SDP search. This non-cached operation may take several seconds (whereas a cached search returns quickly). Bluetooth currently does not proactively cache SDP records from nearby devices, nor does it currently aggressively cache previous queries. Therefore, applications should anticipate that queries may return no results (with an error code of <strong>WSASERVICE_NOT_FOUND</strong>) if <strong>LUP_FLUSHCACHE</strong> is not specified. The cached data that is available by using the Windows Sockets interface may be enhanced in the future. | 
| <strong>LUP_RES_SERVICE</strong> | Return information about the local Bluetooth address. This flag has an effect only if <strong>LUP_RETURN_ADDR</strong> is also specified. | 
| <strong>LUP_RETURN_NAME</strong> | Return the display name of the service in the <strong>lpszServiceInstanceName</strong> member of the <a href="/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw"><strong>WSAQUERYSET</strong></a> structure for each call to the <a href="/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta"><strong>WSALookupServiceNext</strong></a> function. | 
| <strong>LUP_RETURN_TYPE</strong> | Return the service class ID in the <strong>lpServiceClassId</strong> member of the <a href="/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw"><strong>WSAQUERYSET</strong></a> structure.<blockquote>[!Note]<br />Use of this flag is only applicable to the <a href="/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina"><strong>WSALookupServiceBegin</strong></a> function. This value is always zero for <a href="/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta"><strong>WSALookupServiceNext</strong></a>.</blockquote><br /> | 
| <strong>LUP_RETURN_ADDR</strong> | Return an address in the <strong>lpcsaBuffer</strong> member to be used with <a href="/windows/desktop/api/winsock2/nf-winsock2-connect"><strong>connect</strong></a> function calls. The returned address contains the port number. | 
| <strong>LUP_RETURN_BLOB</strong> | Return the matching SD records in the <strong>lpBlob</strong> member, formatted according to the Bluetooth SDP record specification. | 
| <strong>LUP_RETURN_ALL</strong> | Return all of the above flags' information. | 
| <strong>LUP_RETURN_COMMENT</strong> | Return the service description in the <strong>lpszComment</strong> member of the <a href="/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw"><strong>WSAQUERYSET</strong></a> structure for each call to the <a href="/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta"><strong>WSALookupServiceNext</strong></a> function. | 
| <strong>LUP_FLUSHPREVIOUS</strong> | Skip the next available record, and return the record that follows it. | 




 

## Advanced Service Queries

The query operations that are described in the previous section can be used to return all results from a single GUID, which should be sufficient for most applications. An advanced query enables an application to create a more specific query; it provides the capability to match UUIDs and attributes in returned information.

To perform an advanced query for services, Bluetooth clients must specify the following restrictions in the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure that is passed into the *lpqsRestrictions* parameter.



| WSAQUERYSET member   | Restriction                                                                                                                                                                                                                                                                                                                         |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **dwSize**           | Set to **sizeof**([**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw)).                                                                                                                                                                                                                                                                        |
| **lpszContext**      | Set to the Bluetooth Device Address with which to establish an SDP connection to perform the query of services. This member must be a string that is converted by using the [**WSAAddressToString**](/windows/desktop/api/winsock2/nf-winsock2-wsaaddresstostringa) function. If the local radio address is supplied, the local SDP records are searched.<br/> |
| **lpBlob.pBlobData** | Pointer to a [**BTH\_QUERY\_SERVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-bth_query_service) structure that contains all parameters that limit the results of the query.                                                                                                                                                                                           |
| **dwNameSpace**      | Set to **NS\_BTH**.                                                                                                                                                                                                                                                                                                                 |
| Other members        | All other members of the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure are ignored.                                                                                                                                                                                                                                            |



 

The following flags are passed in the *dwControlFlags* parameter of [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) to control the results of an advanced query.

| Flag                     | Result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LUP\_CONTAINERS**      | Must not be set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **LUP\_FLUSHCACHE**      | Applications should generally specify **LUP\_FLUSHCACHE**. This flag instructs the system to ignore any cached information and establish an over-the-air SDP connection to the specified device to perform the SDP search. This non-cached operation may take several seconds (whereas a cached search returns quickly). Bluetooth does not proactively cache SDP records from nearby devices, nor does it aggressively cache previous queries. Therefore applications should expect that queries may frequently return no results (**WSASERVICE\_NOT\_FOUND**) if **LUP\_FLUSHCACHE** is not specified. The cached data that is available by using the Windows Sockets interface may be enhanced in the future. |
| **LUP\_RES\_SERVICE**    | Return information for the local Bluetooth Address. Setting this flag has an effect only if **LUP\_RETURN\_ADDRR** is also specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **LUP\_RETURN\_NAME**    | Return the display name of the service. This flag is ignored for **SDP\_SERVICE\_SEARCH\_REQUEST**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **LUP\_RETURN\_TYPE**    | Return the service class ID. This flag is ignored for **SDP\_SERVICE\_SEARCH\_REQUEST**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **LUP\_RETURN\_ADDR**    | Return an address in the **lpcsaBuffer** member to be used with [**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect) function calls. The returned address contains the port number. This flag is ignored for **SDP\_SERVICE\_SEARCH\_REQUEST**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **LUP\_RETURN\_BLOB**    | Return the matching SD records in a format that conforms to the Bluetooth SDP record specification. For **SDP\_SERVICE\_SEARCH\_REQUEST**, the result in **lpBlob** for the subsequent call to [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) is an array of Bluetooth SDP handles. For **SDP\_SERVICE\_ATTRIBUTE\_REQUEST** and **SDP\_SERVICE\_SEARCH\_ATTRIBUTE\_REQUEST**, the result for each subsequent call to **WSALookupServiceNext** is a binary Bluetooth SDP record whose attributes are restricted to those specified by the **pRange** member of the query. This flag is required for **SDP\_SERVICE\_SEARCH\_REQUEST**.                                                               |
| **LUP\_RETURN\_COMMENT** | Return the service description in the **lpszComment** member of the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure for each call to the [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **LUP\_FLUSHPREVIOUS**   | Skip the next available record, and return the record that follows it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |



 

On input, **lpBlob**->**pBlobData** points to a [**BTH\_QUERY\_SERVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-bth_query_service) structure that contains the values listed in the following table.

> [!Note]  
> The initial search request must be able to fit into one L2CAP packet. The response, however, may be broken into many L2CAP packets.

 



| Member            | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **type**          | Type of search to perform. This value can be one of **SDP\_SERVICE\_SEARCH\_REQUEST**, **SDP\_SERVICE\_ATTRIBUTE\_REQUEST**, or **SDP\_SERVICE\_SEARCH\_ATTRIBUTE\_REQUEST**. Each search type is associated with an underlying search mechanism that is defined by the Bluetooth SDP specification. Each return results in the form described by the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure that is defined earlier in this (Advanced Service Queries) section. |
| **serviceHandle** | Used for attribute searches. This value specifies the service handle with which to query the attributes in the **pRange** member.                                                                                                                                                                                                                                                                                                                                            |
| **uuids**         | Used for service and **serviceAttribute** searches. This value specifies the UUIDs that a record must contain to match the search. If less than **MAX\_UUIDS\_IN\_QUERY** UUIDs are to be queried, this value sets the SdpQueryUuid element that immediately follows the last valid UUID to all zeros.                                                                                                                                                                       |
| **numRange**      | Used for attribute and **serviceAttribute** searches. This value specifies the number of elements in **pRange**.                                                                                                                                                                                                                                                                                                                                                             |
| **pRange**        | Used for attribute and **serviceAttribute** searches. This value specifies the attribute values to retrieve for any matching records.                                                                                                                                                                                                                                                                                                                                        |



 

After each successful call to the [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) function, **lpBlob**->**pBlobData** points to a block of data that contains the values listed in the following table.

| Value                                                                                | Description                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SDP\_SERVICE\_SEARCH\_REQUEST**                                                    | An array of SDP record handles that is identical to the **ServiceRecordHandleList** defined by Bluetooth 1.1 SDP 4.5.2. The number of SDP handles that is returned is calculated by (**lpBlob**->cbSize)/**sizeof**(ULONG). All results are returned in a single call to the [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) function. |
| **SDP\_SERVICE\_ATTRIBUTE\_REQUEST** or **SDP\_SERVICE\_SEARCH\_ATTRIBUTE\_REQUEST** | A binary Bluetooth SDP record. For **SDP\_SERVICE\_ATTRIBUTE\_REQUEST**, all results are returned in a single call to the [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) function.                                                                                                                                                       |



 

> [!Note]  
> If the **lpBlob** member is not specified during input for a service query, a service and attribute search is performed for the service specified in the **lpServiceClassId** member on attributes from 0 through 0xFFFF.

 

## Related topics

<dl> <dt>

[Bluetooth and WSAQUERYSET for Service Inquiry](bluetooth-and-wsaqueryset-for-service-inquiry.md)
</dt> <dt>

[Discovering Bluetooth Devices and Services](discovering-bluetooth-devices-and-services.md)
</dt> <dt>

[Bluetooth and WSALookupServiceNext](bluetooth-and-wsalookupservicenext.md)
</dt> <dt>

[Bluetooth and WSALookupServiceBegin for Device Inquiry](bluetooth-and-wsalookupservicebegin-for-device-inquiry.md)
</dt> <dt>

[**BTH\_QUERY\_SERVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-bth_query_service)
</dt> <dt>

[**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect)
</dt> <dt>

[**SOCKADDR\_BTH**](/windows/desktop/api/Ws2bth/ns-ws2bth-sockaddr_bth)
</dt> <dt>

[**WSAAddressToString**](/windows/desktop/api/winsock2/nf-winsock2-wsaaddresstostringa)
</dt> <dt>

[**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina)
</dt> <dt>

[**WSALookupServiceEnd**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupserviceend)
</dt> <dt>

[**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta)
</dt> <dt>

[**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw)
</dt> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> </dl>

