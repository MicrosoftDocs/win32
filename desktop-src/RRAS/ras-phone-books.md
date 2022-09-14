---
title: RAS Phone Books
description: Phone books provide a standard way to collect and specify the information that the Remote Access Connection Manager needs to establish a remote connection.
ms.assetid: db6d076c-c683-4e27-ace1-d2c0cd0931f6
keywords:
- Phone books, RAS
ms.topic: article
ms.date: 05/31/2018
---

# RAS Phone Books

Phone books provide a standard way to collect and specify the information that the Remote Access Connection Manager needs to establish a remote connection. Phone books associate entry names with information such as phone numbers, COM ports, and modem settings. Each phone-book entry contains the information needed to establish a RAS connection.

Phone books are stored in phone-book files, which are text files that contain the entry names and associated information. RAS creates a phone-book file called RASPHONE.PBK. The user can use the main **Dial-Up Networking** dialog box to create personal phone-book files. The RAS API does not currently provide support for creating a phone-book file. Some RAS functions, such as the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function, have a parameter that specifies a phone-book file. If the caller does not specify a phone-book file, the function uses the default phone-book file, which is the one selected by the user in the **User Preferences** property sheet of the **Dial-Up Networking** dialog box.

Windows NT 4.0 provides the [**RasPhonebookDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasphonebookdlga) and [**RasEntryDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasentrydlga) functions that display the built-in RAS user interface that enable users to work with phone books and phone-book entries.

**Windows 95:** Dial-up networking stores phone-book entries in the registry rather than in a phone-book file. Windows 95 does not support personal phone-book files or functions that display the built-in RAS dialog boxes.

 

 




