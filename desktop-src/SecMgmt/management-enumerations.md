---
Description: Lists the enumerations used by the LSA policy management functions.
ms.assetid: f4fd2a61-61bc-44d2-b01f-3ca07699bcb8
title: Security Management Enumerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Security Management Enumerations

The security management enumerations include the following:

-   [LSA Policy Enumerations](#lsa-policy-enumerations)
-   [Safer Enumerations](#safer-enumerations)

## LSA Policy Enumerations

The following enumeration types are used by the LSA policy management functions.



| Enumeration                                                                               | Description                                                                                                                           |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**POLICY\_AUDIT\_EVENT\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-_policy_audit_event_type?branch=master)                             | Defines the types of events the system can audit.                                                                                     |
| [**POLICY\_INFORMATION\_CLASS**](/windows/win32/Ntsecapi/ne-ntsecapi-_policy_information_class?branch=master)                            | Defines the types of information that can be set or queried for a [**Policy**](policy-object.md) object.                             |
| [**POLICY\_LSA\_SERVER\_ROLE**](/windows/win32/Ntsecapi/ne-ntsecapi-_policy_lsa_server_role?branch=master)                               | Indicate the role of an LSA server.                                                                                                   |
| [**POLICY\_NOTIFICATION\_INFORMATION\_CLASS**](/windows/win32/Ntsecapi/ne-ntsecapi-_policy_notification_information_class?branch=master) | Defines the types of policy information and policy domain information for which your application can request notification of changes. |
| [**POLICY\_SERVER\_ENABLE\_STATE**](/windows/win32/Ntsecapi/ne-ntsecapi-_policy_server_enable_state?branch=master)                       | Represents the state of the LSA server, that is, whether it is enabled or disabled.                                                   |
| [**TRUSTED\_INFORMATION\_CLASS**](/windows/win32/Ntsecapi/ne-ntsecapi-_trusted_information_class?branch=master)                          | Defines the types of information that can be set or queried for a trusted domain.                                                     |



 

## Safer Enumerations

[Safer](safer.md) uses the following enumerated types.



| Name                                                               | Description                                                                                                                                                                                      |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SAFER\_IDENTIFICATION\_TYPES**](/windows/win32/WinSafer/ne-winsafer-_safer_identification_types?branch=master) | Enumeration type that defines the possible types of identification rule structures that can be identified by the [**SAFER\_IDENTIFICATION\_HEADER**](/windows/win32/WinSafer/ns-winsafer-_safer_identification_header?branch=master) structure. |
| [**SAFER\_OBJECT\_INFO\_CLASS**](/windows/win32/WinSafer/ne-winsafer-_safer_object_info_class?branch=master)      | Enumeration type that defines the type of information requested about a Safer object.                                                                                                            |
| [**SAFER\_POLICY\_INFO\_CLASS**](/windows/win32/WinSafer/ne-winsafer-_safer_policy_info_class?branch=master)      | Enumeration type that defines the ways in which a policy may be queried.                                                                                                                         |



 

 

 



