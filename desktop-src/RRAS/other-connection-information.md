---
title: Other Connection Information
description: The members of the RASDIALPARAMS structure can also specify the following connection information.
ms.assetid: 95a8dd78-e424-4d0b-899a-69deb9e1b9cd
ms.topic: article
ms.date: 05/31/2018
---

# Other Connection Information

The members of the [**RASDIALPARAMS**](/previous-versions/windows/desktop/legacy/aa377238(v=vs.85)) structure can also specify the following connection information.

-   A phone number to override the number in the phone-book entry.
-   A [callback](callback-connections.md) phone number that the remote server can call back to establish the connection.
-   The name of the remote network domain on which the authentication is to occur.

For the callback number and the domain, the [**RASDIALPARAMS**](/previous-versions/windows/desktop/legacy/aa377238(v=vs.85)) members can either indicate that RAS should use the information in the phone-book entry, or it can provide information that overrides the phone-book data.

A RAS client can use the *lpRasDialExtensions* parameter of the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function to control whether RAS uses a phone number prefix or suffix specified in a phone-book entry.

 

 