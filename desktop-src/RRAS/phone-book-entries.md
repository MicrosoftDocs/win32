---
title: Phone-Book Entries
description: Phone-book entries contain the information necessary to establish a RAS connection. A user or administrator can use the Dial-Up Networking dialog box to create, edit, and dial phone-book entries.
ms.assetid: '971d7020-f9fd-42d1-97c3-79ad6eba6964'
---

# Phone-Book Entries

Phone-book entries contain the information necessary to establish a RAS connection. A user or administrator can use the **Dial-Up Networking** dialog box to create, edit, and dial phone-book entries.

Beginning with Windows NT Server 4.0, the system supports the functions described for Windows 95, as well as a number of additional functions that an application can use to work with phone books and phone-book entries.

The [**RasEntryDlg**](rasentrydlg.md) function displays a property sheet that enables the user to create, edit, or copy phone-book entries. The [**RasCreatePhonebookEntry**](rascreatephonebookentry.md) and [**RasEditPhonebookEntry**](raseditphonebookentry.md) functions call the **RasEntryDlg** function. You can use the [**RasRenameEntry**](rasrenameentry.md) function to rename a phone-book entry, or the [**RasDeleteEntry**](rasdeleteentry.md) to delete an entry. The [**RasValidateEntryName**](rasvalidateentryname.md) determines whether a specified string has the correct format to be used as an entry name.

You can use the [**RasGetEntryProperties**](rasgetentryproperties.md) and [**RasSetEntryProperties**](rassetentryproperties.md) to get and set additional information about a phone-book entry. These functions use a [**RASENTRY**](rasentry-str.md) structure.

The [**RasGetCredentials**](rasgetcredentials.md) and [**RasSetCredentials**](rassetcredentials.md) functions get and set the user credentials associated with a specified RAS phone-book entry. These functions use a [**RASCREDENTIALS**](rascredentials-str.md) structure.

The [**RasGetCountryInfo**](rasgetcountryinfo.md) function retrieves country/region-specific dialing information from the Windows Telephony list of countries. **RasGetCountryInfo** uses the [**RASCTRYINFO**](rasctryinfo-str.md) structure.

**Windows 95:  ** Supports a limited set of the functions for working with phone-book entries. You can use the [**RasCreatePhonebookEntry**](rascreatephonebookentry.md) and [**RasEditPhonebookEntry**](raseditphonebookentry.md) functions to create or edit a phone-book entry. These functions display a dialog box in which the user can specify information about the phone-book entry. You can use the [**RasGetEntryDialParams**](rasgetentrydialparams.md) and [**RasSetEntryDialParams**](rassetentrydialparams.md) functions to set or retrieve the connection parameters for a phone-book entry. The [**RasEnumEntries**](rasenumentries.md) function retrieves an array of [**RASENTRYNAME**](rasentryname-str.md) structures that contain the phone-book entry names.

 

 




