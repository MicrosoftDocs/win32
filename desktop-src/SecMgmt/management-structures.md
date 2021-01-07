---
description: Lists the structures used with security management APIs.
ms.assetid: 8df25095-a215-464a-abac-39a6ea05f6a3
title: Security Management Structures
ms.topic: article
ms.date: 05/31/2018
---

# Security Management Structures

This section contains reference pages for the following groups of structures:

-   [LSA Policy Management Structures](#lsa-policy-management-structures)
-   [Attachment Structures](#attachment-structures)
-   [Safer Structures](#safer-structures)

## LSA Policy Management Structures

The following structures are used by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) policy management functions.



| Structure                                                                       | Description                                                                                                                                   |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**LSA\_AUTH\_INFORMATION**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-lsa_auth_information)                          | Contains authentication information for a trusted domain.                                                                                     |
| [**LSA\_ENUMERATION\_INFORMATION**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-lsa_enumeration_information)            | Contains a pointer to a [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID).    |
| [**LSA\_OBJECT\_ATTRIBUTES**](/windows/desktop/api/LsaLookup/ns-lsalookup-lsa_object_attributes)                        | Specifies the attributes of a connection to the [**Policy**](policy-object.md) object.                                                       |
| [**LSA\_REFERENCED\_DOMAIN\_LIST**](/windows/win32/api/lsalookup/ns-lsalookup-lsa_referenced_domain_list)             | Contains information about the domains referenced in a lookup operation.                                                                      |
| [**LSA\_TRANSLATED\_NAME**](/windows/desktop/api/LsaLookup/ns-lsalookup-lsa_translated_name)                            | Contains information about the account identified by a SID.                                                                                   |
| [**LSA\_TRANSLATED\_SID**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-lsa_translated_sid)                              | Contains information about the SID that identifies an account.                                                                                |
| [**LSA\_TRANSLATED\_SID2**](/windows/desktop/api/LsaLookup/ns-lsalookup-lsa_translated_sid2)                            | Contains information about the SID that identifies an account.                                                                                |
| [**LSA\_TRUST\_INFORMATION**](/windows/desktop/api/lsalookup/ns-lsalookup-lsa_trust_information)                        | Identifies a domain.                                                                                                                          |
| [**LSA\_UNICODE\_STRING**](/windows/desktop/api/lsalookup/ns-lsalookup-lsa_unicode_string)                              | Contains a string and its length information.                                                                                                 |
| [**POLICY\_ACCOUNT\_DOMAIN\_INFO**](/windows/desktop/api/LsaLookup/ns-lsalookup-policy_account_domain_info)             | Used to set and query the name and SID of the system's account domain.                                                                        |
| [**POLICY\_AUDIT\_EVENTS\_INFO**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-policy_audit_events_info)                 | Used to set and query the system's auditing rules.                                                                                            |
| [**POLICY\_DNS\_DOMAIN\_INFO**](/windows/desktop/api/LsaLookup/ns-lsalookup-policy_dns_domain_info)                     | Used to set and query Domain Name System (DNS) information about the primary domain associated with a [**Policy**](policy-object.md) object. |
| [**POLICY\_LSA\_SERVER\_ROLE\_INFO**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-policy_lsa_server_role_info)          | Used to set and query the role of an LSA server.                                                                                              |
| [**POLICY\_MODIFICATION\_INFO**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-policy_modification_info)                  | Used to query information about the creation time and last modification of the LSA database.                                                  |
| [**POLICY\_PD\_ACCOUNT\_INFO**](policy-pd-account-info.md)                     | Obsolete. Workstations use the workstation name followed by a $ as the account name.                                                          |
| [**POLICY\_PRIMARY\_DOMAIN\_INFO**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-policy_primary_domain_info)             | Obsolete. Use **PolicyDnsDomainInformation** and the [**POLICY\_DNS\_DOMAIN\_INFO**](/windows/desktop/api/LsaLookup/ns-lsalookup-policy_dns_domain_info) structure instead.           |
| [**TRUSTED\_DOMAIN\_AUTH\_INFORMATION**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-trusted_domain_auth_information)   | Used to retrieve authentication information for a trusted domain.                                                                             |
| [**TRUSTED\_DOMAIN\_FULL\_INFORMATION**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-trusted_domain_full_information)   | Used to retrieve complete information about a trusted domain.                                                                                 |
| [**TRUSTED\_DOMAIN\_INFORMATION\_BASIC**](/previous-versions/windows/desktop/legacy/ms722475(v=vs.85)) | Information about a trusted domain. This structure is identical to [**LSA\_TRUST\_INFORMATION**](/windows/desktop/api/lsalookup/ns-lsalookup-lsa_trust_information).                  |
| [**TRUSTED\_DOMAIN\_INFORMATION\_EX**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-trusted_domain_information_ex)       | Used to retrieve extended information about a trusted domain.                                                                                 |
| [**TRUSTED\_DOMAIN\_NAME\_INFO**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-trusted_domain_name_info)                 | Used to query or set the name of a trusted domain.                                                                                            |
| [**TRUSTED\_PASSWORD\_INFO**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-trusted_password_info)                        | Used to query or set the password for a trusted domain.                                                                                       |
| [**TRUSTED\_POSIX\_OFFSET\_INFO**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-trusted_posix_offset_info)               | Used to query or set the value used to generate Posix user and group identifiers.                                                             |



 

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
| [**SCESVC\_CONFIGURATION\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_configuration_info) | Contains configuration information for a service.                                                                                               |
| [**SCESVC\_CONFIGURATION\_LINE**](/windows/win32/api/scesvc/ns-scesvc-scesvc_configuration_line) | Contains information about a line of configuration data.                                                                                        |
| [**SCESVC\_ANALYSIS\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_analysis_info)           | Contains the analysis information.                                                                                                              |
| [**SCESVC\_ANALYSIS\_LINE**](/windows/win32/api/scesvc/ns-scesvc-scesvc_analysis_line)           | Contains the key, value, and value length for a specific line specified by an [**SCESVC\_ANALYSIS\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_analysis_info) structure. |
| [**SCESVC\_CALLBACK\_INFO**](/windows/win32/api/scesvc/ns-scesvc-scesvc_callback_info)           | Contains an opaque database handle and callback function pointers to query, set, and free information.                                          |



 

## Safer Structures

The following structures and enumerated type are used in Safer. They are defined in WinSafer.h.



| Structure                                                                | Description                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SAFER\_CODE\_PROPERTIES**](/windows/desktop/api/WinSafer/ns-winsafer-safer_code_properties_v2)                 | Contains code image information and criteria to be checked on the code image. An array of these structures is passed to the [**SaferIdentifyLevel**](/windows/desktop/api/WinSafer/nf-winsafer-saferidentifylevel) function.                                                                  |
| [**SAFER\_IDENTIFICATION\_HEADER**](/windows/desktop/api/WinSafer/ns-winsafer-safer_identification_header)     | Header structure for [**SAFER\_PATHNAME\_IDENTIFICATION**](/windows/desktop/api/WinSafer/ns-winsafer-safer_pathname_identification), [**SAFER\_HASH\_IDENTIFICATION**](/windows/desktop/api/WinSafer/ns-winsafer-safer_hash_identification), and [**SAFER\_URLZONE\_IDENTIFICATION**](/windows/desktop/api/WinSafer/ns-winsafer-safer_urlzone_identification) structures. |
| [**SAFER\_PATHNAME\_IDENTIFICATION**](/windows/desktop/api/WinSafer/ns-winsafer-safer_pathname_identification) | Holds the path name of a code image to be checked.                                                                                                                                                                                                      |
| [**SAFER\_HASH\_IDENTIFICATION**](/windows/desktop/api/WinSafer/ns-winsafer-safer_hash_identification)         | Identifies a hash of the code image to be checked.                                                                                                                                                                                                      |
| [**SAFER\_URLZONE\_IDENTIFICATION**](/windows/desktop/api/WinSafer/ns-winsafer-safer_urlzone_identification)   | Identifies the URL zone of origin of the code image to be checked.                                                                                                                                                                                      |



 

 

 
