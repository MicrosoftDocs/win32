---
title: opclib.h
description: opclib.h
ms.assetid: 'dcab3b99-8657-4153-b128-ef6b7d317323'
keywords: ["Packaging APIs,set author sample", "packaging,set author sample", "packages,set author sample", "Packaging APIs,sample applications", "packaging,sample applications", "packages,sample applications", "set author sample,opclib.h", "Packaging APIs,opclib.h", "packaging,opclib.h", "packages,opclib.h", "opclib.h", "sample applications,set author"]
---

# opclib.h


```C++
/*****************************************************************************
*
* File: opclib.h
*
* Description:
* This file contains declarations of utility functions that wrap some
* common OPC format related operations needed when working with Packaging
* APIs.
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

namespace opclib
{

//////////////////////////////////////////////////////////////////////////////
// Description:
// Load a package file into a package object to be read.
//////////////////////////////////////////////////////////////////////////////
HRESULT
    LoadPackage(
    IOpcFactory *factory,
    LPCWSTR packageName,
    IOpcPackage **outPackage
    );
//////////////////////////////////////////////////////////////////////////////
// Description:
// Save a package with the specified package file name.
//
// Note: Changes made to a package through a package object are not saved until
// the package is written.
//////////////////////////////////////////////////////////////////////////////
HRESULT
    SavePackage(
    IOpcFactory *factory,
    IOpcPackage *package,
    LPCWSTR targetFileName
    );
//////////////////////////////////////////////////////////////////////////////
// Description:
// If the target of the relationship is a part, get the relative URI of the
// target and resolve this URI to the part name using the URI of the 
// relationship's source as the base URI.
//////////////////////////////////////////////////////////////////////////////
HRESULT
    ResolveTargetUriToPart(
    IOpcRelationship * relativeUri,
    IOpcPartUri **resolvedUri
    );
//////////////////////////////////////////////////////////////////////////////
// Description:
// Find a part that is the target of a package relationship based on the
// specified relationship type. If a content type is specified, check the
// content type of the part to ensure that only a part with the specified
// is retrieved.
// 
// Note: This function finds the first, arbitrary part that is the target of
// a relationship of the specified type and has the specified content type, if
// a content type is provided.
//
// Example of the relationship markup for a relationship that targets a part:
//   <Relationship Id="rId1" 
//      Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" 
//      Target="word/document.xml" />
//
// The "Type" attribute (relationship type) is the definitive way to find a 
// part of interest in a package. The relationship type is defined by the
// package designer or in the OPC and is therefore consistent and predictable.
// 
// In contrast, the "Id" and "Target" attributes are arbitrary and
// unpredictable and are not used to find parts of interest.
//
// Using a relationship type to find a part of interest requires a few steps.
// 1. Identify the relationship type, as defined by the package designer or the
//    OPC, of the relationship(s) that has the part of interest as the target.
// 2. Get relationships of that relationship type from a relationship set.
//    Note: It may be necessary to check that the number of retrieved 
//          relationships conforms to an expected number of relationships
//          specified by the format designer or in the OPC.
// 3. If the target of a retrieved relationship is a part, resolve the part
//    name.
// 4. Get the part.
// 5. If an expected content type is defined by the package designer or the OPC,
//    ensure that the part has the correct content type.
// 6. If the found part has the expected content type, or if no expected
//    content type is defined, return the part.
//////////////////////////////////////////////////////////////////////////////
HRESULT 
    FindPartByRelationshipType(
    IOpcPackage *package,
    LPCWSTR relationshipType,
    LPCWSTR contentType, // optional
    IOpcPart **part
    );

//////////////////////////////////////////////////////////////////////////////
// Description:
// Read part content into a new MSXML DOM document. If selection namespaces
// are provided, set up DOM document for XPath queries. Changes made to
// content from the DOM document must be written to the part explicitly.
//////////////////////////////////////////////////////////////////////////////
HRESULT 
    DOMFromPart(
    IOpcPart * part,
    LPCWSTR selectionNamespaces, // optional
    IXMLDOMDocument2 **document
    );

//////////////////////////////////////////////////////////////////////////////
// Description:
// Helper method that finds the Core Properties part of a package.
//////////////////////////////////////////////////////////////////////////////
HRESULT
    FindCorePropertiesPart(
    IOpcPackage *package,
    IOpcPart **part
    );

//////////////////////////////////////////////////////////////////////////////
// Description:
// Write core properties information to the console.
//////////////////////////////////////////////////////////////////////////////
HRESULT
    PrintCoreProperties(
    IOpcPackage *package
    );

//////////////////////////////////////////////////////////////////////////////
// Description:
// Set the modified by and author core properties of a specified package to a
// specified author.
//////////////////////////////////////////////////////////////////////////////
HRESULT
    SetAuthorAndModifiedBy(
    IOpcPackage *package,
    LPCWSTR AuthorName
    );

}
```



## Related topics

<dl> <dt>

[Set Author Sample](set-author-sample.md)
</dt> </dl>

 

 




