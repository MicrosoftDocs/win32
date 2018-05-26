---
title: validate.h
description: validate.h
ms.assetid: 0cc8ecf9-b820-4c63-b6bd-a10953d81d44
keywords:
- Packaging APIs,sample applications
- packaging,sample applications
- packages,sample applications
- Packaging APIs,music bundle signature sample
- packaging,music bundle signature sample
- packages,music bundle signature sample
- music bundle signature sample,validate.h
- Packaging APIs,validate.h
- packaging,validate.h
- packages,validate.h
- validate.h
- sample applications,music bundle signature
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# validate.h


```C++
/*****************************************************************************
*
* File: Validate.h
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

// Performs music bundle signature validation task.
HRESULT
ValidateMusicBundleSignature(
    IOpcFactory* opcFactory
    );
```



## Related topics

<dl> <dt>

[Music Bundle Signature Sample](music-bundle-signature-sample.md)
</dt> </dl>

 

 




