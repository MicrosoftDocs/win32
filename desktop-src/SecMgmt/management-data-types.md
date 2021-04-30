---
description: Lists the data types used by the Security Configuration attachment DLLs and their supporting functions.
ms.assetid: 1d3bdf0d-320c-4b25-9e9b-fda134876979
title: Security Management Data Types
ms.topic: article
ms.date: 05/31/2018
---

# Security Management Data Types

The security management data types include the following:

-   [Attachment Data Types](#attachment-data-types)
-   [LSA Policy Data Types](#lsa-policy-data-types)

## Attachment Data Types

The following data types are used by the Security Configuration attachment DLLs and their supporting functions.



| Data type                                                    | Description                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCE\_ENUMERATION\_CONTEXT**](sce-enumeration-context.md) | Used by the [**PFSCE\_QUERY\_INFO**](/windows/win32/api/scesvc/nc-scesvc-pfsce_query_info) function to navigate through the security database.                                                                                                                                              |
| [**SCE\_HANDLE**](sce-handle.md)                            | Used by [**PFSCE\_QUERY\_INFO**](/windows/win32/api/scesvc/nc-scesvc-pfsce_query_info) and [**PFSCE\_SET\_INFO**](/windows/win32/api/scesvc/nc-scesvc-pfsce_set_info) to pass information between the attachment and the security database.                                                                                 |
| [**SCESTATUS**](scestatus.md)                               | Data type is used by the Security Configuration tool set API to return information about the results of a function call.                                                                                                                                    |
| [**SCESVC\_HANDLE**](scesvc-handle.md)                      | Used by methods of the [**ISceSvcAttachmentData**](/windows/desktop/api/Scesvc/nn-scesvc-iscesvcattachmentdata) and [**ISceSvcAttachmentPersistInfo**](/windows/desktop/api/Scesvc/nn-scesvc-iscesvcattachmentpersistinfo) interfaces to pass information between the Security Configuration snap-in and the snap-in extension. |
| [**SCESVC\_INFO\_TYPE**](/windows/desktop/api/Scesvc/ne-scesvc-scesvc_info_type)               | Enumeration is used by [**PFSCE\_QUERY\_INFO**](/windows/win32/api/scesvc/nc-scesvc-pfsce_query_info) and [**PFSCE\_SET\_INFO**](/windows/win32/api/scesvc/nc-scesvc-pfsce_set_info) to indicate the type of information requested from or passed to the security database.                                                 |



 

## LSA Policy Data Types

The following data types are used by the LSA policy management functions.



| Data type                                                  | Description                                                               |
|------------------------------------------------------------|---------------------------------------------------------------------------|
| [**LSA\_ENUMERATION\_HANDLE**](lsa-enumeration-handle.md) | Used to track enumerations in which multiple function calls are required. |
| [**LSA\_HANDLE**](lsa-handle.md)                          | Handle to a [**Policy**](policy-object.md) object.                       |



 

 

 
