---
description: Explains the strings used by SDDLs.
ms.assetid: a531532f-afba-46a1-8576-90d4ff881b94
title: SID Strings
ms.topic: article
ms.date: 05/31/2018
---

# SID Strings

In the [security descriptor definition language](security-descriptor-definition-language.md) (SDDL), [security descriptor string](security-descriptor-string-format.md) use SID strings for the following components of a [*security descriptor*](/windows/desktop/SecGloss/s-gly):

-   Owner
-   Primary group
-   The [trustee](trustees.md) in an ACE

A SID string in a security descriptor string can use either the standard string representation of a SID (S-*R*-*I*-*S*-*S* ) or one of the string constants defined in Sddl.h. For more information about the standard SID string notation, see [SID Components](sid-components.md).

The following SID string constants for well-known SIDs are defined in Sddl.h. For information about the corresponding [*relative IDs*](/windows/desktop/SecGloss/r-gly) (RIDs), see [Well-known SIDs](well-known-sids.md).



| SDDL SID string | Constant in Sddl.h                               | Account alias and corresponding RID                                                                                                                                                                                                                        |
|-----------------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "AN"<br/> | SDDL\_ANONYMOUS<br/>                       | Anonymous logon. The corresponding RID is SECURITY\_ANONYMOUS\_LOGON\_RID.<br/>                                                                                                                                                                      |
| "AO"<br/> | SDDL\_ACCOUNT\_OPERATORS<br/>              | Account operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_ACCOUNT\_OPS.<br/>                                                                                                                                                                   |
| "AU"<br/> | SDDL\_AUTHENTICATED\_USERS<br/>            | Authenticated users. The corresponding RID is SECURITY\_AUTHENTICATED\_USER\_RID.<br/>                                                                                                                                                               |
| "BA"<br/> | SDDL\_BUILTIN\_ADMINISTRATORS<br/>         | Built-in administrators. The corresponding RID is DOMAIN\_ALIAS\_RID\_ADMINS.<br/>                                                                                                                                                                   |
| "BG"<br/> | SDDL\_BUILTIN\_GUESTS<br/>                 | Built-in guests. The corresponding RID is DOMAIN\_ALIAS\_RID\_GUESTS.<br/>                                                                                                                                                                           |
| "BO"<br/> | SDDL\_BACKUP\_OPERATORS<br/>               | Backup operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_BACKUP\_OPS.<br/>                                                                                                                                                                     |
| "BU"<br/> | SDDL\_BUILTIN\_USERS<br/>                  | Built-in users. The corresponding RID is DOMAIN\_ALIAS\_RID\_USERS.<br/>                                                                                                                                                                             |
| "CA"<br/> | SDDL\_CERT\_SERV\_ADMINISTRATORS<br/>      | Certificate publishers. The corresponding RID is DOMAIN\_GROUP\_RID\_CERT\_ADMINS.<br/>                                                                                                                                                              |
| "CD"<br/> | SDDL\_CERTSVC\_DCOM\_ACCESS<br/>           | Users who can connect to certification authorities using Distributed Component Object Model (DCOM). The corresponding RID is DOMAIN\_ALIAS\_RID\_CERTSVC\_DCOM\_ACCESS\_GROUP.<br/>                                                                  |
| "CG"<br/> | SDDL\_CREATOR\_GROUP<br/>                  | Creator group. The corresponding RID is SECURITY\_CREATOR\_GROUP\_RID.<br/>                                                                                                                                                                          |
| "CO"<br/> | SDDL\_CREATOR\_OWNER<br/>                  | Creator owner. The corresponding RID is SECURITY\_CREATOR\_OWNER\_RID.<br/>                                                                                                                                                                          |
| "DA"<br/> | SDDL\_DOMAIN\_ADMINISTRATORS<br/>          | Domain administrators. The corresponding RID is DOMAIN\_GROUP\_RID\_ADMINS.<br/>                                                                                                                                                                     |
| "DC"<br/> | SDDL\_DOMAIN\_COMPUTERS<br/>               | Domain computers. The corresponding RID is DOMAIN\_GROUP\_RID\_COMPUTERS.<br/>                                                                                                                                                                       |
| "DD"<br/> | SDDL\_DOMAIN\_DOMAIN\_CONTROLLERS<br/>     | Domain controllers. The corresponding RID is DOMAIN\_GROUP\_RID\_CONTROLLERS.<br/>                                                                                                                                                                   |
| "DG"<br/> | SDDL\_DOMAIN\_GUESTS<br/>                  | Domain guests. The corresponding RID is DOMAIN\_GROUP\_RID\_GUESTS.<br/>                                                                                                                                                                             |
| "DU"<br/> | SDDL\_DOMAIN\_USERS<br/>                   | Domain users. The corresponding RID is DOMAIN\_GROUP\_RID\_USERS.<br/>                                                                                                                                                                               |
| "EA"<br/> | SDDL\_ENTERPRISE\_ADMINS<br/>              | Enterprise administrators. The corresponding RID is DOMAIN\_GROUP\_RID\_ENTERPRISE\_ADMINS.<br/>                                                                                                                                                     |
| "ED"<br/> | SDDL\_ENTERPRISE\_DOMAIN\_CONTROLLERS<br/> | Enterprise domain controllers. The corresponding RID is SECURITY\_SERVER\_LOGON\_RID.<br/>                                                                                                                                                           |
| "HI"<br/> | SDDL\_ML\_HIGH<br/>                        | High integrity level. The corresponding RID is SECURITY\_MANDATORY\_HIGH\_RID.<br/>                                                                                                                                                                  |
| "IU"<br/> | SDDL\_INTERACTIVE<br/>                     | Interactively logged-on user. This is a group identifier added to the token of a process when it was logged on interactively. The corresponding logon type is LOGON32\_LOGON\_INTERACTIVE. The corresponding RID is SECURITY\_INTERACTIVE\_RID.<br/> |
| "LA"<br/> | SDDL\_LOCAL\_ADMIN<br/>                    | Local administrator. The corresponding RID is DOMAIN\_USER\_RID\_ADMIN.<br/>                                                                                                                                                                         |
| "LG"<br/> | SDDL\_LOCAL\_GUEST<br/>                    | Local guest. The corresponding RID is DOMAIN\_USER\_RID\_GUEST.<br/>                                                                                                                                                                                 |
| "LS"<br/> | SDDL\_LOCAL\_SERVICE<br/>                  | Local service account. The corresponding RID is SECURITY\_LOCAL\_SERVICE\_RID.<br/>                                                                                                                                                                  |
| "LW"<br/> | SDDL\_ML\_LOW<br/>                         | Low integrity level. The corresponding RID is SECURITY\_MANDATORY\_LOW\_RID.<br/>                                                                                                                                                                    |
| "ME"<br/> | SDDL\_MLMEDIUM<br/>                        | Medium integrity level. The corresponding RID is SECURITY\_MANDATORY\_MEDIUM\_RID.<br/>                                                                                                                                                              |
| "MU"<br/> | SDDL\_PERFMON\_USERS<br/>                  | Performance Monitor users.<br/>                                                                                                                                                                                                                      |
| "NO"<br/> | SDDL\_NETWORK\_CONFIGURATION\_OPS<br/>     | Network configuration operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_NETWORK\_CONFIGURATION\_OPS.<br/>                                                                                                                                      |
| "NS"<br/> | SDDL\_NETWORK\_SERVICE<br/>                | Network service account. The corresponding RID is SECURITY\_NETWORK\_SERVICE\_RID.<br/>                                                                                                                                                              |
| "NU"<br/> | SDDL\_NETWORK<br/>                         | Network logon user. This is a group identifier added to the token of a process when it was logged on across a network. The corresponding logon type is LOGON32\_LOGON\_NETWORK. The corresponding RID is SECURITY\_NETWORK\_RID.<br/>                |
| "PA"<br/> | SDDL\_GROUP\_POLICY\_ADMINS<br/>           | Group Policy administrators. The corresponding RID is DOMAIN\_GROUP\_RID\_POLICY\_ADMINS.<br/>                                                                                                                                                       |
| "PO"<br/> | SDDL\_PRINTER\_OPERATORS<br/>              | Printer operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_PRINT\_OPS.<br/>                                                                                                                                                                     |
| "PS"<br/> | SDDL\_PERSONAL\_SELF<br/>                  | Principal self. The corresponding RID is SECURITY\_PRINCIPAL\_SELF\_RID.<br/>                                                                                                                                                                        |
| "PU"<br/> | SDDL\_POWER\_USERS<br/>                    | Power users. The corresponding RID is DOMAIN\_ALIAS\_RID\_POWER\_USERS.<br/>                                                                                                                                                                         |
| "RC"<br/> | SDDL\_RESTRICTED\_CODE<br/>                | Restricted code. This is a restricted token created using the [**CreateRestrictedToken**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken) function. The corresponding RID is SECURITY\_RESTRICTED\_CODE\_RID.<br/>                                                        |
| "RD"<br/> | SDDL\_REMOTE\_DESKTOP<br/>                 | Terminal server users. The corresponding RID is DOMAIN\_ALIAS\_RID\_REMOTE\_DESKTOP\_USERS.<br/>                                                                                                                                                     |
| "RE"<br/> | SDDL\_REPLICATOR<br/>                      | Replicator. The corresponding RID is DOMAIN\_ALIAS\_RID\_REPLICATOR.<br/>                                                                                                                                                                            |
| "RO"<br/> | SDDL\_ENTERPRISE\_RO\_DCs<br/>             | Enterprise Read-only domain controllers. The corresponding RID is DOMAIN\_GROUP\_RID\_ENTERPRISE\_READONLY\_DOMAIN\_CONTROLLERS.<br/>                                                                                                                |
| "RS"<br/> | SDDL\_RAS\_SERVERS<br/>                    | RAS servers group. The corresponding RID is DOMAIN\_ALIAS\_RID\_RAS\_SERVERS.<br/>                                                                                                                                                                   |
| "RU"<br/> | SDDL\_ALIAS\_PREW2KCOMPACC<br/>            | Alias to grant permissions to accounts that use applications compatible with operating systems previous to Windows 2000. The corresponding RID is DOMAIN\_ALIAS\_RID\_PREW2KCOMPACCESS.<br/>                                                         |
| "SA"<br/> | SDDL\_SCHEMA\_ADMINISTRATORS<br/>          | Schema administrators. The corresponding RID is DOMAIN\_GROUP\_RID\_SCHEMA\_ADMINS.<br/>                                                                                                                                                             |
| "SI"<br/> | SDDL\_ML\_SYSTEM<br/>                      | System integrity level. The corresponding RID is SECURITY\_MANDATORY\_SYSTEM\_RID.<br/>                                                                                                                                                              |
| "SO"<br/> | SDDL\_SERVER\_OPERATORS<br/>               | Server operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_SYSTEM\_OPS.<br/>                                                                                                                                                                     |
| "SU"<br/> | SDDL\_SERVICE<br/>                         | Service logon user. This is a group identifier added to the token of a process when it was logged as a service. The corresponding logon type is LOGON32\_LOGON\_SERVICE. The corresponding RID is SECURITY\_SERVICE\_RID.<br/>                       |
| "SY"<br/> | SDDL\_LOCAL\_SYSTEM<br/>                   | Local system. The corresponding RID is SECURITY\_LOCAL\_SYSTEM\_RID.<br/>                                                                                                                                                                            |
| "WD"<br/> | SDDL\_EVERYONE<br/>                        | Everyone. The corresponding RID is SECURITY\_WORLD\_RID.<br/>                                                                                                                                                                                        |



 

The [**ConvertSidToStringSid**](/windows/desktop/api/Sddl/nf-sddl-convertsidtostringsida) and [**ConvertStringSidToSid**](/windows/desktop/api/Sddl/nf-sddl-convertstringsidtosida) functions always use the standard SID string notation and do not support SDDL SID string constants.

For more information about well-known SIDs, see [Well-known SIDs](well-known-sids.md).

## Related topics

<dl> <dt>

[\[MS-DTYP\]: Security Descriptor Description Language](/openspecs/windows_protocols/ms-dtyp/4f4251cc-23b6-44b6-93ba-69688422cb06)
</dt> </dl>

