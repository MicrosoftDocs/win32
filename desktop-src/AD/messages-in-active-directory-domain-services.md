---
title: Messages in Active Directory Domain Services
description: Messages in Active Directory Domain Services are functional in Windows 2000 and Windows NT 4.0 with Service Pack 6a (SP6a) and later with DSClient.
ms.assetid: 32a4724b-3182-4521-975c-cef33afee0b2
ms.tgt_platform: multiple
keywords:
- Active Directory Messages AD
ms.topic: article
ms.date: 05/31/2018
---

# Messages in Active Directory Domain Services

Messages in Active Directory Domain Services are functional in Windows 2000 and Windows NT 4.0 with Service Pack 6a (SP6a) and later with DSClient. They are also functional in Windows 98/95 workstations with IE4.01 and later and DSClient. However, if multiselect property pages are launched from the shell, then the [**WM\_ADSPROP\_NOTIFY\_ERROR**](wm-adsprop-notify-error.md) message and its corresponding helper functions, [**ADsPropSendErrorMessage**](/windows/desktop/api/Adsprop/nf-adsprop-adspropsenderrormessage) and [**ADsPropShowErrorDialog**](/windows/desktop/api/Adsprop/nf-adsprop-adspropshowerrordialog) are not functional and will not be displayed. If multiselect property pages are launched within an admin tool, for example, AD Users and Computers, then all messages are functional and available to be displayed within the multiselect property pages.

Active Directory Domain Services use the following messages:

-   [**WM\_ADSPROP\_NOTIFY\_APPLY**](wm-adsprop-notify-apply.md)
-   [**WM\_ADSPROP\_NOTIFY\_CHANGE**](wm-adsprop-notify-change.md)
-   [**WM\_ADSPROP\_NOTIFY\_ERROR**](wm-adsprop-notify-error.md)
-   [**WM\_ADSPROP\_NOTIFY\_EXIT**](wm-adsprop-notify-exit.md)
-   [**WM\_ADSPROP\_NOTIFY\_FOREGROUND**](wm-adsprop-notify-foreground.md)
-   [**WM\_ADSPROP\_NOTIFY\_PAGEHWND**](wm-adsprop-notify-pagehwnd.md)
-   [**WM\_ADSPROP\_NOTIFY\_PAGEINIT**](wm-adsprop-notify-pageinit.md)
-   [**WM\_ADSPROP\_NOTIFY\_SETFOCUS**](wm-adsprop-notify-setfocus.md)
-   [**WM\_ADSPROP\_SHEET\_CREATE**](wm-adsprop-sheet-create.md)
-   [**WM\_DSA\_SHEET\_CLOSE\_NOTIFY**](wm-dsa-sheet-close-notify.md)
-   [**WM\_DSA\_SHEET\_CREATE\_NOTIFY**](wm-dsa-sheet-create-notify.md)

 

 




