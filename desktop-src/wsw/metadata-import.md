---
title: Metadata Import
description: The WWSAPI includes API elements that can be used to process WSDL and Policy from an endpoint with the goal of extracting information that can be used to communicate with the endpoint.
ms.assetid: '77738bf1-ef8b-4fd6-a36a-43f1932868dd'
keywords: ["Metadata Import Web Services for Windows", "WWSAPI", "WWS"]
---

# Metadata Import

The WWSAPI includes API elements that can be used to process WSDL and Policy from an endpoint with the goal of extracting information that can be used to communicate with the endpoint. These APIs are typically used when the communication protocol supported by the endpoint is not already known.

## 

Use the following sequence to process metadata:

``` syntax
WsCreateMetadata    // create a metadata object

while there are metadata documents to add
{
    // retrieve the metadata document from it's location
    // (download, read from file, etc)

    // add the document to the metadata object
    WsReadMetadata

    // optionally query the metadata object for any missing documents
    WsGetMissingMetadataDocumentAddress?
}

// get the endpoints from the metadata object
WsGetMetadataEndpoints

for each endpoint
{            
    // examine the endpoint information to see if 
    // the endpoint is relevant for the particular scenario

    if the endpoint is relevant
    {
        // get the policy object from the endpoint

        // get the number of policy alternatives in the policy
        WsGetPolicyAlternativeCount

        for each policy alternative
        {
            // construct a policy constraints structure that specifies
            // what policy is acceptable and what information to extract
            // from the policy

            // see if the policy alternative matches the constraints
            WsMatchPolicyAlternative

            // if there is a match, then use it

            // if there is not a match, then it is also possible to 
            // try with a different constraint structure
        }
    }
}

// If reusing the metadata object for a different set of documents
WsResetMetadata? // reset metadata object, which removes all documents

WsFreeMetadata // free the metadata object
```

for information about how WSDL and WS-Policy assertions correspond to the API, see the [Metadata Mapping](metadata-mapping.md) topic.

## Security

The metadata downloaded is only as good as the address used to download it. An application should ensure that is trusts the address. Also, an application should ensure that it uses a security protocol to download the metadata documents that does not allow tampering with the metadata.

An application should inspect the addresses of the services exposed by the metadata. By default, the runtime ensures that the host name of the service matches that of the original URL used to download the metadata, but the application may want to perform additional checks. An application can disable the host name verification by overwriting [**WS\_METADATA\_PROPERTY\_VERIFY\_HOST\_NAMES**](ws-metadata-property-id.md) property. If the hostname check that is done by default is disabled, the application will need to protect itself against the metadata documents containing the address of a service from a different party that it does not trust in some other way.

By default, the maximum amount of memory used by the metadata runtime to deserialize and process the metadata is 256k, and the maximum number of documents that may be added is 32. These default values can be overwritten by [**WS\_METADATA\_PROPERTY\_HEAP\_REQUESTED\_SIZE**](ws-metadata-property-id.md) and **WS\_METADATA\_PROPERTY\_MAX\_DOCUMENTS** properties. These bounds are designed to limit the amount of downloads and limit the amount of memory allocated in order to accumulate the metadata. Increasing these values may lead to excessive memory usage, CPU usage, or network bandwidth consumption. Note that due to expansion of dictionary strings in the binary format, a small message may lead to a much larger deserialized form, so relying on small messages to limit metadata memory allocation is not sufficient when using the binary format.

By default, the maximum number of policy alternatives is 32, though it can be overwritten by [**WS\_POLICY\_PROPERTY\_MAX\_ALTERNATIVES**](ws-policy-property-id.md) property. If an application loops through each alternative looking for a match, it may need to search all alternatives before finding a match. Increasing the maximum number of alternatives may lead to excessive CPU utilization.

The following enumerations are part of metadata import:

-   [**WS\_METADATA\_PROPERTY\_ID**](ws-metadata-property-id.md)
-   [**WS\_METADATA\_STATE**](ws-metadata-state.md)
-   [**WS\_POLICY\_EXTENSION\_TYPE**](ws-policy-extension-type.md)
-   [**WS\_POLICY\_PROPERTY\_ID**](ws-policy-property-id.md)
-   [**WS\_POLICY\_STATE**](ws-policy-state.md)
-   [**WS\_SECURITY\_BINDING\_CONSTRAINT\_TYPE**](ws-security-binding-constraint-type.md)

The following functions are part of metadata import:

-   [**WsCreateMetadata**](wscreatemetadata.md)
-   [**WsFreeMetadata**](wsfreemetadata.md)
-   [**WsGetMetadataEndpoints**](wsgetmetadataendpoints.md)
-   [**WsGetMetadataProperty**](wsgetmetadataproperty.md)
-   [**WsGetMissingMetadataDocumentAddress**](wsgetmissingmetadatadocumentaddress.md)
-   [**WsGetPolicyAlternativeCount**](wsgetpolicyalternativecount.md)
-   [**WsGetPolicyProperty**](wsgetpolicyproperty.md)
-   [**WsMatchPolicyAlternative**](wsmatchpolicyalternative.md)
-   [**WsReadMetadata**](wsreadmetadata.md)
-   [**WsResetMetadata**](wsresetmetadata.md)

The following handles are part of metadata import:

-   [WS\_METADATA](ws-metadata.md)
-   [WS\_POLICY](ws-policy.md)

The following structures are part of metadata import:

-   [**WS\_CERT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](ws-cert-message-security-binding-constraint.md)
-   [**WS\_CHANNEL\_PROPERTY\_CONSTRAINT**](ws-channel-property-constraint.md)
-   [**WS\_ENDPOINT\_POLICY\_EXTENSION**](ws-endpoint-policy-extension.md)
-   [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING\_CONSTRAINT**](ws-http-header-auth-security-binding-constraint.md)
-   [**WS\_ISSUED\_TOKEN\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](ws-issued-token-message-security-binding-constraint.md)
-   [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](ws-kerberos-apreq-message-security-binding-constraint.md)
-   [**WS\_METADATA\_ENDPOINT**](ws-metadata-endpoint.md)
-   [**WS\_METADATA\_ENDPOINTS**](ws-metadata-endpoints.md)
-   [**WS\_METADATA\_PROPERTY**](ws-metadata-property.md)
-   [**WS\_POLICY\_CONSTRAINTS**](ws-policy-constraints.md)
-   [**WS\_POLICY\_EXTENSION**](ws-policy-extension.md)
-   [**WS\_POLICY\_PROPERTIES**](ws-policy-properties.md)
-   [**WS\_POLICY\_PROPERTY**](ws-policy-property.md)
-   [**WS\_REQUEST\_SECURITY\_TOKEN\_PROPERTY\_CONSTRAINT**](ws-request-security-token-property-constraint.md)
-   [**WS\_SECURITY\_BINDING\_CONSTRAINT**](ws-security-binding-constraint.md)
-   [**WS\_SECURITY\_BINDING\_PROPERTY\_CONSTRAINT**](ws-security-binding-property-constraint.md)
-   [**WS\_SECURITY\_CONSTRAINTS**](ws-security-constraints.md)
-   [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](ws-security-context-message-security-binding-constraint.md)
-   [**WS\_SECURITY\_PROPERTY\_CONSTRAINT**](ws-security-property-constraint.md)
-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING\_CONSTRAINT**](ws-ssl-transport-security-binding-constraint.md)
-   [**WS\_TCP\_SSPI\_TRANSPORT\_SECURITY\_BINDING\_CONSTRAINT**](ws-tcp-sspi-transport-security-binding-constraint.md)
-   [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](ws-username-message-security-binding-constraint.md)

 

 




