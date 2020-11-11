---
title: Service Metadata
description: The WWSAPI service host supports WS-MetadataExchange for its endpoints.
ms.assetid: 5a6feb34-7fff-4000-b3be-63112b22905a
keywords:
- Service Metadata Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Service Metadata

The WWSAPI service host supports WS-MetadataExchange for its endpoints. You enable such metadata exchange on the service host with the following steps:

-   Specify metadata documents in the [**WS\_SERVICE\_METADATA**](/windows/desktop/api/WebServices/ns-webservices-ws_service_metadata) property on the [WS\_SERVICE\_HOST](ws-service-host.md).
-   Specify the service name in the [**WS\_SERVICE\_METADATA**](/windows/desktop/api/WebServices/ns-webservices-ws_service_metadata) property on the [WS\_SERVICE\_HOST](ws-service-host.md).
-   Specify the port for individual endpoints by using the [**WS\_SERVICE\_ENDPOINT\_PROPERTY\_METADATA**](/windows/desktop/api/WebServices/ne-webservices-ws_service_endpoint_property_id) property on the [**WS\_SERVICE\_ENDPOINT**](/windows/desktop/api/WebServices/ns-webservices-ws_service_endpoint).
-   Enable one or more [**WS\_SERVICE\_ENDPOINT**](/windows/desktop/api/WebServices/ns-webservices-ws_service_endpoint) structures to service the WS-MetadataExchange requests.
-   Optionally, specify **WS\_SERVICE\_ENDPOINT\_PROPERTY\_METADATA\_EXCHANGE\_URL\_SUFFIX** in the [**WS\_SERVICE\_ENDPOINT\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_service_endpoint_property_id) enumeration for servicing Ws-MetadataExchange requests on a specific address.


Specifying Metadata documents / Service name on the Service Host

The first step is to specify the metadata documents on the service host. Do this by gathering the individual documents as an array of WS\_XML\_STRING\*'s. These strings can be XML Schema, WSDL or WS-Policy document. This is specified through the [**WS\_SERVICE\_PROPERTY\_METADATA**](/windows/desktop/api/WebServices/ne-webservices-ws_service_property_id) property.

Optionally, an application can also specify the service name and namespace as part of the [**WS\_SERVICE\_METADATA**](/windows/desktop/api/WebServices/ns-webservices-ws_service_metadata). If the metadata document does not specify the service element for the given service name, the service model will generate a service element with the corresponding WSDL ports for the service.

``` syntax
WS_SERVICE_METADATA_DOCUMENT document = {0};
WS_STRING documentName = WS_STRING_VALUE(L&quot;a.wsdl&quot;);
document.name = &documentName;
document.content = &wsdlDocument
WS_SERVICE_METADATA_DOCUMENT** metadataDocuments [] = {&document};
WS_SERVICE_METADATA serviceMetadata = {0};
// Specify Metadata documents
serviceMetadata.count = WsCountOf(metadataDocuments);
serviceMetadata.documents = &metadataDocuments;
// Specify service name
serviceMetadata.serviceName = &serviceName;
serviceMetadata.serviceNs = &serviceNamespace;


WS_SERVICE_PROPERTY serviceProperties[1] = {0};
serviceProperties[0].id = WS_SERVICE_PROPERTY_METADATA;
serviceProperties[0].value =  &serviceMetadata;
serviceProperties[0].ValueSize = sizeof(serviceMetadata);
```

Note that no verification of the individual metadata documents will be performed on the documents. It is the responsiblity of the application to validate contents of the documents and ensure that all the imports paths are relatively specified.

The namespace specified is used to locate the document in which the service element will be added by the service host.

Addition of service element to the WSDL document

The service host provides facility for the application to add a service element on its behalf if one is not already specified. In order to enable this behavior an application must specify serivceName and serviceNs fields on the [**WS\_SERVICE\_METADATA**](/windows/desktop/api/WebServices/ns-webservices-ws_service_metadata) structure. If serviceName and serviceNs are both **NULL** no service element is added to the WSDL document. Both these are used to identify document in which the serviceElement is going to be added.

If [**WS\_SERVICE\_PROPERTY\_METADATA**](/windows/desktop/api/WebServices/ne-webservices-ws_service_property_id) property is not specified no metadata exhange will take place on the service host.

Specifying the port on the WS\_SERVICE\_ENDPOINT

For a [**WS\_SERVICE\_ENDPOINT**](/windows/desktop/api/WebServices/ns-webservices-ws_service_endpoint) to be available as a port inside the service element in the WSDL document, the application must specify [**WS\_SERVICE\_ENDPOINT\_PROPERTY\_METADATA**](/windows/desktop/api/WebServices/ne-webservices-ws_service_endpoint_property_id) property on it.

``` syntax
WS_SERVICE_ENDPOINT_METADATA endpointPort = {0}
endpointPort.name = &portName;
endpointPort.bindingName = &bindingName;
endpointPort.bindingNs = &bindingNs;

WS_SERVICE_ENDPOINT_PROPERTY serviceProperties[1] = {0};
serviceProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA;
serviceProperties[0].value =  &endpointPort;
serviceProperties[0].valueSize = sizeof(endpointPort);
```

It is assumed that the reference to the binding name and namespace exists in the documents specified on the service host as part of WS\_SERVICE\_PROPERTY\_METADATA. The runtime does not verify this on behalf of the application.

Enable WS-MetadataExchange servicing on WS\_SERVICE\_ENDPOINT

In order to service WS-MetadataExchange requests,the service host must have at least one endpoint enabled for servicing WS-MetadataExchange requests. This is done by setting the appropriate version for WS-MetadataExchange on the [**WS\_SERVICE\_ENDPOINT**](/windows/desktop/api/WebServices/ns-webservices-ws_service_endpoint).

``` syntax
WS_METADATA_EXCHANGE_TYPE metadataExchangeType = WS_METADATA_EXCHANGE_TYPE_MEX;
WS_SERVICE_ENDPOINT_PROPERTY serviceProperties[1] = {0};
serviceProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_TYPE;
serviceProperties[0].value =  &metadataExchangeType;
serviceProperties[0].ValueSize = sizeof(metadataExchangeType);
```

Enable HTTP GET servicing on WS\_SERVICE\_ENDPOINT

In order to serviceHTTP GET requests, the service host must have at least one endpoint enabled for servicing WS-MetadataExchange requests. This is done by setting the appropriate version for WS-MetadataExchange on the [**WS\_SERVICE\_ENDPOINT**](/windows/desktop/api/WebServices/ns-webservices-ws_service_endpoint).

``` syntax
WS_METADATA_EXCHANGE_TYPE metadataExchangeType = WS_METADATA_EXCHANGE_TYPE_HTTP_GET;
WS_SERVICE_ENDPOINT_PROPERTY serviceProperties[1] = {0};
serviceProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_TYPE;
serviceProperties[0].value =  &metadataExchangeType;
serviceProperties[0].ValueSize = sizeof(metadataExchangeType);
```

Specifying URL suffix for Ws-MetadataExchange requests

An application can optionally enable only accepting requests for WS-MetadataExchange on a specific path. This is done by specifying a suffix for the given WS\_SERVICE\_ENDPOINT. This suffix is concatenated as-is to the actual URL for the WS\_SERVICE\_ENDPOINT. The concatenated string is used as the matching URL to the 'to' header received.

``` syntax
const WS_STRING suffix = WS_STRING_VALUE(L&quot;mex&quot;);
WS_SERVICE_ENDPOINT_PROPERTY serviceProperties[1] = {};
serviceProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_URL_SUFFIX;
serviceProperties[0].value =  &suffix;
serviceProperties[0].valueSize = sizeof(suffix);
```

The following API elements relate to service metada.

| Enumeration                                                       | Description                                                                     |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**WS\_METADATA\_EXCHANGE\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_metadata_exchange_type) | Enables or disables WS-MetadataExchange and HTTP GET servicing on the endpoint. |



 



| Structure                                                               | Description                                                           |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [**WS\_SERVICE\_ENDPOINT\_METADATA**](/windows/desktop/api/WebServices/ns-webservices-ws_service_endpoint_metadata) | Represents the port element for the endpoint.                         |
| [**WS\_SERVICE\_METADATA**](/windows/desktop/api/WebServices/ns-webservices-ws_service_metadata)                    | Specifies the service metadata documents array.                       |
| [**WS\_SERVICE\_METADATA\_DOCUMENT**](/windows/desktop/api/WebServices/ns-webservices-ws_service_metadata_document) | Specifies the individual documents that make up the service metadata. |



 

 

 




