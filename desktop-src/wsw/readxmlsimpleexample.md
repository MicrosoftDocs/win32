---
title: ReadXmlSimpleExample
description: This example reads a simple xml document.
ms.assetid: bb4492d9-fa37-4078-b4e1-8a57001ff99b
keywords:
- ReadXmlSimpleExample Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# ReadXmlSimpleExample

This example reads a simple xml document.

## ReadXmlSimple.cpp


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

#pragma comment(lib, "WebServices.lib")

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

WS_XML_STRING valueLocalName = WS_XML_STRING_VALUE("value");
WS_XML_STRING valueNs = WS_XML_STRING_VALUE("");

char xml[] = 
"<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
"<value>Hello World.</value>";

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_XML_READER* reader = NULL;
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create an XML reader
    hr = WsCreateReader(
        NULL,
        0, 
        &reader, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Setup the input
    WS_XML_READER_BUFFER_INPUT bufferInput;
    ZeroMemory(
        &bufferInput,
        sizeof(bufferInput));
    bufferInput.input.inputType = WS_XML_READER_INPUT_TYPE_BUFFER;
    bufferInput.encodedData = (BYTE*)xml;
    bufferInput.encodedDataSize = sizeof(xml) - 1;
    
    // Setup the encoding
    WS_XML_READER_TEXT_ENCODING textEncoding;
    ZeroMemory(
        &textEncoding,
        sizeof(textEncoding));
    textEncoding.encoding.encodingType = WS_XML_READER_ENCODING_TYPE_TEXT;
    textEncoding.charSet = WS_CHARSET_AUTO;
    
    
    // Setup the reader
    hr = WsSetInput(
        reader, 
        &textEncoding.encoding, 
        &bufferInput.input, 
        NULL, 
        0, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsReadToStartElement(
        reader, 
        &valueLocalName, 
        &valueNs, 
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsReadStartElement(
        reader,
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    for (;;)
    {
        WCHAR chars[128];
        ULONG charCount;
        hr = WsReadChars(
            reader,
            chars,
            128, 
            &charCount,
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
        if (charCount == 0)
        {
            break;
        }
        wprintf(L"%.*s", charCount, chars);
    }
    wprintf(L"\n");
    hr = WsReadEndElement(
        reader,
        error);
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
    
    if (reader != NULL)
    {
        WsFreeReader(reader);
    }
    if (error != NULL)
    {
        WsFreeError(error);
    }
    fflush(stdout);
    return SUCCEEDED(hr) ? 0 : -1;
}

```



 

 




