---
title: sign.cpp
description: sign.cpp
ms.assetid: c2954145-fa34-4ff7-a968-43b6047e6f94
keywords:
- Packaging APIs,sample applications
- packaging,sample applications
- packages,sample applications
- Packaging APIs,music bundle signature sample
- packaging,music bundle signature sample
- packages,music bundle signature sample
- music bundle signature sample,sign.cpp
- Packaging APIs,sign.cpp
- packaging,sign.cpp
- packages,sign.cpp
- sign.cpp
- sample applications,music bundle signature
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# sign.cpp


```C++
/*****************************************************************************
*
* File: Sign.cpp
*
* Description:
* This sample is a simple application that might be used as a starting-point
* for an application that uses the Packaging API. This sample demonstrates
* signature generation and validation using a sample signing policy described
* in Sign.h
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
#include "Sign.h"
#include "urlmon.h" // for Uri stuff


// Input/Output file names.
static const WCHAR g_unsignedFilePath[] = L"SampleMusicBundle.zip";
const WCHAR g_signedFilePath[] = L"SampleMusicBundle_signed.zip";

static const WCHAR g_signatureMethod[] = L"http://www.w3.org/2000/09/xmldsig#rsa-sha1";
static const WCHAR g_defaultDigestMethod[] = L"http://www.w3.org/2000/09/xmldsig#sha1";

static const WCHAR g_signatureOriginPartName[] = L"/package/services/digital-signature/origin.psdsor";

// Content types for parts in music bundle.
static const WCHAR g_trackContentType[] = L"audio/x-ms-wma";
static const WCHAR g_lyricContentType[] = L"text/plain";
static const WCHAR g_albumArtContentType[] = L"image/jpeg";
static const WCHAR g_tracklistPartContentType[] = L"application/vnd.ms-wpl";

// Relationship types for relationships in music bundle.
static const WCHAR g_tracklistRelationshipType[] = 
    L"http://schemas.example.com/package/2008/relationships/media-bundle/tracklist";

// The relationship used to target the album art part is the thumbnail
// relationship that is defined in the OPC (ECMA-376 1st edition Part 2).
static const WCHAR g_albumArtRelationshipType[] = 
    L"http://schemas.openxmlformats.org/package/2006/relationships/metadata/thumbnail";

static const WCHAR g_albumWebsiteRelationshipType[] = 
    L"http://schemas.example.com/package/2008/relationships/media-bundle/album-website";

static LPCWSTR g_trackRelationshipType = 
    L"http://schemas.example.com/package/2008/relationships/media-bundle/playlist-song";

static LPCWSTR g_lyricRelationshipType = 
    L"http://schemas.example.com/package/2008/relationships/media-bundle/song-lryic";

// Signature relationship type as defined in OPC spec.
static LPCWSTR g_signatureRelationshipType = 
    L"http://schemas.openxmlformats.org/package/2006/relationships/digital-signature/signature";


// Get the parts that need to be signed according to the signing policy.
// This method may return valid values for some of the out parameters even
// when the method fails. The caller must free resources if a non-NULL
// value is returned.
//
// Parameters:
//  opcPackage - the package of the parts
//  trackParts - when the function returns successfully, it holds the array of track parts.
//  lyricParts - when the function returns successfully, it holds the array of lyric parts.
//  tracklistPart - when the function returns successfully, it holds the tracklist part.
//  albumArtPart - when the function returns successfully, it holds the album art part.
HRESULT
GetPartsToBeSigned(
    IOpcPackage* opcPackage,
    OpcPartArray* trackParts,
    OpcPartArray* lyricParts,
    IOpcPart** tracklistPart,
    IOpcPart** albumArtPart
    )
{
    IOpcPartSet * partSet = NULL;
    IOpcRelationshipSet * relsSet = NULL;
    IOpcRelationshipSet * partRelsSet = NULL;
    IOpcRelationshipEnumerator * partRelsEnumerator = NULL;
    UINT32 count = 0;
    BOOL hasNext = FALSE;
    BOOL hasPrevious = FALSE;

    HRESULT hr = opcPackage->GetRelationshipSet(&amp;relsSet);

    if (SUCCEEDED(hr))
    {
        hr = opcPackage->GetPartSet(&amp;partSet);
    }


    if (SUCCEEDED(hr))
    {
        // Get album art part. According to the sample signing policy,
        // this part needs to be signed.
        hr = GetPartByRelationshipType(
                partSet, 
                relsSet, 
                g_albumArtRelationshipType, 
                g_albumArtContentType,
                albumArtPart
                );
    }

    // Get tracklist part; as defined by the sample signing policy, this part
        // needs to be signed.
    if (SUCCEEDED(hr))
    {
        // Get tracklist part; as defined by the sample signing policy, this
        // part needs to be signed.
        hr = GetPartByRelationshipType(
                partSet, 
                relsSet, 
                g_tracklistRelationshipType, 
                g_tracklistPartContentType, 
                tracklistPart
                );
    }


    if (SUCCEEDED(hr))
    {
        // Get the set relationships that have the tracklist part as
        // their source.
        hr = (*tracklistPart)->GetRelationshipSet(&amp;partRelsSet);
    }


    if (SUCCEEDED(hr))
    {
        // Get the relationships of the track relationship type from
        // the set. These relationships have the tracklist part as their
        // source and a track part as their target.
        hr = partRelsSet->GetEnumeratorForType(g_trackRelationshipType, &amp;partRelsEnumerator);
    }

    // Count the number of relationships in the set that target track parts.
    // This count is the number of track parts in the music bundle.
    // Note: The number of track parts and lyric parts are assumed to be equal.
    while (
        SUCCEEDED(hr) &amp;&amp;
        SUCCEEDED(hr = partRelsEnumerator->MoveNext(&amp;hasNext)) &amp;&amp;
        hasNext
        )
    {
        count++;
    }
    
    // Initialize the OpcPartArrays with the number of track parts in the
    // music bundle.
    if (SUCCEEDED(hr))
    {
        hr = trackParts->Init(count);
    }
    if (SUCCEEDED(hr))
    {
        hr = lyricParts->Init(count);
    }

    // There is no method to reset the current position of the enumerator
    // to its starting position. Instead, there are two ways to rest an 
    // enumerator to its starting position:
    //     1. Iterate backwards through the enumerator until the starting
    //        position is reached.
    //     2. Clone the enumerator BEFORE iterating and when a reset is
    //        desired, iterate through the clone, which will still be in
    //        its starting position.
    while (
        SUCCEEDED(hr) &amp;&amp;
        SUCCEEDED(hr = partRelsEnumerator->MovePrevious(&amp;hasPrevious)) &amp;&amp;
        hasPrevious
        )
    {
        IOpcRelationship * rels = NULL;
        IOpcPart * trackPart = NULL;
        IOpcRelationshipSet * trackPartRelationshipSet = NULL;
        IOpcPart * lyricPart = NULL;

        hr = partRelsEnumerator->GetCurrent(&amp;rels);

        if (SUCCEEDED(hr))
        {
            // Get track part; as defined by the sample signing policy, this part
            // needs to be signed.
            hr = GetRelationshipTargetPart(partSet, rels, g_trackContentType, &amp;trackPart);
        }

        if (SUCCEEDED(hr))
        {
            // Track part was retrieved; therefore, add it to the array of track
            // parts to be signed.
            hr = trackParts->Append(trackPart);
        }

        if (SUCCEEDED(hr))
        {
            // Get the relationships that have this track part as their source.
            hr = trackPart->GetRelationshipSet(&amp;trackPartRelationshipSet);
        }

        if (SUCCEEDED(hr))
        {
            // Get lyric part; as defined by the sample signing policy, this part
            // needs to be signed.
            hr = GetPartByRelationshipType(
                    partSet, 
                    trackPartRelationshipSet, 
                    g_lyricRelationshipType, 
                    g_lyricContentType, 
                    &amp;lyricPart
                    );
        }
        
        if (SUCCEEDED(hr))
        {
            // Lyric part was retrieved; therefore, add it to the array of lyric
            // parts to be signed.
            hr = lyricParts->Append(lyricPart);
        }

        // Release resources
        if (rels)
        {
            rels->Release();
            rels = NULL;
        }

        if (trackPart)
        {
            trackPart->Release();
            trackPart = NULL;
        }

        if (trackPartRelationshipSet)
        {
            trackPartRelationshipSet->Release();
            trackPartRelationshipSet = NULL;
        }

        if (lyricPart)
        {
            lyricPart->Release();
            lyricPart = NULL;
        }
    }
    
    // Release resources
    if (partSet)
    {
        partSet->Release();
        partSet = NULL;
    }

    if (relsSet)
    {
        relsSet->Release();
        relsSet = NULL;
    }

    if (partRelsSet)
    {
        partRelsSet->Release();
        partRelsSet = NULL;
    }

    if (partRelsEnumerator)
    {
        partRelsEnumerator->Release();
        partRelsEnumerator = NULL;
    }

    // Note: If the package format specification has specific requirements
    // for some parts (such as size or content type), the package should be
    // validated against those requirements before it is signed. For
    // example, if the specification requires that a specific part never be
    // empty, that requirement should be validated by checking whether the part
    // size is zero.
    return hr;
}

// Adds a reference to a Relationships part that contains relationships that will
// be selected for signing using a relationship type. More than one relationship
// type may be specified. 
//
// Parameters:
//  relsReferenceSet - The set that the new reference will be added to.
//  sourceUri - The source URI of the relationships.
//  count - The number of relationship types in the relationshipTypes array.
//  relationshipTypes - An array of relationship types.
HRESULT
AddReferenceByRelationshipType(
    IOpcSignatureRelationshipReferenceSet* relsReferenceSet,
    IOpcUri* sourceUri,
    UINT32 count,
    LPCWSTR relationshipTypes[]
    )
{
    // Create a set that will be used to create the criterion used to select relationships
    // to be signed.
    IOpcRelationshipSelectorSet * relsSelectorSet = NULL;

    HRESULT hr = relsReferenceSet->CreateRelationshipSelectorSet(&amp;relsSelectorSet);

    if (SUCCEEDED(hr))
    {
        for (UINT32 i = 0; i < count &amp;&amp; SUCCEEDED(hr); i++)
        {
            // Create a selection criterion that uses a relationship type and
            // add the criterion to the set.
            //
            // Because relationships are being selected by relationship type,
            // relationships that have those types are guarded against changes.
            // However, relationships with different types can be changed, added, or
            // removed, without breaking the signature. To permit even fewer changes,
            // sign all of the relationships in the referenced Relationships part
            // (see OPC_RELATIONSHIP_SIGN_PART) so that any change to the relationships
            // part will break the signature.
            hr = relsSelectorSet->Create(
                    OPC_RELATIONSHIP_SELECT_BY_TYPE,
                    relationshipTypes[i],
                    NULL
                    );
        }

        if (SUCCEEDED(hr))
        {
            // Create the reference using the selector set and add the reference
            // to the set.
            relsReferenceSet->Create(
                sourceUri, 
                NULL,       // Use the default digest method, which is set by
                            // IOpcSigningOptions::SetDefaultDigestMethod().
                OPC_RELATIONSHIP_SIGN_USING_SELECTORS, 
                relsSelectorSet, 
                OPC_CANONICALIZATION_C14N, 
                NULL        // No need to get a pointer to the new reference.
                );
        }
    }

    // Release resources
    if (relsSelectorSet)
    {
        relsSelectorSet->Release();
        relsSelectorSet = NULL;
    }

    return hr;
}

// This method demonstrates how to add application-specific <Object> elements
// to the signature, and how to sign XML in those elements.
HRESULT
AddCustomObjectsToSign(
    IOpcSigningOptions* signingOptions
    )
{
    IOpcSignatureCustomObjectSet * customObjectSet = NULL;
    IOpcSignatureReferenceSet * customReferenceSet = NULL;
    IUri * referenceUri1 = NULL;
    IUri * referenceUri2 = NULL;

    UINT32 count = 0;

    // Custom <Object> elements allow applications to add extra information to
    // the signature, such as adding a trustable timestamp.
    //
    // Note: The signing time provided by the OPC digital signature spec is not
    // trustable because it is recorded from the clock of the local machine
    // where the signature is generated and this clock may be inaccurate.  
    //
    // To show one way that you can use an application-specific <Object> element,
    // we created an application-specific element that contains a fake timestamp.
    // For real-world use, a trustable timestamp would need to be retrieved from
    // a timestamp server.
    //
    // To better understand this sample, open and view the signature markup that is stored in
    // the signature part in the signed package. The default file extension of the signature
    // part is .psdsxs.

    // Example of constructing a fully signed application-specific <Object> element.
    // The entire element will be signed because we will reference the Id attribute 
    // of the <Object> element. 
    //
    // Note: The namespace declaration must be included in the XML markup; 
    // otherwise the markup is not valid XML.
    UINT8 customObject1[] = 
        "<Object Id=\"idMyCustomObject_Timestamp1\" xmlns=\"http://www.w3.org/2000/09/xmldsig#\" xmlns:x=\"http://www.example.com/MusicBundle\">"
            "<x:Comment>This is a fake timestamp.</x:Comment>"
            "<x:EncodedTime>ABCDEFGHIJK</x:EncodedTime>"
        "</Object>";

    // Example of constructing a partially signed application-specific <Object>
    // element.
    UINT8 customObject2[] = 
        "<Object xmlns=\"http://www.w3.org/2000/09/xmldsig#\">"
            // The <TimeStamp> element will be signed, because we will 
            // reference its Id attribute.
            "<TimeStamp Id=\"idMyCustomObject_Timestamp2\" xmlns=\"http://www.example.com/MusicBundle\">"
                "<Comment>This is a fake timestamp.</Comment>"
                "<EncodedTime>ABCDEFGHIJK</EncodedTime>"
            "</TimeStamp>"
            // Outside of the <TimeStamp> element is the unsigned portion of
            // this application-specific element. Updates (changes such as
            // addition or deletion) can be made in that portion without
            // breaking the signature.
            "<Extension xmlns=\"http://www.example.com/MusicBundle\">"
                "<Comment>Unsigned portion of XML. Can be updated without breaking the signature.</Comment>"
            "</Extension>"
        "</Object>";


    // Get the set of application-specific <Object> eleemnts. Application-specific
    // <Object> elements that are added to the set will be serialized in the
    // signature markup when the signature is generated.
    HRESULT hr = signingOptions->GetCustomObjectSet(&amp;customObjectSet);
    
    // Create and add the custom object into the custom object set.
    if (SUCCEEDED(hr))
    {
        // Number of bytes of the application-specific element; subtract 1 because
        // the last byte of the buffer is the string terminator ('\0').
        count = sizeof(customObject1)/sizeof(customObject1[0]) - 1;

        hr = customObjectSet->Create(customObject1, count, NULL);
    }
   
    // Create and add the custom object into the custom object set.
    if (SUCCEEDED(hr))
    {
        // Number of bytes of the application-specific element; subtract 1 because
        // the last byte of the buffer is the string terminator ('\0').
        count = sizeof(customObject2)/sizeof(customObject2[0]) - 1;
     
        hr = customObjectSet->Create(customObject2, count, NULL);
    }

    // Application-specific <Object> elements that are represented by custom
    // objects in the set will appear in the signature markup. However, these
    // elements will not be signed unless you add references to them.

    if (SUCCEEDED(hr))
    {
        // Get the set of references to XML elements to be signed, that are in
        // application-specific <Object> elements.
        hr = signingOptions->GetCustomReferenceSet(&amp;customReferenceSet);
    }

    if (SUCCEEDED(hr))
    {
        // Create the URI to be used for the reference to the first application
        // -specific element. Here, "#idMyCustomObject_Timestamp1" refers 
        // to the first application-specific element. Its entire XML markup will
        // be signed.
        //
        // Note: The reference URI for the element to be signed is constructed as 
        // "#" + the Id attribute value of the element to be signed.
        hr = CreateUri(L"#idMyCustomObject_Timestamp1", Uri_CREATE_ALLOW_RELATIVE, 0, &amp;referenceUri1);

    }

    if (SUCCEEDED(hr))
    {
        // Create reference to the first application-specific <Object> element. The 
        // reference uses a URI to identify the element to be signed.
        hr = customReferenceSet->Create(
                referenceUri1, 
                NULL,                        // No Id specified for the reference.
                L"http://www.w3.org/2000/09/xmldsig#Object", // Type of the entity
                                                             // that is referenced.
                NULL,                        // Use the default digest method, which is set by
                                            // IOpcSigningOptions::SetDefaultDigestMethod().
                OPC_CANONICALIZATION_C14N,  // Use C14N to canonicalize the referenced XML markup
                                            // before signing.
                NULL                        // No need for pointer to new reference.
                );
    }

    // Create reference to the element we want to sign in the second custom object. 
    // Note that the reference Uri is constructed as "#" + the Id value of the element 
    // you want to sign. Here "#idMyCustomObject_Timestamp2" refers to the <TimeStamp>
    // element inside of the second custom object. Only the <TimeStamp> XML markup, including
    // its nested elements will be signed.

    if (SUCCEEDED(hr))
    {
        // Create the URI to be used for the reference to the second application
        // -specific element. Here,"#idMyCustomObject_Timestamp2" refers to the
        // <TimeStamp> element inside of the second application-specific element.
        // Only the <TimeStamp> XML markup, including its nested elements, will be signed.
        //
        // Note: The reference URI for the element to be signed is constructed as 
        // "#" + the Id attribute value of the element to be signed.
        hr = CreateUri(
                L"#idMyCustomObject_Timestamp2",
                Uri_CREATE_ALLOW_RELATIVE,
                0,
                &amp;referenceUri2
                );
    }

    if (SUCCEEDED(hr))
    {
        hr = customReferenceSet->Create(
                referenceUri2, 
                NULL,                        // No Id specified for the reference.
                L"http://www.example.com/MusicBundle#TimestampObject", // Type of the entity
                                                                       // that is referenced.
                NULL,                        // Use the default digest method, which is set by
                                            // IOpcSigningOptions::SetDefaultDigestMethod().
                OPC_CANONICALIZATION_C14N,  // Use C14N to canonicalize the referenced XML markup
                                            // before signing.
                NULL                        // No need for pointer to new reference.
                );
    }

    // Release resources
    if (customObjectSet)
    {
        customObjectSet->Release();
        customObjectSet = NULL;
    }

    if (customReferenceSet)
    {
        customReferenceSet->Release();
        customReferenceSet = NULL;
    }

    if (referenceUri1)
    {
        referenceUri1->Release();
        referenceUri1 = NULL;
    }

    if (referenceUri2)
    {
        referenceUri2->Release();
        referenceUri2 = NULL;
    }

    return hr;
}

// Display a certificate selection dialog and let the user select a certificate
// for signing.
HRESULT
SelectCert(
    PCCERT_CONTEXT* certContext
    )
{
    typedef BOOL (WINAPI *fnCertSelectCertificate)(PCERT_SELECT_STRUCT_W);

    HMODULE hCryptDlgInst = LoadLibrary(L"CryptDlg.dll");

    if (hCryptDlgInst == NULL)
    {
        fwprintf(stderr, L"Cannot load CryptDlg.dll.\n");
        return HRESULT_FROM_WIN32(GetLastError());
    }

    HRESULT hr = S_OK;

    fnCertSelectCertificate  pfnCertSelectCertificate = 
        (fnCertSelectCertificate)GetProcAddress(hCryptDlgInst, "CertSelectCertificateW");

    if (pfnCertSelectCertificate)
    {
        HCERTSTORE hMySysStore = CertOpenSystemStore(NULL, L"MY");
        if (hMySysStore)
        {
            CERT_SELECT_STRUCT certSelect = {0};
            certSelect.dwSize = sizeof(CERT_SELECT_STRUCT);
            certSelect.hInstance = hCryptDlgInst;

            certSelect.szTitle = L"Select signing certificate.";
            certSelect.cCertStore = 1;
            certSelect.arrayCertStore = &amp;hMySysStore;

            certSelect.cCertContext = 1;
            certSelect.arrayCertContext = certContext;

            BOOL result = pfnCertSelectCertificate(&amp;certSelect);

            if (!result) 
            {
                hr = HRESULT_FROM_WIN32(GetLastError());

                if (SUCCEEDED(hr))
                {
                    // The user just clicked "Cancel".
                    fwprintf(stderr, L"You must select a certificate for signing to proceed.\n");
                    hr = E_FAIL;
                }
                else
                {
                    fwprintf(stderr, L"CertSelectCertificate() failed.\n");
                }
            }

            CertCloseStore(hMySysStore, 0);
        }
        else 
        {
            fwprintf(stderr, L"CertOpenSystemStore() failed.\n");
            hr = HRESULT_FROM_WIN32(GetLastError());
        }
    }
    else 
    {
        fwprintf(stderr, L"Cannot find CertSelectCertificateW function in CryptDlg.dll.\n");
        hr = HRESULT_FROM_WIN32(GetLastError());
    }

    FreeLibrary(hCryptDlgInst);
    return hr;
}

// Add signing information to signing options to be prepared for
// signature generation.
//
// Parameters:
//  opcFactory - The IOpcFactory instance.
//  opcPackage - The package to be signed.
//  signingOptions - The signing options that will be populated
//                   with signing information.
//  opcDigSigManager - The digital signature manager that will control
//                     the signing process.
HRESULT
PrepareForSigning(
    IOpcFactory* opcFactory,
    IOpcPackage* opcPackage,
    IOpcSigningOptions* signingOptions,
    IOpcDigitalSignatureManager* opcDigSigManager
    )
{
    IOpcPart * albumArtPart = NULL;
    IOpcPart * tracklistPart = NULL;
    IOpcSignaturePartReferenceSet * partReferenceSet = NULL;
    IOpcSignatureRelationshipReferenceSet * relsReferenceSet = NULL;
    IOpcUri * rootUri = NULL;
    IOpcPartUri * albumArtPartUri = NULL;
    IOpcPartUri * tracklistPartUri = NULL;
    IOpcPartUri * signatureOriginPartUri = NULL;

    OpcPartArray trackParts;
    OpcPartArray lyricParts;

    // As defined by the sample signing policy, any root relationship with
    // tracklist, album art, or album website relationship type needs to
    // be signed. 
    LPCWSTR rootRelationshipTypesToSign[] = 
    {
        g_tracklistRelationshipType, 
        g_albumArtRelationshipType, 
        g_albumWebsiteRelationshipType
    };
    
    // Get the parts that need to be signed according to the sample signing
    // policy.
    HRESULT hr = GetPartsToBeSigned(
                    opcPackage,
                    &amp;trackParts,
                    &amp;lyricParts,
                    &amp;tracklistPart,
                    &amp;albumArtPart
                    );

    if (SUCCEEDED(hr))
    {
        // Get the set of references to the parts that will be signed.
        hr = signingOptions->GetSignaturePartReferenceSet(&amp;partReferenceSet);
    }

    if (SUCCEEDED(hr))
    {
        // Get the set of references to Relationships parts that contain 
        // the relationships that will be signed (relsReferenceSet).
        hr = signingOptions->GetSignatureRelationshipReferenceSet(&amp;relsReferenceSet);
    }

    if (SUCCEEDED(hr))
    {
        // Create a URI for the package-root.
        hr = opcFactory->CreatePackageRootUri(&amp;rootUri);
    }

    if (SUCCEEDED(hr))
    {
        // To relsReferenceSet, add a reference to the Relationships part that
        // stores package relationships. These relationships will be selected for
        // signing by using their relationship type.
        hr = AddReferenceByRelationshipType(relsReferenceSet, rootUri, 3, rootRelationshipTypesToSign);
    }

    if (SUCCEEDED(hr))
    {
        // Get the URI of the album art part.
        hr = albumArtPart->GetName(&amp;albumArtPartUri);
    }

    if (SUCCEEDED(hr))
    {
        // Create a reference to the album art part for signing.
        hr = partReferenceSet->Create(
                albumArtPartUri, 
                NULL,   // Use the default digest method, which is set by
                        // IOpcSigningOptions::SetDefaultDigestMethod().
                OPC_CANONICALIZATION_NONE,
                NULL    // No pointer needed to the new reference.
                );
    }

    if (SUCCEEDED(hr))
    {
        // Get the URI of the tracklist part.
        hr = tracklistPart->GetName(&amp;tracklistPartUri);
    }

    if (SUCCEEDED(hr))
    {
        // Create a reference to the tracklist part so that this part
        // will be signed.
        hr = partReferenceSet->Create(
                tracklistPartUri, 
                NULL,   // Use the default digest method, which is set by
                        // IOpcSigningOptions::SetDefaultDigestMethod().
                OPC_CANONICALIZATION_NONE,
                NULL    // No pointer needed to the new reference.
                );
    }

    // As defined in the sample signing policy, all relationships that are the
    // tracklist relationship type and that have the tracklist part as their
    // source need to be signed. 
    if (SUCCEEDED(hr))
    {
        // Add a reference to the Relationships part that stores the
        // relationships that have the tracklist part as their source. Select the
        // relationships that will be signed using the tracklist relationship type.
        hr = AddReferenceByRelationshipType(
                relsReferenceSet,
                tracklistPartUri,
                1,
                &amp;g_trackRelationshipType
                );
    }

    if (SUCCEEDED(hr))
    {
        // Create references to the track parts so that these parts
        // will be signed.
        UINT32 numberOfTracks = trackParts.GetCount();
    
        for (UINT32 i=0; i<numberOfTracks &amp;&amp; SUCCEEDED(hr); i++)
        {
            IOpcPart * trackPart = NULL;
            IOpcPartUri * trackPartUri = NULL;
    
            hr = trackParts.GetAt(i, &amp;trackPart);
            
            if (SUCCEEDED(hr))
            {
                hr = trackPart->GetName(&amp;trackPartUri);
            }
    
            if (SUCCEEDED(hr))
            {
                hr = partReferenceSet->Create(
                        trackPartUri, 
                        NULL,   // Use the default digest method, which is set by
                                // IOpcSigningOptions::SetDefaultDigestMethod().
                        OPC_CANONICALIZATION_NONE,
                        NULL    // No pointer needed to the new reference.
                        );
            }
    
            // As defined in the sample signing policy, all relationships that have
            // the lyric relationship type and a track part as their source need to
            // be signed. 
            if (SUCCEEDED(hr))
            {
                // Add a reference to the Relationships part that stores the
                // relationships that have the track part as their source. Select
                // the relationships that will be signed by using the lyric
                // relationship type.
                hr = AddReferenceByRelationshipType(
                        relsReferenceSet,
                        trackPartUri,
                        1,
                        &amp;g_lyricRelationshipType
                        );
            }
    
            if (trackPart)
            {
                trackPart->Release();
                trackPart = NULL;
            }
    
            if (trackPartUri)
            {
                trackPartUri->Release();
                trackPartUri = NULL;
            }
        }
    }

    if (SUCCEEDED(hr))
    {
        // Create references to the lyric parts so that these parts
        // will be signed. 
        UINT32 numberOfLyrics = lyricParts.GetCount();
    
        for (UINT32 i=0; i<numberOfLyrics &amp;&amp; SUCCEEDED(hr); i++)
        {
            IOpcPart * lyricPart = NULL;
            IOpcPartUri * lyricPartUri = NULL;
    
            hr = lyricParts.GetAt(i, &amp;lyricPart);
    
            if (SUCCEEDED(hr))
            {
                hr = lyricPart->GetName(&amp;lyricPartUri);
            }
    
            if (SUCCEEDED(hr))
            {
                hr = partReferenceSet->Create(
                        lyricPartUri, 
                        NULL,   // Use the default digest method, which is set by
                                // IOpcSigningOptions::SetDefaultDigestMethod().
                        OPC_CANONICALIZATION_NONE,
                        NULL    // No pointer needed to the new reference.
                        );
            }
    
            if (lyricPart)
            {
                lyricPart->Release();
                lyricPart = NULL;
            }
    
            if (lyricPartUri)
            {
                lyricPartUri->Release();
                lyricPartUri = NULL;
            }
        }
    }

    // As defined in the sample signing policy, any relationship that has
    // the signature relationship type and that has the signature origin part
    // as its source needs to be signed.
    //
    // Note: Signing these relationships is not required by section 12. Digital
    // Signatures of the OPC (ECMA-376 1st edition Part 2). If these
    // relationships are signed, adding new signatures to the pacakge will not
    // be permitted. Signing may be desirable, or not, depending on the user's
    // scenario, and it should be specified in the signing policy of the format.
    // To allow somebody else to sign the package after it has already been
    // signed (counter-sign scenario), do not sign these relationships.
    if (SUCCEEDED(hr))
    {
        hr = opcFactory->CreatePartUri(g_signatureOriginPartName, &amp;signatureOriginPartUri);
    }
    
    if (SUCCEEDED(hr))
    {    
        // The name of the signature origin part must be set before calling Sign(). If the name of
        // the signature origin part is not unique in the package, Sign() will fail.
        hr = opcDigSigManager->SetSignatureOriginPartName(signatureOriginPartUri);
    }

    if (SUCCEEDED(hr))
    {
        // Add a reference to the Relationships part that stores the
        // relationships that have the digital signature origin part
        // as their source. Select the relationships that will be signed
        // by using the signature relationship type.
        hr = AddReferenceByRelationshipType(
                relsReferenceSet,
                signatureOriginPartUri,
                1,
                &amp;g_signatureRelationshipType
                );
    }
 
    if (SUCCEEDED(hr))
    {
        // The following code shows how to set the certificate embedding option. 
        // The default certificate embedding option is recommended because if the
        // certificate is stored in a part, multiple signatures use the same
        // certificate. Omit this code if the default embedding
        // option is acceptable.
        hr = signingOptions->SetCertificateEmbeddingOption(OPC_CERTIFICATE_IN_CERTIFICATE_PART);
    }

    if (SUCCEEDED(hr))
    {
        // Add application-specific <Object> elements to the signature. These elements
        // can be used to add more information (such as an XAdES timestamp) to the
        // signature. Omit this code if the package to be signed does not need any
        // application-specific elements.
        hr = AddCustomObjectsToSign(signingOptions);
    }

    if (SUCCEEDED(hr))
    {
        // The default digest method must be set before calling Sign(). 
        hr = signingOptions->SetDefaultDigestMethod(g_defaultDigestMethod);
    }

    if (SUCCEEDED(hr))
    {
        // The signature method must be set before calling Sign().
        // Additionally, the certificate to be used for signing must support
        // the signature method; otherwise Sign() will fail. For more
        // information on how to find the supported signature methods for a
        // certificate, see the CryptXmlEnumAlgorithmInfo API.
        hr = signingOptions->SetSignatureMethod(g_signatureMethod);
    }

    // Release resources
    if (albumArtPart)
    {
        albumArtPart->Release();
        albumArtPart = NULL;
    }

    if (tracklistPart)
    {
        tracklistPart->Release();
        tracklistPart = NULL;
    }

    if (partReferenceSet)
    {
        partReferenceSet->Release();
        partReferenceSet = NULL;
    }

    if (relsReferenceSet)
    {
        relsReferenceSet->Release();
        relsReferenceSet = NULL;
    }

    if (rootUri)
    {
        rootUri->Release();
        rootUri = NULL;
    }

    if (albumArtPartUri)
    {
        albumArtPartUri->Release();
        albumArtPartUri = NULL;
    }

    if (tracklistPartUri)
    {
        tracklistPartUri->Release();
        tracklistPartUri = NULL;
    }

    if (signatureOriginPartUri)
    {
        signatureOriginPartUri->Release();
        signatureOriginPartUri = NULL;
    }

    return hr;
}

// Sign a music bundle.
HRESULT
SignMusicBundle(
    IOpcFactory* opcFactory
    )
{
    IOpcPackage * opcPackage = NULL;
    IOpcDigitalSignatureManager * opcDigSigManager = NULL;
    IOpcDigitalSignatureEnumerator * signatureEnumerator = NULL;
    IOpcSigningOptions * signingOptions = NULL;
    IOpcDigitalSignature * signature = NULL;

    // Load the input music bundle package.
    HRESULT hr = ReadPackageFromFile(g_unsignedFilePath, opcFactory, &amp;opcPackage);

    // Create a digital signature manager for the package.
    if (SUCCEEDED(hr))
    {
        hr = opcFactory->CreateDigitalSignatureManager(opcPackage, &amp;opcDigSigManager);
    }

    // Detect whether the package has been signed previously because the
    // signing policy for this sample disallows counter-signing
    // (adding more signatures to an already signed music bundle). Therefore,
    // attemping to sign a music bundle that has already been signed will break
    // the existing signature because relationships of the signature relationship
    // type that have the signature origin part as thier source were signed.  
    //
    // Note: It is not required or recommended for a signing policy to disallow
    // the counter-signature scenario. If your signing policy allows counter-
    // signature, do not sign relationships  of the signature relationship
    // type that have the signature origin part as thier source were signed.
    if (SUCCEEDED(hr))
    {
        hr = opcDigSigManager->GetSignatureEnumerator(&amp;signatureEnumerator);
    }
    if (SUCCEEDED(hr))
    {
        // Check for an existing signature.
        BOOL hasNext = FALSE;
        hr = signatureEnumerator->MoveNext(&amp;hasNext);

        if (SUCCEEDED(hr) &amp;&amp; hasNext)
        {
            fwprintf(
                stderr, 
                L"This music bundle has been signed. To sign a music bundle, it must have not been signed before.\n"
                );

            hr = E_UNEXPECTED;
        }
    }

    if (SUCCEEDED(hr))
    {
        hr = opcDigSigManager->CreateSigningOptions(&amp;signingOptions);
    }

    if (SUCCEEDED(hr))
    {
        // Configure signing options, adding references to parts and relationships
        // that need to be signed.
        hr = PrepareForSigning(opcFactory, opcPackage, signingOptions, opcDigSigManager);
    }

    // Let the user select a certificate from the certificate store on the local machine.
    // The certificate will be used to sign the music bundle, and the signer can be identified
    // by the certificate. It is not always necessary to display a UI dialog for the user to select
    // a signer certificate. In a server signing scenario (no human interaction), the server process 
    // may use a predefined certificate or pick a certificate from a certificate store using
    // the CertFindCertificateInStore API.
    //
    // The signature method, RSA-SHA1, that is used for this sample was chosen arbitrarily; therefore,
    // the certificate that is selected must support the RSA-SHA1 signature method. RSA is the
    // encryption algorithm; users can check whether a certificate supports RSA by checking
    // its public key type. SHA1 is the hash algorithm and is not related to a certificate. Because the
    // encryption algorithm can be determined from the certificate, and because the hash algorithm is
    // independent from the certificate, the certificate that is used for signing can used to determine
    // the signature method. For more information about how to find which signature methods are supported
    // by a certificate, see the CryptXmlEnumAlgorithmInfo API.
    //
    // Note: Sign() does not verify the certificate, the user should do so by making sure that,
    // for example, the certificate is not expired, or is not in revocation lists, etc. The user
    // should also verify the certification path of the certificate to check whether it leads to
    // a trusted root certificate. this check can be performed programmatically in production code.
    // For more information, check CertGetCertificateChain API.
    PCCERT_CONTEXT cert = NULL;
    if (SUCCEEDED(hr))
    {
        hr = SelectCert(&amp;cert);
    }

    // Sign() will add signature-related parts and relationships to the package. 
    // If Sign() fails, it may leave unwanted parts and relationships in the package. 
    // However, changes will not persist, until IOpcFactory::WritePackageToStream()
    // is called. If Sign() fails, do not save the resultant pacakge by calling
    // WritePackageToStream, and the original package on disk will be intact. 
    //
    // However, before calling Sign() on a new package or edited, existing package,
    // save the package to prevent loss of data if Sign() fails. 

    if (SUCCEEDED(hr))
    {
        // For this sample, because the package has no changes that need to be
        // saved, call Sign() immediately.
        hr = opcDigSigManager->Sign(cert, signingOptions, &amp;signature);
    }

    // Release the CERT_CONTEXT retrieved by SelectCert().
    if (cert)
    {
        CertFreeCertificateContext(cert);
    }

    // Save the signed music bundle.
    if (SUCCEEDED(hr))
    {
        hr = WritePackageToFile(g_signedFilePath, opcPackage, opcFactory);
    }

    if (SUCCEEDED(hr))
    {
        fwprintf(stdout, L"Music bundle has been signed successfully and saved to %s\n", g_signedFilePath);
    }

    // Release resources
    if (opcPackage)
    {
        opcPackage->Release();
        opcPackage = NULL;
    }

    if (opcDigSigManager)
    {
        opcDigSigManager->Release();
        opcDigSigManager = NULL;
    }

    if (signatureEnumerator)
    {
        signatureEnumerator->Release();
        signatureEnumerator = NULL;
    }

    if (signingOptions)
    {
        signingOptions->Release();
        signingOptions = NULL;
    }

    if (signature)
    {
        signature->Release();
        signature = NULL;
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[Music Bundle Signature Sample](music-bundle-signature-sample.md)
</dt> </dl>

 

 




