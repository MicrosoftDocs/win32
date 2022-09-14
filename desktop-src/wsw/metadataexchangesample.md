---
title: MetadataExchangeSample
description: This example shows how to use service host for hosting a PurchaseOrder service over TCP. The service also supports WS-MetadataExchange.
ms.assetid: 8f14e6a8-ccb9-4556-b04f-df08c6c80adf
keywords:
- MetadataExchangeSample Windows Web Services API
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# MetadataExchangeSample

This example shows how to use service host for hosting a PurchaseOrder service over TCP. The service also supports WS-MetadataExchange.

-   [MexService.cpp](#mexservicecpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## MexService.cpp


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
        hr = WsGetErrorProperty(error, WS_ERROR_PROPERTY_STRING_COUNT, &errorCount, sizeof(errorCount));
        if (FAILED(hr))
        {
            goto Exit;
        }
        for (ULONG i = 0; i < errorCount; i++)
        {
            WS_STRING string;
            hr = WsGetErrorString(error, i, &string);
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
"  <wsp:Policy wsu:Id='NetTcpBinding_HelloService_policy'>"
"   <wsp:ExactlyOne>"
"      <wsp:All>"
"       <msb:BinaryEncoding xmlns:msb='http://schemas.microsoft.com/ws/06/2004/mspolicy/netbinary1'/>"
"       <wsaw:UsingAddressing/>"
"      </wsp:All>"
"   </wsp:ExactlyOne>"
"  </wsp:Policy>"
"  <wsdl:types>"
"    <xsd:schema targetNamespace='http://example.org/Imports'>"
"      <xsd:import namespace='http://example.org' />"
"    </xsd:schema>"
"  </wsdl:types>"
"  <wsdl:message name='PurchaseOrder'>"
"        <wsdl:part name='parameters' element='tns:PurchaseOrderType'/>"
"  </wsdl:message>"
"  <wsdl:message name='OrderConfirmation'>"
"        <wsdl:part name='parameters' element='tns:OrderConfirmationType'/>"
"  </wsdl:message>"
"  <wsdl:message name='GetOrderStatus'>"
"        <wsdl:part name='parameters' element='tns:GetOrderStatusType'/>"
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
"  <wsp:PolicyReference URI='#NetTcpBinding_HelloService_policy'/>"
"  <soap12:binding transport='http://schemas.microsoft.com/soap/tcp'/>"
"        <wsdl:operation name='Order'>"
"            <soap12:operation soapAction='http://example.org/purchaseorder' style='document'/>"
"            <wsdl:input>"
"                <soap12:body use='literal'/>"
"            </wsdl:input>"
"            <wsdl:output>"
"                <soap12:body use='literal'/>"
"            </wsdl:output>"
"        </wsdl:operation>"
"        <wsdl:operation name='OrderStatus'>"
"            <soap12:operation soapAction='http://example.org/getorderstatus' style='document'/>"
"            <wsdl:input>"
"                <soap12:body use='literal'/>"
"            </wsdl:input>"
"            <wsdl:output>"
"                <soap12:body use='literal'/>"
"            </wsdl:output>"
"        </wsdl:operation>"
"    </wsdl:binding>"
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

static const WS_STRING wsdlDocumentName = WS_STRING_VALUE(L"wsdl");
static const WS_STRING xsdDocumentName = WS_STRING_VALUE(L"xsd");
static const WS_SERVICE_METADATA_DOCUMENT wsdlDocument =
{
    (WS_XML_STRING*)&wsdl,
    (WS_STRING*)&wsdlDocumentName
};

static const WS_SERVICE_METADATA_DOCUMENT xsdDocument =
{
    (WS_XML_STRING*)&xsd,
    (WS_STRING*)&xsdDocumentName
};

static const WS_SERVICE_METADATA_DOCUMENT* metadataDocuments[] =
{
    &wsdlDocument,
    &xsdDocument
};

                
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
    
    hr = WsGetOperationContextProperty(context, WS_OPERATION_CONTEXT_PROPERTY_HEAP, &heap, sizeof(heap), error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = WsAlloc(heap, sizeof(ExpectedShipDate), (void**)&expectedShipDate->chars, error);
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
    
    hr = WsGetOperationContextProperty(context, WS_OPERATION_CONTEXT_PROPERTY_HEAP, &heap, sizeof(heap), error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = WsAlloc(heap, sizeof(OrderStatusString), (void**)&status->chars, error);
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

    if (InterlockedIncrement(&numberOfSession) == 2)
    {
        SetEvent(closeServer);
    }
    return NOERROR;
}

static const PurchaseOrderBindingFunctionTable purchaseOrderFunctions = {PurchaseOrderImpl, GetOrderStatusImpl};

// Method contract for the service
static const WS_SERVICE_CONTRACT purchaseOrderContract = 
{
    &PurchaseOrder_wsdl.contracts.PurchaseOrderBinding, // comes from the generated header.
    NULL, // for not specifying the default contract
    &purchaseOrderFunctions // specified by the user
};


// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_SERVICE_HOST* host = NULL;
    WS_SERVICE_ENDPOINT serviceEndpoint = {0};
    const WS_SERVICE_ENDPOINT* serviceEndpoints[1];
    serviceEndpoints[0] = &serviceEndpoint;
    WS_ERROR* error = NULL;
    HANDLE serverStartedEvent = NULL;
    WS_SERVICE_PROPERTY serviceProperties[1];
    WS_SERVICE_METADATA serviceMetadata = {0};
    WS_SERVICE_ENDPOINT_PROPERTY serviceEndpointProperties[4];
    WS_SERVICE_PROPERTY_CLOSE_CALLBACK closeCallbackProperty = {CloseChannelCallback};
    WS_SERVICE_ENDPOINT_METADATA endpointMetadata = {0};
    WS_METADATA_EXCHANGE_TYPE metadataExchangeType = WS_METADATA_EXCHANGE_TYPE_MEX;
    
    // Configure Port on the endpoint for Mex
    endpointMetadata.portName = &portName;
    endpointMetadata.bindingName = &bindingName;
    endpointMetadata.bindingNs = &bindingNs;                    
    
    serviceEndpointProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK;
    serviceEndpointProperties[0].value = &closeCallbackProperty;
    serviceEndpointProperties[0].valueSize = sizeof(closeCallbackProperty);
    
    // Specifying Port on the endpoint.
    serviceEndpointProperties[1].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA;
    serviceEndpointProperties[1].value = &endpointMetadata;
    serviceEndpointProperties[1].valueSize = sizeof(endpointMetadata);
    
    // Marking the endpoint to service WS-MetadataExchnage Requests
    serviceEndpointProperties[2].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_TYPE;
    serviceEndpointProperties[2].value = &metadataExchangeType;
    serviceEndpointProperties[2].valueSize = sizeof(metadataExchangeType);
    
    WS_STRING mexPrefix = WS_STRING_VALUE(L"mex");
    // Marking the endpoint to service WS-MetadataExchnage Requests
    serviceEndpointProperties[3].id = WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_URL_SUFFIX;
    serviceEndpointProperties[3].value = &mexPrefix;
    serviceEndpointProperties[3].valueSize = sizeof(mexPrefix);
    
    serviceEndpoint.address.url.chars = L"net.tcp://localhost/example"; // address given as uri
    serviceEndpoint.address.url.length = (ULONG)wcslen(serviceEndpoint.address.url.chars);
    serviceEndpoint.channelBinding = WS_TCP_CHANNEL_BINDING; // channel binding for the endpoint
    serviceEndpoint.channelType = WS_CHANNEL_TYPE_DUPLEX_SESSION; // the channel type
    serviceEndpoint.contract = (WS_SERVICE_CONTRACT*)&purchaseOrderContract;  // the contract
    serviceEndpoint.properties = serviceEndpointProperties;
    serviceEndpoint.propertyCount = WsCountOf(serviceEndpointProperties);
        
    // Specifying WSDL document
    serviceMetadata.documentCount = WsCountOf(metadataDocuments);
    serviceMetadata.documents = (WS_SERVICE_METADATA_DOCUMENT**) metadataDocuments;
    
    // Initializing name of the service
    serviceMetadata.serviceName = &serviceName;
    
    // Note that this should concide be the target namespace of the wsdl document 
    serviceMetadata.serviceNs = &serviceNamespace;
    
    // Specifying metadata document
    serviceProperties[0].id = WS_SERVICE_PROPERTY_METADATA;
    serviceProperties[0].value =  &serviceMetadata;
    serviceProperties[0].valueSize = sizeof(serviceMetadata);
    
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
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
    hr = WsCreateServiceHost(
        serviceEndpoints, 
        1, 
        serviceProperties, 
        WsCountOf(serviceProperties), 
        &host, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // WsOpenServiceHost to start the listeners in the service host 
    hr = WsOpenServiceHost(
            host, 
            NULL, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // Create an event to synchronize the client and server processes.
    serverStartedEvent = CreateEventW(
        NULL, 
        TRUE, 
        FALSE, 
        L"WebServicesExampleServerStartedEvent");
    if (NULL == serverStartedEvent)
    {
        wprintf(
            L"Failed to create the client-server synchronization event (errorCode=0x%lx).\n",
            GetLastError());
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto Exit;
    }
    // Server is started, set the event to signal the clients.
    if (!SetEvent(
            serverStartedEvent))
    {
        wprintf(
            L"Failed to set the client-server synchronization event (errorCode=0x%lx).\n", 
            GetLastError());
        hr = HRESULT_FROM_WIN32(GetLastError());
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
    if (NULL != serverStartedEvent)
    {
        CloseHandle(serverStartedEvent);
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
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib Iphlpapi.lib

all: $(OUTDIR) $(OUTDIR)\WsMexService.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    

$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\MexService.obj: MexService.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" MexService.cpp

$(OUTDIR)\WsMexService.exe: $(OUTDIR)\MexService.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsMexService.exe $(OUTDIR)\MexService.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsMexService.PDB

clean:
    $(CLEANUP)
```

 

 




