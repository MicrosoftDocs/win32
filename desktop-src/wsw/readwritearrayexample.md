---
title: ReadWriteArrayExample
description: This example reads and writes an array of elements.
ms.assetid: '3c4851b5-1c31-4de7-929e-03a8199b273a'
keywords: ["ReadWriteArrayExample Web Services for Windows", "WWSAPI", "WWS"]
---

# ReadWriteArrayExample

This example reads and writes an array of elements.

## ReadWriteArray.cpp


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
#include "intsafe.h"

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
        hr = WsGetErrorProperty(error, WS_ERROR_PROPERTY_STRING_COUNT, &amp;errorCount, sizeof(errorCount));
        if (FAILED(hr))
        {
            goto Exit;
        }
        for (ULONG i = 0; i < errorCount; i++)
        {
            WS_STRING string;
            hr = WsGetErrorString(error, i, &amp;string);
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
    WS_XML_WRITER* xmlWriter = NULL;
    WS_XML_READER* xmlReader = NULL;
    WS_XML_STRING arrayElement = WS_XML_STRING_VALUE("array");
    WS_XML_STRING itemElement = WS_XML_STRING_VALUE("item");
    WS_XML_STRING emptyNamespace = WS_XML_STRING_VALUE("");
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &amp;error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    WS_XML_WRITER_BUFFER_OUTPUT bufferOutput;
    ZeroMemory(&amp;bufferOutput, sizeof(bufferOutput));
    bufferOutput.output.outputType = WS_XML_WRITER_OUTPUT_TYPE_BUFFER;
    
    WS_XML_WRITER_TEXT_ENCODING writerTextEncoding;
    ZeroMemory(&amp;writerTextEncoding, sizeof(writerTextEncoding));
    writerTextEncoding.encoding.encodingType = WS_XML_WRITER_ENCODING_TYPE_TEXT;
    writerTextEncoding.charSet = WS_CHARSET_UTF8;
    
    // Create an XML writer
    hr = WsCreateWriter(
        NULL, 
        0, 
        &amp;xmlWriter, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsSetOutput(xmlWriter, &amp;writerTextEncoding.encoding, &amp;bufferOutput.output, NULL, 0, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsWriteStartElement(xmlWriter, NULL, &amp;arrayElement, &amp;emptyNamespace, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    ULONG data[] = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
    hr = WsWriteArray(xmlWriter, 
        &amp;itemElement, &amp;emptyNamespace, WS_UINT32_VALUE_TYPE, 
        data, sizeof(data), 0, WsCountOf(data), error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsWriteEndElement(xmlWriter, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    WS_BYTES buffer;
    hr = WsGetWriterProperty(xmlWriter, WS_XML_WRITER_PROPERTY_BYTES, &amp;buffer, sizeof(buffer), error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    WS_XML_READER_BUFFER_INPUT bufferInput;
    ZeroMemory(&amp;bufferInput, sizeof(bufferInput));
    bufferInput.input.inputType = WS_XML_READER_INPUT_TYPE_BUFFER;
    bufferInput.encodedData = buffer.bytes;
    bufferInput.encodedDataSize = buffer.length;
    
    WS_XML_READER_TEXT_ENCODING readerTextEncoding;
    ZeroMemory(&amp;readerTextEncoding, sizeof(readerTextEncoding));
    readerTextEncoding.encoding.encodingType = WS_XML_READER_ENCODING_TYPE_TEXT;
    readerTextEncoding.charSet = WS_CHARSET_AUTO;
    
    // Create an XML reader
    hr = WsCreateReader(NULL, 0, &amp;xmlReader, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsSetInput(xmlReader, &amp;readerTextEncoding.encoding, &amp;bufferInput.input, NULL, 0, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsReadToStartElement(xmlReader, &amp;arrayElement, &amp;emptyNamespace, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsReadStartElement(xmlReader, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    ULONG items[32];
    ULONG itemCount = 0;
    for (;;)
    {
        ULONG actualCount;
        hr = WsReadArray(xmlReader, 
            &amp;itemElement, &amp;emptyNamespace, WS_UINT32_VALUE_TYPE, 
            items, sizeof(items), itemCount, WsCountOf(items) - itemCount, &amp;actualCount, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        if (actualCount == 0)
        {
            break;
        }
        itemCount += actualCount;
    }
    
    for (ULONG i = 0; i < itemCount; i++)
    {
        wprintf(L"%d\n", items[i]);
    }
    
    hr = WsReadEndElement(xmlReader, error);
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
    
    if (xmlReader != NULL)
    {
        WsFreeReader(xmlReader);
    }
    if (xmlWriter != NULL)
    {
        WsFreeWriter(xmlWriter);
    }
    if (error != NULL)
    {
        WsFreeError(error);
    }
    fflush(stdout);
    return SUCCEEDED(hr) ? 0 : -1;
}

```



 

 




