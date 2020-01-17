---
title: HttpCalculatorWithUsernameXmlTokenOverSslClient example
description: This example shows a HTTP client that uses service proxy to talk to a calculator service, with XML security token over SSL mixed-mode security.
ms.assetid: 9b687099-c59f-4aea-862f-c29d1978d955
keywords:
- HttpCalculatorWithUsernameXmlTokenOverSslClientExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# HttpCalculatorWithUsernameXmlTokenOverSslClient example

This example shows a HTTP client that uses service proxy to talk to a calculator service, with XML security token over SSL mixed-mode security. In this setup, the transport connection is protected (signed, encrypted) by SSL which also provides server authentication. Client authentication is provided by a WS-Security username/password pair that is used as an XML security token by the example.

Note that this client side example uses the [**WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_token_message_security_binding). An equivalent way of doing the same client side security using the [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding) is illustrated by the example [HttpCalculatorWithUsernameOverSslClientExample](httpcalculatorwithusernameoversslclientexample.md).

A matching server side for both of these client side examples is provided by the example [HttpCalculatorWithUserNameOverSslServiceExample](httpcalculatorwithusernameoversslserviceexample.md).

-   [CalculatorClientUserNameXmlTokenOverSsl.cpp](#calculatorclientusernamexmltokenoversslcpp)
-   [CalculatorService.wsdl](#calculatorservicewsdl)
-   [Makefile](#makefile)
-   [Related topics](#related-topics)

## CalculatorClientUserNameXmlTokenOverSsl.cpp


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
#include "stdio.h"
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

$$RC_START_HIGHLIGHT
HRESULT CreateXmlSecurityToken(
    __deref_out WS_SECURITY_TOKEN** xmlSecurityToken,
    __in_opt WS_ERROR* error)
{
    HRESULT hr = NOERROR;
    WS_HEAP* heap = NULL;
    WS_XML_READER* reader = NULL;
    WS_XML_BUFFER* buffer = NULL;

    // The username/password are included in code for the simplicity
    // of the sample.  This should NOT be done for real applications.
    char* securityTokenWireXmlForm = "<x:UsernameToken xmlns:x='https://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd'><x:Username>usr1</x:Username><x:Password>pwd1</x:Password></x:UsernameToken>";

    // create an XML reader
    hr = WsCreateReader(
        NULL, 
        0, 
        &reader, 
        error);
if (FAILED(hr))
{
    goto Exit;
}

    // define the input and encoding for the XML reader
    WS_XML_READER_BUFFER_INPUT readerInput;
    ZeroMemory(&readerInput, sizeof(readerInput));
    readerInput.input.inputType = WS_XML_READER_INPUT_TYPE_BUFFER;
    readerInput.encodedData = securityTokenWireXmlForm;
    readerInput.encodedDataSize = (ULONG)strlen(securityTokenWireXmlForm);

    WS_XML_READER_TEXT_ENCODING readerEncoding;
    ZeroMemory(&readerEncoding, sizeof(readerEncoding));
    readerEncoding.encoding.encodingType = WS_XML_READER_ENCODING_TYPE_TEXT;
    readerEncoding.charSet = WS_CHARSET_UTF8;

    // set the input and encoding for the XML reader
    hr = WsSetInput(
        reader, 
        &readerEncoding.encoding, 
        &readerInput.input, 
        NULL, 
        0, 
        error);
if (FAILED(hr))
{
    goto Exit;
}

    // create a heap to read the security token XML form into an XML buffer allocated on that heap
    hr = WsCreateHeap(
        2048, 
        512, 
        NULL, 0, 
        &heap, 
        error);
if (FAILED(hr))
{
    goto Exit;
}

    // read the security token XML form into an XML buffer
    hr = WsReadType(
        reader, 
        WS_ELEMENT_TYPE_MAPPING, 
        WS_XML_BUFFER_TYPE, NULL, 
        WS_READ_REQUIRED_POINTER, 
        heap, 
        &buffer, 
        sizeof(buffer), 
        error);
if (FAILED(hr))
{
    goto Exit;
}

    // create an XML security token from the token's wire form available in the XML buffer
    hr = WsCreateXmlSecurityToken(
        buffer, 
        NULL, 
        NULL, 
        0, 
        xmlSecurityToken, 
        error);

 Exit:
    // The heap, and the XML buffer allocated on it, need not be kept
    // alive once the token creation call returns.  Note that the XML
    // buffer allocated on the heap is automatically freed along with
    // the heap, and is never freed directly.
    if (heap != NULL)
    {
        WsFreeHeap(
            heap);
    }

    if (reader != NULL)
    {
        WsFreeReader(
            reader);
    }

    return hr;
}
$$RC_END_HIGHLIGHT


// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_HEAP* heap = NULL;
$$RC_START_HIGHLIGHT
    WS_SECURITY_TOKEN* securityToken = NULL;
$$RC_END_HIGHLIGHT
    WS_SERVICE_PROXY* proxy = NULL;
    
$$RC_START_HIGHLIGHT
    // declare and initialize an XML security token message security binding
    WS_XML_TOKEN_MESSAGE_SECURITY_BINDING xmlTokenBinding = {}; // zero out the struct
    xmlTokenBinding.binding.bindingType = WS_XML_TOKEN_MESSAGE_SECURITY_BINDING_TYPE; // set the binding type
    xmlTokenBinding.bindingUsage = WS_SUPPORTING_MESSAGE_SECURITY_USAGE; // set the binding usage
    
    // declare and initialize an SSL transport security binding
    WS_SSL_TRANSPORT_SECURITY_BINDING sslBinding = {}; // zero out the struct
    sslBinding.binding.bindingType = WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE; // set the binding type
    
    // declare and initialize the array of all security bindings
    WS_SECURITY_BINDING* securityBindings[2] = { &sslBinding.binding, &xmlTokenBinding.binding };
    
    // declare and initialize the security description
    WS_SECURITY_DESCRIPTION securityDescription = {}; // zero out the struct
    securityDescription.securityBindings = securityBindings;
    securityDescription.securityBindingCount = WsCountOf(securityBindings);
$$RC_END_HIGHLIGHT
    
    int result = 0;
    WS_ENDPOINT_ADDRESS address = {};
    WS_STRING url = WS_STRING_VALUE(L"https://localhost:8443/example");
    address.url = url;
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
$$RC_START_HIGHLIGHT
    // create an XML security token and set it on the relevant security binding
    hr = CreateXmlSecurityToken(&securityToken, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    xmlTokenBinding.xmlToken = securityToken;
$$RC_END_HIGHLIGHT
    
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
    
$$RC_START_HIGHLIGHT
    // after the proxy is created, the security token handle can be freed
    if (securityToken != NULL)
    {
        WsFreeSecurityToken(securityToken);
        securityToken = NULL;
    }
$$RC_END_HIGHLIGHT
    
    
    
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
$$RC_START_HIGHLIGHT
    if (securityToken != NULL)
    {
        WsFreeSecurityToken(
            securityToken);
    }
$$RC_END_HIGHLIGHT
    
    
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



CalculatorService.wsdl

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

all: $(OUTDIR) $(OUTDIR)\WsCalculatorClientUserNameXmlTokenOverSsl.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\CalculatorService.wsdl.c: CalculatorService.wsdl
     Wsutil.exe /wsdl:CalculatorService.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\CalculatorService.wsdl.obj: $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\CalculatorService.wsdl.c

$(OUTDIR)\CalculatorClientUserNameXmlTokenOverSsl.obj: CalculatorClientUserNameXmlTokenOverSsl.cpp $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" CalculatorClientUserNameXmlTokenOverSsl.cpp

$(OUTDIR)\WsCalculatorClientUserNameXmlTokenOverSsl.exe: $(OUTDIR)\CalculatorClientUserNameXmlTokenOverSsl.obj $(OUTDIR)\CalculatorService.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsCalculatorClientUserNameXmlTokenOverSsl.exe $(OUTDIR)\CalculatorClientUserNameXmlTokenOverSsl.obj $(OUTDIR)\CalculatorService.wsdl.obj /PDB:$(OUTDIR)\WsCalculatorClientUserNameXmlTokenOverSsl.PDB

clean:
    $(CLEANUP)
```

## Related topics

<dl> <dt>

[**WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_token_message_security_binding)
</dt> <dt>

[**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding)
</dt> <dt>

[HttpCalculatorWithUsernameOverSslClientExample](httpcalculatorwithusernameoversslclientexample.md)
</dt> <dt>

[HttpCalculatorWithUserNameOverSslServiceExample](httpcalculatorwithusernameoversslserviceexample.md)
</dt> </dl>

 

 




