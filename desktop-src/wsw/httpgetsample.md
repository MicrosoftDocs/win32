---
title: HttpGetSample
description: This example shows how to use service host for hosting a PurchaseOrder service over HTTP. The service exposes metadata over HTTP GET and WS-Metadata Exchange v1.1. The service also shows how to implement a cover page for a WWSAPI service.
ms.assetid: 5e3a2d24-afd1-451d-94c4-4234c24a4895
keywords:
- HttpGetSample Native-Web-Services
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HttpGetSample

This example shows how to use service host for hosting a PurchaseOrder service over HTTP. The service exposes metadata over HTTP GET and WS-Metadata Exchange v1.1. The service also shows how to implement a cover page for a WWSAPI service.

-   [HttpGetService.cpp](#httpgetservicecpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## HttpGetService.cpp


```C++
//------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
//------------------------------------------------------------

#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>
#include <stdio.h>
#include "WebServices.h"
#include "process.h"
#include "string.h"
#include <strsafe.h>
#include "PurchaseOrder.wsdl.h"

// Print out rich error info
void PrintError(HRESULT errorCode, WS_ERROR* error)
{
    wprintf(L"Failure: errorCode=0x%lx\n", errorCode);

    if (errorCode == E_INVALIDARG || errorCode == WS_E_INVALID_OPERATION)
    {
        // Correct use of the APIs should never generate these errors
        wprintf(L"The error was due to an invalid use of an API.  This is likely due to a bug in the program.\n");
        DebugBreak();
    }

    HRESULT hr = NOERROR;
    if (error != NULL)
    {
        ULONG errorCount;
        hr = WsGetErrorProperty(error, WS_ERROR_PROPERTY_STRING_COUNT, &amp;errorCount, sizeof(errorCount));
        if (FAILED(hr))
        {
            goto Exit;
        }
        for (ULONG i = 0; i < errorCount; i++)
        {
            WS_STRING string;
            hr = WsGetErrorString(error, i, &amp;string);
            if (FAILED(hr))
            {
                goto Exit;
            }
            wprintf(L"%.*s\n", string.length, string.chars);
        }
    }
Exit:
    if (FAILED(hr))
    {
        wprintf(L"Could not get error string (errorCode=0x%lx)\n", hr);
    }
}

HANDLE closeServer = NULL;  


static const WCHAR ExpectedShipDate [] = L"1/1/2006";
static const WCHAR OrderStatusString [] = L"Pending";

static WS_XML_STRING serviceName = WS_XML_STRING_VALUE("PurchaseOrderService");
static WS_XML_STRING serviceNamespace = WS_XML_STRING_VALUE("http://example.org");

static WS_XML_STRING portName = WS_XML_STRING_VALUE("IPurchaseOrder");
static WS_XML_STRING bindingName = WS_XML_STRING_VALUE("PurchaseOrderBinding");
static WS_XML_STRING bindingNs = WS_XML_STRING_VALUE("http://example.org");

// The WSDL document used by this example
const static WS_XML_STRING wsdl = WS_XML_STRING_VALUE(
"<wsdl:definitions "
"    xmlns:soap='http://schemas.xmlsoap.org/wsdl/soap/' "
"    xmlns:wsu='http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd' "
"    xmlns:soapenc='http://schemas.xmlsoap.org/soap/encoding/' "
"    xmlns:tns='http://example.org' xmlns:wsa='http://schemas.xmlsoap.org/ws/2004/08/addressing' "
"    xmlns:wsp='http://schemas.xmlsoap.org/ws/2004/09/policy' "
"    xmlns:wsap='http://schemas.xmlsoap.org/ws/2004/08/addressing/policy' "
"    xmlns:xsd='http://www.w3.org/2001/XMLSchema' "
"    xmlns:msc='http://schemas.microsoft.com/ws/2005/12/wsdl/contract' "
"    xmlns:wsaw='http://www.w3.org/2006/05/addressing/wsdl' "
"    xmlns:soap12='http://schemas.xmlsoap.org/wsdl/soap12/' xmlns:wsa10='http://www.w3.org/2005/08/addressing' "
"    xmlns:wsx='http://schemas.xmlsoap.org/ws/2004/09/mex' xmlns:wsdl='http://schemas.xmlsoap.org/wsdl/' "
"    targetNamespace='http://example.org'>"
"  <wsdl:types>"
"    <xsd:schema targetNamespace='http://example.org/Imports'>"
"      <xsd:import namespace='http://example.org' schemaLocation='xsd'/>"
"    </xsd:schema>"
"  </wsdl:types>"
"  <wsdl:message name='PurchaseOrder'>"
"       <wsdl:part name='parameters' element='tns:PurchaseOrderType'/>"
"  </wsdl:message>"
"  <wsdl:message name='OrderConfirmation'>"
"       <wsdl:part name='parameters' element='tns:OrderConfirmationType'/>"
"  </wsdl:message>"
"  <wsdl:message name='GetOrderStatus'>"
"       <wsdl:part name='parameters' element='tns:GetOrderStatusType'/>"
"  </wsdl:message>"
"  <wsdl:message name='GetOrderStatusResponse'>"
"     <wsdl:part name='parameters' element='tns:GetOrderStatusResponseType'/>"
"  </wsdl:message>"
"  <wsdl:portType name='IPurchaseOrder'>"
"    <wsdl:operation name='Order'>"
"       <wsdl:input message='tns:PurchaseOrder' wsaw:Action='http://example.org/purchaseorder'/>"
"       <wsdl:output message='tns:OrderConfirmation' wsaw:Action='http://example.org/orderconfirmation'/>"
"    </wsdl:operation>"
"    <wsdl:operation name='OrderStatus'>"
"       <wsdl:input message='tns:GetOrderStatus' wsaw:Action='http://example.org/getorderstatus'/>"
"       <wsdl:output message='tns:GetOrderStatusResponse' wsaw:Action='http://example.org/getorderstatusresponse'/>"
"     </wsdl:operation>"
"  </wsdl:portType>"
" <wsdl:binding name='PurchaseOrderBinding' type='tns:IPurchaseOrder'>"
"  <soap12:binding transport='http://schemas.xmlsoap.org/soap/http' />"
"       <wsdl:operation name='Order'>"
"           <soap12:operation soapAction='http://example.org/purchaseorder' style='document'/>"
"           <wsdl:input>"
"               <soap12:body use='literal'/>"
"           </wsdl:input>"
"           <wsdl:output>"
"               <soap12:body use='literal'/>"
"           </wsdl:output>"
"       </wsdl:operation>"
"       <wsdl:operation name='OrderStatus'>"
"           <soap12:operation soapAction='http://example.org/getorderstatus' style='document'/>"
"           <wsdl:input>"
"               <soap12:body use='literal'/>"
"           </wsdl:input>"
"           <wsdl:output>"
"               <soap12:body use='literal'/>"
"           </wsdl:output>"
"       </wsdl:operation>"
"   </wsdl:binding>"
"</wsdl:definitions>"
);

static const WS_XML_STRING xsd = WS_XML_STRING_VALUE(
"<xsd:schema xmlns:tns='http://example.org'"
"elementFormDefault='qualified' "
"targetNamespace='http://example.org' "
"xmlns:xsd='http://www.w3.org/2001/XMLSchema'>"
"<xsd:element name='PurchaseOrderType'>"
"<xsd:complexType>"
"<xsd:sequence>"
"<xsd:element minOccurs='0' name='quantity' type='xsd:int'/>"
"<xsd:element minOccurs='0' name='productName' type='xsd:string'/>"
"</xsd:sequence>"
"</xsd:complexType>"
"</xsd:element>"
"<xsd:element name='OrderConfirmationType'>"
"<xsd:complexType>"
"<xsd:sequence>"
"<xsd:element minOccurs='0' name='orderID' type='xsd:unsignedInt'/>"
"<xsd:element minOccurs='0' name='expectedShipDate' type='xsd:string'/>"
"</xsd:sequence>"
"</xsd:complexType>"
"</xsd:element>"
"<xsd:element name='GetOrderStatusType'>"
"<xsd:complexType>"
"<xsd:sequence>"
"<xsd:element minOccurs='0' name='orderID' type='xsd:unsignedInt'/>"
"</xsd:sequence>"
"</xsd:complexType>"
"</xsd:element>"
"<xsd:element name='GetOrderStatusResponseType'>"
"<xsd:complexType>"
"<xsd:sequence>"
"<xsd:element minOccurs='0' name='orderID' type='xsd:unsignedInt'/>"
"<xsd:element minOccurs='0' name='status' type='xsd:string'/>"
"</xsd:sequence>"
"</xsd:complexType>"
"</xsd:element>"
"</xsd:schema>"
);

static const WS_MESSAGE_DESCRIPTION emptyMessageDescription = 
{ 
    NULL,
    NULL
};

static const WS_XML_STRING verbHeaderName = WS_XML_STRING_VALUE("Verb");
static const WS_XML_STRING contentTypeHeaderName = WS_XML_STRING_VALUE("Content-Type");

static const WS_XML_STRING statusCodeName = WS_XML_STRING_VALUE("StatusCode");
static const WS_XML_STRING statusTextName = WS_XML_STRING_VALUE("StatusText");

static const WS_STRING replyContentType = WS_STRING_VALUE(L"text/html");
static const BYTE replyBodyBytes[] = 
"<html>"
"<head>"
"<title>Welcome To Web Services Sample</title><style>"
"body { font-family: Verdana; font-size: x-small; }"
"h1 { margin-top: 4pt; margin-bottom: 4pt; font-size: large; font-family: Verdana; }"
"h2 { margin-top: 4pt; margin-bottom: 4pt; font-size: small; font-family: Verdana; }"
"h3 { margin-top: 12pt; margin-bottom: 12pt; color: black; font-size: x-small; font-family: Verdana; }"
"h4 { margin-top: 12pt; margin-bottom: 12pt; color: darkblue; font-size: x-small; font-family: Verdana; }"
"p { font-size: x-small; }"
"font.comment { color: darkgreen; }"
"font.literal { color: darkred; }"
"pre.code { padding: 3pt; font-family: Lucida Console; background-color: #e8e8e8; font-size: x-small; }"
"div.indent { padding-left: 12pt; }"
"span.security { color: red; }"
"span.platforms { color: OrangeRed; }"
"span.sal { color: darkgreen; }"
"div.code { padding-top: 3pt; padding-bottom: 3pt; padding-left: 23pt; text-indent: -20pt; padding-right: 3pt; background-color: #e8e8e8; font-size: x-small; }"
"div.title { font-family: Verdana; padding: 3pt; margin: 0pt; border: 1pt solid; background-color: skyblue; width=100%; padding: 3pt; }"
"div.titlelink { border: 0pt; background-color: skyblue; position: absolute; right=6pt; padding: 3pt 3pt 3pt 3pt; margin: 3pt 3pt 3pt 3pt; }"
"div.highlight { background-color: #ffffa0; }"
"p.code { margin-top: 3pt; margin-bottom: 3pt; font-family: Lucida Console; font-size: x-small; }"
"span.code { padding: 3pt; background-color: #e8e8e8;  }"
"p.feedback { margin-top: 0pt; margin-bottom: 0pt; font-style: italic; font-family: Verdana; font-size: xx-small; color: darkgreen; }"
"span.notimpl { font-size: xx-small; border: 1pt solid; padding: 2pt; background-color: #99cc00; }"
"table.outergroup { }"
"tr.outergroup { }"
"td.outergroup { background-color: #e8e8e8; }"
"p.group { font-size: x-small; font-family: Lucida Console; }"
"div.innergroup { }"
"table.innergroup { }"
"tr.innergroup { }"
"td.innergroup { }"
"td.doc { background-color: #DBE5F1; font-size: 8pt; border: 1px solid; padding: 0.1em 1em; }"
"th.doc { background-color: #C5D9F1; font-size: 10pt; border: 1px solid; padding: 0.1em 1em; }"
"table.doc { }"
"</style>"
"</head>"
"<body>"
"<div class=title><h2>Welcome To Web Services Sample</h2></div>"
"<h3>Introduction</h3>"
"<p>"
"You are receiving this request from a service written using Windows Web Services"
"</p>"
"<h3>Metadata</h3>"
"<p>"
"Metadata for this service can be fetched using WS-MetadataExchange v1.1 by using the address, http://localhost/example"
"</p>"
"<p>"
"Alternatively you can fetch the WSDL document directly using the address, http://localhost/metadata/wsdl"
"</p>"
"</body>"
"</html>"
;

static const WS_STRING wsdlDocumentName = WS_STRING_VALUE(L"wsdl");
static const WS_STRING xsdDocumentName = WS_STRING_VALUE(L"xsd");
static const WS_SERVICE_METADATA_DOCUMENT wsdlDocument =
{
    (WS_XML_STRING*)&amp;wsdl,
    (WS_STRING*)&amp;wsdlDocumentName
};

static const WS_SERVICE_METADATA_DOCUMENT xsdDocument =
{
    (WS_XML_STRING*)&amp;xsd,
    (WS_STRING*)&amp;xsdDocumentName
};

static const WS_SERVICE_METADATA_DOCUMENT* metadataDocuments[] =
{
    &amp;wsdlDocument,
    &amp;xsdDocument
};

static const WS_ELEMENT_DESCRIPTION bytesBodyDescription = 
{ 
    NULL,
    NULL,
    WS_BYTES_TYPE,
    NULL
};

static const WS_MESSAGE_DESCRIPTION bytesMessageDescription = 
{ 
    NULL,
    const_cast<WS_ELEMENT_DESCRIPTION*>(&amp;bytesBodyDescription)
};

HRESULT SetStatus(
    __in WS_MESSAGE* replyMessage, 
    __in ULONG statusCode, 
    __in_z WCHAR* statusText,
    __in_opt WS_ERROR* error)
{
    HRESULT hr;

    // Add the status text to the message
    hr = WsAddMappedHeader(
        replyMessage,
        &amp;statusTextName,
        WS_WSZ_TYPE,
        WS_WRITE_REQUIRED_POINTER,
        &amp;statusText,
        sizeof(statusText),
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }

    // Add the status code to the message
    hr = WsAddMappedHeader(
        replyMessage,
        &amp;statusCodeName,
        WS_UINT32_TYPE,
        WS_WRITE_REQUIRED_VALUE,
        &amp;statusCode,
        sizeof(statusCode),
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }

Exit:
    return hr;
}

HRESULT SendFailureMessage(
    __in WS_CHANNEL* channel, 
    __in WS_MESSAGE* replyMessage, 
    __in ULONG statusCode, 
    __in_z WCHAR* statusText, 
    __in_opt WS_ERROR* error)
{
    HRESULT hr;

    // Add status code/text to the reply
    hr = SetStatus(
        replyMessage,
        statusCode,
        statusText,
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }

    // Send the reply
    hr = WsSendMessage(
        channel, 
        replyMessage, 
        &amp;emptyMessageDescription, 
        WS_WRITE_REQUIRED_VALUE,
        NULL,
        0,
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }

Exit:
    return hr;
}

HRESULT CALLBACK ProcessMessage(
    __in const WS_OPERATION_CONTEXT* context, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);
    
    WS_CHANNEL* channel = NULL;
    HRESULT hr = NOERROR;
    WS_MESSAGE* requestMessage = NULL;
    WS_MESSAGE* replyMessage = NULL;
    WS_HEAP* heap;
    
    // Get the request mesasge
    hr = WsGetOperationContextProperty(
        context, 
        WS_OPERATION_CONTEXT_PROPERTY_INPUT_MESSAGE, 
        &amp;requestMessage, 
        sizeof(requestMessage), 
        error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    // Get the channel 
    hr = WsGetOperationContextProperty(
        context, 
        WS_OPERATION_CONTEXT_PROPERTY_CHANNEL, 
        &amp;channel, 
        sizeof(channel), 
        error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    // Get the heap 
    hr = WsGetOperationContextProperty(
        context, 
        WS_OPERATION_CONTEXT_PROPERTY_HEAP, 
        &amp;heap, 
        sizeof(heap), 
        error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    // Create a reply message
    hr = WsCreateMessageForChannel(
        channel,
        NULL, 
        0, 
        &amp;replyMessage, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Initialize reply message
    hr = WsInitializeMessage(replyMessage, WS_REPLY_MESSAGE, requestMessage, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
        
    // Get the HTTP Verb
    WS_STRING verb;
    hr = WsGetMappedHeader(
        requestMessage, 
        &amp;verbHeaderName, 
        WS_SINGLETON_HEADER,
        0,
        WS_STRING_TYPE,
        WS_READ_REQUIRED_VALUE, 
        NULL, 
        &amp;verb, 
        sizeof(verb), 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    wprintf(L"Verb: %.*s\n", verb.length, verb.chars);
    
    if (CompareString(LOCALE_INVARIANT, NORM_IGNORECASE, verb.chars, verb.length, L"GET", 3) != CSTR_EQUAL)
    {
        // Unrecognized verb
        hr = SendFailureMessage(channel, replyMessage, 405, L"Method Not Allowed", error);
        goto Exit;
    }
    
    // Read end of request message
    hr = WsReadMessageEnd(channel, requestMessage, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Set content type header of reply
    hr = WsAddMappedHeader(
        replyMessage,
        &amp;contentTypeHeaderName, 
        WS_STRING_TYPE,
        WS_WRITE_REQUIRED_VALUE,
        &amp;replyContentType,
        sizeof(replyContentType),
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Set status of reply
    hr = SetStatus(replyMessage, 200, L"OK", error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Set up the bytes to return in the HTTP body
    WS_BYTES body;
    body.bytes = const_cast<BYTE*>(replyBodyBytes);
    body.length = sizeof(replyBodyBytes);
    
    // Send the reply message
    hr = WsSendMessage(
        channel, 
        replyMessage, 
        &amp;bytesMessageDescription, 
        WS_WRITE_REQUIRED_VALUE,
        &amp;body,
        sizeof(body),
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
Exit:
    if (replyMessage != NULL)
    {
        WsFreeMessage(replyMessage);
    }
    return hr;    
}



                
HRESULT CALLBACK PurchaseOrderImpl(
    const WS_OPERATION_CONTEXT* context,
    int quantity, 
    WS_STRING productName, 
    unsigned int* orderID,
    WS_STRING* expectedShipDate, 
    const WS_ASYNC_CONTEXT* asyncContext,
    WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    WS_HEAP* heap = NULL;
    HRESULT hr = NOERROR;
    
    wprintf(L"%ld, %.*s\n", 
        quantity, 
        productName.length,
        productName.chars);
    fflush(stdout);
    
    hr = WsGetOperationContextProperty(context, WS_OPERATION_CONTEXT_PROPERTY_HEAP, &amp;heap, sizeof(heap), error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = WsAlloc(heap, sizeof(ExpectedShipDate), (void**)&amp;expectedShipDate->chars, error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = StringCbCopyW(expectedShipDate->chars, sizeof(ExpectedShipDate), ExpectedShipDate);
    if (FAILED(hr))
    {
        return hr;
    }
    
    *orderID = 123;
    expectedShipDate->length = (ULONG)wcslen(ExpectedShipDate);
    
    return NOERROR;
}


HRESULT CALLBACK GetOrderStatusImpl(
    const WS_OPERATION_CONTEXT* context,
    unsigned int* orderID,
    WS_STRING* status, 
    const WS_ASYNC_CONTEXT* asyncContext,
    WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    WS_HEAP* heap = NULL;
    HRESULT hr = NOERROR;
    
    *orderID = *orderID;
    
    hr = WsGetOperationContextProperty(context, WS_OPERATION_CONTEXT_PROPERTY_HEAP, &amp;heap, sizeof(heap), error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = WsAlloc(heap, sizeof(OrderStatusString), (void**)&amp;status->chars, error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = StringCbCopyW(status->chars, sizeof(OrderStatusString), OrderStatusString);
    if (FAILED(hr))
    {
        return hr;
    }
    
    status->length = (ULONG)wcslen(OrderStatusString);
    
    return NOERROR;
}

ULONG numberOfSession = 0;
HRESULT CALLBACK CloseChannelCallback(
    __in const WS_OPERATION_CONTEXT* context, 
    __in const WS_ASYNC_CONTEXT* asyncContext)
{
    UNREFERENCED_PARAMETER(context);
    UNREFERENCED_PARAMETER(asyncContext);

    if (InterlockedIncrement(&amp;numberOfSession) == 6)
    {
        SetEvent(closeServer);
    }
    return NOERROR;
}

static const PurchaseOrderBindingFunctionTable purchaseOrderFunctions = {PurchaseOrderImpl, GetOrderStatusImpl};

static const WS_SERVICE_CONTRACT messageContract = 
{ 
    NULL, 
    ProcessMessage, 
    NULL
};

// Method contract for the service
static const WS_SERVICE_CONTRACT purchaseOrderContract = 
{
    &amp;PurchaseOrder_wsdl.contracts.PurchaseOrderBinding, // comes from the generated header.
    NULL, // for not specifying the default contract
    &amp;purchaseOrderFunctions // specified by the user
};


// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_SERVICE_HOST* host = NULL;
    WS_SERVICE_ENDPOINT typedHttpEndpoint = {};
    WS_SERVICE_ENDPOINT unTypedHttpEndpoint = {};
    const WS_SERVICE_ENDPOINT* serviceEndpoints[] = {&amp;typedHttpEndpoint, &amp;unTypedHttpEndpoint};
    WS_ERROR* error = NULL;
    WS_SERVICE_PROPERTY serviceProperties[1];
    WS_SERVICE_METADATA serviceMetadata = {};
    WS_SERVICE_ENDPOINT_PROPERTY serviceEndpointPropertiesTypedContract[3];
    WS_SERVICE_ENDPOINT_PROPERTY serviceEndpointPropertiesMetadata[2];
    WS_SERVICE_PROPERTY_CLOSE_CALLBACK closeCallbackProperty = {CloseChannelCallback};
    WS_SERVICE_ENDPOINT_METADATA endpointMetadata = {};
    WS_METADATA_EXCHANGE_TYPE metadataExchangeTypeMex = WS_METADATA_EXCHANGE_TYPE_MEX;
    WS_METADATA_EXCHANGE_TYPE metadataExchangeTypeHttpGet = WS_METADATA_EXCHANGE_TYPE_HTTP_GET;
    
    // Configure Port on the endpoint for Mex
    endpointMetadata.portName = &amp;portName;
    endpointMetadata.bindingName = &amp;bindingName;
    endpointMetadata.bindingNs = &amp;bindingNs;                    
    
    serviceEndpointPropertiesTypedContract[0].id = WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK;
    serviceEndpointPropertiesTypedContract[0].value = &amp;closeCallbackProperty;
    serviceEndpointPropertiesTypedContract[0].valueSize = sizeof(closeCallbackProperty);
    
    // Specifying Port on the endpoint.
    serviceEndpointPropertiesTypedContract[1].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA;
    serviceEndpointPropertiesTypedContract[1].value = &amp;endpointMetadata;
    serviceEndpointPropertiesTypedContract[1].valueSize = sizeof(endpointMetadata);
    
    // Marking the endpoint to service WS-MetadataExchnage Requests
    serviceEndpointPropertiesTypedContract[2].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_TYPE;
    serviceEndpointPropertiesTypedContract[2].value = &amp;metadataExchangeTypeMex;
    serviceEndpointPropertiesTypedContract[2].valueSize = sizeof(metadataExchangeTypeMex);
    
    typedHttpEndpoint.address.url.chars = L"http://+:80/example"; // address given as uri
    typedHttpEndpoint.address.url.length = (ULONG)wcslen(typedHttpEndpoint.address.url.chars);
    typedHttpEndpoint.channelBinding = WS_HTTP_CHANNEL_BINDING; // channel binding for the endpoint
    typedHttpEndpoint.channelType = WS_CHANNEL_TYPE_REPLY; // the channel type
    typedHttpEndpoint.contract = (WS_SERVICE_CONTRACT*)&amp;purchaseOrderContract;  // the contract
    typedHttpEndpoint.properties = serviceEndpointPropertiesTypedContract;
    typedHttpEndpoint.propertyCount = WsCountOf(serviceEndpointPropertiesTypedContract);
    
    serviceEndpointPropertiesMetadata[0].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_TYPE;
    serviceEndpointPropertiesMetadata[0].value = &amp;metadataExchangeTypeHttpGet;
    serviceEndpointPropertiesMetadata[0].valueSize = sizeof(metadataExchangeTypeHttpGet);
    
    serviceEndpointPropertiesMetadata[1].id = WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK;
    serviceEndpointPropertiesMetadata[1].value = &amp;closeCallbackProperty;
    serviceEndpointPropertiesMetadata[1].valueSize = sizeof(closeCallbackProperty);
    
    unTypedHttpEndpoint.address.url.chars = L"http://+:80/metadata"; // address given as uri
    unTypedHttpEndpoint.address.url.length = (ULONG)wcslen(unTypedHttpEndpoint.address.url.chars);
    unTypedHttpEndpoint.channelBinding = WS_HTTP_CHANNEL_BINDING; // channel binding for the endpoint
    unTypedHttpEndpoint.channelType = WS_CHANNEL_TYPE_REPLY; // the channel type
    unTypedHttpEndpoint.contract = &amp;messageContract;
    unTypedHttpEndpoint.properties = serviceEndpointPropertiesMetadata;
    unTypedHttpEndpoint.propertyCount = WsCountOf(serviceEndpointPropertiesMetadata);
    
    
    // Specifying WSDL document
    serviceMetadata.documentCount = WsCountOf(metadataDocuments);
    serviceMetadata.documents = (WS_SERVICE_METADATA_DOCUMENT**) metadataDocuments;
    
    // Initializing name of the service
    serviceMetadata.serviceName = &amp;serviceName;
    
    // Note that this should concide be the target namespace of the wsdl document 
    serviceMetadata.serviceNs = &amp;serviceNamespace;
    
    // Specifying metadata document
    serviceProperties[0].id = WS_SERVICE_PROPERTY_METADATA;
    serviceProperties[0].value =  &amp;serviceMetadata;
    serviceProperties[0].valueSize = sizeof(serviceMetadata);
    
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &amp;error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // Create Event object for closing the server
    closeServer = CreateEvent(
        NULL, 
        TRUE, 
        FALSE, 
        NULL);
    if (closeServer == NULL)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto Exit;
    }   
    
    
    // Creating a service host
    hr = WsCreateServiceHost(serviceEndpoints, WsCountOf(serviceEndpoints), serviceProperties, WsCountOf(serviceProperties), &amp;host, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // WsOpenServiceHost to start the listeners in the service host 
    hr = WsOpenServiceHost(host, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    WaitForSingleObject(closeServer, INFINITE);
    // Close the service host
    hr = WsCloseServiceHost(host, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
Exit:
    if (FAILED(hr))
    {
        // Print out the error
        PrintError(hr, error);
    }
    fflush(
        stdout);
    if (host != NULL)
    {
        WsFreeServiceHost(host);
    }
    
    
    if (error != NULL)
    {
        WsFreeError(error);
    }
    if (closeServer != NULL)
    {
        CloseHandle(closeServer);
    }
    fflush(stdout);
    return SUCCEEDED(hr) ? 0 : -1;
}



```



## PurchaseOrder.wsdl

``` syntax
<wsdl:definitions 
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" 
    xmlns:tns="http://example.org" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
    xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" 
    xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" 
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" 
    targetNamespace="http://example.org">
    <wsdl:types>
        <xsd:schema targetNamespace="http://example.org" elementFormDefault="qualified">
            <xsd:element name="PurchaseOrderType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="quantity" type="xsd:int"/>
                        <xsd:element minOccurs="0" name="productName" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="OrderConfirmationType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="orderID" type="xsd:unsignedInt"/>
                        <xsd:element minOccurs="0" name="expectedShipDate" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="GetOrderStatusType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="orderID" type="xsd:unsignedInt"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="GetOrderStatusResponseType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="orderID" type="xsd:unsignedInt"/>
                        <xsd:element minOccurs="0" name="status" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="OrderNotFoundFaultType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="orderID" type="xsd:unsignedInt"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
        </xsd:schema>
    </wsdl:types>
    <wsdl:message name="PurchaseOrder">
        <wsdl:part name="parameters" element="tns:PurchaseOrderType"/>
    </wsdl:message>
    <wsdl:message name="OrderConfirmation">
        <wsdl:part name="parameters" element="tns:OrderConfirmationType"/>
    </wsdl:message>
    <wsdl:message name="GetOrderStatus">
        <wsdl:part name="parameters" element="tns:GetOrderStatusType"/>
    </wsdl:message>
    <wsdl:message name="GetOrderStatusResponse">
        <wsdl:part name="parameters" element="tns:GetOrderStatusResponseType"/>
    </wsdl:message>
    <wsdl:message name="OrderNotFoundFault">
        <wsdl:part name="parameters" element="tns:OrderNotFoundFaultType"/>
    </wsdl:message>
    <wsdl:portType name="IPurchaseOrder">
        <wsdl:operation name="Order">
            <wsdl:input message="tns:PurchaseOrder" wsaw:Action="http://example.org/purchaseorder"/>
            <wsdl:output message="tns:OrderConfirmation" wsaw:Action="http://example.org/orderconfirmation"/>
        </wsdl:operation>
        <wsdl:operation name="OrderStatus">
            <wsdl:input message="tns:GetOrderStatus" wsaw:Action="http://example.org/getorderstatus"/>
            <wsdl:output message="tns:GetOrderStatusResponse" wsaw:Action="http://example.org/getorderstatusresponse"/>
            <wsdl:fault name="OrderNotFound" message="tns:OrderNotFoundFault" wsaw:Action="http://example.org/ordernotfound"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="PurchaseOrderBinding" type="tns:IPurchaseOrder">
        <soap:binding transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="Order">
            <soap:operation soapAction="http://example.org/purchaseorder" style="document"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="OrderStatus">
            <soap:operation soapAction="http://example.org/getorderstatus" style="document"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="OrderNotFound">
                <soap:body use="literal"/>
            </wsdl:fault>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="PurchaseOrderService">
        <wsdl:port name="IPurchaseOrder" binding="tns:PurchaseOrderBinding">
            <soap:address location="http://example.org/IPurchaseOrder"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

## Makefile

``` syntax
#------------------------------------------------------------
# Copyright (C) Microsoft.  All rights reserved.
#------------------------------------------------------------

!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib Iphlpapi.lib

all: $(OUTDIR) $(OUTDIR)\WsHttpGetService.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    

$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\HttpGetService.obj: HttpGetService.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" HttpGetService.cpp

$(OUTDIR)\WsHttpGetService.exe: $(OUTDIR)\HttpGetService.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsHttpGetService.exe $(OUTDIR)\HttpGetService.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsHttpGetService.PDB

clean:
    $(CLEANUP)
```

 

 




