---
Description: This topic lists the access rights users must have to successfully call certain fax client functions in the Microsoft Win32 environment.
ms.assetid: ed45f799-f287-475f-9a58-313d66761ac6
title: Required Fax Access Rights by Function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Required Fax Access Rights by Function

The following table lists the access rights users must have to successfully call certain fax client functions in the Microsoft Win32 environment.



| Required access right | Function                                                                                                                                                                                                                                                                                                                                           |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FAX\_CONFIG\_QUERY    | [**FaxEnumGlobalRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumglobalroutinginfoa), [**FaxGetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetconfigurationa), [**FaxGetLoggingCategories**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetloggingcategoriesa)                                                                                                                                                     |
| FAX\_CONFIG\_SET      | [**FaxSetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetconfigurationa), [**FaxEnumGlobalRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumglobalroutinginfoa), [**FaxGetLoggingCategories**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetloggingcategoriesa)                                                                                                                                                     |
| FAX\_JOB\_QUERY       | [**FaxEnumJobs**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumjobsa), [**FaxGetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetjoba), [**FaxGetPageData**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxgetpagedata)                                                                                                                                                                                                                     |
| FAX\_JOB\_SET         | [**FaxAbort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxabort), [**FaxSetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetjoba)                                                                                                                                                                                                                                                                           |
| FAX\_JOB\_SUBMIT      | [**FaxSendDocument**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumenta), [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta)                                                                                                                                                                                                                         |
| FAX\_PORT\_QUERY      | [**FaxClose**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxclose), [**FaxEnumPorts**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumportsa)\*, [**FaxEnumRoutingMethods**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumroutingmethodsa), [**FaxGetDeviceStatus**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetdevicestatusa)\*, [**FaxGetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetporta)\*, [**FaxGetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetroutinginfoa), [**FaxOpenPort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxopenport) |
| FAX\_PORT\_SET        | [**FaxEnableRoutingMethod**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenableroutingmethoda), [**FaxSetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetporta)\*, [**FaxGetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetroutinginfoa)                                                                                                                                                                                     |



 

\*This function also requires a specific fax port access level. For more information, see [Fax Port Access Levels](-mfax-fax-port-access-levels.md).

Note that the FAX\_JOB\_MANAGE access level also permits a user to call the [**FaxAbort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxabort) function and the [**FaxSetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetjoba) function. For additional information, see [Managing Fax Jobs](-mfax-managing-fax-jobs.md).

 

 



