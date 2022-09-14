---
title: HttpCalculatorWithKerberosOverSslClientExample
description: This example shows a HTTP client that uses service proxy to talk to a calculator service, with kerberos over SSL mixed-mode security.
ms.assetid: eb3ae71f-0bbb-42d7-af81-20c5dbb03c3f
keywords:
- HttpCalculatorWithKerberosOverSslClientExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# HttpCalculatorWithKerberosOverSslClientExample

This example shows a HTTP client that uses service proxy to talk to a calculator service, with kerberos over SSL mixed-mode security. In this setup, the transport connection is protected (signed, encrypted) by SSL which also provides server authentication. Client authentication is provided by a kerberos APREQ ticket in a WS-Security header in the message.

-   [CalculatorClientKerberosOverSsl.cpp](#calculatorclientkerberosoversslcpp)
-   [CalculatorService.wsdl](#calculatorservicewsdl)
-   [Makefile](#makefile)

## CalculatorClientKerberosOverSsl.cpp


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
$$RC_START_HIGHLIGHT
#include "wincrypt.h"
$$RC_END_HIGHLIGHT
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

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_HEAP* heap = NULL;
    WS_SERVICE_PROXY* proxy = NULL;
    
    // Command line parameter specifies the SPN for the target server.
    WS_STRING serviceSpn;
    if (argc == 2)
    {
        serviceSpn.chars = argv[1];
        size_t length = wcslen(
            serviceSpn.chars);
        // let's make sure the length is within a reasonable limit
        if (1024 >= length)
        {
            serviceSpn.length = (ULONG) length;
        }
        else
        {
            wprintf(
                L"SPN parameter is too long: '%s'\n",
                serviceSpn.chars);
            return 1;
        }
    }
    else
    {
        wprintf(
            L"Service SPN parameter is missing.\n");
        return 1;
    }
    
$$RC_START_HIGHLIGHT
    // declare and initialize a windows credential
    WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL windowsCredential = {}; // zero out the struct
    windowsCredential.credential.credentialType = WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE; // set the credential type
    
    // declare and initialize a kerberos APREQ message security binding
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING kerberosBinding = {}; // zero out the struct
    kerberosBinding.binding.bindingType = WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TYPE; // set the binding type
    kerberosBinding.bindingUsage = WS_SUPPORTING_MESSAGE_SECURITY_USAGE; // set the binding usage
    kerberosBinding.clientCredential = &windowsCredential.credential;
    
    // declare and initialize an SSL transport security binding
    WS_SSL_TRANSPORT_SECURITY_BINDING sslBinding = {}; // zero out the struct
    sslBinding.binding.bindingType = WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE; // set the binding type
    
    // declare and initialize the array of all security bindings
    WS_SECURITY_BINDING* securityBindings[2] = { &sslBinding.binding, &kerberosBinding.binding };
    
    // declare and initialize the security description
    WS_SECURITY_DESCRIPTION securityDescription = {}; // zero out the struct
    securityDescription.securityBindings = securityBindings;
    securityDescription.securityBindingCount = WsCountOf(securityBindings);
$$RC_END_HIGHLIGHT
    
    int result = 0;
    WS_ENDPOINT_ADDRESS address = {};
    WS_STRING url = WS_STRING_VALUE(L"https://localhost:8443/example");
    address.url = url;
    WS_SPN_ENDPOINT_IDENTITY serviceIdentity;
    serviceIdentity.identity.identityType = WS_SPN_ENDPOINT_IDENTITY_TYPE;
    serviceIdentity.spn = serviceSpn;
    address.identity = &serviceIdentity.identity;
    
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
    
    // Create the proxy
    hr = WsCreateServiceProxy(
        WS_CHANNEL_TYPE_REQUEST, 
        WS_HTTP_CHANNEL_BINDING, 
        &securityDescription, 
        NULL, 
        0, 
        NULL,
        0,
        &proxy, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    
    
    hr = WsOpenServiceProxy(
        proxy, 
        &address, 
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = DefaultBinding_ICalculator_Add(
        proxy, 
        1, 
        2, 
        &result, 
        heap, 
        NULL, 
        0, 
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    wprintf(L"%d + %d = %d\n", 1, 2, result);
                   
Exit:
    if (FAILED(hr))
    {
        // Print out the error
        PrintError(hr, error);
    }
    fflush(
        stdout);
    if (proxy != NULL)
    {
        WsCloseServiceProxy(
            proxy, 
            NULL, 
            NULL);
    
        WsFreeServiceProxy(
            proxy);
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

all: $(OUTDIR) $(OUTDIR)\WsCalculatorClientKerberosOverSsl.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\CalculatorService.wsdl.c: CalculatorService.wsdl
     Wsutil.exe /wsdl:CalculatorService.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\CalculatorService.wsdl.obj: $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\CalculatorService.wsdl.c

$(OUTDIR)\CalculatorClientKerberosOverSsl.obj: CalculatorClientKerberosOverSsl.cpp $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" CalculatorClientKerberosOverSsl.cpp

$(OUTDIR)\WsCalculatorClientKerberosOverSsl.exe: $(OUTDIR)\CalculatorClientKerberosOverSsl.obj $(OUTDIR)\CalculatorService.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsCalculatorClientKerberosOverSsl.exe $(OUTDIR)\CalculatorClientKerberosOverSsl.obj $(OUTDIR)\CalculatorService.wsdl.obj /PDB:$(OUTDIR)\WsCalculatorClientKerberosOverSsl.PDB

clean:
    $(CLEANUP)
```

 

 




