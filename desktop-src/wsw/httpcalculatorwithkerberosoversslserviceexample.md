---
title: HttpCalculatorWithKerberosOverSslServiceExample
description: This example shows how to use service host for hosting a calculator service over HTTP, with kerberos over SSL mixed-mode security.
ms.assetid: a006ce15-9470-49f7-80d6-8d40ffec8651
keywords:
- HttpCalculatorWithKerberosOverSslServiceExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# HttpCalculatorWithKerberosOverSslServiceExample

This example shows how to use service host for hosting a calculator service over HTTP, with kerberos over SSL mixed-mode security. In this setup, the transport connection is protected (signed, encrypted) by SSL which also provides server authentication. Client authentication is provided by a kerberos APREQ ticket in a WS-Security header in the message.

-   [CalculatorServiceKerberosOverSsl.cpp](#calculatorservicekerberosoversslcpp)
-   [CalculatorService.wsdl](#calculatorservicewsdl)
-   [Makefile](#makefile)

## CalculatorServiceKerberosOverSsl.cpp


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
#include "CalculatorService.wsdl.h"

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


HRESULT CALLBACK Add(
    __in const WS_OPERATION_CONTEXT* context, 
    __in int a, 
    __in int b, 
    __out int* result, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(context);
    UNREFERENCED_PARAMETER(asyncContext);
    UNREFERENCED_PARAMETER(error);

    *result = a + b;
    printf ("%d + %d = %d\n", a, b, *result);
    fflush(stdout);
    return NOERROR;
}

HRESULT CALLBACK Subtract(
    __in const WS_OPERATION_CONTEXT* context, 
    __in int a, 
    __in int b, 
    __out int* result, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(context);
    UNREFERENCED_PARAMETER(asyncContext);
    UNREFERENCED_PARAMETER(error);

    *result = a - b;
    printf ("%d - %d = %d\n", a, b, *result);
    fflush(stdout);
    return NOERROR;
}

HRESULT CALLBACK CloseChannelCallback(
    __in const WS_OPERATION_CONTEXT* context, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext)
{
    UNREFERENCED_PARAMETER(context);
    UNREFERENCED_PARAMETER(asyncContext);

    SetEvent(closeServer);
    return NOERROR;
}

static const DefaultBinding_ICalculatorFunctionTable calculatorFunctions = {Add, Subtract};

// Method contract for the service
static const WS_SERVICE_CONTRACT calculatorContract = 
{
    &CalculatorService_wsdl.contracts.DefaultBinding_ICalculator, // comes from the generated header.
    NULL, // for not specifying the default contract
    &calculatorFunctions // specified by the user
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
    
    
    // declare and initialize a kerberos APREQ message security binding
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING kerberosBinding = {}; // zero out the struct
    kerberosBinding.binding.bindingType = WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TYPE; // set the binding type
    kerberosBinding.bindingUsage = WS_SUPPORTING_MESSAGE_SECURITY_USAGE; // set the binding usage
    
    // declare and initialize an SSL transport security binding
    WS_SSL_TRANSPORT_SECURITY_BINDING sslBinding = {}; // zero out the struct
    sslBinding.binding.bindingType = WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE; // set the binding type
    // NOTE: At the server, the SSL certificate for the listen URI must be
    // registered with http.sys using a tool such as httpcfg.exe.
    
    // declare and initialize the array of all security bindings
    WS_SECURITY_BINDING* securityBindings[2] = { &sslBinding.binding, &kerberosBinding.binding };
    
    // declare and initialize the security description
    WS_SECURITY_DESCRIPTION securityDescription = {}; // zero out the struct
    securityDescription.securityBindings = securityBindings;
    securityDescription.securityBindingCount = WsCountOf(securityBindings);
    WS_SERVICE_ENDPOINT_PROPERTY serviceEndpointProperties[1];
    WS_SERVICE_PROPERTY_CLOSE_CALLBACK closeCallbackProperty = {CloseChannelCallback};
    serviceEndpointProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK;
    serviceEndpointProperties[0].value = &closeCallbackProperty;
    serviceEndpointProperties[0].valueSize = sizeof(closeCallbackProperty);
    
    
    // Initialize service endpoint
    serviceEndpoint.address.url.chars = L"https://localhost:8443/example"; // address given as uri
    serviceEndpoint.address.url.length = (ULONG)wcslen(serviceEndpoint.address.url.chars);
    serviceEndpoint.channelBinding = WS_HTTP_CHANNEL_BINDING; // channel binding for the endpoint
    serviceEndpoint.channelType = WS_CHANNEL_TYPE_REPLY; // the channel type
    serviceEndpoint.securityDescription = &securityDescription; // security description
    serviceEndpoint.contract = &calculatorContract;  // the contract
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



## CalculatorService.wsdl

``` syntax
<wsdl:definitions 
    xmlns:soap="https://schemas.xmlsoap.org/wsdl/soap/" 
    xmlns:tns="https://Example.org" 
    xmlns:xsd="https://www.w3.org/2001/XMLSchema" 
    xmlns:wsaw="https://www.w3.org/2006/05/addressing/wsdl" 
    xmlns:soap12="https://schemas.xmlsoap.org/wsdl/soap12/" 
    targetNamespace="https://Example.org" 
    xmlns:wsdl="https://schemas.xmlsoap.org/wsdl/">
    <wsdl:types>
        <xsd:schema targetNamespace="https://Example.org" elementFormDefault="qualified" >
            <xsd:element name="Add">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="a" type="xsd:int" />
                        <xsd:element minOccurs="0" name="b" type="xsd:int" />
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="AddResponse">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="result" type="xsd:int" />
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="Subtract">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="a" type="xsd:int" />
                        <xsd:element minOccurs="0" name="b" type="xsd:int" />
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="SubtractResponse">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="result" type="xsd:int" />
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
        </xsd:schema>
    </wsdl:types>
    <wsdl:message name="ICalculator_Add_InputMessage">
        <wsdl:part name="parameters" element="tns:Add" />
    </wsdl:message>
    <wsdl:message name="ICalculator_Add_OutputMessage">
        <wsdl:part name="parameters" element="tns:AddResponse" />
    </wsdl:message>
    <wsdl:message name="ICalculator_Subtract_InputMessage">
        <wsdl:part name="parameters" element="tns:Subtract" />
    </wsdl:message>
    <wsdl:message name="ICalculator_Subtract_OutputMessage">
        <wsdl:part name="parameters" element="tns:SubtractResponse" />
    </wsdl:message>
    <wsdl:portType name="ICalculator">
        <wsdl:operation name="Add">
            <wsdl:input wsaw:Action="https://Example.org/ICalculator/Add" message="tns:ICalculator_Add_InputMessage" />
            <wsdl:output wsaw:Action="https://Example.org/ICalculator/AddResponse" message="tns:ICalculator_Add_OutputMessage" />
        </wsdl:operation>
        <wsdl:operation name="Subtract">
            <wsdl:input wsaw:Action="https://Example.org/ICalculator/Subtract" message="tns:ICalculator_Subtract_InputMessage" />
            <wsdl:output wsaw:Action="https://Example.org/ICalculator/SubtractResponse" message="tns:ICalculator_Subtract_OutputMessage" />
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="DefaultBinding_ICalculator" type="tns:ICalculator">
        <soap:binding transport="https://schemas.xmlsoap.org/soap/http" />
        <wsdl:operation name="Add">
            <soap:operation soapAction="https://Example.org/ICalculator/Add" style="document" />
            <wsdl:input>
                <soap:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="Subtract">
            <soap:operation soapAction="https://Example.org/ICalculator/Subtract" style="document" />
            <wsdl:input>
                <soap:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="CalculatorService">
        <wsdl:port name="ICalculator" binding="tns:DefaultBinding_ICalculator">
            <soap:address location="https://Example.org/ICalculator" />
        </wsdl:port>
    </wsdl:service>

</wsdl:definitions>
```

## Makefile

``` syntax
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib Iphlpapi.lib

all: $(OUTDIR) $(OUTDIR)\WsCalculatorServiceKerberosOverSsl.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\CalculatorService.wsdl.c: CalculatorService.wsdl
     Wsutil.exe /wsdl:CalculatorService.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\CalculatorService.wsdl.obj: $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\CalculatorService.wsdl.c

$(OUTDIR)\CalculatorServiceKerberosOverSsl.obj: CalculatorServiceKerberosOverSsl.cpp $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" CalculatorServiceKerberosOverSsl.cpp

$(OUTDIR)\WsCalculatorServiceKerberosOverSsl.exe: $(OUTDIR)\CalculatorServiceKerberosOverSsl.obj $(OUTDIR)\CalculatorService.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsCalculatorServiceKerberosOverSsl.exe $(OUTDIR)\CalculatorServiceKerberosOverSsl.obj $(OUTDIR)\CalculatorService.wsdl.obj /PDB:$(OUTDIR)\WsCalculatorServiceKerberosOverSsl.PDB

clean:
    $(CLEANUP)
```

 

 




