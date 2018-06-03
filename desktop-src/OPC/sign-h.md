---
title: sign.h
description: sign.h
ms.assetid: fef4998a-feb9-477f-8384-76439e087bbf
keywords:
- Packaging APIs,sample applications
- packaging,sample applications
- packages,sample applications
- Packaging APIs,music bundle signature sample
- packaging,music bundle signature sample
- packages,music bundle signature sample
- music bundle signature sample,sign.h
- Packaging APIs,sign.h
- packaging,sign.h
- packages,sign.h
- sign.h
- sample applications,music bundle signature
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# sign.h


```C++
/*****************************************************************************
*
* File: Sign.h
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

#pragma once

//  ============================= Signing Policy ==================================
//
//  A signing policy defines which and how parts and relationships should be signed
//  for a package to ensure compliance with a custom package format. The OPC
//  enables users to build custom package formats; it does not define a signing
//  policy. Users of the Packaging Digital Signature APIs must define the signing
//  policy for their custom package formats.
//
//  The signing policy for the sample package format called a media bundle is as
//  follows: 
//
//      Parts that need to be signed:    
//  ---------------------------------------------
//  Part                Canonicalization Method
//  ---------------------------------------------
//  Album art part      OPC_CANONICALIZATION_NONE
//  Tracklist part      OPC_CANONICALIZATION_NONE
//  Track part          OPC_CANONICALIZATION_NONE
//  Lyric part          OPC_CANONICALIZATION_NONE
//
//  Note: Because none of these parts contain XML markup, no canonicalization
//  method (OPC_CANONICALIZATION_NONE) can be applied to part content. If the parts
//  to be signed contain XML, then either C14N canonicalization method
//  (OPC_CANONICALIZATION_C14N or OPC_CANONICALIZATION_C14N_WITH_COMMENTS) may be
//  applied.
//
//      Relationships that need to be signed:
//  ---------------------------------------------
//  Relationship Source        Relationship Type
//  ---------------------------------------------
//  Package root            http://schemas.openxmlformats.org/package/2006/relationships/metadata/thumbnail
//  Package root            http://schemas.example.com/package/2008/relationships/media-bundle/album-website
//  Package root            http://schemas.example.com/package/2008/relationships/media-bundle/tracklist
//  Tracklist part          http://schemas.example.com/package/2008/relationships/media-bundle/playlist-song
//  Track part              http://schemas.example.com/package/2008/relationships/media-bundle/song-lryic
//  Signature Origin part   http://schemas.openxmlformats.org/package/2006/relationships/digital-signature/signature
//
//  Relationships of the signature type that have the Signature Origin part as their source
//  must be signed in order to prevent signatures being added to an already signed music
//  bundle (no countersignature is allowed in this policy). To allow new signature(s) to be
//  added to a package that has already been signed package (countersignature), do not sign
//  these signature relationships in your format's signing policy.
//
//  ==========================================================================================

// The file path of the signed music bundle
extern const WCHAR g_signedFilePath[];

// Sign a music bundle.
HRESULT
SignMusicBundle(
    IOpcFactory* opcFactory
    );

```



## Related topics

<dl> <dt>

[Music Bundle Signature Sample](music-bundle-signature-sample.md)
</dt> </dl>

 

 




