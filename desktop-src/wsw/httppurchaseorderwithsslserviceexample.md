---
title: HttpPurchaseOrderWithSslServiceExample
description: This example shows how to use service host for hosting a PurchaseOrder service over HTTP, with SSL transport security.
ms.assetid: 814660d7-98d7-4038-8243-d2f37929d516
keywords:
- HttpPurchaseOrderWithSslServiceExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# HttpPurchaseOrderWithSslServiceExample

This example shows how to use service host for hosting a PurchaseOrder service over HTTP, with SSL transport security.

-   [HttpPurchaseOrderServiceWithSsl.cpp](#httppurchaseorderservicewithsslcpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## HttpPurchaseOrderServiceWithSsl.cpp


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
#include "wincrypt.h"
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

volatile long numberOfOrders = 0;


HRESULT CALLBACK PurchaseOrderImpl(
    __in const WS_OPERATION_CONTEXT* context,
    __in int quantity, 
    __in WS_STRING productName, 
    __out unsigned int* orderID,
    __in WS_STRING* expectedShipDate, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    WS_HEAP* heap = NULL;
    HRESULT hr = NOERROR;
    
    wprintf(L"%ld, %.*s\n", 
        quantity, 
        productName.length,
        productName.chars);
    fflush(stdout);
    
    hr = WsGetOperationContextProperty(
        context, 
        WS_OPERATION_CONTEXT_PROPERTY_HEAP, 
        &heap, 
        sizeof(heap), 
        error);
if (FAILED(hr))
{
    goto Exit;
}
    
    hr = WsAlloc(
        heap, 
        sizeof(ExpectedShipDate), 
        (void**)&expectedShipDate->chars, 
        error);
if (FAILED(hr))
{
    goto Exit;
}
    
    hr = StringCbCopyW(
        expectedShipDate->chars, 
        sizeof(ExpectedShipDate), 
        ExpectedShipDate);
if (FAILED(hr))
{
    goto Exit;
}
    
    *orderID = 123;
    expectedShipDate->length = (ULONG)wcslen(ExpectedShipDate);
    
Exit:
    return hr;
}


HRESULT CALLBACK GetOrderStatusImpl(
    __in const WS_OPERATION_CONTEXT* context,
    __out unsigned int* orderID,
    __out WS_STRING* status, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    WS_HEAP* heap = NULL;
    HRESULT hr = NOERROR;

    // Generate a fault if we don't recognize the order ID
    if (*orderID != 123)
    {
        // Fill out details about the fault
        _OrderNotFoundFaultType orderNotFound;
        orderNotFound.orderID = *orderID;
        
        // TODO: the following should be removed when wsutil generates it
        WS_XML_STRING _faultDetailName = WS_XML_STRING_VALUE("OrderNotFound");
        WS_XML_STRING _faultDetailNs = WS_XML_STRING_VALUE("http://example.com");
        WS_XML_STRING _faultAction = WS_XML_STRING_VALUE("http://example.com/fault");
        WS_ELEMENT_DESCRIPTION _faultElementDescription = { &_faultDetailName, &_faultDetailNs, WS_UINT32_TYPE, NULL };
        WS_FAULT_DETAIL_DESCRIPTION orderNotFoundFaultTypeDescription = { &_faultAction, &_faultElementDescription };
        
        // Set fault detail information in the error object
        hr = WsSetFaultErrorDetail(
            error,
            &orderNotFoundFaultTypeDescription,
            WS_WRITE_REQUIRED_VALUE,
            &orderNotFound,
            sizeof(orderNotFound));
        
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        // Add an error string to the error object.  This string will
        // be included in the fault that is sent.
        WS_STRING errorMessage = WS_STRING_VALUE(L"Invalid order ID");
        hr = WsAddErrorString(error, &errorMessage);
        
        if (FAILED(hr))
        {
            goto Exit;
        }

        hr = E_FAIL;
        goto Exit;
    }
    
    *orderID = *orderID;
    
    hr = WsGetOperationContextProperty(
        context, 
        WS_OPERATION_CONTEXT_PROPERTY_HEAP, 
        &heap, 
        sizeof(heap), 
        error);
if (FAILED(hr))
{
    goto Exit;
}
    
    hr = WsAlloc(
        heap, 
        sizeof(OrderStatusString), 
        (void**)&status->chars, 
        error);
if (FAILED(hr))
{
    goto Exit;
}
    
    hr = StringCbCopyW(
        status->chars, 
        sizeof(OrderStatusString), 
        OrderStatusString);
if (FAILED(hr))
{
    goto Exit;
}
    
    status->length = (ULONG)wcslen(OrderStatusString);
Exit:
    return hr;
}

HRESULT CALLBACK CloseChannelCallback(const WS_OPERATION_CONTEXT* context, const WS_ASYNC_CONTEXT* asyncContext)
{
    UNREFERENCED_PARAMETER(context);
    UNREFERENCED_PARAMETER(asyncContext);

    ULONG orderCount = InterlockedIncrement(
        &numberOfOrders);
    if (orderCount == 300)
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
    WS_SERVICE_ENDPOINT serviceEndpoint = {};
    const WS_SERVICE_ENDPOINT* serviceEndpoints[1];
    serviceEndpoints[0] = &serviceEndpoint;
    WS_ERROR* error = NULL;
    
    // declare and initialize an SSL transport security binding
    WS_SSL_TRANSPORT_SECURITY_BINDING sslBinding = {}; // zero out the struct
    sslBinding.binding.bindingType = WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE; // set the binding type
    // NOTE: At the server, the SSL certificate for the listen URI must be
    // registered with http.sys using a tool such as httpcfg.exe.
    
    // declare and initialize the array of all security bindings
    WS_SECURITY_BINDING* securityBindings[1] = { &sslBinding.binding };
    
    // declare and initialize the security description
    WS_SECURITY_DESCRIPTION securityDescription = {}; // zero out the struct
    securityDescription.securityBindings = securityBindings;
    securityDescription.securityBindingCount = WsCountOf(securityBindings);
    WS_SERVICE_ENDPOINT_PROPERTY serviceProperties[1];
    WS_SERVICE_PROPERTY_CLOSE_CALLBACK closeCallbackProperty = {CloseChannelCallback};
    serviceProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK;
    serviceProperties[0].value = &closeCallbackProperty;
    serviceProperties[0].valueSize = sizeof(closeCallbackProperty);
    
    
    // Initialize service endpoint
    serviceEndpoint.address.url.chars = L"https://localhost:8443/example"; // address given as uri
    serviceEndpoint.address.url.length = (ULONG)wcslen(serviceEndpoint.address.url.chars);
    serviceEndpoint.channelBinding = WS_HTTP_CHANNEL_BINDING; // channel binding for the endpoint
    serviceEndpoint.channelType = WS_CHANNEL_TYPE_REPLY; // the channel type
    serviceEndpoint.securityDescription = &securityDescription; // security description
    serviceEndpoint.contract = &purchaseOrderContract;  // the contract
    serviceEndpoint.properties = serviceProperties;
    serviceEndpoint.propertyCount = WsCountOf(serviceProperties);
    
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
        NULL, 
        0, 
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
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib Iphlpapi.lib

all: $(OUTDIR) $(OUTDIR)\WsHttpPurchaseOrderServiceWithSsl.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\HttpPurchaseOrderServiceWithSsl.obj: HttpPurchaseOrderServiceWithSsl.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" HttpPurchaseOrderServiceWithSsl.cpp

$(OUTDIR)\WsHttpPurchaseOrderServiceWithSsl.exe: $(OUTDIR)\HttpPurchaseOrderServiceWithSsl.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsHttpPurchaseOrderServiceWithSsl.exe $(OUTDIR)\HttpPurchaseOrderServiceWithSsl.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsHttpPurchaseOrderServiceWithSsl.PDB

clean:
    $(CLEANUP)
```

 

 




