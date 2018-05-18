---
Description: 'Lists the structures used with security management APIs.'
ms.assetid: '8df25095-a215-464a-abac-39a6ea05f6a3'
title: Security Management Structures
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
| [**LSA\_AUTH\_INFORMATION**](lsa-auth-information.md)                          | Contains authentication information for a trusted domain.                                                                                     |
| [**LSA\_ENUMERATION\_INFORMATION**](lsa-enumeration-information.md)            | Contains a pointer to a [*security identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SID).    |
| [**LSA\_OBJECT\_ATTRIBUTES**](lsa-object-attributes.md)                        | Specifies the attributes of a connection to the [**Policy**](policy-object.md) object.                                                       |
| [**LSA\_REFERENCED\_DOMAIN\_LIST**](lsa-referenced-domain-list.md)             | Contains information about the domains referenced in a lookup operation.                                                                      |
| [**LSA\_TRANSLATED\_NAME**](lsa-translated-name.md)                            | Contains information about the account identified by a SID.                                                                                   |
| [**LSA\_TRANSLATED\_SID**](lsa-translated-sid.md)                              | Contains information about the SID that identifies an account.                                                                                |
| [**LSA\_TRANSLATED\_SID2**](lsa-translated-sid2.md)                            | Contains information about the SID that identifies an account.                                                                                |
| [**LSA\_TRUST\_INFORMATION**](lsa-trust-information.md)                        | Identifies a domain.                                                                                                                          |
| [**LSA\_UNICODE\_STRING**](lsa-unicode-string.md)                              | Contains a string and its length information.                                                                                                 |
| [**POLICY\_ACCOUNT\_DOMAIN\_INFO**](policy-account-domain-info.md)             | Used to set and query the name and SID of the system's account domain.                                                                        |
| [**POLICY\_AUDIT\_EVENTS\_INFO**](policy-audit-events-info.md)                 | Used to set and query the system's auditing rules.                                                                                            |
| [**POLICY\_DNS\_DOMAIN\_INFO**](policy-dns-domain-info.md)                     | Used to set and query Domain Name System (DNS) information about the primary domain associated with a [**Policy**](policy-object.md) object. |
| [**POLICY\_LSA\_SERVER\_ROLE\_INFO**](policy-lsa-server-role-info.md)          | Used to set and query the role of an LSA server.                                                                                              |
| [**POLICY\_MODIFICATION\_INFO**](policy-modification-info.md)                  | Used to query information about the creation time and last modification of the LSA database.                                                  |
| [**POLICY\_PD\_ACCOUNT\_INFO**](policy-pd-account-info.md)                     | Obsolete. Workstations use the workstation name followed by a $ as the account name.                                                          |
| [**POLICY\_PRIMARY\_DOMAIN\_INFO**](policy-primary-domain-info.md)             | Obsolete. Use **PolicyDnsDomainInformation** and the [**POLICY\_DNS\_DOMAIN\_INFO**](policy-dns-domain-info.md) structure instead.           |
| [**TRUSTED\_DOMAIN\_AUTH\_INFORMATION**](trusted-domain-auth-information.md)   | Used to retrieve authentication information for a trusted domain.                                                                             |
| [**TRUSTED\_DOMAIN\_FULL\_INFORMATION**](trusted-domain-full-information.md)   | Used to retrieve complete information about a trusted domain.                                                                                 |
| [**TRUSTED\_DOMAIN\_INFORMATION\_BASIC**](trusted-domain-information-basic.md) | Information about a trusted domain. This structure is identical to [**LSA\_TRUST\_INFORMATION**](lsa-trust-information.md).                  |
| [**TRUSTED\_DOMAIN\_INFORMATION\_EX**](trusted-domain-information-ex.md)       | Used to retrieve extended information about a trusted domain.                                                                                 |
| [**TRUSTED\_DOMAIN\_NAME\_INFO**](trusted-domain-name-info.md)                 | Used to query or set the name of a trusted domain.                                                                                            |
| [**TRUSTED\_PASSWORD\_INFO**](trusted-password-info.md)                        | Used to query or set the password for a trusted domain.                                                                                       |
| [**TRUSTED\_POSIX\_OFFSET\_INFO**](trusted-posix-offset-info.md)               | Used to query or set the value used to generate Posix user and group identifiers.                                                             |



 

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
| [**SCESVC\_CONFIGURATION\_INFO**](scesvc-configuration-info.md) | Contains configuration information for a service.                                                                                               |
| [**SCESVC\_CONFIGURATION\_LINE**](scesvc-configuration-line.md) | Contains information about a line of configuration data.                                                                                        |
| [**SCESVC\_ANALYSIS\_INFO**](scesvc-analysis-info.md)           | Contains the analysis information.                                                                                                              |
| [**SCESVC\_ANALYSIS\_LINE**](scesvc-analysis-line.md)           | Contains the key, value, and value length for a specific line specified by an [**SCESVC\_ANALYSIS\_INFO**](scesvc-analysis-info.md) structure. |
| [**SCESVC\_CALLBACK\_INFO**](scesvc-callback-info.md)           | Contains an opaque database handle and callback function pointers to query, set, and free information.                                          |



 

## Safer Structures

The following structures and enumerated type are used in Safer. They are defined in WinSafer.h.



| Structure                                                                | Description                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SAFER\_CODE\_PROPERTIES**](safer-code-properties.md)                 | Contains code image information and criteria to be checked on the code image. An array of these structures is passed to the [**SaferIdentifyLevel**](saferidentifylevel.md) function.                                                                  |
| [**SAFER\_IDENTIFICATION\_HEADER**](safer-identification-header.md)     | Header structure for [**SAFER\_PATHNAME\_IDENTIFICATION**](safer-pathname-identification.md), [**SAFER\_HASH\_IDENTIFICATION**](safer-hash-identification.md), and [**SAFER\_URLZONE\_IDENTIFICATION**](safer-urlzone-identification.md) structures. |
| [**SAFER\_PATHNAME\_IDENTIFICATION**](safer-pathname-identification.md) | Holds the path name of a code image to be checked.                                                                                                                                                                                                      |
| [**SAFER\_HASH\_IDENTIFICATION**](safer-hash-identification.md)         | Identifies a hash of the code image to be checked.                                                                                                                                                                                                      |
| [**SAFER\_URLZONE\_IDENTIFICATION**](safer-urlzone-identification.md)   | Identifies the URL zone of origin of the code image to be checked.                                                                                                                                                                                      |



 

 

 



