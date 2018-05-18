---
title: util.cpp
description: util.cpp
ms.assetid: '61a7145f-bafc-411f-9dc2-65d8982be055'
keywords: ["Packaging APIs,sample applications", "packaging,sample applications", "packages,sample applications", "Packaging APIs,music bundle signature sample", "packaging,music bundle signature sample", "packages,music bundle signature sample", "music bundle signature sample,util.cpp", "Packaging APIs,util.cpp", "packaging,util.cpp", "packages,util.cpp", "util.cpp,music bundle signature sample", "sample applications,music bundle signature"]
---

# util.cpp


```C++
/*****************************************************************************
*
* File: Util.h
*
* Description: 
* Utility functions for Packaging APIs.
*
* ------------------------------------
*
*  This file is part of the Microsoft Windows SDK Code Samples.
* 
*  Copyright (C) Microsoft Corporation.  All rights reserved.
* 
* This source code is intended only as a supplement to Microsoft
* Development Tools and/or on-line documentation.  See these other
* materials for detailed information regarding Microsoft code samples.
* 
* THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
* KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
* PARTICULAR PURPOSE.
* 
****************************************************************************/

#include <stdio.h>
#include <windows.h>
#include <shlobj.h>

#include <msopc.h>  // For OPC APIs

#include <WinCrypt.h>   // For certificate stuff
#include <CryptDlg.h>   // For certificate selection dialog

#include <strsafe.h>
#include <new>

#include "Util.h"

// Gets the target part of a relationship.
//
// Parameters:
//      partSet         - The set of parts in the package.
//      relationship    - The relationship from which we get the target part.
//      expectedContentType - The expected content type of the target part.
//      targetedPart    - The target part. This pointer may be valid even if
//                        the method fails. The caller must release the pointer
//                        if a non-NULL value is returned.
HRESULT
GetRelationshipTargetPart(
    IOpcPartSet* partSet,
    IOpcRelationship* relationship,
    LPCWSTR expectedContentType,
    IOpcPart** targetedPart
    )
{
    // Check target mode of the relationship; for the target to be internal,
    // the target mode must be internal.
    OPC_URI_TARGET_MODE targetMode;
    IOpcUri * sourceUri = NULL;
    IUri * targetUri = NULL;
    IOpcPartUri * tracklistPartUri = NULL;
    LPWSTR contentType = NULL;
    BOOL partExists = FALSE;

    HRESULT hr = relationship->GetTargetMode(&amp;targetMode);

    if (SUCCEEDED(hr) &amp;&amp; targetMode != OPC_URI_TARGET_MODE_INTERNAL)
    {
        // Check whether the TargetMode of the relationship is internal. If
        // the target mode is not internal, the target cannot be a part inside
        // the package.
    
        LPWSTR relationshipType = NULL;
        relationship->GetRelationshipType(&amp;relationshipType);

        fwprintf(
            stderr, 
            L"Invalid music bundle package: relationship with type %s must have Internal target mode.\n",
            relationshipType
            );

        hr = E_FAIL;

        CoTaskMemFree(static_cast<LPVOID>(relationshipType));
    }

    // To get the URI of the target part, resolve the target URI based on the
    // source URI, because the target URI may be a relative URI.
    if (SUCCEEDED(hr))
    {
        hr = relationship->GetSourceUri(&amp;sourceUri);
    }

    if (SUCCEEDED(hr))
    {
        hr = relationship->GetTargetUri(&amp;targetUri);
    }

    if (SUCCEEDED(hr))
    {
        hr = sourceUri->CombinePartUri(targetUri, &amp;tracklistPartUri);
    }

    if (SUCCEEDED(hr))
    {
        hr = partSet->PartExists(tracklistPartUri, &amp;partExists);
    }

    if (SUCCEEDED(hr) &amp;&amp; !partExists)
    {
        fwprintf(
            stderr, 
            L"Invalid music bundle package: the target part of relationship does not exist.\n"
            );

        hr = E_FAIL;
    }

    if (SUCCEEDED(hr))
    {
        hr = partSet->GetPart(tracklistPartUri, targetedPart);
    }

    // Check that the actual content type of the part matches the expected
    // content type for the part.
    if (SUCCEEDED(hr))
    {
        hr = (*targetedPart)->GetContentType(&amp;contentType);
    }

    if (SUCCEEDED(hr))
    {
        if (wcscmp(contentType, expectedContentType) != 0)
        {
            fwprintf(
                stderr, 
                L"Invalid music bundle package: the target part does not have correct content type.\n"
                );

            hr = E_FAIL;
        }
    }

    // Release resources
    if (sourceUri)
    {
        sourceUri->Release();
        sourceUri = NULL;
    }

    if (targetUri)
    {
        targetUri->Release();
        targetUri = NULL;
    }

    if (tracklistPartUri)
    {
        tracklistPartUri->Release();
        tracklistPartUri = NULL;
    }

    CoTaskMemFree(static_cast<LPVOID>(contentType));

    return hr;
}

// Gets the target part of a relationship with the specified relationship type,
// from the specified set of relationships. The relationship set must have only
// one relationship with the specified relationship type; otherwise, this
// function will report an error.
//
// Parameters:
//      partSet          - The set of parts in the package.
//      relsSet          - The relationship set in which a relationship of the
//                         specified type is found.
//      relationshipType - The specified relationship type of the relationship
//                         to be found.
//      expectedContentType - The expected content type of the target part.
//      targetedPart     - The target part. This pointer may be valid even if
//                         the method fails. The caller must release the pointer
//                         if a non-NULL value is returned.
HRESULT
GetPartByRelationshipType(
    IOpcPartSet* partSet,
    IOpcRelationshipSet* relsSet,
    LPCWSTR relationshipType,
    LPCWSTR expectedContentType,
    IOpcPart** targetedPart
    )
{
    IOpcRelationshipEnumerator * relsEnumerator = NULL;
    BOOL hasNext = FALSE;
    int count = 0;

    HRESULT hr = relsSet->GetEnumeratorForType(relationshipType, &amp;relsEnumerator);

    while (
        SUCCEEDED(hr)
        &amp;&amp;
        SUCCEEDED(hr = relsEnumerator->MoveNext(&amp;hasNext))
        &amp;&amp;
        hasNext
        )
    {
        IOpcRelationship * relationship = NULL;

        count++;

        if (count > 1)
        {
            // Our custom format for music bundle expects that only one
            // relationship of a specific type exists in a Relationships
            // part. Note that it is not an OPC rule.
            fwprintf(
                stderr, 
                L"Invalid music bundle package: cannot have more than 1 relationship with type: %s.\n",
                relationshipType
                );

            hr = E_FAIL;
            break;
        }

        if (SUCCEEDED(hr))
        {
            hr = relsEnumerator->GetCurrent(&amp;relationship);
        }

        if (SUCCEEDED(hr))
        {
            hr = GetRelationshipTargetPart(partSet, relationship, expectedContentType, targetedPart);
        }

        // Release resources
        if (relationship)
        {
            relationship->Release();
            relationship = NULL;
        }
    }
    
    if (SUCCEEDED(hr))
    {
         if (count == 0)
         {
             fwprintf(
                 stderr, 
                 L"Invalid music bundle package: relationship with type %s does not exist.\n",
                 relationshipType
                 );

             hr = E_FAIL;
         }
    }

    // Release resources
    if (relsEnumerator)
    {
        relsEnumerator->Release();
        relsEnumerator = NULL;
    }

    return hr;
}

// Begin reading the package from the specified file.
HRESULT
ReadPackageFromFile(
    LPCWSTR filename,
    IOpcFactory* opcFactory,
    IOpcPackage** opcPackage
    )
{
    IStream * fileStream = NULL;

    // Create a stream over the package file.
    HRESULT hr = opcFactory->CreateStreamOnFile(
                    filename,
                    OPC_STREAM_IO_READ, 
                    NULL,                   // Use default security attribute.
                    FILE_ATTRIBUTE_NORMAL,  // dwFlagsAndAttributes.
                    &amp;fileStream             // The new stream over the file,
                    );

    // Read the package from the stream. 
    if (SUCCEEDED(hr))
    {
        hr = opcFactory->ReadPackageFromStream(
                fileStream, 
                OPC_READ_DEFAULT,
                opcPackage
                );
    }

    if (FAILED(hr))
    {
        fwprintf(stderr, L"Failed to load package file: %s.\n", filename);
    }

    // Release resources.
    if (fileStream)
    {
        fileStream->Release();
        fileStream = NULL;
    }

    return hr;
}

// Write the package to the specified file.
HRESULT
WritePackageToFile(
    LPCWSTR filename,
    IOpcPackage* opcPackage,
    IOpcFactory* opcFactory
    )
{
    IStream * fileStream = NULL;

    HRESULT hr = opcFactory->CreateStreamOnFile(
                    filename,               // Output file.
                    OPC_STREAM_IO_WRITE,
                    NULL,                   // Use default security attribute.
                    FILE_ATTRIBUTE_NORMAL,  // dwFlagsAndAttributes.
                    &amp;fileStream             // The new stream over the file.
                    );

    // Write the package to the stream. 
    if (SUCCEEDED(hr))
    {
        hr = opcFactory->WritePackageToStream(
                opcPackage,
                OPC_WRITE_DEFAULT,
                fileStream
                );
    }

    // Release resources.
    if (fileStream)
    {
        fileStream->Release();
        fileStream = NULL;
    }

    return hr;
}

// Saves a certificate to the specified file.
HRESULT
SaveCertificateToFile(
    PCCERT_CONTEXT cert,
    LPCWSTR filename
    )
{
    HANDLE hFile = CreateFile(filename, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, 0, NULL);

    DWORD written = 0;
    HRESULT hr = S_OK;

    if (hFile == INVALID_HANDLE_VALUE)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        fwprintf(stderr, L"CreateFile failed with hr=0x%x\n", hr);
    }

    if (SUCCEEDED(hr))
    {
        if (!WriteFile(hFile, cert->pbCertEncoded, cert->cbCertEncoded, &amp;written, NULL))
        {
            hr = HRESULT_FROM_WIN32(GetLastError());
            fwprintf(stderr, L"WriteFile failed with hr=0x%x\n", hr);
        }
        else if (written != cert->cbCertEncoded)
        {
            hr = E_UNEXPECTED;
            fwprintf(stderr, L"WriteFile did not write all the bytes.\n");
        }
    }

    // Release resources
    CloseHandle(hFile);
    return hr;
}
```



## Related topics

<dl> <dt>

[Music Bundle Signature Sample](music-bundle-signature-sample.md)
</dt> </dl>

 

 




