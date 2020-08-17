---
title: Phone-Book Files and Connection Information
description: A RasDial call must specify the information that the Remote Access Connection Manager needs to establish the connection.
ms.assetid: bc3885a4-3c1e-47bc-b622-072b33ac3b51
ms.topic: article
ms.date: 05/31/2018
---

# Phone-Book Files and Connection Information

A [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call must specify the information that the Remote Access Connection Manager needs to establish the connection. Typically, the **RasDial** call provides the connection information by specifying a phone-book entry. The connection information in a phone-book entry includes phone numbers, bps rates, [user authentication information](user-authentication-information.md), and [other connection information](other-connection-information.md).

A RAS client uses the parameters of the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function to specify a phone-book file and an entry in that file. The *lpszPhonebookPath* parameter can specify the name of a phone-book file, or it can be **NULL** to indicate that the default phone-book file should be used. The *lpRasDialParams* parameter points to a [**RASDIALPARAMS**](/previous-versions/windows/desktop/legacy/aa377238(v=vs.85)) structure that specifies the name of the phone-book entry to use.

To display a list of phone-book entries from which the user can select a connection, a RAS client can call the [**RasEnumEntries**](/windows/desktop/api/Ras/nf-ras-rasenumentriesa) function to enumerate the entries in a phone-book file.

To make a connection without using a phone-book entry, the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call can specify an empty string for the **szEntryName** member of the [**RASDIALPARAMS**](/previous-versions/windows/desktop/legacy/aa377238(v=vs.85)) structure. The **RASDIALPARAMS.szPhoneNumber** member must contain the number to call. In this case, the Remote Access Connection Manager uses the first available modem port and default values for all other settings.

 

 