---
title: HttpCalculatorWithEncodedChannelServiceExample
description: Review a Windows Web Services API (WWSAPI) C++ example of an HTTP calculator with encoded channel service.
ms.assetid: 3b8d58dd-2f0c-4008-81ad-abda23a26a52
keywords:
- HttpCalculatorWithEncodedChannelServiceExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# HttpCalculatorWithEncodedChannelServiceExample

This example shows how to use service host for hosting a calculator service with a custom channel and listener implementation that layer on top of HTTP.

-   [HttpCalculatorWithEncodedChannelService.cpp](#httpcalculatorwithencodedchannelservicecpp)
-   [EncodedChannel.h](#encodedchannelh)
-   [EncodedChannel.cpp](#encodedchannelcpp)
-   [CalculatorService.wsdl](#calculatorservicewsdl)
-   [Makefile](#makefile)

## HttpCalculatorWithEncodedChannelService.cpp


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
#include "CalculatorService.wsdl.h"
//------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
//------------------------------------------------------------

extern WS_CHANNEL_ENCODER channelEncoder;
extern WS_CHANNEL_DECODER channelDecoder;

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
    
    
    // Set up channel properties for the custom channel
    WS_CHANNEL_PROPERTY channelPropertyArray[1];
    
    // Set up channel property that specifies the callbacks that implement the custom channel
    channelPropertyArray[0].id = WS_CHANNEL_PROPERTY_DECODER;
    channelPropertyArray[0].value = &channelDecoder;
    channelPropertyArray[0].valueSize = sizeof(channelDecoder);
    
    // Set up service endpoint properties
    WS_SERVICE_ENDPOINT_PROPERTY serviceEndpointProperties[1];
    
    WS_SERVICE_PROPERTY_CLOSE_CALLBACK closeCallbackProperty = {CloseChannelCallback};
    serviceEndpointProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK;
    serviceEndpointProperties[0].value = &closeCallbackProperty;
    serviceEndpointProperties[0].valueSize = sizeof(closeCallbackProperty);
    
    
    // Initialize service endpoint
    serviceEndpoint.address.url.chars = L"https://+:80/example"; // address given as uri
    serviceEndpoint.address.url.length = (ULONG)wcslen(serviceEndpoint.address.url.chars);
    serviceEndpoint.channelBinding = WS_HTTP_CHANNEL_BINDING; // channel binding for the endpoint
    serviceEndpoint.channelType = WS_CHANNEL_TYPE_REPLY; // the channel type
    serviceEndpoint.contract = &calculatorContract;  // the contract
    serviceEndpoint.properties = serviceEndpointProperties;
    serviceEndpoint.propertyCount = WsCountOf(serviceEndpointProperties);
    serviceEndpoint.channelProperties.properties = channelPropertyArray; // Channel properties
    serviceEndpoint.channelProperties.propertyCount = WsCountOf(channelPropertyArray); // Channel property Count
    
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



## EncodedChannel.h


```C++
extern WS_CHANNEL_ENCODER channelEncoder;
extern WS_CHANNEL_DECODER channelDecoder;
```



## EncodedChannel.cpp


```C++
#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>
#include "WebServices.h"
#include "process.h"
#include "stdio.h"
#include "string.h"

WS_STRING encodedContentType = WS_STRING_VALUE(L"myContentType");

struct Encoder
{
    BYTE* buffer;
    ULONG bufferLength;
    WCHAR contentType[256];
    ULONG contentTypeLength;
    WS_WRITE_CALLBACK writeCallback;
    void* writeContext;
};

HRESULT CreateEncoder(
    __in void* createContext,
    __in WS_WRITE_CALLBACK writeCallback,
    __in void* writeContext,
    __deref_out void** encoderContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(createContext);
    UNREFERENCED_PARAMETER(error);

    Encoder* encoder = new Encoder;
    if (encoder == NULL)
    {
        return E_OUTOFMEMORY;
    }
    encoder->bufferLength = 1024;
    encoder->buffer = new BYTE[encoder->bufferLength];
    if (encoder->buffer == NULL)
    {
        delete encoder;
        return E_OUTOFMEMORY;
    }
    encoder->writeCallback = writeCallback;
    encoder->writeContext = writeContext;
    (*encoderContext) = encoder;
    return NOERROR;
}

HRESULT EncoderGetContentType(
    __in void* encoderContext,
    __in const WS_STRING* contentType,
    __out WS_STRING* newContentType,
    __out WS_STRING* contentEncoding,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(error);

    Encoder* encoder = (Encoder*)encoderContext;
    if (contentType->length > WsCountOf(encoder->contentType))
    {
        return E_FAIL;
    }
    ::memcpy(encoder->contentType, contentType->chars, contentType->length * sizeof(WCHAR));
    encoder->contentTypeLength = contentType->length;
    (*newContentType) = encodedContentType;
    contentEncoding->length = 0;
    contentEncoding->chars = NULL;
    return NOERROR;
}

HRESULT EncoderStart(
    __in void* encoderContext,
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    HRESULT hr;
    Encoder* encoder = (Encoder*)encoderContext;
    WS_BYTES bytes1 = { sizeof(encoder->contentTypeLength), (BYTE*)&encoder->contentTypeLength };
    hr = encoder->writeCallback(encoder->writeContext, &bytes1, 1, NULL, error);
    if (FAILED(hr))
    {
        return hr;
    }
    WS_BYTES bytes2 = { encoder->contentTypeLength * sizeof(WCHAR), (BYTE*)encoder->contentType };
    hr = encoder->writeCallback(encoder->writeContext, &bytes2, 1, NULL, error);
    if (FAILED(hr))
    {
        return hr;
    }
    return NOERROR;
}

HRESULT EncoderEncode(
    __in Encoder* encoder,
    __in_ecount(bufferLength) const BYTE* buffer,
    __in ULONG bufferLength,
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    HRESULT hr;
    while (bufferLength > encoder->bufferLength)
    {
        memcpy(encoder->buffer, buffer, encoder->bufferLength);
        for (ULONG i = 0; i < encoder->bufferLength; i++)
        {
            encoder->buffer[i]++;
        }
        WS_BYTES newBytes = { encoder->bufferLength, encoder->buffer };
        hr = encoder->writeCallback(encoder->writeContext, &newBytes, 1, NULL, error);
        if (FAILED(hr))
        {
            return hr;
        }
        buffer += encoder->bufferLength;
        bufferLength -= encoder->bufferLength;
    }
    memcpy(encoder->buffer, buffer, bufferLength);
    for (ULONG i = 0; i < bufferLength; i++)
    {
        encoder->buffer[i]++;
    }
    WS_BYTES newBytes = { bufferLength, encoder->buffer };
    return encoder->writeCallback(encoder->writeContext, &newBytes, 1, NULL, error);
}

HRESULT EncoderEncode(
    __in void* encoderContext,
    __in_ecount(count) const WS_BYTES* buffers,
    __in ULONG count,
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    HRESULT hr;
    Encoder* encoder = (Encoder*)encoderContext;
    for (ULONG i = 0; i < count; i++)
    {
        hr = EncoderEncode(encoder, buffers[i].bytes, buffers[i].length, NULL, error);
        if (FAILED(hr))
        {
            return hr;
        }
    }
    return NOERROR;
}

HRESULT EncoderEnd(
    __in void* encoderContext,
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(encoderContext);
    UNREFERENCED_PARAMETER(asyncContext);
    UNREFERENCED_PARAMETER(error);
    return NOERROR;
}

void FreeEncoder(
    __in void* encoderContext)
{
    Encoder* encoder = (Encoder*)encoderContext;
    delete encoder;
}

WS_CHANNEL_ENCODER channelEncoder =
{
    NULL,
    (WS_CREATE_ENCODER_CALLBACK)CreateEncoder, 
    (WS_ENCODER_GET_CONTENT_TYPE_CALLBACK)EncoderGetContentType, 
    (WS_ENCODER_START_CALLBACK)EncoderStart,
    (WS_ENCODER_ENCODE_CALLBACK)EncoderEncode, 
    (WS_ENCODER_END_CALLBACK)EncoderEnd,
    (WS_FREE_ENCODER_CALLBACK)FreeEncoder 
};

struct Decoder
{
    WCHAR contentType[256];
    ULONG contentTypeLength;
    WS_READ_CALLBACK readCallback;
    void* readContext;
};

HRESULT ReadBlock(
    __in Decoder* decoder,
    __out_ecount_part_opt(maxLength, *outLength) void* buffer,
    __in ULONG maxLength,
    __out_opt ULONG* outLength,
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    HRESULT hr;
    ULONG length = 0;
    while (length < maxLength)
    {
        ULONG actualLength;
        hr = decoder->readCallback(decoder->readContext, &((BYTE*)buffer)[length], maxLength - length, &actualLength, NULL, error);
        if (FAILED(hr))
        {
            return hr;
        }
        if (actualLength == 0)
        {
            break;
        }
        length += actualLength;
    }
    if (outLength == NULL)
    {
        if (length != maxLength)
        {
            return E_FAIL;
        }
    }
    else
    {
        (*outLength) = length;
    }
    return NOERROR;
}

HRESULT CreateDecoder(
    __in void* createContext,
    __in WS_READ_CALLBACK readCallback,
    __in void* readContext,
    __deref_out void** decoderContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(createContext);
    UNREFERENCED_PARAMETER(error);

    Decoder* decoder = new Decoder;
    if (decoder == NULL)
    {
        return E_OUTOFMEMORY;
    }
    decoder->readCallback = readCallback;
    decoder->readContext = readContext;
    (*decoderContext) = decoder;
    return NOERROR;
}

HRESULT DecoderGetContentType(
    __in void* decoderContext,
    __in const WS_STRING* contentType,
    __in_opt const WS_STRING* contentEncoding,
    __out WS_STRING* newContentType,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(error);

    Decoder* decoder = (Decoder*)decoderContext;
    if (contentEncoding != NULL)
    {
        return E_FAIL;
    }
    if (contentType->length != encodedContentType.length)
    {
        return E_FAIL;
    }
    if (::memcmp(contentType->chars, encodedContentType.chars, encodedContentType.length * sizeof(WCHAR)) != 0)
    {
        return E_FAIL;
    }
    newContentType->chars = decoder->contentType;
    newContentType->length = decoder->contentTypeLength;
    return NOERROR;
}

HRESULT DecoderStart(
    __in void* decoderContext,
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    HRESULT hr;
    Decoder* decoder = (Decoder*)decoderContext;

    hr = ReadBlock(decoder, &decoder->contentTypeLength, sizeof(ULONG), NULL, NULL, error);
    if (FAILED(hr))
    {
        return hr;
    }
    if (decoder->contentTypeLength > WsCountOf(decoder->contentType))
    {
        return E_FAIL;
    }
    hr = ReadBlock(decoder, &decoder->contentType, decoder->contentTypeLength * sizeof(WCHAR), NULL, NULL, error);
    if (FAILED(hr))
    {
        return hr;
    }
    return NOERROR;
}

HRESULT DecoderDecode(
    __in void* decoderContext,
    __out_ecount_part_opt(maxLength, *outLength) void* buffer,
    __in ULONG maxLength,
    __out ULONG* outLength,
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    HRESULT hr;
    Decoder* decoder = (Decoder*)decoderContext;
    ULONG length;
    hr = ReadBlock(decoder, buffer, maxLength, &length, NULL, error);
    if (FAILED(hr))
    {
        return hr;
    }
    for (ULONG i = 0; i < length; i++)
    {
        ((BYTE*)buffer)[i]--;
    }
    (*outLength) = length;
    return hr;
}

HRESULT DecoderEnd(
    __in void* decoderContext,
    __in_opt const WS_ASYNC_CONTEXT* asyncContext,
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(decoderContext);
    UNREFERENCED_PARAMETER(asyncContext);
    UNREFERENCED_PARAMETER(error);
    return NOERROR;
}

void FreeDecoder(
    __in void* decoderContext)
{
    Decoder* decoder = (Decoder*)decoderContext;
    delete decoder;
}

WS_CHANNEL_DECODER channelDecoder =
{
    NULL,
    (WS_CREATE_DECODER_CALLBACK)CreateDecoder, 
    (WS_DECODER_GET_CONTENT_TYPE_CALLBACK)DecoderGetContentType, 
    (WS_DECODER_START_CALLBACK)DecoderStart,
    (WS_DECODER_DECODE_CALLBACK)DecoderDecode, 
    (WS_DECODER_END_CALLBACK)DecoderEnd,
    (WS_FREE_DECODER_CALLBACK)FreeDecoder 
};
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

EXTRA_LIBS = WebServices.lib

all: $(OUTDIR) $(OUTDIR)\WsHttpCalculatorWithEncodedChannelService.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\CalculatorService.wsdl.c: CalculatorService.wsdl
     Wsutil.exe /wsdl:CalculatorService.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\CalculatorService.wsdl.obj: $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\CalculatorService.wsdl.c

$(OUTDIR)\HttpCalculatorWithEncodedChannelService.obj: HttpCalculatorWithEncodedChannelService.cpp $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" HttpCalculatorWithEncodedChannelService.cpp

$(OUTDIR)\EncodedChannel.obj: EncodedChannel.cpp
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" EncodedChannel.cpp

$(OUTDIR)\WsHttpCalculatorWithEncodedChannelService.exe: $(OUTDIR)\HttpCalculatorWithEncodedChannelService.obj $(OUTDIR)\CalculatorService.wsdl.obj $(OUTDIR)\EncodedChannel.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsHttpCalculatorWithEncodedChannelService.exe $(OUTDIR)\HttpCalculatorWithEncodedChannelService.obj $(OUTDIR)\CalculatorService.wsdl.obj $(OUTDIR)\EncodedChannel.obj /PDB:$(OUTDIR)\WsHttpCalculatorWithEncodedChannelService.PDB

clean:
    $(CLEANUP)
```

 

 




