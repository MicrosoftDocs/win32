---
title: Handling Server Application Errors
description: If the server application successfully processes the uploaded file, the application should return 200.
ms.assetid: fd0b10f1-52b4-4564-9683-620f3b965680
ms.topic: article
ms.date: 05/31/2018
---

# Handling Server Application Errors

If the server application successfully processes the uploaded file, the application should return 200. If the application does not return 200, the BITS client uses the error code to determine if the error is a transient error or fatal error.

All 3xx error codes are transient errors except 300 - 305 and 307, which are fatal errors. All 4xx error codes are fatal errors except for 408 and 409, which are transient errors. All 5xx error codes are transient errors except 501 and 505, which are fatal errors. All other HTTP codes are considered transient errors. Note that a 403 error code is the only error code that prevents BITS from posting the upload file to the server application again.

To retrieve the error, call the [**IBackgroundCopyError::GetError**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyerror-geterror) method. The error context will be BG\_ERROR\_CONTEXT\_REMOTE\_APPLICATION.

 

 




