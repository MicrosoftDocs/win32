---
Description: This section describes the protocol-specific Quality of Service (QOS) structure for ATM, which is contained in the ProviderSpecific field of the QOS structure.
ms.assetid: ec7882f7-7197-439a-82a4-ff081505a9d7
title: Winsock ATM QoS Extension
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Winsock ATM QoS Extension

This section describes the protocol-specific Quality of Service ([**QOS**](https://msdn.microsoft.com/windows/desktop/859faa13-bd66-46ee-8452-6ff5d53d66c9)) structure for ATM, which is contained in the [ProviderSpecific](https://msdn.microsoft.com/windows/desktop/16c99de7-be29-4e58-b648-b6719385dc1c) field of the **QOS** structure. Note that the use of this ATM-specific **QOS** structure is optional by Windows Sockets 2 clients, and the ATM service provider is required to map the generic [**FLOWSPEC**](https://msdn.microsoft.com/windows/desktop/268e0d3a-2b04-40fd-91eb-f1780236b3e4) structure to appropriate Q.2931 information elements. However, if both the generic **FLOWSPEC** structure and ATM-specific **QOS** structure are specified, the value specified in the ATM-specific **QOS** structure should take precedence should there be any conflicts. See Windows Sockets 2 API Specification Section 2.7 for more information about QoS provisions and **FLOWSPEC** structure.

The protocol-specific [**QOS**](https://msdn.microsoft.com/windows/desktop/859faa13-bd66-46ee-8452-6ff5d53d66c9) structure for ATM is a concatenation of Q.2931 information element (IE) structures, which are defined in the following text. If an application omits an IE that UNI 3.x mandates, the service provider should insert a reasonable default value, taking the information in the [**FLOWSPEC**](https://msdn.microsoft.com/windows/desktop/268e0d3a-2b04-40fd-91eb-f1780236b3e4) structure into account if applicable.

The handling of repeated IEs is dependent on the IE itself. If an IE is repeated and it is one that is allowed to be repeated per the ATM Forum UNI specification then the provider must handle it properly. In this case, order in the list determines preference order, with elements appearing earlier in the list being more preferred. If an IE is repeated and this is not allowed per ATM Forum UNI specification, the provider may either fail the request from the client (the preferred option) or use the last IE of that type found.

Each individual IE structure is formatted in the following manner and identified by the **IEType** field:

``` syntax
typedef struct {
    Q2931_IE_TYPE IEType;
    ULONG         IELength;
    UCHAR         IE[1];
} Q2931_IE;
```

Legal values for the **IEType** field are defined as:

``` syntax
typedef enum {
    IE_AALParameters,
    IE_TrafficDescriptor,
    IE_BroadbandBearerCapability,
    IE_BHLI,
    IE_BLLI,
    IE_CalledPartyNumber,
    IE_CalledPartySubaddress,
    IE_CallingPartyNumber,
    IE_CallingPartySubaddress,
    IE_Cause,
    IE_QOSClass,
    IE_TransitNetworkSelection,
} Q2931_IE_TYPE;
```

The **IE** field is overlaid by a specific IE structure and the **IELength** field is the total length in bytes of the IE structure including the **IEType** and **IELength** fields. The semantics and legal values for each element of these IE structures are per ATM UNI 3.x specification. SAP\_FIELD\_ABSENT can be used for those elements that are optional for a given IE structure, per ATM UNI 3.x specification.

 

 



