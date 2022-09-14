---
title: RequestReplyNamedPipesClientWithWindowsTransportSecurityExample
description: This example shows a named pipes client that sends request-reply messages with security provided by Windows SSPI transport security. It illustrates the client using security token properties to modify the allowed impersonation level from the default.
ms.assetid: 50BA8F67-95F4-414A-952C-8AF91C511753
ms.topic: article
ms.date: 05/31/2018
---

# RequestReplyNamedPipesClientWithWindowsTransportSecurityExample

This example shows a named pipes client that sends request-reply messages with security provided by Windows SSPI transport security. It illustrates the client using security token properties to modify the allowed impersonation level from the default.

-   [RequestReplyNamedPipesClientWithWindowsTransportSecurity.cpp](#requestreplynamedpipesclientwithwindowstransportsecuritycpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## RequestReplyNamedPipesClientWithWindowsTransportSecurity.cpp


```C++
//------------------------------------------------------------
// Copyright (c) Microsoft Corporation.  All rights reserved.
//------------------------------------------------------------

#ifndef UNICODE
#define UNICODE
#endif
#include "WebServices.h"
#include "process.h"
#include "stdio.h"
#include "string.h"
#include "wincrypt.h"
#include "PurchaseOrder.wsdl.h"

// Print out rich error info
void PrintError(
    __in HRESULT errorCode, 
    __in_opt WS_ERROR* error)
{
    wprintf(L"Failure: errorCode=0x%lx\n", errorCode);

    if (errorCode == E_INVALIDARG || errorCode == WS_E_INVALID_OPERATION)
    {
        // Correct use of the APIs should never generate these errors
        wprintf(L"The error was due to an invalid use of an API.  This is likely due to a bug in the program.\n");
        DebugBreak();
    }

    HRESULT hr = S_OK;
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

// Main entry point
int __cdecl wmain()
{
    
    HRESULT hr = S_OK;
    WS_ERROR* error = NULL;
    WS_CHANNEL* channel = NULL;
    WS_MESSAGE* requestMessage = NULL;
    WS_MESSAGE* replyMessage = NULL;
    WS_HEAP* heap = NULL;
    
    // declare and initialize a windows credential
    WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL windowsCredential = {}; // zero out the struct
    windowsCredential.credential.credentialType = WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE; // set the credential type
    
    ULONG impersonation = SecurityImpersonation;
    BOOL requireServerAuth = FALSE;
    
    // declare and initialize properties to change the impersonation level from the default.
    // to run client and service on single machine you have to specify either:
    //  - WS_WINDOWS_INTEGRATED_AUTH_PACKAGE set to WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_KERBEROS
    //  - or WS_SECURITY_BINDING_PROPERTY_REQUIRE_SERVER_AUTH set to FALSE (less secure but should always work).
    // in default settings NTLM is used and it does not support server authentication.
    WS_SECURITY_BINDING_PROPERTY sspiBindingProperties[2] =
    {
        { WS_SECURITY_BINDING_PROPERTY_ALLOWED_IMPERSONATION_LEVEL, &impersonation, sizeof(impersonation) },
        { WS_SECURITY_BINDING_PROPERTY_REQUIRE_SERVER_AUTH, &requireServerAuth, sizeof(requireServerAuth) } 
    };
    
    // declare and initialize an Windows SSPI transport security binding
    WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING sspiBinding = {}; // zero out the struct
    sspiBinding.binding.bindingType = WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING_TYPE; // set the binding type
    sspiBinding.binding.properties = sspiBindingProperties;
    sspiBinding.binding.propertyCount = WsCountOf(sspiBindingProperties);
    sspiBinding.clientCredential = &windowsCredential.credential;
    
    // declare and initialize the array of all security bindings
    WS_SECURITY_BINDING* securityBindings[1] = { &sspiBinding.binding };
    
    // declare and initialize the security description
    WS_SECURITY_DESCRIPTION securityDescription = {}; // zero out the struct
    securityDescription.securityBindings = securityBindings;
    securityDescription.securityBindingCount = WsCountOf(securityBindings);
    
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
    
    
    
    // Create a named pipe duplex session channel
    hr = WsCreateChannel(
        WS_CHANNEL_TYPE_DUPLEX_SESSION, 
        WS_NAMEDPIPE_CHANNEL_BINDING, 
        NULL, 
        0, 
        &securityDescription, 
        &channel, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Initialize address of service
    WS_ENDPOINT_ADDRESS address;
    address.url.chars = L"net.pipe://localhost/example";
    address.url.length = (ULONG)::wcslen(address.url.chars);
    address.headers = NULL;
    address.extensions = NULL;
    address.identity = NULL;
    
    // Open channel to address
    hr = WsOpenChannel(
        channel, 
        &address, 
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsCreateMessageForChannel(
        channel,
        NULL, 
        0, 
        &requestMessage, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsCreateMessageForChannel(
        channel,
        NULL, 
        0, 
        &replyMessage, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Send some request-replies
    for (int i = 0; i < 100; i++)
    {
        // Initialize purchase order
        _PurchaseOrderType purchaseOrder;
        purchaseOrder.quantity = 100;
        WS_STRING name = WS_STRING_VALUE(L"pencil");
        purchaseOrder.productName = name;
        
        _OrderConfirmationType orderConfirmation;
        
        // Send purchase order, get order confirmation
        hr = WsRequestReply(
            channel,
            requestMessage, 
            &PurchaseOrder_wsdl.messages.PurchaseOrder, 
            WS_WRITE_REQUIRED_VALUE,
            &purchaseOrder,
            sizeof(purchaseOrder),
            replyMessage, 
            &PurchaseOrder_wsdl.messages.OrderConfirmation, 
            WS_READ_REQUIRED_VALUE, 
            heap, 
            &orderConfirmation, 
            sizeof(orderConfirmation), 
            NULL, 
            error);
        
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        // Print out confirmation contents
        wprintf(L"Expected ship date for order %lu is %s\n",
            orderConfirmation.orderID,
            orderConfirmation.expectedShipDate);
        
        // Reset the message so it can be used again
        hr = WsResetMessage(requestMessage, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        // Reset the message so it can be used again
        hr = WsResetMessage(replyMessage, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        // Initialize request for order status
        _GetOrderStatusType getOrderStatus;
        getOrderStatus.orderID = orderConfirmation.orderID;
        
        _GetOrderStatusResponseType getOrderStatusResponse;
        
        // Send order status request, get order status reply
        hr = WsRequestReply(
            channel,
            requestMessage, 
            &PurchaseOrder_wsdl.messages.GetOrderStatus, 
            WS_WRITE_REQUIRED_VALUE,
            &getOrderStatus,
            sizeof(getOrderStatus),
            replyMessage, 
            &PurchaseOrder_wsdl.messages.GetOrderStatusResponse, 
            WS_READ_REQUIRED_VALUE, 
            heap, 
            &getOrderStatusResponse, 
            sizeof(getOrderStatusResponse), 
            NULL, 
            error);
        
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        // Print out order status
        wprintf(L"Order status for order %lu is: %s\n",
            getOrderStatusResponse.orderID,
            getOrderStatusResponse.status);
        
        // Reset the message so it can be used again
        hr = WsResetMessage(requestMessage, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        // Reset the message so it can be used again
        hr = WsResetMessage(replyMessage, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        // Make same request, but this time with an invalid order ID
        getOrderStatus.orderID = 321;
        hr = WsRequestReply(
            channel,
            requestMessage, 
            &PurchaseOrder_wsdl.messages.GetOrderStatus, 
            WS_WRITE_REQUIRED_VALUE,
            &getOrderStatus,
            sizeof(getOrderStatus),
            replyMessage, 
            &PurchaseOrder_wsdl.messages.GetOrderStatusResponse, 
            WS_READ_REQUIRED_VALUE, 
            heap, 
            &getOrderStatusResponse, 
            sizeof(getOrderStatusResponse), 
            NULL, 
            error);
        
        // Check to see if we got a fault
        if (hr == WS_E_ENDPOINT_FAULT_RECEIVED)
        {
            // Print the strings in the error object
            PrintError(hr, error);
        
            static const WS_XML_STRING _faultDetailName = WS_XML_STRING_VALUE("OrderNotFound");
            static const WS_XML_STRING _faultDetailNs = WS_XML_STRING_VALUE("http://example.com");
            static const WS_XML_STRING _faultAction = WS_XML_STRING_VALUE("http://example.com/fault");
            static const WS_ELEMENT_DESCRIPTION _faultElementDescription = 
            { 
                (WS_XML_STRING*)&_faultDetailName, 
                (WS_XML_STRING*)&_faultDetailNs, 
                WS_UINT32_TYPE, 
                NULL 
            };
            static const WS_FAULT_DETAIL_DESCRIPTION orderNotFoundFaultTypeDescription = 
            { 
                (WS_XML_STRING*)&_faultAction, 
                (WS_ELEMENT_DESCRIPTION*)&_faultElementDescription 
            };
        
            // Try to get the fault detail from the error object
            _OrderNotFoundFaultType* orderNotFound;
            hr = WsGetFaultErrorDetail(
                error,
                &orderNotFoundFaultTypeDescription,
                WS_READ_OPTIONAL_POINTER,
                heap,
                &orderNotFound,
                sizeof(orderNotFound));
                
            if (FAILED(hr))
            {
                goto Exit;
            }
        
            if (orderNotFound != NULL)
            {
                // Print out the fault detail
                wprintf(L"Order %lu was not found\n", orderNotFound->orderID);
            }
        
            // Reset error so it can be used again
            hr = WsResetError(error);
            if (FAILED(hr))
            {
                goto Exit;
            }
        }
        
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        // Reset the message so it can be used again
        hr = WsResetMessage(requestMessage, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        // Reset the message so it can be used again
        hr = WsResetMessage(replyMessage, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        wprintf(L"\n");
        
        // Reset the heap
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
    
    if (channel != NULL)
    {
        // Close the channel
        WsCloseChannel(channel, NULL, error);
    }
    if (requestMessage != NULL)
    {
        WsFreeMessage(requestMessage);
    }
    if (replyMessage != NULL)
    {
        WsFreeMessage(replyMessage);
    }
    if (channel != NULL)
    {
        WsFreeChannel(channel);
    }
    
    
    if (error != NULL)
    {
        WsFreeError(error);
    }
    if (heap != NULL)
    {
        WsFreeHeap(heap);
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

all: $(OUTDIR) $(OUTDIR)\WsOneWayUdpServer.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    

$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\OneWayUdpServer.obj: OneWayUdpServer.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" OneWayUdpServer.cpp

$(OUTDIR)\WsOneWayUdpServer.exe: $(OUTDIR)\OneWayUdpServer.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsOneWayUdpServer.exe $(OUTDIR)\OneWayUdpServer.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsOneWayUdpServer.PDB

clean:
    $(CLEANUP)
```

 

 




