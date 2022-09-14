---
title: Phone-Book Entries
description: Phone-book entries contain the information necessary to establish a RAS connection. A user or administrator can use the Dial-Up Networking dialog box to create, edit, and dial phone-book entries.
ms.assetid: 971d7020-f9fd-42d1-97c3-79ad6eba6964
ms.topic: article
ms.date: 05/31/2018
---

# Phone-Book Entries

Phone-book entries contain the information necessary to establish a RAS connection. A user or administrator can use the **Dial-Up Networking** dialog box to create, edit, and dial phone-book entries.

Beginning with Windows NT Server 4.0, the system supports the functions described for Windows 95, as well as a number of additional functions that an application can use to work with phone books and phone-book entries.

The [**RasEntryDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasentrydlga) function displays a property sheet that enables the user to create, edit, or copy phone-book entries. The [**RasCreatePhonebookEntry**](/windows/desktop/api/Ras/nf-ras-rascreatephonebookentrya) and [**RasEditPhonebookEntry**](/windows/desktop/api/Ras/nf-ras-raseditphonebookentrya) functions call the **RasEntryDlg** function. You can use the [**RasRenameEntry**](/windows/desktop/api/Ras/nf-ras-rasrenameentrya) function to rename a phone-book entry, or the [**RasDeleteEntry**](/windows/desktop/api/Ras/nf-ras-rasdeleteentrya) to delete an entry. The [**RasValidateEntryName**](/windows/desktop/api/Ras/nf-ras-rasvalidateentrynamea) determines whether a specified string has the correct format to be used as an entry name.

You can use the [**RasGetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rasgetentrypropertiesa) and [**RasSetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rassetentrypropertiesa) to get and set additional information about a phone-book entry. These functions use a [**RASENTRY**](/previous-versions/windows/desktop/legacy/aa377274(v=vs.85)) structure.

The [**RasGetCredentials**](/windows/desktop/api/Ras/nf-ras-rasgetcredentialsa) and [**RasSetCredentials**](/windows/desktop/api/Ras/nf-ras-rassetcredentialsa) functions get and set the user credentials associated with a specified RAS phone-book entry. These functions use a [**RASCREDENTIALS**](/previous-versions/windows/desktop/legacy/aa376730(v=vs.85)) structure.

The [**RasGetCountryInfo**](/windows/desktop/api/Ras/nf-ras-rasgetcountryinfoa) function retrieves country/region-specific dialing information from the Windows Telephony list of countries. **RasGetCountryInfo** uses the [**RASCTRYINFO**](/previous-versions/windows/desktop/legacy/aa376731(v=vs.85)) structure.

**Windows 95:  ** Supports a limited set of the functions for working with phone-book entries. You can use the [**RasCreatePhonebookEntry**](/windows/desktop/api/Ras/nf-ras-rascreatephonebookentrya) and [**RasEditPhonebookEntry**](/windows/desktop/api/Ras/nf-ras-raseditphonebookentrya) functions to create or edit a phone-book entry. These functions display a dialog box in which the user can specify information about the phone-book entry. You can use the [**RasGetEntryDialParams**](/windows/desktop/api/Ras/nf-ras-rasgetentrydialparamsa) and [**RasSetEntryDialParams**](/windows/desktop/api/Ras/nf-ras-rassetentrydialparamsa) functions to set or retrieve the connection parameters for a phone-book entry. The [**RasEnumEntries**](/windows/desktop/api/Ras/nf-ras-rasenumentriesa) function retrieves an array of [**RASENTRYNAME**](/previous-versions/windows/desktop/legacy/aa377267(v=vs.85)) structures that contain the phone-book entry names.

 

 