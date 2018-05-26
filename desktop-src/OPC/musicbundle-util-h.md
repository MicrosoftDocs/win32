---
title: util.h
description: util.h
ms.assetid: e0a8abb0-ef11-4067-9790-a899117a8dbd
keywords:
- Packaging APIs,sample applications
- packaging,sample applications
- packages,sample applications
- Packaging APIs,music bundle sample
- packaging,music bundle sample
- packages,music bundle sample
- music bundle sample,util.h
- Packaging APIs,util.h
- packaging,util.h
- packages,util.h
- util.h,music bundle sample
- sample applications,music bundle
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# util.h


```C++
/*****************************************************************************
*
* File: Util.h
*
* Description: This file contains declarations for helper classes and functions.
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

#define countof(x) (sizeof(x)/sizeof(*(x)))

#define MAX_BUFFER_SIZE 1024

HRESULT
GetLastErrorAsHResult(
    VOID
    );

HRESULT
GetRelationshipTargetPart(
    IOpcPartSet         *partSet,
    IOpcRelationship    *rels,
    LPCWSTR              expectedContentType,
    IOpcPart           **targetedPart
    );

HRESULT
GetRelationshipByType(
    IOpcRelationshipSet   *relsSet,
    LPCWSTR                relationshipType,
    IOpcRelationship     **targetedRelationship
    );

HRESULT
GetFullFileName(
    LPCWSTR        filePath,
    LPCWSTR        fileName,
    LPWSTR        *fullFileName
    );

HRESULT
CreateDirectoryFromPartName(
    LPCWSTR        filePath,
    LPCWSTR        partName,
    LPWSTR        *fullFileName
    );

HRESULT
WriteFileContentToPart(
    IOpcFactory     *opcFactory,
    LPCWSTR          filePath,
    LPCWSTR          fileName,
    IOpcPart        *opcPart
    );

HRESULT
DisplayStreamContent(
    LPCWSTR           title,
    IStream          *stream
    );

HRESULT
WritePartContentToFile(
    IOpcFactory     *opcFactory,
    LPCWSTR          pathName,
    IOpcPart        *opcPart
    );
```



## Related topics

<dl> <dt>

[Music Bundle Sample](music-bundle-sample.md)
</dt> </dl>

 

 




