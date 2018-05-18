---
title: util.h
description: util.h
ms.assetid: 'fdbaaf21-d784-4258-863d-42417ed83108'
keywords: ["Packaging APIs,sample applications", "packaging,sample applications", "packages,sample applications", "Packaging APIs,music bundle signature sample", "packaging,music bundle signature sample", "packages,music bundle signature sample", "music bundle signature sample,util.h", "Packaging APIs,util.h", "packaging,util.h", "packages,util.h", "util.h,music bundle signature sample", "sample applications,music bundle signature"]
---

# util.h


```C++
/*****************************************************************************
*
* File: Util.h
*
* Description:
* Utility classes and function declarations for Packaging APIs.
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

#pragma once

// Array class for storing and managing IOpcPart interface pointers.
class OpcPartArray
{
public:
    OpcPartArray() : m_container(NULL), m_count(0), m_bufferSize(0)
    {
    }

    ~OpcPartArray()
    {
        if (m_container)
        {
            for (UINT32 i=0; i<m_count; i++)
            {
                IOpcPart* part = m_container[i];
                
                if (part)
                {
                    part->Release();
                }
            }

            delete[] m_container;
        }
    }

    // Allocate and initialize the internal buffer for storing array elements.
    HRESULT
    Init(
        UINT32 numberOfElementsWantToStore
        )
    {
        HRESULT hr = S_OK;

        if (m_container)
        {
            hr = E_NOT_VALID_STATE;   // Already initialized.
        }

        if (SUCCEEDED(hr))
        {
            m_container = new(std::nothrow) IOpcPart*[numberOfElementsWantToStore];
        }

        if (SUCCEEDED(hr) &amp;&amp; !m_container)
        {
            hr = E_OUTOFMEMORY;   // Not enough memory.
        }

        if (SUCCEEDED(hr))
        {
            ZeroMemory(m_container, numberOfElementsWantToStore*sizeof(m_container[0]));
        
            m_bufferSize = numberOfElementsWantToStore;
        }

        return hr;
    }

    // Get the number of elements in the array.
    UINT32
    GetCount() { return m_count; }

    HRESULT
    Append(
        IOpcPart* part
        )
    {
        HRESULT hr = S_OK;

        if (m_count >= m_bufferSize)
        {
            hr = E_NOT_SUFFICIENT_BUFFER;   // Overflow.
        }

        if (SUCCEEDED(hr))
        {
            m_container[m_count] = part;
            part->AddRef();
            m_count++;
        }

        return hr;
    }

    HRESULT
    GetAt(
        UINT32 index,
        IOpcPart** part
        )
    {
        HRESULT hr = S_OK;

        if (index >= m_count)
        {
            hr = E_INVALIDARG;    // Out of range.
        }

        if (SUCCEEDED(hr))
        {
            *part = m_container[index];

            (*part)->AddRef();
        }

        return hr;
    }

private:
    IOpcPart** m_container;
    UINT32 m_count;
    UINT32 m_bufferSize;
};

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
    );

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
    );

// Begin reading the package from the specified file.
HRESULT
ReadPackageFromFile(
    LPCWSTR filename,
    IOpcFactory* opcFactory,
    IOpcPackage** opcPackage
    );

// Write the package to the specified file.
HRESULT
WritePackageToFile(
    LPCWSTR filename,
    IOpcPackage* opcPackage,
    IOpcFactory* opcFactory
    );

// Saves a certificate to the specified file.
HRESULT
SaveCertificateToFile(
    PCCERT_CONTEXT cert,
    LPCWSTR filename
    );
```



## Related topics

<dl> <dt>

[Music Bundle Signature Sample](music-bundle-signature-sample.md)
</dt> </dl>

 

 




