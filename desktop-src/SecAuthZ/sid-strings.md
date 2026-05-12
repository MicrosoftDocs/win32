---
description: Explains the strings used by SDDLs.
ms.assetid: a531532f-afba-46a1-8576-90d4ff881b94
title: SID Strings
ms.topic: reference
ms.date: 09/26/2023
---

# SID Strings

In the [security descriptor definition language](security-descriptor-definition-language.md) (SDDL), [security descriptor string](security-descriptor-string-format.md) use SID strings for the following components of a [*security descriptor*](/windows/win32/SecGloss/s-gly):

- Owner
- Primary group
- The [trustee](trustees.md) in an ACE

A SID string in a security descriptor string can use either the standard string representation of a SID (S-*R*-*I*-*S*-*S* ) or one of the string constants defined in Sddl.h. For more information about the standard SID string notation, see [SID Components](sid-components.md).

The following SID string constants for well-known SIDs are defined in Sddl.h. For information about the corresponding [*relative IDs*](/windows/win32/SecGloss/r-gly) (RIDs), see [Well-known SIDs](well-known-sids.md).

| SDDL SID string | Constant in Sddl.h | Account alias and corresponding RID |
|-----------------|-----------------|-----------------|
| "AA" | SDDL\_ACCESS\_CONTROL\_ASSISTANCE\_OPS | Access control assistance operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_ACCESS\_CONTROL\_ASSISTANCE\_OPS. **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "AC" | SDDL\_ALL\_APP\_PACKAGES | All applications running in an app package context. The corresponding RID is SECURITY\_BUILTIN\_PACKAGE\_ANY\_PACKAGE. **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "AN" | SDDL\_ANONYMOUS | Anonymous logon. The corresponding RID is SECURITY\_ANONYMOUS\_LOGON\_RID. |
| "AO" | SDDL\_ACCOUNT\_OPERATORS | Account operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_ACCOUNT\_OPS. |
| "AP" | SDDL\_PROTECTED\_USERS | [Protected Users](/windows-server/security/credentials-protection-and-management/protected-users-security-group). The corresponding RID is DOMAIN\_GROUP\_RID\_PROTECTED\_USERS. **Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "AU" | SDDL\_AUTHENTICATED\_USERS | Authenticated users. The corresponding RID is SECURITY\_AUTHENTICATED\_USER\_RID. |
| "BA" | SDDL\_BUILTIN\_ADMINISTRATORS | Built-in administrators. The corresponding RID is DOMAIN\_ALIAS\_RID\_ADMINS. |
| "BG" | SDDL\_BUILTIN\_GUESTS | Built-in guests. The corresponding RID is DOMAIN\_ALIAS\_RID\_GUESTS. |
| "BO" | SDDL\_BACKUP\_OPERATORS | Backup operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_BACKUP\_OPS. |
| "BU" | SDDL\_BUILTIN\_USERS | Built-in users. The corresponding RID is DOMAIN\_ALIAS\_RID\_USERS. |
| "CA" | SDDL\_CERT\_SERV\_ADMINISTRATORS | Certificate publishers. The corresponding RID is DOMAIN\_GROUP\_RID\_CERT\_ADMINS. |
| "CD" | SDDL\_CERTSVC\_DCOM\_ACCESS | Users who can connect to certification authorities using Distributed Component Object Model (DCOM). The corresponding RID is DOMAIN\_ALIAS\_RID\_CERTSVC\_DCOM\_ACCESS\_GROUP. **Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "CG" | SDDL\_CREATOR\_GROUP | Creator group. The corresponding RID is SECURITY\_CREATOR\_GROUP\_RID. |
| "CN" | SDDL\_CLONEABLE\_CONTROLLERS | Cloneable domain controllers. The corresponding RID is DOMAIN\_GROUP\_RID\_CLONEABLE\_CONTROLLERS. **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "CO" | SDDL\_CREATOR\_OWNER | Creator owner. The corresponding RID is SECURITY\_CREATOR\_OWNER\_RID. |
| "CY" | SDDL\_CRYPTO\_OPERATORS | Crypto operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_CRYPTO\_OPERATORS.  *Windows Server 2003:** Not available. |
| "DA" | SDDL\_DOMAIN\_ADMINISTRATORS | Domain administrators. The corresponding RID is DOMAIN\_GROUP\_RID\_ADMINS. |
| "DC" | SDDL\_DOMAIN\_COMPUTERS | Domain computers. The corresponding RID is DOMAIN\_GROUP\_RID\_COMPUTERS. |
| "DD" | SDDL\_DOMAIN\_DOMAIN\_CONTROLLERS | Domain controllers. The corresponding RID is DOMAIN\_GROUP\_RID\_CONTROLLERS. |
| "DG" | SDDL\_DOMAIN\_GUESTS | Domain guests. The corresponding RID is DOMAIN\_GROUP\_RID\_GUESTS. |
| "DU" | SDDL\_DOMAIN\_USERS | Domain users. The corresponding RID is DOMAIN\_GROUP\_RID\_USERS. |
| "EA" | SDDL\_ENTERPRISE\_ADMINS | Enterprise administrators. The corresponding RID is DOMAIN\_GROUP\_RID\_ENTERPRISE\_ADMINS. |
| "ED" | SDDL\_ENTERPRISE\_DOMAIN\_CONTROLLERS | Enterprise domain controllers. The corresponding RID is SECURITY\_SERVER\_LOGON\_RID. |
| "EK" | SDDL\_ENTERPRISE\_KEY\_ADMINS | Enterprise key admins. The corresponding RID is DOMAIN\_GROUP\_RID\_ENTERPRISE\_KEY\_ADMINS. **Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "ER" | SDDL\_EVENT\_LOG\_READERS | Event log readers. The corresponding RID is DOMAIN\_ALIAS\_RID\_EVENT\_LOG\_READERS\_GROUP. **Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "ES" | SDDL\_RDS\_ENDPOINT\_SERVERS | Endpoint servers. The corresponding RID is DOMAIN\_ALIAS\_RID\_RDS\_ENDPOINT\_SERVERS. **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "HA" | SDDL\_HYPER\_V\_ADMINS | Hyper-V administrators. The corresponding RID is DOMAIN\_ALIAS\_RID\_HYPER\_V\_ADMINS. **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "HI" | SDDL\_ML\_HIGH | High integrity level. The corresponding RID is SECURITY\_MANDATORY\_HIGH\_RID. **Windows Server 2003:** Not available. |
| "HO" | SDDL_USER_MODE_HARDWARE_OPERATORS | Group members may operate hardware from user mode. The corresponding RID is DOMAIN_ALIAS_RID_USER_MODE_HARDWARE_OPERATORS. |
| "IS" | SDDL\_IIS\_USERS | Anonymous Internet users. The corresponding RID is DOMAIN\_ALIAS\_RID\_IUSERS. **Windows Server 2003:** Not available. |
| "IU" | SDDL\_INTERACTIVE | Interactively logged-on user. This is a group identifier added to the token of a process when it was logged on interactively. The corresponding logon type is LOGON32\_LOGON\_INTERACTIVE. The corresponding RID is SECURITY\_INTERACTIVE\_RID. |
| "KA" | SDDL\_KEY\_ADMINS | Domain key admins. The corresponding RID is DOMAIN\_GROUP\_RID\_KEY\_ADMINS. **Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "LA" | SDDL\_LOCAL\_ADMIN | Local administrator. The corresponding RID is DOMAIN\_USER\_RID\_ADMIN. |
| "LG" | SDDL\_LOCAL\_GUEST | Local guest. The corresponding RID is DOMAIN\_USER\_RID\_GUEST. |
| "LS" | SDDL\_LOCAL\_SERVICE | Local service account. The corresponding RID is SECURITY\_LOCAL\_SERVICE\_RID. |
| "LU" | SDDL\_PERFLOG\_USERS | Performance Log users. The corresponding RID is DOMAIN\_ALIAS\_RID\_LOGGING\_USERS. |
| "LW" | SDDL\_ML\_LOW | Low integrity level. The corresponding RID is SECURITY\_MANDATORY\_LOW\_RID. **Windows Server 2003:** Not available. |
| "ME" | SDDL\_ML\_MEDIUM | Medium integrity level. The corresponding RID is SECURITY\_MANDATORY\_MEDIUM\_RID. **Windows Server 2003:** Not available. |
| "MP" | SDDL\_ML\_MEDIUM\_PLUS | Medium Plus integrity level. The corresponding RID is SECURITY\_MANDATORY\_MEDIUM\_PLUS\_RID. **Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "MU" | SDDL\_PERFMON\_USERS | Performance Monitor users. The corresponding RID is DOMAIN\_ALIAS\_RID\_MONITORING\_USERS. |
| "NO" | SDDL\_NETWORK\_CONFIGURATION\_OPS | Network configuration operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_NETWORK\_CONFIGURATION\_OPS. |
| "NS" | SDDL\_NETWORK\_SERVICE | Network service account. The corresponding RID is SECURITY\_NETWORK\_SERVICE\_RID. |
| "NU" | SDDL\_NETWORK | Network logon user. This is a group identifier added to the token of a process when it was logged on across a network. The corresponding logon type is LOGON32\_LOGON\_NETWORK. The corresponding RID is SECURITY\_NETWORK\_RID. |
| "OW" | SDDL\_OWNER\_RIGHTS | Owner Rights SID. The corresponding RID is SECURITY\_CREATOR\_OWNER\_RIGHTS\_RID. *Windows Server 2003:** Not available. |
| "PA" | SDDL\_GROUP\_POLICY\_ADMINS | Group Policy administrators. The corresponding RID is DOMAIN\_GROUP\_RID\_POLICY\_ADMINS. |
| "PO" | SDDL\_PRINTER\_OPERATORS | Printer operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_PRINT\_OPS |
| "PS" | SDDL\_PERSONAL\_SELF | Principal self. The corresponding RID is SECURITY\_PRINCIPAL\_SELF\_RID. |
| "PU" | SDDL\_POWER\_USERS | Power users. The corresponding RID is DOMAIN\_ALIAS\_RID\_POWER\_USERS. |
| "RA" | SDDL\_RDS\_REMOTE\_ACCESS\_SERVERS | RDS remote access servers. The corresponding RID is DOMAIN\_ALIAS\_RID\_RDS\_REMOTE\_ACCESS\_SERVERS. **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "RC" | SDDL\_RESTRICTED\_CODE | Restricted code. This is a restricted token created using the [**CreateRestrictedToken**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken) function. The corresponding RID is SECURITY\_RESTRICTED\_CODE\_RID. |
| "RD" | SDDL\_REMOTE\_DESKTOP | Terminal server users. The corresponding RID is DOMAIN\_ALIAS\_RID\_REMOTE\_DESKTOP\_USERS. |
| "RE" | SDDL\_REPLICATOR | Replicator. The corresponding RID is DOMAIN\_ALIAS\_RID\_REPLICATOR. |
| "RM" | SDDL\_RMS_\_SERVICE\_OPERATORS | RMS Service. **Available only in Windows Vista**. |
| "RO" | SDDL\_ENTERPRISE\_RO\_DCs | Enterprise Read-only domain controllers. The corresponding RID is DOMAIN\_GROUP\_RID\_ENTERPRISE\_READONLY\_DOMAIN\_CONTROLLERS. **Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "RS" | SDDL\_RAS\_SERVERS | RAS servers group. The corresponding RID is DOMAIN\_ALIAS\_RID\_RAS\_SERVERS. |
| "RU" | SDDL\_ALIAS\_PREW2KCOMPACC | Alias to grant permissions to accounts that use applications compatible with operating systems previous to Windows 2000. The corresponding RID is DOMAIN\_ALIAS\_RID\_PREW2KCOMPACCESS. |
| "SA" | SDDL\_SCHEMA\_ADMINISTRATORS | Schema administrators. The corresponding RID is DOMAIN\_GROUP\_RID\_SCHEMA\_ADMINS. |
| "SH" | SDDL\_OPENSSH\_USERS | Users allowed to connect with OpenSSH. The corresponding RID is DOMAIN\_ALIAS\_RID\_OPENSSH\_USERS. |
| "SI" | SDDL\_ML\_SYSTEM | System integrity level. The corresponding RID is SECURITY\_MANDATORY\_SYSTEM\_RID. **Windows Server 2003:** Not available. |
| "SO" | SDDL\_SERVER\_OPERATORS | Server operators. The corresponding RID is DOMAIN\_ALIAS\_RID\_SYSTEM\_OPS. |
| "SS" | SDDL\_SERVICE\_ASSERTED | Authentication service asserted. The corresponding RID is SECURITY\_AUTHENTICATION\_SERVICE\_ASSERTED\_RID. **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "SU" | SDDL\_SERVICE | Service logon user. This is a group identifier added to the token of a process when it was logged as a service. The corresponding logon type is LOGON32\_LOGON\_SERVICE. The corresponding RID is SECURITY\_SERVICE\_RID. |
| "SY" | SDDL\_LOCAL\_SYSTEM | Local system. The corresponding RID is SECURITY\_LOCAL\_SYSTEM\_RID. |
| "UD" | SDDL\_USER\_MODE\_DRIVERS | User-mode driver. The corresponding RID is SECURITY\_USERMODEDRIVERHOST\_ID\_BASE\_RID. **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista and Windows Server 2003:** Not available. |
| "WD" | SDDL\_EVERYONE | Everyone. The corresponding RID is SECURITY\_WORLD\_RID. |
| "WR" | SDDL\_WRITE\_RESTRICTED\_CODE | Write Restricted code. The corresponding RID is SECURITY\_WRITE\_RESTRICTED\_CODE\_RID. *Windows Server 2003:** Not available. |

The [**ConvertSidToStringSid**](/windows/desktop/api/Sddl/nf-sddl-convertsidtostringsida) and [**ConvertStringSidToSid**](/windows/win32/api/Sddl/nf-sddl-convertstringsidtosida) functions always use the standard SID string notation and do not support SDDL SID string constants.

For more information about well-known SIDs, see [Well-known SIDs](well-known-sids.md).

## See also

[\[MS-DTYP\]: Security Descriptor Description Language](/openspecs/windows_protocols/ms-dtyp/4f4251cc-23b6-44b6-93ba-69688422cb06)
