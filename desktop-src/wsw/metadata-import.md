---
title: Metadata Import
description: The WWSAPI includes API elements that can be used to process WSDL and Policy from an endpoint with the goal of extracting information that can be used to communicate with the endpoint.
ms.assetid: 77738bf1-ef8b-4fd6-a36a-43f1932868dd
keywords:
- Metadata Import Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Metadata Import

The WWSAPI includes API elements that can be used to process WSDL and Policy from an endpoint with the goal of extracting information that can be used to communicate with the endpoint. These APIs are typically used when the communication protocol supported by the endpoint is not already known.


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

An application should inspect the addresses of the services exposed by the metadata. By default, the runtime ensures that the host name of the service matches that of the original URL used to download the metadata, but the application may want to perform additional checks. An application can disable the host name verification by overwriting [**WS\_METADATA\_PROPERTY\_VERIFY\_HOST\_NAMES**](/windows/desktop/api/WebServices/ne-webservices-ws_metadata_property_id) property. If the hostname check that is done by default is disabled, the application will need to protect itself against the metadata documents containing the address of a service from a different party that it does not trust in some other way.

By default, the maximum amount of memory used by the metadata runtime to deserialize and process the metadata is 256k, and the maximum number of documents that may be added is 32. These default values can be overwritten by [**WS\_METADATA\_PROPERTY\_HEAP\_REQUESTED\_SIZE**](/windows/desktop/api/WebServices/ne-webservices-ws_metadata_property_id) and **WS\_METADATA\_PROPERTY\_MAX\_DOCUMENTS** properties. These bounds are designed to limit the amount of downloads and limit the amount of memory allocated in order to accumulate the metadata. Increasing these values may lead to excessive memory usage, CPU usage, or network bandwidth consumption. Note that due to expansion of dictionary strings in the binary format, a small message may lead to a much larger deserialized form, so relying on small messages to limit metadata memory allocation is not sufficient when using the binary format.

By default, the maximum number of policy alternatives is 32, though it can be overwritten by [**WS\_POLICY\_PROPERTY\_MAX\_ALTERNATIVES**](/windows/desktop/api/WebServices/ne-webservices-ws_policy_property_id) property. If an application loops through each alternative looking for a match, it may need to search all alternatives before finding a match. Increasing the maximum number of alternatives may lead to excessive CPU utilization.

The following enumerations are part of metadata import:

-   [**WS\_METADATA\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_metadata_property_id)
-   [**WS\_METADATA\_STATE**](/windows/desktop/api/WebServices/ne-webservices-ws_metadata_state)
-   [**WS\_POLICY\_EXTENSION\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_policy_extension_type)
-   [**WS\_POLICY\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_policy_property_id)
-   [**WS\_POLICY\_STATE**](/windows/desktop/api/WebServices/ne-webservices-ws_policy_state)
-   [**WS\_SECURITY\_BINDING\_CONSTRAINT\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_security_binding_constraint_type)

The following functions are part of metadata import:

-   [**WsCreateMetadata**](/windows/desktop/api/WebServices/nf-webservices-wscreatemetadata)
-   [**WsFreeMetadata**](/windows/desktop/api/WebServices/nf-webservices-wsfreemetadata)
-   [**WsGetMetadataEndpoints**](/windows/desktop/api/WebServices/nf-webservices-wsgetmetadataendpoints)
-   [**WsGetMetadataProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetmetadataproperty)
-   [**WsGetMissingMetadataDocumentAddress**](/windows/desktop/api/WebServices/nf-webservices-wsgetmissingmetadatadocumentaddress)
-   [**WsGetPolicyAlternativeCount**](/windows/desktop/api/WebServices/nf-webservices-wsgetpolicyalternativecount)
-   [**WsGetPolicyProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetpolicyproperty)
-   [**WsMatchPolicyAlternative**](/windows/desktop/api/WebServices/nf-webservices-wsmatchpolicyalternative)
-   [**WsReadMetadata**](/windows/desktop/api/WebServices/nf-webservices-wsreadmetadata)
-   [**WsResetMetadata**](/windows/desktop/api/WebServices/nf-webservices-wsresetmetadata)

The following handles are part of metadata import:

-   [WS\_METADATA](ws-metadata.md)
-   [WS\_POLICY](ws-policy.md)

The following structures are part of metadata import:

-   [**WS\_CERT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_cert_message_security_binding_constraint)
-   [**WS\_CHANNEL\_PROPERTY\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_channel_property_constraint)
-   [**WS\_ENDPOINT\_POLICY\_EXTENSION**](/windows/desktop/api/WebServices/ns-webservices-ws_endpoint_policy_extension)
-   [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding_constraint)
-   [**WS\_ISSUED\_TOKEN\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_issued_token_message_security_binding_constraint)
-   [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding_constraint)
-   [**WS\_METADATA\_ENDPOINT**](/windows/desktop/api/WebServices/ns-webservices-ws_metadata_endpoint)
-   [**WS\_METADATA\_ENDPOINTS**](/windows/desktop/api/WebServices/ns-webservices-ws_metadata_endpoints)
-   [**WS\_METADATA\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_metadata_property)
-   [**WS\_POLICY\_CONSTRAINTS**](/windows/desktop/api/WebServices/ns-webservices-ws_policy_constraints)
-   [**WS\_POLICY\_EXTENSION**](/windows/desktop/api/WebServices/ns-webservices-ws_policy_extension)
-   [**WS\_POLICY\_PROPERTIES**](/windows/desktop/api/WebServices/ns-webservices-ws_policy_properties)
-   [**WS\_POLICY\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_policy_property)
-   [**WS\_REQUEST\_SECURITY\_TOKEN\_PROPERTY\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_request_security_token_property_constraint)
-   [**WS\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_security_binding_constraint)
-   [**WS\_SECURITY\_BINDING\_PROPERTY\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_security_binding_property_constraint)
-   [**WS\_SECURITY\_CONSTRAINTS**](/windows/desktop/api/WebServices/ns-webservices-ws_security_constraints)
-   [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_security_context_message_security_binding_constraint)
-   [**WS\_SECURITY\_PROPERTY\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_security_property_constraint)
-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding_constraint)
-   [**WS\_TCP\_SSPI\_TRANSPORT\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_tcp_sspi_transport_security_binding_constraint)
-   [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING\_CONSTRAINT**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding_constraint)

 

 




