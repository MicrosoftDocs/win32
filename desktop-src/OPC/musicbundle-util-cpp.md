---
title: util.cpp
description: util.cpp
ms.assetid: '70b7bec7-0f6a-4087-a21a-1a1923554a0e'
keywords: ["Packaging APIs,sample applications", "packaging,sample applications", "packages,sample applications", "Packaging APIs,music bundle sample", "packaging,music bundle sample", "packages,music bundle sample", "music bundle sample,util.cpp", "Packaging APIs,util.cpp", "packaging,util.cpp", "packages,util.cpp", "util.cpp,music bundle sample", "sample applications,music bundle"]
---

# util.cpp


```C++
/*****************************************************************************
*
* File: Util.cpp
*
* Description: This file contains definitions for helper classes and functions.
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

#include <msopc.h>  // For Packaging APIs

#include <strsafe.h>

#include "util.h"

///////////////////////////////////////////////////////////////////////////////
// Description:
// Returns the last error as an HRESULT.
///////////////////////////////////////////////////////////////////////////////
HRESULT
GetLastErrorAsHResult(
    VOID
    )
{
    DWORD dwError = GetLastError();

    return HRESULT_FROM_WIN32(dwError);
}

///////////////////////////////////////////////////////////////////////////////
// Description:
// Gets the target part of a relationship with the 'Internal' target mode.
///////////////////////////////////////////////////////////////////////////////
HRESULT
GetRelationshipTargetPart(
    IOpcPartSet  *partSet,          // Set of the parts in the package.
    IOpcRelationship  *relationship,// Relationship that targets the required part.
    LPCWSTR  expectedContentType,   // Content type expected for the target part.
    IOpcPart  **targetPart          // Receives pointer to target part. Method may return a valid
                                    // pointer even on failure, and the caller must always release
                                    // if a non-NULL value is returned.
    )
{
    OPC_URI_TARGET_MODE targetMode;
    IOpcUri * sourceUri = NULL;
    IUri * targetUri = NULL;
    IOpcPartUri * targetPartUri = NULL;
    BOOL partExists = FALSE;
    LPWSTR contentType = NULL;

    HRESULT hr = relationship->GetTargetMode(&amp;targetMode);

    if (SUCCEEDED(hr) &amp;&amp; targetMode != OPC_URI_TARGET_MODE_INTERNAL)
    {
        // The relationship's target is not a part.

        LPWSTR relationshipType = NULL;
        relationship->GetRelationshipType(&amp;relationshipType);

        fwprintf(
            stderr, 
            L"Invalid music bundle package: relationship with type %s must have Internal target mode.\n",
            (PWSTR)relationshipType
            );

        // Set the return code to an error.
        hr = E_FAIL;

        CoTaskMemFree(static_cast<LPVOID>(relationshipType));
    }
        
    // Relationship's target is a part; the target mode is 'Internal'.

    if (SUCCEEDED(hr))
    {
        // Get the URI of the relationship source.
        hr = relationship->GetSourceUri(&amp;sourceUri);
    }
    
    
    if (SUCCEEDED(hr))
    {
        // Get the URI of the relationship target.
        hr = relationship->GetTargetUri(&amp;targetUri);
    }
    
    if (SUCCEEDED(hr))
    {
        // Resolve the target URI to the part name of the target part.
        hr = sourceUri->CombinePartUri(targetUri, &amp;targetPartUri);
    }

    if (SUCCEEDED(hr))
    {
        // Check that a part with the resolved part name exists in the
        // part set.
        hr = partSet->PartExists(targetPartUri, &amp;partExists);
    }

    if (SUCCEEDED(hr) &amp;&amp; !partExists)
    {
        // The part does not exist in the part set.
        fwprintf(
            stderr, 
            L"Invalid music bundle package: the target part of relationship does not exist.\n"
            );

        // Set the return code to an error.
        hr = E_FAIL;
    }

    if (SUCCEEDED(hr))
    {
        // Get the part.
        hr = partSet->GetPart(targetPartUri, targetPart);
    }

    if (SUCCEEDED(hr))
    {
        // Get the content type of the part.
        hr = (*targetPart)->GetContentType(&amp;contentType);
    }

    if (SUCCEEDED(hr))
    {
        if (wcscmp(contentType, expectedContentType) != 0)
        {
            // Content type of the part did not match the expected content
            // type.
            fwprintf(
                stderr, 
                L"Invalid music bundle package: the target part does not have correct content type.\n"
                );

            // Set the return code to an error.
            hr = E_FAIL;
        }
    }

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

    if (targetPartUri)
    {
        targetPartUri->Release();
        targetPartUri = NULL;
    }

    CoTaskMemFree(static_cast<LPVOID>(contentType));

    return hr;
}

///////////////////////////////////////////////////////////////////////////////
// Description:
// Gets the relationship of the specified type from a specified relationship
// set.
// Note: Method expects exactly one relationship of the specified type. This
// limitation is described in the Music Bundle Package specification--and is not
// imposed by the Packaging APIs or the OPC.
///////////////////////////////////////////////////////////////////////////////
HRESULT
GetRelationshipByType(
    IOpcRelationshipSet  *relsSet,         // Relationship set that contains the relationship.
    LPCWSTR  relationshipType,             // The relationship type of the relationship.
    IOpcRelationship  **targetRelationship // Receives the relationship. Method may return a valid
                                           // pointer even on failure, and the caller must always release
                                           // if a non-NULL value is returned.
    )
{
    IOpcRelationshipEnumerator * relsEnumerator = NULL;
    BOOL hasNext;
    int count = 0;

    // Get an enumerator of all relationships of the required type.
    HRESULT hr = relsSet->GetEnumeratorForType(relationshipType, &amp;relsEnumerator);

    // Enumerate through relationships, ensuring that there is exactly one
    // relationship that has the specified type.
    while (SUCCEEDED(hr) &amp;&amp;
           SUCCEEDED(hr = relsEnumerator->MoveNext(&amp;hasNext)) &amp;&amp;
           hasNext)
    {
        count++;

        if (count > 1)
        {
            // There is more than one relationship of the specified type.
            fwprintf(
                stderr, 
                L"Invalid music bundle package: cannot have more than 1 relationship with type: %s.\n",
                relationshipType
                );

            // Set the return code to an error.
            hr = E_FAIL;

            // An error was encountered; stop enumerating.
            break;
        }

        if (SUCCEEDED(hr))
        {
            // Get the relationship at the current position of the enumerator.
            hr = relsEnumerator->GetCurrent(targetRelationship);
        }
    }
    
    if (SUCCEEDED(hr))
    {
         if (count == 0)
         {
             // There were no relationships in the set that had the specified
             // type.
             fwprintf(
                 stderr, 
                 L"Invalid music bundle package: relationship with type %s does not exist.\n",
                 relationshipType
                 );

             // Set the return code to an error.
             hr = E_FAIL;
         }
    }

    if (relsEnumerator)
    {
        relsEnumerator->Release();
        relsEnumerator = NULL;
    }

    return hr;
}

///////////////////////////////////////////////////////////////////////////////
// Description:
// Forms and retrieves a full file name by combining the file name with the
// base directory path. Memory for the full file name is allocated by calling
// CoTaskMemAlloc, and the caller free the memory by calling CoTaskMemFree.
///////////////////////////////////////////////////////////////////////////////
HRESULT
GetFullFileName(
    LPCWSTR  filePath,    // The base directory path.
    LPCWSTR  fileName,    // Name of the file.
    LPWSTR  *fullFileName // The resultant full file name. The caller must free the memory allocated
                          // for this string buffer.
    )
{
    HRESULT hr = S_OK;
    size_t cchFileName = 0;
    size_t cchLength = 0;
    WCHAR * szDest = NULL;
    
    if (fullFileName == NULL)
    {
        // The fullFileName out parameter is required.
        // Set the return code to an error.
        hr = E_INVALIDARG;
    }

    // Calculate the length of the full file name buffer.
    if (SUCCEEDED(hr))
    {
        // Get the length of the base directory string buffer.
        hr = StringCchLength(filePath, STRSAFE_MAX_CCH, &amp;cchLength);
    }

    if (SUCCEEDED(hr))
    {
        // Store the length of the base directory string buffer.
        cchFileName += cchLength;

        // Get the length of the file name string buffer.
        hr = StringCchLength(fileName, STRSAFE_MAX_CCH, &amp;cchLength);
    }

    if (SUCCEEDED(hr))
    {
        // Calculate the length of the full file name string buffer by adding
        // the length of the base directory buffer to the length of the file
        // name buffer, and adding 1 to account for the terminating null
        // character.
        cchFileName += cchLength;
        cchFileName += 1;
    
        // Allocate memory for the full file name buffer of the length in 
        // cchFileName.
        *fullFileName = (LPWSTR)CoTaskMemAlloc(cchFileName*sizeof(WCHAR));
    
        if (*fullFileName == NULL)
        {
            // Error encountered during allocation
            // Set the return code to an error.
            hr = E_OUTOFMEMORY;
        }
    }

    if (SUCCEEDED(hr))
    {
        // Copy the base directory string to the full file name buffer;
        // retrieve a pointer to the end of the base directory string in the
        // full file name buffer; retrieve the number of unused characters in
        // the full file name buffer; finally, set the flag to fill the
        // remainder of the buffer with '0's if the copy succeeds, or fill the
        // entire buffer with '0's if the copy fails.
        szDest = *fullFileName;
        hr = StringCchCopyEx(szDest, cchFileName, filePath, &amp;szDest, &amp;cchFileName, 0);
    }

    if (SUCCEEDED(hr))
    {
        // Append file name to base path in the full file name string
        // buffer.
        hr = StringCchCat(szDest, cchFileName, fileName);
    }

    return hr;
}

///////////////////////////////////////////////////////////////////////////////
// Description:
// Creates and retrieves a full file name by combining the part name with the
// base directory path. The part name is converted to a file name by replacing
// the leading '/' character with '\'. Method creates the directory
// structure to the full file name. Memory for the full file name is allocated
// by calling CoTaskMemAlloc, and the caller free the memory by calling
// CoTaskMemFree.
///////////////////////////////////////////////////////////////////////////////
HRESULT
CreateDirectoryFromPartName(
    LPCWSTR  filePath,    // The base directory path.
    LPCWSTR  partName,    // Part name to use to create full file name.
    LPWSTR  *fullFileName // The resultant full file name. The caller must free the memory allocated
                          // for this string buffer.
    )
{
    HRESULT hr = S_OK;
    size_t cchFileName = 0;
    size_t cchLength = 0;
    LPWSTR szDest = NULL;

    if (fullFileName == NULL)
    {
        // The fullFileName out parameter is required.
        // Set the return code to an error.
        hr = E_INVALIDARG;
    }

    // Calculate the length of the full file name buffer.
    if (SUCCEEDED(hr))
    {
        // Get the length of the base directory string buffer.
        hr = StringCchLength(filePath, STRSAFE_MAX_CCH, &amp;cchLength);
    }
    
    if (SUCCEEDED(hr))
    {
        // Store the length of the base directory string buffer.
        cchFileName += cchLength;

        // Get the length of the part name string buffer.    
        hr = StringCchLength(partName, STRSAFE_MAX_CCH, &amp;cchLength);
    }
    
    if (SUCCEEDED(hr))
    {
        // Calculate the length of the full file name string buffer by adding
        // the length of the base directory buffer to the length of the part
        // name buffer, and adding 1 to account for the terminating null
        // character.
        cchFileName += cchLength;
        cchFileName += 1;
    
        // Allocate memory for the full file name buffer of the length in 
        // cchFileName. 
        *fullFileName = (LPWSTR)CoTaskMemAlloc(cchFileName*sizeof(WCHAR));
    
        if (!*fullFileName)
        {
            // Error encountered during allocation
            // Set the return code to an error.
            hr = E_OUTOFMEMORY;
        }
    }

    szDest = *fullFileName;

    if (SUCCEEDED(hr))
    {
        // Copy the base directory string to the full file name buffer;
        // retrieve a pointer to the end of the base directory string in the
        // full file name buffer; retrieve the number of unused characters in
        // the full file name buffer; finally, set the flag to fill the
        // remainder of the buffer with '0's if the copy succeeds, or fill the
        // entire buffer with '0's if the copy fails.
        hr = StringCchCopyEx(szDest, cchFileName, filePath, &amp;szDest, &amp;cchFileName, 0);
    }
    
    if (SUCCEEDED(hr))
    {
        // Recursively create the directory structure using base file path
        // and the part name, which is converted to the file name.
        for (size_t i = 0; i <= cchLength &amp;&amp; SUCCEEDED(hr); i++, szDest++, partName++)
        {
            if (*partName == '/')
            {
                // The character is '/'; therefore, the szDest buffer
                // contains a directory name.
                // Temporarily null terminate string and create the directory.
                *szDest = '\0';
    
                BOOL createDirSucceeded = CreateDirectory(*fullFileName, NULL);

                if (!createDirSucceeded)
                {
                    // Creation of the directory failed; get the error returned
                    // by the CreateDirectory function.
                    hr = GetLastErrorAsHResult();
    
                    if (hr == HRESULT_FROM_WIN32(ERROR_ALREADY_EXISTS))
                    {
                        // Ignore error if directory already exists.
                        hr = S_OK;
                    }
                }

                // Change the null character to a '\'.
                *szDest = '\\';
            }
            else
            {
                // Copy the character at the current part name buffer index
                // into the memory of current szDest buffer index.
                *szDest = *partName;
            }
        }
    }

    return hr;
}

///////////////////////////////////////////////////////////////////////////////
// Description:
// Opens a stream to the path and file name specified, and deserializes the
// file's content as the content of the part.
///////////////////////////////////////////////////////////////////////////////
HRESULT
WriteFileContentToPart(
    IOpcFactory  *opcFactory,
    LPCWSTR  filePath, // Directory where the file is located.
    LPCWSTR  fileName, // Name of file whose content will be deserialized.
    IOpcPart  *opcPart // Part into which the file content is deserialized.
   
    )
{
    HRESULT hr = S_OK;
    LPWSTR fullFileName = NULL;
    IStream * fileStream = NULL;
    IStream * partStream = NULL;
    
    // Get the full file name of the file.
    hr = GetFullFileName(filePath, fileName, &amp;fullFileName);

    if (SUCCEEDED(hr))
    {
        // Create a read-only stream over the file.
        hr = opcFactory->CreateStreamOnFile(
                fullFileName,
                OPC_STREAM_IO_READ,
                NULL,
                FILE_ATTRIBUTE_NORMAL,
                &amp;fileStream
                );
    }

    if (SUCCEEDED(hr))
    {
        // Get the content stream of the part.
        hr = opcPart->GetContentStream(&amp;partStream);
    }
    
    if (SUCCEEDED(hr))
    {
        // Part content is overwritten; truncate the size of the stream to zero.
        ULARGE_INTEGER zero = {0};
        hr = partStream->SetSize(zero);
    }
    
    if (SUCCEEDED(hr))
    {
        // Copy the content from the file stream to the part content stream.
        ULARGE_INTEGER ul = {(UINT) -1, (UINT) -1};
        hr = fileStream->CopyTo(partStream, ul, NULL, NULL);
    }
    
    CoTaskMemFree(static_cast<LPVOID>(fullFileName));
    
    if (fileStream)
    {
        fileStream->Release();
        fileStream = NULL;
    }

    if (partStream)
    {
        partStream->Release();
        partStream = NULL;
    }

    return hr;
}

///////////////////////////////////////////////////////////////////////////////
// Description:
// Displays stream content in the console.
///////////////////////////////////////////////////////////////////////////////
HRESULT
DisplayStreamContent(
    LPCWSTR  title,  // The title to be displayed above the stream contents.
    IStream  *stream // The stream whose contents are displayed.
    
    )
{
    HRESULT hr = S_OK;
    byte buffer[MAX_BUFFER_SIZE] = {};
    ULONG bytesRead = 1;
    
    // Display title.
    wprintf(L"++++++ %s ++++++\n", title);
    
    // Read and display data from screen.
    while (SUCCEEDED(hr) &amp;&amp; bytesRead > 0)
    {
        // Pass in 'size - 1' so the buffer is always null-terminated
        // when passed in to the wprintf method.
        hr = stream->Read(buffer, sizeof(buffer) - 1, &amp;bytesRead);
    
        if (SUCCEEDED(hr) &amp;&amp; bytesRead > 0)
        {   
            // Display data.
            wprintf(L"%S\n", buffer);
        }
    }
    
    if (SUCCEEDED(hr))
    {
        // Display end delimiter.
        wprintf(L"++++++ End %s ++++++\n\n", title);
    }
    
    return hr;
}

///////////////////////////////////////////////////////////////////////////////
// Description:
// Reads and serializes part content to a specified file. Also creates the
// required directory structure that contains the file.
///////////////////////////////////////////////////////////////////////////////
HRESULT
WritePartContentToFile(
    IOpcFactory  *opcFactory,
    LPCWSTR  filePath, // Base directory path where the file is created.
    IOpcPart  *opcPart // Part whose content is serialized.
    
    )
{
    HRESULT hr = S_OK;
    LPWSTR fullFileName = NULL;
    IStream * fileStream = NULL;
    IStream * partStream = NULL;
    IOpcPartUri * opcPartUri = NULL;
    BSTR partUriString = NULL;
    
    // Get the part name of this part.
    hr = opcPart->GetName(&amp;opcPartUri);
    
    if (SUCCEEDED(hr))
    {
        // Get the part name as string.
        hr = opcPartUri->GetAbsoluteUri(&amp;partUriString);
    }
    
    if (SUCCEEDED(hr))
    {
        // Create the full file name and the directory structure.
        hr = CreateDirectoryFromPartName(filePath, partUriString, &amp;fullFileName);
    }
    
    if (SUCCEEDED(hr))
    {
        // Create a write-only stream over the file where part content will be
        // serialized.
        hr = opcFactory->CreateStreamOnFile(
                fullFileName,
                OPC_STREAM_IO_WRITE,
                NULL,
                FILE_ATTRIBUTE_NORMAL,
                &amp;fileStream
                );
    }
    
    if (SUCCEEDED(hr))
    {
        // Get the part content stream.
        hr = opcPart->GetContentStream(&amp;partStream);
    }
    
    if (SUCCEEDED(hr))
    {
        // Copy the part content stream to the file stream.
        ULARGE_INTEGER const ul = {(UINT) -1, (UINT) -1};
        hr = partStream->CopyTo(fileStream, ul, NULL, NULL);
    }
    
    CoTaskMemFree(static_cast<LPVOID>(fullFileName));
    
    if (fileStream)
    {
        fileStream->Release();
        fileStream = NULL;
    }

    if (partStream)
    {
        partStream->Release();
        partStream = NULL;
    }
    
    if (opcPartUri)
    {
        opcPartUri->Release();
        opcPartUri = NULL;
    }
    SysFreeString(partUriString);
    
    return hr;
}
```



## Related topics

<dl> <dt>

[Music Bundle Sample](music-bundle-sample.md)
</dt> </dl>

 

 




