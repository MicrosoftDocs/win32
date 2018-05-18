---
Description: 'This topic lists the access rights users must have to successfully call certain fax client functions in the Microsoft Win32 environment.'
ms.assetid: 'ed45f799-f287-475f-9a58-313d66761ac6'
title: Required Fax Access Rights by Function
---

# Required Fax Access Rights by Function

The following table lists the access rights users must have to successfully call certain fax client functions in the Microsoft Win32 environment.



| Required access right | Function                                                                                                                                                                                                                                                                                                                                           |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FAX\_CONFIG\_QUERY    | [**FaxEnumGlobalRoutingInfo**](-mfax-faxenumglobalroutinginfo.md), [**FaxGetConfiguration**](-mfax-faxgetconfiguration.md), [**FaxGetLoggingCategories**](-mfax-faxgetloggingcategories.md)                                                                                                                                                     |
| FAX\_CONFIG\_SET      | [**FaxSetConfiguration**](-mfax-faxsetconfiguration.md), [**FaxEnumGlobalRoutingInfo**](-mfax-faxenumglobalroutinginfo.md), [**FaxGetLoggingCategories**](-mfax-faxgetloggingcategories.md)                                                                                                                                                     |
| FAX\_JOB\_QUERY       | [**FaxEnumJobs**](-mfax-faxenumjobs.md), [**FaxGetJob**](-mfax-faxgetjob.md), [**FaxGetPageData**](-mfax-faxgetpagedata.md)                                                                                                                                                                                                                     |
| FAX\_JOB\_SET         | [**FaxAbort**](-mfax-faxabort.md), [**FaxSetJob**](-mfax-faxsetjob.md)                                                                                                                                                                                                                                                                           |
| FAX\_JOB\_SUBMIT      | [**FaxSendDocument**](-mfax-faxsenddocument.md), [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md)                                                                                                                                                                                                                         |
| FAX\_PORT\_QUERY      | [**FaxClose**](-mfax-faxclose.md), [**FaxEnumPorts**](-mfax-faxenumports.md)\*, [**FaxEnumRoutingMethods**](-mfax-faxenumroutingmethods.md), [**FaxGetDeviceStatus**](-mfax-faxgetdevicestatus.md)\*, [**FaxGetPort**](-mfax-faxgetport.md)\*, [**FaxGetRoutingInfo**](-mfax-faxgetroutinginfo.md), [**FaxOpenPort**](-mfax-faxopenport.md) |
| FAX\_PORT\_SET        | [**FaxEnableRoutingMethod**](-mfax-faxenableroutingmethod.md), [**FaxSetPort**](-mfax-faxsetport.md)\*, [**FaxGetRoutingInfo**](-mfax-faxgetroutinginfo.md)                                                                                                                                                                                     |



 

\*This function also requires a specific fax port access level. For more information, see [Fax Port Access Levels](-mfax-fax-port-access-levels.md).

Note that the FAX\_JOB\_MANAGE access level also permits a user to call the [**FaxAbort**](-mfax-faxabort.md) function and the [**FaxSetJob**](-mfax-faxsetjob.md) function. For additional information, see [Managing Fax Jobs](-mfax-managing-fax-jobs.md).

 

 



