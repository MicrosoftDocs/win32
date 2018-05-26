---
Description: Lists the structures used with security management APIs.
ms.assetid: 8df25095-a215-464a-abac-39a6ea05f6a3
title: Security Management Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Security Management Structures

This section contains reference pages for the following groups of structures:

-   [LSA Policy Management Structures](#lsa-policy-management-structures)
-   [Attachment Structures](#attachment-structures)
-   [Safer Structures](#safer-structures)

## LSA Policy Management Structures

The following structures are used by the [*Local Security Authority*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-local-security-authority-gly) (LSA) policy management functions.



| Structure                                                                       | Description                                                                                                                                   |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**LSA\_AUTH\_INFORMATION**](/windows/win32/Ntsecapi/ns-ntsecapi-_lsa_auth_information?branch=master)                          | Contains authentication information for a trusted domain.                                                                                     |
| [**LSA\_ENUMERATION\_INFORMATION**](/windows/win32/Ntsecapi/ns-ntsecapi-_lsa_enumeration_information?branch=master)            | Contains a pointer to a [*security identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SID).    |
| [**LSA\_OBJECT\_ATTRIBUTES**](/windows/win32/LsaLookup/ns-lsalookup-_lsa_object_attributes?branch=master)                        | Specifies the attributes of a connection to the [**Policy**](policy-object.md) object.                                                       |
| [**LSA\_REFERENCED\_DOMAIN\_LIST**](/windows/win32/Ntsecapi/ns-lsalookup-_lsa_referenced_domain_list?branch=master)             | Contains information about the domains referenced in a lookup operation.                                                                      |
| [**LSA\_TRANSLATED\_NAME**](/windows/win32/LsaLookup/ns-lsalookup-_lsa_translated_name?branch=master)                            | Contains information about the account identified by a SID.                                                                                   |
| [**LSA\_TRANSLATED\_SID**](/windows/win32/Ntsecapi/ns-ntsecapi-_lsa_translated_sid?branch=master)                              | Contains information about the SID that identifies an account.                                                                                |
| [**LSA\_TRANSLATED\_SID2**](/windows/win32/LsaLookup/ns-lsalookup-_lsa_translated_sid2?branch=master)                            | Contains information about the SID that identifies an account.                                                                                |
| [**LSA\_TRUST\_INFORMATION**](/windows/win32/lsalookup/ns-lsalookup-_lsa_trust_information?branch=master)                        | Identifies a domain.                                                                                                                          |
| [**LSA\_UNICODE\_STRING**](/windows/win32/lsalookup/ns-lsalookup-_lsa_unicode_string?branch=master)                              | Contains a string and its length information.                                                                                                 |
| [**POLICY\_ACCOUNT\_DOMAIN\_INFO**](/windows/win32/LsaLookup/ns-lsalookup-_policy_account_domain_info?branch=master)             | Used to set and query the name and SID of the system's account domain.                                                                        |
| [**POLICY\_AUDIT\_EVENTS\_INFO**](/windows/win32/Ntsecapi/ns-ntsecapi-_policy_audit_events_info?branch=master)                 | Used to set and query the system's auditing rules.                                                                                            |
| [**POLICY\_DNS\_DOMAIN\_INFO**](/windows/win32/LsaLookup/ns-lsalookup-_policy_dns_domain_info?branch=master)                     | Used to set and query Domain Name System (DNS) information about the primary domain associated with a [**Policy**](policy-object.md) object. |
| [**POLICY\_LSA\_SERVER\_ROLE\_INFO**](/windows/win32/Ntsecapi/ns-ntsecapi-_policy_lsa_server_role_info?branch=master)          | Used to set and query the role of an LSA server.                                                                                              |
| [**POLICY\_MODIFICATION\_INFO**](/windows/win32/Ntsecapi/ns-ntsecapi-_policy_modification_info?branch=master)                  | Used to query information about the creation time and last modification of the LSA database.                                                  |
| [**POLICY\_PD\_ACCOUNT\_INFO**](policy-pd-account-info.md)                     | Obsolete. Workstations use the workstation name followed by a $ as the account name.                                                          |
| [**POLICY\_PRIMARY\_DOMAIN\_INFO**](/windows/win32/Ntsecapi/ns-ntsecapi-_policy_primary_domain_info?branch=master)             | Obsolete. Use **PolicyDnsDomainInformation** and the [**POLICY\_DNS\_DOMAIN\_INFO**](/windows/win32/LsaLookup/ns-lsalookup-_policy_dns_domain_info?branch=master) structure instead.           |
| [**TRUSTED\_DOMAIN\_AUTH\_INFORMATION**](/windows/win32/Ntsecapi/ns-ntsecapi-_trusted_domain_auth_information?branch=master)   | Used to retrieve authentication information for a trusted domain.                                                                             |
| [**TRUSTED\_DOMAIN\_FULL\_INFORMATION**](/windows/win32/Ntsecapi/ns-ntsecapi-_trusted_domain_full_information?branch=master)   | Used to retrieve complete information about a trusted domain.                                                                                 |
| [**TRUSTED\_DOMAIN\_INFORMATION\_BASIC**](/windows/win32/Ntsecapi/?branch=master) | Information about a trusted domain. This structure is identical to [**LSA\_TRUST\_INFORMATION**](/windows/win32/lsalookup/ns-lsalookup-_lsa_trust_information?branch=master).                  |
| [**TRUSTED\_DOMAIN\_INFORMATION\_EX**](/windows/win32/Ntsecapi/ns-ntsecapi-_trusted_domain_information_ex?branch=master)       | Used to retrieve extended information about a trusted domain.                                                                                 |
| [**TRUSTED\_DOMAIN\_NAME\_INFO**](/windows/win32/Ntsecapi/ns-ntsecapi-_trusted_domain_name_info?branch=master)                 | Used to query or set the name of a trusted domain.                                                                                            |
| [**TRUSTED\_PASSWORD\_INFO**](/windows/win32/Ntsecapi/ns-ntsecapi-_trusted_password_info?branch=master)                        | Used to query or set the password for a trusted domain.                                                                                       |
| [**TRUSTED\_POSIX\_OFFSET\_INFO**](/windows/win32/Ntsecapi/ns-ntsecapi-_trusted_posix_offset_info?branch=master)               | Used to query or set the value used to generate Posix user and group identifiers.                                                             |



 

The following structure types are obsolete or are reserved for future use:

-   **POLICY\_AUDIT\_FULL\_QUERY\_INFO**
-   **POLICY\_AUDIT\_FULL\_SET\_INFO**
-   **POLICY\_AUDIT\_LOG\_INFO**
-   **POLICY\_DEFAULT\_QUOTA\_INFO**
-   **POLICY\_REPLICA\_SOURCE\_INFO**
-   **TRUSTED\_CONTROLLERS\_INFO**

## Attachment Structures

The following structures are used by the Security Configuration attachment DLLs and their supporting functions. These structures are defined in Scesvc.h.



| Structure                                                        | Description                                                                                                                                     |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCESVC\_CONFIGURATION\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_configuration_info_?branch=master) | Contains configuration information for a service.                                                                                               |
| [**SCESVC\_CONFIGURATION\_LINE**](/windows/win32/Scesvc/ns-scesvc-_scesvc_configuration_line_?branch=master) | Contains information about a line of configuration data.                                                                                        |
| [**SCESVC\_ANALYSIS\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_analysis_info_?branch=master)           | Contains the analysis information.                                                                                                              |
| [**SCESVC\_ANALYSIS\_LINE**](/windows/win32/Scesvc/ns-scesvc-_scesvc_analysis_line_?branch=master)           | Contains the key, value, and value length for a specific line specified by an [**SCESVC\_ANALYSIS\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_analysis_info_?branch=master) structure. |
| [**SCESVC\_CALLBACK\_INFO**](/windows/win32/Scesvc/ns-scesvc-_scesvc_callback_info_?branch=master)           | Contains an opaque database handle and callback function pointers to query, set, and free information.                                          |



 

## Safer Structures

The following structures and enumerated type are used in Safer. They are defined in WinSafer.h.



| Structure                                                                | Description                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SAFER\_CODE\_PROPERTIES**](/windows/win32/WinSafer/ns-winsafer-_safer_code_properties_v2?branch=master)                 | Contains code image information and criteria to be checked on the code image. An array of these structures is passed to the [**SaferIdentifyLevel**](/windows/win32/WinSafer/nf-winsafer-saferidentifylevel?branch=master) function.                                                                  |
| [**SAFER\_IDENTIFICATION\_HEADER**](/windows/win32/WinSafer/ns-winsafer-_safer_identification_header?branch=master)     | Header structure for [**SAFER\_PATHNAME\_IDENTIFICATION**](/windows/win32/WinSafer/ns-winsafer-_safer_pathname_identification?branch=master), [**SAFER\_HASH\_IDENTIFICATION**](/windows/win32/WinSafer/ns-winsafer-_safer_hash_identification?branch=master), and [**SAFER\_URLZONE\_IDENTIFICATION**](/windows/win32/WinSafer/ns-winsafer-_safer_urlzone_identification?branch=master) structures. |
| [**SAFER\_PATHNAME\_IDENTIFICATION**](/windows/win32/WinSafer/ns-winsafer-_safer_pathname_identification?branch=master) | Holds the path name of a code image to be checked.                                                                                                                                                                                                      |
| [**SAFER\_HASH\_IDENTIFICATION**](/windows/win32/WinSafer/ns-winsafer-_safer_hash_identification?branch=master)         | Identifies a hash of the code image to be checked.                                                                                                                                                                                                      |
| [**SAFER\_URLZONE\_IDENTIFICATION**](/windows/win32/WinSafer/ns-winsafer-_safer_urlzone_identification?branch=master)   | Identifies the URL zone of origin of the code image to be checked.                                                                                                                                                                                      |



 

 

 



