---
title: HttpCustomHeaderPurchaseOrderServiceExample
description: Review a Windows Web Services API (WWSAPI) C++ example of a purchase order service over HTTP custom headers.
ms.assetid: 7a86e0be-6e52-4ad2-bca4-0162a8030cdc
keywords:
- HttpCustomHeaderPurchaseOrderServiceExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# HttpCustomHeaderPurchaseOrderServiceExample

This example shows how to use service host for hosting a PurchaseOrder service over HTTP.

-   [HttpCustomHeaderService.cpp](#httpcustomheaderservicecpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [OrderSessionHeader.xsd](#ordersessionheaderxsd)
-   [Makefile](#makefile)

## HttpCustomHeaderService.cpp


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
#include "OrderSessionHeader.xsd.h"
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
    WS_MESSAGE* inputMessage = NULL;
    WS_MESSAGE* outputMessage = NULL;
    _OrderSession* inputSession = NULL;
    _OrderSession outputSession;
    HRESULT hr = NOERROR;
    
    ZeroMemory(
        &outputSession,
        sizeof(outputSession));

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
        return hr;
    }
    
    hr = WsGetOperationContextProperty(
        context, 
        WS_OPERATION_CONTEXT_PROPERTY_INPUT_MESSAGE, 
        &inputMessage, 
        sizeof(inputMessage), 
        error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = WsGetOperationContextProperty(
        context, 
        WS_OPERATION_CONTEXT_PROPERTY_OUTPUT_MESSAGE, 
        &outputMessage, 
        sizeof(outputMessage), 
        error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = WsGetCustomHeader(
        inputMessage, 
        &OrderSessionHeader_xsd.globalElements.OrderSession, 
        WS_SINGLETON_HEADER,
        0,
        WS_READ_REQUIRED_POINTER, 
        NULL, 
        &inputSession, 
        sizeof(inputSession), 
        NULL, 
        error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    wprintf(L"%.*s\n", 
        inputSession->sessionId.length,
        inputSession->sessionId.chars);
    fflush(stdout);
    
    outputSession = *inputSession;

    // Add reply sessionID
    hr = WsAddCustomHeader(
        outputMessage, 
        &OrderSessionHeader_xsd.globalElements.OrderSession, 
        WS_WRITE_REQUIRED_VALUE,
        &outputSession, 
        sizeof(outputSession), 
        0, 
        error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = WsAlloc(
        heap, 
        sizeof(ExpectedShipDate), 
        (void**)&expectedShipDate->chars, 
        error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    hr = StringCbCopyW(
        expectedShipDate->chars, 
        sizeof(ExpectedShipDate), 
        ExpectedShipDate);
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

    if (InterlockedIncrement(&numberOfSession) == 100)
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
    WS_ERROR* error = NULL;
    serviceEndpoints[0] = &serviceEndpoint;
    
    WS_SERVICE_ENDPOINT_PROPERTY serviceEndpointProperties[1];
    WS_SERVICE_PROPERTY_CLOSE_CALLBACK closeCallbackProperty = {CloseChannelCallback};
    
    serviceEndpointProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK;
    serviceEndpointProperties[0].value = &closeCallbackProperty;
    serviceEndpointProperties[0].valueSize = sizeof(closeCallbackProperty);
    
    serviceEndpoint.address.url.chars = L"https://+/example"; // address given as uri
    serviceEndpoint.address.url.length = (ULONG)wcslen(serviceEndpoint.address.url.chars);
    serviceEndpoint.channelBinding = WS_HTTP_CHANNEL_BINDING; // channel binding for the endpoint
    serviceEndpoint.channelType = WS_CHANNEL_TYPE_REPLY; // the channel type
    serviceEndpoint.contract = (WS_SERVICE_CONTRACT*)&purchaseOrderContract;  // the contract
    serviceEndpoint.properties = serviceEndpointProperties;
    serviceEndpoint.propertyCount = WsCountOf(serviceEndpointProperties);
    
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
    xmlns:soap="https://schemas.xmlsoap.org/wsdl/soap/" 
    xmlns:tns="https://example.org" 
    xmlns:xsd="https://www.w3.org/2001/XMLSchema" 
    xmlns:wsaw="https://www.w3.org/2006/05/addressing/wsdl" 
    xmlns:soap12="https://schemas.xmlsoap.org/wsdl/soap12/" 
    xmlns:wsdl="https://schemas.xmlsoap.org/wsdl/" 
    targetNamespace="https://example.org">
    <wsdl:types>
        <xsd:schema targetNamespace="https://example.org" elementFormDefault="qualified">
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
            <wsdl:input message="tns:PurchaseOrder" wsaw:Action="https://example.org/purchaseorder"/>
            <wsdl:output message="tns:OrderConfirmation" wsaw:Action="https://example.org/orderconfirmation"/>
        </wsdl:operation>
        <wsdl:operation name="OrderStatus">
            <wsdl:input message="tns:GetOrderStatus" wsaw:Action="https://example.org/getorderstatus"/>
            <wsdl:output message="tns:GetOrderStatusResponse" wsaw:Action="https://example.org/getorderstatusresponse"/>
            <wsdl:fault name="OrderNotFound" message="tns:OrderNotFoundFault" wsaw:Action="https://example.org/ordernotfound"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="PurchaseOrderBinding" type="tns:IPurchaseOrder">
        <soap:binding transport="https://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="Order">
            <soap:operation soapAction="https://example.org/purchaseorder" style="document"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="OrderStatus">
            <soap:operation soapAction="https://example.org/getorderstatus" style="document"/>
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
            <soap:address location="https://example.org/IPurchaseOrder"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

## OrderSessionHeader.xsd

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<xsd:schema targetNamespace="https://example.org/session"
    elementFormDefault="qualified"
    xmlns:xsd="https://www.w3.org/2001/XMLSchema"
>
        <xsd:element name="OrderSession">
            <xsd:complexType>
                <xsd:sequence>
                    <xsd:element minOccurs="0" name="sessionId" type="xsd:string"/>
                </xsd:sequence>
            </xsd:complexType>
        </xsd:element>
 </xsd:schema>
```

## Makefile

``` syntax
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib

all: $(OUTDIR) $(OUTDIR)\WsHttpCustomHeaderService.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c $(OUTDIR)\OrderSessionHeader.xsd.c: PurchaseOrder.wsdl OrderSessionHeader.xsd
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /xsd:OrderSessionHeader.xsd /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\OrderSessionHeader.xsd.obj: $(OUTDIR)\OrderSessionHeader.xsd.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\OrderSessionHeader.xsd.c

$(OUTDIR)\HttpCustomHeaderService.obj: HttpCustomHeaderService.cpp $(OUTDIR)\PurchaseOrder.wsdl.c $(OUTDIR)\OrderSessionHeader.xsd.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" HttpCustomHeaderService.cpp

$(OUTDIR)\WsHttpCustomHeaderService.exe: $(OUTDIR)\HttpCustomHeaderService.obj $(OUTDIR)\PurchaseOrder.wsdl.obj $(OUTDIR)\OrderSessionHeader.xsd.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsHttpCustomHeaderService.exe $(OUTDIR)\HttpCustomHeaderService.obj $(OUTDIR)\PurchaseOrder.wsdl.obj $(OUTDIR)\OrderSessionHeader.xsd.obj /PDB:$(OUTDIR)\WsHttpCustomHeaderService.PDB

clean:
    $(CLEANUP)
```

 

 




