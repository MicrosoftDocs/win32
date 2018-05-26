---
Description: This topic lists the access rights users must have to successfully call certain fax client functions in the Microsoft Win32 environment.
ms.assetid: ed45f799-f287-475f-9a58-313d66761ac6
title: Required Fax Access Rights by Function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Required Fax Access Rights by Function

The following table lists the access rights users must have to successfully call certain fax client functions in the Microsoft Win32 environment.



| Required access right | Function                                                                                                                                                                                                                                                                                                                                           |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FAX\_CONFIG\_QUERY    | [**FaxEnumGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxenumglobalroutinginfoa?branch=master), [**FaxGetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxgetconfigurationa?branch=master), [**FaxGetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxgetloggingcategoriesa?branch=master)                                                                                                                                                     |
| FAX\_CONFIG\_SET      | [**FaxSetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxsetconfigurationa?branch=master), [**FaxEnumGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxenumglobalroutinginfoa?branch=master), [**FaxGetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxgetloggingcategoriesa?branch=master)                                                                                                                                                     |
| FAX\_JOB\_QUERY       | [**FaxEnumJobs**](/windows/previous-versions/Winfax/nf-winfax-faxenumjobsa?branch=master), [**FaxGetJob**](/windows/previous-versions/Winfax/nf-winfax-faxgetjoba?branch=master), [**FaxGetPageData**](/windows/previous-versions/Winfax/nc-winfax-pfaxgetpagedata?branch=master)                                                                                                                                                                                                                     |
| FAX\_JOB\_SET         | [**FaxAbort**](/windows/previous-versions/Winfax/nc-winfax-pfaxabort?branch=master), [**FaxSetJob**](/windows/previous-versions/Winfax/nf-winfax-faxsetjoba?branch=master)                                                                                                                                                                                                                                                                           |
| FAX\_JOB\_SUBMIT      | [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master), [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master)                                                                                                                                                                                                                         |
| FAX\_PORT\_QUERY      | [**FaxClose**](/windows/previous-versions/Winfax/nc-winfax-pfaxclose?branch=master), [**FaxEnumPorts**](/windows/previous-versions/Winfax/nf-winfax-faxenumportsa?branch=master)\*, [**FaxEnumRoutingMethods**](/windows/previous-versions/Winfax/nf-winfax-faxenumroutingmethodsa?branch=master), [**FaxGetDeviceStatus**](/windows/previous-versions/Winfax/nf-winfax-faxgetdevicestatusa?branch=master)\*, [**FaxGetPort**](/windows/previous-versions/Winfax/nf-winfax-faxgetporta?branch=master)\*, [**FaxGetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxgetroutinginfoa?branch=master), [**FaxOpenPort**](/windows/previous-versions/Winfax/nc-winfax-pfaxopenport?branch=master) |
| FAX\_PORT\_SET        | [**FaxEnableRoutingMethod**](/windows/previous-versions/Winfax/nf-winfax-faxenableroutingmethoda?branch=master), [**FaxSetPort**](/windows/previous-versions/Winfax/nf-winfax-faxsetporta?branch=master)\*, [**FaxGetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxgetroutinginfoa?branch=master)                                                                                                                                                                                     |



 

\*This function also requires a specific fax port access level. For more information, see [Fax Port Access Levels](-mfax-fax-port-access-levels.md).

Note that the FAX\_JOB\_MANAGE access level also permits a user to call the [**FaxAbort**](/windows/previous-versions/Winfax/nc-winfax-pfaxabort?branch=master) function and the [**FaxSetJob**](/windows/previous-versions/Winfax/nf-winfax-faxsetjoba?branch=master) function. For additional information, see [Managing Fax Jobs](-mfax-managing-fax-jobs.md).

 

 



