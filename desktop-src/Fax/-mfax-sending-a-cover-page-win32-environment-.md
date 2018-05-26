---
Description: This topic describes how to send common and personal cover pages in the Microsoft Win32 environment.
ms.assetid: 40cedde9-291a-426c-beac-1ed51542af09
title: Sending a Cover Page (Win32 Environment)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sending a Cover Page (Win32 Environment)

You can send a personal cover page or a common cover page located on a server with a fax transmission.

To transmit a cover page with a fax, call the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function or the [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) function.

When you call the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function to transmit a fax, you must supply a pointer to a [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure. The structure provides the name of a cover page template file and an indication of whether the file is located locally or on the fax server. The structure can also contain user-supplied information to display on the cover page.

## To send a common cover page

-   Provide a pointer to a [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure when you call the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function.
-   Set the **UseServerCoverPage** member of the [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure equal to **TRUE**.
-   Specify a valid common cover page file in the **CoverpageName** member of the [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure.

## To send a personal cover page

-   Provide a pointer to a [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure when you call the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function.
-   Set the **UseServerCoverPage** member of the [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure equal to **FALSE**.
-   Specify a valid personal cover page file that the fax server can access in the **CoverpageName** member of the [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure.

To determine if the fax server is configured to permit personal cover pages, you can call the [**FaxGetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxgetconfigurationa?branch=master) function.

If your application calls the [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) function to transmit a fax to multiple recipients, the function calls the [**FAX\_RECIPIENT\_CALLBACK**](/windows/previous-versions/Winfax/nc-winfax-pfax_recipient_callbacka?branch=master) function. You must provide a pointer to a [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure when you call **FAX\_RECIPIENT\_CALLBACK** and set the members as outlined previously. The callback function can retrieve user-specified cover page information for each designated fax recipient.

 

 



