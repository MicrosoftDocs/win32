---
title: HttpCustomHeaderPurchaseOrderClientExample
description: This examples shows how to use custom headers with service proxy.
ms.assetid: d56e68cd-c910-4f41-a672-c894ba134e3b
keywords:
- HttpCustomHeaderPurchaseOrderClientExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# HttpCustomHeaderPurchaseOrderClientExample

This examples shows how to use custom headers with service proxy.

-   [HttpCustomHeaderClient.cpp](#httpcustomheaderclientcpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [OrderSessionHeader.xsd](#ordersessionheaderxsd)
-   [Makefile](#makefile)

## HttpCustomHeaderClient.cpp


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


HRESULT CALLBACK AddSessionHeader(
    __in WS_MESSAGE* message,
    __in WS_HEAP* heap,
    __in void* state,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(heap);

    _OrderSession* orderSession = (_OrderSession*) state;
    // Add reply sessionID
    return WsAddCustomHeader(
        message, 
        &OrderSessionHeader_xsd.globalElements.OrderSession, 
        WS_WRITE_REQUIRED_VALUE,
        orderSession, 
        sizeof(*orderSession), 
        0, 
        error);
}

HRESULT CALLBACK RetrieveSessionHeader(
    __in WS_MESSAGE* message,
    __in WS_HEAP* heap,
    __in void* state,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(heap);

    _OrderSession* inputOrderSession = (_OrderSession*) state;
    _OrderSession* outputOrderSession = NULL;

    HRESULT hr = WsGetCustomHeader(
        message, 
        &OrderSessionHeader_xsd.globalElements.OrderSession, 
        WS_SINGLETON_HEADER,
        0,
        WS_READ_REQUIRED_POINTER, 
        NULL, 
        &outputOrderSession, 
        sizeof(outputOrderSession), 
        NULL, 
        error);
    if (FAILED(hr))
    {
        return hr;
    }
    
    wprintf(L"%.*s == %.*s\n", 
        outputOrderSession->sessionId.length,
        outputOrderSession->sessionId.chars,
        inputOrderSession->sessionId.length,
        inputOrderSession->sessionId.chars
        );
    fflush(stdout);
    
    return NOERROR;
}



// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_SERVICE_PROXY* serviceProxy = NULL;
    WS_HEAP* heap = NULL;
    WS_ENDPOINT_ADDRESS address = {0};
    WS_STRING serviceUrl = WS_STRING_VALUE(L"http://localhost/example");
    address.url = serviceUrl;
    WS_CALL_PROPERTY callProperties[2];
    WS_STRING sessionId = WS_STRING_VALUE(L"ExampleSession");
    _OrderSession orderSession;
    orderSession.sessionId = sessionId;
    WS_PROXY_MESSAGE_CALLBACK_CONTEXT inputMessageContext = {0};
    WS_PROXY_MESSAGE_CALLBACK_CONTEXT outputMessageContext = {0};
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // Create a heap to store deserialized data
    hr = WsCreateHeap(
        /*maxSize*/ 2048, 
        /*trimSize*/ 512, 
        NULL, 
        0, 
        &heap, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsCreateServiceProxy(
            WS_CHANNEL_TYPE_REQUEST, 
            WS_HTTP_CHANNEL_BINDING, 
            NULL, 
            NULL,
            0,
            NULL, 
            0, 
            &serviceProxy, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    
    // Open channel to address
    hr = WsOpenServiceProxy(
            serviceProxy, 
            &address, 
            NULL, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    inputMessageContext.callback = AddSessionHeader;
    inputMessageContext.state = &orderSession;
    outputMessageContext.callback = RetrieveSessionHeader;
    outputMessageContext.state = &orderSession;
    
    callProperties[0].id = WS_CALL_PROPERTY_SEND_MESSAGE_CONTEXT;
    callProperties[0].value = &inputMessageContext;
    callProperties[0].valueSize = sizeof(inputMessageContext);
    
    callProperties[1].id = WS_CALL_PROPERTY_RECEIVE_MESSAGE_CONTEXT;
    callProperties[1].value = &outputMessageContext;
    callProperties[1].valueSize = sizeof(outputMessageContext);
    
    for (int i = 0; i < 100; i++)
    {
        WS_STRING productName = {0};
        WS_STRING expectedShipDate = {0};
        unsigned int orderID;
        productName.chars = L"Pencil";
        productName.length = 6;
    
        hr = PurchaseOrderBinding_Order(
            serviceProxy, 
            100, 
            productName, 
            &orderID, 
            &expectedShipDate, 
            heap, 
            callProperties, 
            WsCountOf(callProperties), 
            NULL, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Print out confirmation contents
        wprintf(L"Expected ship date for order %lu is %.*s\n",
            orderID,
            expectedShipDate.length,
            expectedShipDate.chars);
    
        hr = WsResetHeap(heap, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
    
        
    }
    
Exit:
    if (FAILED(hr))
    {
        // Print out the error
        PrintError(hr, error);
    }
    fflush(
        stdout);
    if (serviceProxy != NULL)
    {
        WsCloseServiceProxy(serviceProxy, NULL, NULL);
        WsFreeServiceProxy(serviceProxy);
    }
    
    
    if (heap != NULL)
    {
        WsFreeHeap(heap);
    }
    if (error != NULL)
    {
        WsFreeError(error);
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

## OrderSessionHeader.xsd

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<xsd:schema targetNamespace="http://example.org/session"
    elementFormDefault="qualified"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
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

all: $(OUTDIR) $(OUTDIR)\WsHttpCustomHeaderClient.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c $(OUTDIR)\OrderSessionHeader.xsd.c: PurchaseOrder.wsdl OrderSessionHeader.xsd
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /xsd:OrderSessionHeader.xsd /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\OrderSessionHeader.xsd.obj: $(OUTDIR)\OrderSessionHeader.xsd.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\OrderSessionHeader.xsd.c

$(OUTDIR)\HttpCustomHeaderClient.obj: HttpCustomHeaderClient.cpp $(OUTDIR)\PurchaseOrder.wsdl.c $(OUTDIR)\OrderSessionHeader.xsd.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" HttpCustomHeaderClient.cpp

$(OUTDIR)\WsHttpCustomHeaderClient.exe: $(OUTDIR)\HttpCustomHeaderClient.obj $(OUTDIR)\PurchaseOrder.wsdl.obj $(OUTDIR)\OrderSessionHeader.xsd.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsHttpCustomHeaderClient.exe $(OUTDIR)\HttpCustomHeaderClient.obj $(OUTDIR)\PurchaseOrder.wsdl.obj $(OUTDIR)\OrderSessionHeader.xsd.obj /PDB:$(OUTDIR)\WsHttpCustomHeaderClient.PDB

clean:
    $(CLEANUP)
```

 

 




