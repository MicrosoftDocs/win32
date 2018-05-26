---
title: Other Connection Information
description: The members of the RASDIALPARAMS structure can also specify the following connection information.
ms.assetid: 95a8dd78-e424-4d0b-899a-69deb9e1b9cd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Other Connection Information

The members of the [**RASDIALPARAMS**](/windows/win32/Ras/?branch=master) structure can also specify the following connection information.

-   A phone number to override the number in the phone-book entry.
-   A [callback](callback-connections.md) phone number that the remote server can call back to establish the connection.
-   The name of the remote network domain on which the authentication is to occur.

For the callback number and the domain, the [**RASDIALPARAMS**](/windows/win32/Ras/?branch=master) members can either indicate that RAS should use the information in the phone-book entry, or it can provide information that overrides the phone-book data.

A RAS client can use the *lpRasDialExtensions* parameter of the [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) function to control whether RAS uses a phone number prefix or suffix specified in a phone-book entry.

 

 




