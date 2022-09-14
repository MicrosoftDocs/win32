---
title: Handling RAS Errors
description: When an error occurs, the Remote Access Connection Manager invokes the client's notification handler.
ms.assetid: 73595fa9-9548-49bf-bcce-d023bc1351d5
keywords:
- Remote Access Service RAS ,errors
ms.topic: article
ms.date: 05/31/2018
---

# Handling RAS Errors

When an error occurs, the Remote Access Connection Manager invokes the client's notification handler. The notification indicates the connection state when the error occurred, and a code that identifies the error. In these cases, the notification handler should call [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa) to end the RAS connection.

The error codes that identify RAS errors are defined in the file raserror.h. The RAS client can use the [**RasGetErrorString**](/windows/desktop/api/Ras/nf-ras-rasgeterrorstringa) function to get a display string describing the error. See [Routing and Remote Access Error Codes](routing-and-remote-access-error-codes.md) for a description of these errors.

 

 




