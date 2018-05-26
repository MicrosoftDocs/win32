---
title: Phone-Book Entries
description: Phone-book entries contain the information necessary to establish a RAS connection. A user or administrator can use the Dial-Up Networking dialog box to create, edit, and dial phone-book entries.
ms.assetid: 971d7020-f9fd-42d1-97c3-79ad6eba6964
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Phone-Book Entries

Phone-book entries contain the information necessary to establish a RAS connection. A user or administrator can use the **Dial-Up Networking** dialog box to create, edit, and dial phone-book entries.

Beginning with Windows NT Server 4.0, the system supports the functions described for Windows 95, as well as a number of additional functions that an application can use to work with phone books and phone-book entries.

The [**RasEntryDlg**](/windows/win32/Rasdlg/nf-rasdlg-rasentrydlga?branch=master) function displays a property sheet that enables the user to create, edit, or copy phone-book entries. The [**RasCreatePhonebookEntry**](/windows/win32/Ras/nf-ras-rascreatephonebookentrya?branch=master) and [**RasEditPhonebookEntry**](/windows/win32/Ras/nf-ras-raseditphonebookentrya?branch=master) functions call the **RasEntryDlg** function. You can use the [**RasRenameEntry**](/windows/win32/Ras/nf-ras-rasrenameentrya?branch=master) function to rename a phone-book entry, or the [**RasDeleteEntry**](/windows/win32/Ras/nf-ras-rasdeleteentrya?branch=master) to delete an entry. The [**RasValidateEntryName**](/windows/win32/Ras/nf-ras-rasvalidateentrynamea?branch=master) determines whether a specified string has the correct format to be used as an entry name.

You can use the [**RasGetEntryProperties**](/windows/win32/Ras/nf-ras-rasgetentrypropertiesa?branch=master) and [**RasSetEntryProperties**](/windows/win32/Ras/nf-ras-rassetentrypropertiesa?branch=master) to get and set additional information about a phone-book entry. These functions use a [**RASENTRY**](/windows/win32/Ras/?branch=master) structure.

The [**RasGetCredentials**](/windows/win32/Ras/nf-ras-rasgetcredentialsa?branch=master) and [**RasSetCredentials**](/windows/win32/Ras/nf-ras-rassetcredentialsa?branch=master) functions get and set the user credentials associated with a specified RAS phone-book entry. These functions use a [**RASCREDENTIALS**](/windows/win32/Ras/?branch=master) structure.

The [**RasGetCountryInfo**](/windows/win32/Ras/nf-ras-rasgetcountryinfoa?branch=master) function retrieves country/region-specific dialing information from the Windows Telephony list of countries. **RasGetCountryInfo** uses the [**RASCTRYINFO**](/windows/win32/Ras/?branch=master) structure.

**Windows 95:  ** Supports a limited set of the functions for working with phone-book entries. You can use the [**RasCreatePhonebookEntry**](/windows/win32/Ras/nf-ras-rascreatephonebookentrya?branch=master) and [**RasEditPhonebookEntry**](/windows/win32/Ras/nf-ras-raseditphonebookentrya?branch=master) functions to create or edit a phone-book entry. These functions display a dialog box in which the user can specify information about the phone-book entry. You can use the [**RasGetEntryDialParams**](/windows/win32/Ras/nf-ras-rasgetentrydialparamsa?branch=master) and [**RasSetEntryDialParams**](/windows/win32/Ras/nf-ras-rassetentrydialparamsa?branch=master) functions to set or retrieve the connection parameters for a phone-book entry. The [**RasEnumEntries**](/windows/win32/Ras/nf-ras-rasenumentriesa?branch=master) function retrieves an array of [**RASENTRYNAME**](/windows/win32/Ras/?branch=master) structures that contain the phone-book entry names.

 

 




