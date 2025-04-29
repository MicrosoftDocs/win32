---
description: Well-known security identifiers (SIDs) identify generic groups and generic users.
ms.assetid: eb2f95c4-9465-409b-b76c-9ccae1d05eda
title: Well-known SIDs
ms.topic: concept-article
ms.date: 11/25/2024
#Customer intent: As a Windows developer, I want to learn about well-known SIDs so that I can use them in my Win32 applications.
---

# Well-known SIDs

Well-known [*security identifiers*](/windows/win32/SecGloss/s-gly) (SIDs) identify generic groups and generic users. For example, there are well-known SIDs to identify the following groups and users:

- Everyone or World, which is a group that includes all users.
- CREATOR\_OWNER, which is used as a placeholder in an inheritable ACE. When the ACE is inherited, the system replaces the CREATOR\_OWNER SID with the SID of the object's creator.
- The Administrators group for the built-in domain on the local computer.

There are [*universal well-known SIDs*](/windows/win32/SecGloss/u-gly), which are meaningful on all secure systems using this security model, including operating systems other than Windows. In addition, there are well-known SIDs that are meaningful only on Windows systems.

The Windows API defines a set of constants for well-known identifier authority and [*relative identifier*](/windows/win32/SecGloss/r-gly) (RID) values. You can use these constants to create well-known SIDs. The following example combines the SECURITY\_WORLD\_SID\_AUTHORITY and SECURITY\_WORLD\_RID constants to show the universal well-known SID for the special group representing all users (Everyone or World):

`S-1-1-0`

This example uses the string notation for SIDs in which S identifies the string as a SID, the first 1 is the revision level of the SID, and the remaining two digits are the SECURITY\_WORLD\_SID\_AUTHORITY and SECURITY\_WORLD\_RID constants.

You can use the [**AllocateAndInitializeSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-allocateandinitializesid) function to build a SID by combining an identifier authority value with up to eight subauthority values. For example, to determine whether the logged-on user is a member of a particular well-known group, call **AllocateAndInitializeSid** to build a SID for the well-known group and use the [**EqualSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-equalsid) function to compare that SID to the group SIDs in the user's [*access token*](/windows/win32/SecGloss/a-gly). For an example, see [Searching for a SID in an Access Token in C++](searching-for-a-sid-in-an-access-token-in-c--.md). You must call the [**FreeSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-freesid) function to free a SID allocated by **AllocateAndInitializeSid**.

The remainder of this section contains tables of well-known SIDs and tables of identifier authority and subauthority constants that you can use to build well-known SIDs.

The following are some [*universal well-known SIDs*](/windows/win32/SecGloss/u-gly).

| Universal well-known SID | Identifies |
|--------------------------|------------|
| Null SID<br/>String value: `S-1-0-0` | A group with no members. This is often used when a SID value is not known. |
| World<br/>String value: `S-1-1-0` | A group that includes all users. |
| Local<br/>String value: `S-1-2-0` | Users who log on to [*terminals*](/windows/win32/SecGloss/t-gly) locally (physically) connected to the system. |
| Creator Owner ID<br/>String value: `S-1-3-0` | A security identifier to be replaced by the security identifier of the user who created a new object. This SID is used in inheritable ACEs. |
| Creator Group ID<br/>String value: `S-1-3-1` | A security identifier to be replaced by the primary-group SID of the user who created a new object. Use this SID in inheritable ACEs. |

The following table lists the predefined identifier authority constants. The first four values are used with universal well-known SIDs; the last value is used with Windows well-known SIDs.

| Identifier authority | Value | String value |
|----------------------|-------|--------------|
| SECURITY_NULL_SID_AUTHORITY | `0` | `S-1-0` |
| SECURITY_WORLD_SID_AUTHORITY | `1` | `S-1-1` |
| SECURITY_LOCAL_SID_AUTHORITY | `2` | `S-1-2` |
| SECURITY_CREATOR_SID_AUTHORITY | `3` | `S-1-3` |
| SECURITY_NT_AUTHORITY | `5` | `S-1-5` |

The following [*RID*](/windows/win32/SecGloss/r-gly) values are used with [*universal well-known SIDs*](/windows/win32/SecGloss/u-gly). The Identifier authority column shows the prefix of the identifier authority with which you can combine the RID to create a universal well-known SID.

| Relative identifier authority | Value | String value |
|-------------------------------|-------|--------------|
| SECURITY_NULL_RID          | `0` | `S-1-0-0` |
| SECURITY_WORLD_RID         | `0` | `S-1-1-0` |
| SECURITY_LOCAL_RID         | `0` | `S-1-2-0` |
| SECURITY_LOCAL_LOGON_RID   | `1` | `S-1-2-1` |
| SECURITY_CREATOR_OWNER_RID | `0` | `S-1-3-0` |
| SECURITY_CREATOR_GROUP_RID | `1` | `S-1-3-1` |

The SECURITY_NT_AUTHORITY (S-1-5) predefined identifier authority produces SIDs that are not universal but are meaningful only on Windows installations. You can use the following RID values with SECURITY_NT_AUTHORITY to create well-known SIDs.

| Constant | Identifies |
|----------|------------|
| SECURITY_DIALUP_RID<br/>String value: `S-1-5-1` | Users who log on to [*terminals*](/windows/win32/SecGloss/t-gly) using a dial-up modem. This is a group identifier. |
| SECURITY_NETWORK_RID<br/>String value: `S-1-5-2` | Users who log on across a network. This is a group identifier added to the token of a process when it was logged on across a network. The corresponding logon type is LOGON32_LOGON_NETWORK. |
| SECURITY_BATCH_RID<br/>String value: `S-1-5-3` | Users who log on using a batch queue facility. This is a group identifier added to the token of a process when it was logged as a batch job. The corresponding logon type is LOGON32_LOGON_BATCH. |
| SECURITY_INTERACTIVE_RID<br/>String value: `S-1-5-4` | Users who log on for interactive operation. This is a group identifier added to the token of a process when it was logged on interactively. The corresponding logon type is LOGON32_LOGON_INTERACTIVE. |
| SECURITY_LOGON_IDS_RID<br/>String value: `S-1-5-5-*X*-*Y*` | A logon session. This is used to ensure that only [*processes*](/windows/win32/SecGloss/p-gly) in a given logon session can gain access to the window-station objects for that session. The *X* and *Y* values for these SIDs are different for each logon session. The value SECURITY_LOGON_IDS_RID_COUNT is the number of RIDs in this identifier (5-*X*-*Y*). |
| SECURITY_SERVICE_RID<br/>String value: `S-1-5-6` | Accounts authorized to log on as a service. This is a group identifier added to the token of a process when it was logged as a service. The corresponding logon type is LOGON32_LOGON_SERVICE. |
| SECURITY_ANONYMOUS_LOGON_RID<br/>String value: `S-1-5-7` | Anonymous logon, or null session logon. |
| SECURITY_PROXY_RID<br/>String value: `S-1-5-8` | Proxy. |
| SECURITY_ENTERPRISE_CONTROLLERS_RID<br/>String value: `S-1-5-9` | Enterprise controllers. |
| SECURITY_PRINCIPAL_SELF_RID<br/>String value: `S-1-5-10` | The PRINCIPAL_SELF security identifier can be used in the ACL of a user or group object. During an access check, the system replaces the SID with the SID of the object. The PRINCIPAL_SELF SID is useful for specifying an inheritable ACE that applies to the user or group object that inherits the ACE. It the only way of representing the SID of a created object in the default [*security descriptor*](/windows/win32/SecGloss/s-gly) of the schema. |
| SECURITY_AUTHENTICATED_USER_RID<br/>String value: `S-1-5-11` | The authenticated users. |
| SECURITY_RESTRICTED_CODE_RID<br/>String value: `S-1-5-12` | Restricted code. |
| SECURITY_TERMINAL_SERVER_RID<br/>String value: `S-1-5-13` | Terminal Services. Automatically added to the security token of a user who logs on to a terminal server. |
| SECURITY_LOCAL_SYSTEM_RID<br/>String value: `S-1-5-18` | A special account used by the operating system. |
| SECURITY_NT_NON_UNIQUE<br/>String value: `S-1-5-21` | SIDS are not unique. |
| SECURITY_BUILTIN_DOMAIN_RID<br/>String value: `S-1-5-32` | The built-in system domain. |
| SECURITY_WRITE_RESTRICTED_CODE_RID<br/>String value: `S-1-5-33` | Write restricted code. |
| SECURITY_RESTRICTED_SERVICES_BASE_RID<br/>String value:`S-1-5-99` | Restricted Services. |

The following RIDs are relative to each domain.

| RID                                                                | Identifies |
|--------------------------------------------------------------------|------------|
| DOMAIN_ALIAS_RID_CERTSVC_DCOM_ACCESS_GROUP<br/>Value: `0x0000023E` | The group of users who can connect to certification authorities using Distributed Component Object Model (DCOM). |
| DOMAIN_USER_RID_ADMIN<br/>Value: `0x000001F4` | The administrative user account in a domain. |
| DOMAIN_USER_RID_GUEST<br/>Value: `0x000001F5` | The guest-user account in a domain. Users who do not have an account can automatically log on to this account. |
| DOMAIN_GROUP_RID_ADMINS<br/>Value: `0x00000200` | The domain administrators' group. This account exists only on systems running server operating systems. |
| DOMAIN_GROUP_RID_USERS<br/>Value: `0x00000201` | A group that contains all user accounts in a domain. All users are automatically added to this group. |
| DOMAIN_GROUP_RID_GUESTS<br/>Value: `0x00000202` | The guest-group account in a domain. |
| DOMAIN_GROUP_RID_COMPUTERS<br/>Value: `0x00000203` | The domain computers' group. All computers in the domain are members of this group. |
| DOMAIN_GROUP_RID_CONTROLLERS<br/>Value: `0x00000204` | The domain controllers' group. All DCs in the domain are members of this group. |
| DOMAIN_GROUP_RID_CERT_ADMINS<br/>Value: `0x00000205` | The certificate publishers' group. Computers running Certificate Services are members of this group. |
| DOMAIN_GROUP_RID_ENTERPRISE_READONLY_DOMAIN_CONTROLLERS<br/>Value: `0x000001F2` | The group of enterprise read-only domain controllers. |
| DOMAIN_GROUP_RID_SCHEMA_ADMINS<br/>Value: `0x00000206` | The schema administrators' group. Members of this group can modify the Active Directory schema. |
| DOMAIN_GROUP_RID_ENTERPRISE_ADMINS<br/>Value: `0x00000207` | The enterprise administrators' group. Members of this group have full access to all domains in the Active Directory forest. Enterprise administrators are responsible for forest-level operations such as adding or removing new domains. |
| DOMAIN_GROUP_RID_POLICY_ADMINS<br/>Value: `0x00000208` | The policy administrators' group. |
| DOMAIN_GROUP_RID_READONLY_CONTROLLERS<br/>Value: `0x00000209` | The group of read-only domain controllers |
| DOMAIN_GROUP_RID_CLONEABLE_CONTROLLERS<br/>Value: `0x0000020A` | The group of cloneable domain controllers. |
| DOMAIN_GROUP_RID_CDC_RESERVED<br/>Value: `0x0000020C` | The reserved CDC group. |
| DOMAIN_GROUP_RID_PROTECTED_USERS<br/>Value: `0x0000020D` | The protected users group. |
| DOMAIN_GROUP_RID_KEY_ADMINS<br/>Value: `0x0000020E` | The key admins group. |
| DOMAIN_GROUP_RID_ENTERPRISE_KEY_ADMINS<br/>Value: `0x0000020F` | The enterprise key admins group. |
| DOMAIN_GROUP_RID_FOREST_TRUSTS<br/>Value: `0x00000210` | The primary group of forest trust user accounts. |
| DOMAIN_GROUP_RID_EXTERNAL_TRUSTS<br/>Value: `0x00000211` | The primary group of external trust user accounts. |

The following RIDs are used to specify mandatory integrity level.

| RID                                      | Value                                   | Identifies             |
|------------------------------------------|-----------------------------------------|------------------------|
| SECURITY_MANDATORY_UNTRUSTED_RID         | `0x00000000`                            | Untrusted.             |
| SECURITY_MANDATORY_LOW_RID               | `0x00001000`                            | Low integrity.         |
| SECURITY_MANDATORY_MEDIUM_RID            | `0x00002000`                            | Medium integrity.      |
| SECURITY_MANDATORY_MEDIUM_PLUS_RID       | SECURITY_MANDATORY_MEDIUM_RID + `0x100` | Medium high integrity. |
| SECURITY_MANDATORY_HIGH_RID              | `0X00003000`                            | High integrity.        |
| SECURITY_MANDATORY_SYSTEM_RID            | `0x00004000`                            | System integrity.      |
| SECURITY_MANDATORY_PROTECTED_PROCESS_RID | `0x00005000`                            | Protected process.     |

The following table has examples of domain-relative RIDs that you can use to form well-known SIDs for local groups (aliases). For more information about local and global groups, see [Local Group Functions](/windows/win32/NetMgmt/local-group-functions) and [Group Functions](/windows/win32/NetMgmt/group-functions).

| RID                                                              | Identifies |
|------------------------------------------------------------------|------------|
| DOMAIN\_ALIAS\_RID\_ADMINS<br/>Value: `0x00000220`<br/>String value: `S-1-5-32-544` | A local group used for administration of the domain. |
| DOMAIN\_ALIAS\_RID\_USERS<br/>Value: `0x00000221`<br/>String value: `S-1-5-32-545` | A local group that represents all users in the domain. |
| DOMAIN\_ALIAS\_RID\_GUESTS<br/>Value: `0x00000222`<br/>String value: `S-1-5-32-546` | A local group that represents guests of the domain. |
| DOMAIN\_ALIAS\_RID\_POWER\_USERS<br/>Value: `0x00000223`<br/>String value: `S-1-5-32-547` | A local group used to represent a user or set of users who expect to treat a system as if it were their personal computer rather than as a workstation for multiple users. |
| DOMAIN\_ALIAS\_RID\_ACCOUNT\_OPS<br/>Value: `0x00000224`<br/>String value: `S-1-5-32-548` | A local group that exists only on systems running server operating systems. This local group permits control over nonadministrator accounts. |
| DOMAIN\_ALIAS\_RID\_SYSTEM\_OPS<br/>Value: `0x00000225`<br/>String value: `S-1-5-32-549` | A local group that exists only on systems running server operating systems. This local group performs system administrative functions, not including security functions. It establishes network shares, controls printers, unlocks workstations, and performs other operations. |
| DOMAIN\_ALIAS\_RID\_PRINT\_OPS<br/>Value: `0x00000226`<br/>String value: `S-1-5-32-550` | A local group that exists only on systems running server operating systems. This local group controls printers and print queues. |
| DOMAIN\_ALIAS\_RID\_BACKUP\_OPS<br/>Value: `0x00000227`<br/>String value: `S-1-5-32-551` | A local group used for controlling assignment of file backup-and-restore privileges. |
| DOMAIN\_ALIAS\_RID\_REPLICATOR<br/>Value: `0x00000228`<br/>String value: `S-1-5-32-552` | A local group responsible for copying security databases from the primary domain controller to the backup domain controllers. These accounts are used only by the system. |
| DOMAIN\_ALIAS\_RID\_RAS\_SERVERS<br/>Value: `0x00000229`<br/>String value: `S-1-5-32-553` | A local group that represents RAS and IAS servers. This group permits access to various attributes of user objects. |
| DOMAIN\_ALIAS\_RID\_PREW2KCOMPACCESS<br/>Value: `0x0000022A`<br/>String value: `S-1-5-32-554` | A local group that exists only on systems running Windows 2000 Server. For more information, see [Allowing Anonymous Access](allowing-anonymous-access.md). |
| DOMAIN\_ALIAS\_RID\_REMOTE\_DESKTOP\_USERS<br/>Value: `0x0000022B`<br/>String value: `S-1-5-32-555` | A local group that represents all remote desktop users. |
| DOMAIN\_ALIAS\_RID\_NETWORK\_CONFIGURATION\_OPS<br/>Value: `0x0000022C`<br/>String value: `S-1-5-32-556` | A local group that represents the network configuration. |
| DOMAIN\_ALIAS\_RID\_INCOMING\_FOREST\_TRUST\_BUILDERS<br/>Value: `0x0000022D`<br/>String value: `S-1-5-32-557` | A local group that represents any forest trust users. |
| DOMAIN\_ALIAS\_RID\_MONITORING\_USERS<br/>Value: `0x0000022E`<br/>String value: `S-1-5-32-558` | A local group that represents all users being monitored. |
| DOMAIN\_ALIAS\_RID\_LOGGING\_USERS<br/>Value: `0x0000022F`<br/>String value: `S-1-5-32-559` | A local group responsible for logging users. |
| DOMAIN\_ALIAS\_RID\_AUTHORIZATIONACCESS<br/>Value: `0x00000230`<br/>String value: `S-1-5-32-560` | A local group that represents all authorized access. |
| DOMAIN\_ALIAS\_RID\_TS\_LICENSE\_SERVERS<br/>Value: `0x00000231`<br/>String value: `S-1-5-32-561` | A local group that exists only on systems running server operating systems that allow for terminal services and remote access. |
| DOMAIN\_ALIAS\_RID\_DCOM\_USERS<br/>Value: `0x00000232`<br/>String value: `S-1-5-32-562` | A local group that represents users who can use Distributed Component Object Model (DCOM). |
| DOMAIN\_ALIAS\_RID\_IUSERS<br/>Value: `0X00000238`<br/>String value: `S-1-5-32-568` | A local group that represents Internet users. |
| DOMAIN\_ALIAS\_RID\_CRYPTO\_OPERATORS<br/>Value: `0x00000239`<br/>String value: `S-1-5-32-569` | A local group that represents access to cryptography operators. |
| DOMAIN\_ALIAS\_RID\_CACHEABLE\_PRINCIPALS\_GROUP<br/>Value: `0x0000023B`<br/>String value: `S-1-5-32-571` | A local group that represents principals that can be cached. |
| DOMAIN\_ALIAS\_RID\_NON\_CACHEABLE\_PRINCIPALS\_GROUP<br/>Value: `0x0000023C`<br/>String value: `S-1-5-32-572` | A local group that represents principals that cannot be cached. |
| DOMAIN\_ALIAS\_RID\_EVENT\_LOG\_READERS\_GROUP<br/>Value: `0x0000023D`<br/>String value: `S-1-5-32-573` | A local group that represents event log readers. |
| DOMAIN\_ALIAS\_RID\_CERTSVC\_DCOM\_ACCESS\_GROUP<br/>Value: `0x0000023E`<br/>String value: `S-1-5-32-574` | The local group of users who can connect to certification authorities using Distributed Component Object Model (DCOM). |
| DOMAIN\_ALIAS\_RID\_RDS\_REMOTE\_ACCESS\_SERVERS<br/>Value: `0x0000023F`<br/>String value: `S-1-5-32-575` | A local group that represents RDS remote access servers. |
| DOMAIN\_ALIAS\_RID\_RDS\_ENDPOINT\_SERVERS<br/>Value: `0x00000240`<br/>String value: `S-1-5-32-576` | A local group that represents endpoint servers. |
| DOMAIN\_ALIAS\_RID\_RDS\_MANAGEMENT\_SERVERS<br/>Value: `0x00000241`<br/>String value: `S-1-5-32-577` | A local group that represents management servers. |
| DOMAIN\_ALIAS\_RID\_HYPER\_V\_ADMINS<br/>Value: `0x00000242`<br/>String value: `S-1-5-32-578` | A local group that represents hyper-v admins. |
| DOMAIN\_ALIAS\_RID\_ACCESS\_CONTROL\_ASSISTANCE\_OPS<br/>Value: `0x00000243`<br/>String value: `S-1-5-32-579` | A local group that represents access control assistance OPS. |
| DOMAIN\_ALIAS\_RID\_REMOTE\_MANAGEMENT\_USERS<br/>Value: `0x00000244`<br/>String value: `S-1-5-32-580` | A local group that represents remote management users. |
| DOMAIN\_ALIAS\_RID\_DEFAULT\_ACCOUNT<br/>Value: `0x00000245`<br/>String value: `S-1-5-32-581` | A local group that represents the default account. |
| DOMAIN\_ALIAS\_RID\_STORAGE\_REPLICA\_ADMINS<br/>Value: `0x00000246`<br/>String value: `S-1-5-32-582` | A local group that represents storage replica admins. |
| DOMAIN\_ALIAS\_RID\_DEVICE\_OWNERS<br/>Value: `0x00000247`<br/>String value: `S-1-5-32-583` | A local group that represents can make settings expected for Device Owners. |
| DOMAIN\_ALIAS\_RID\_USER\_MODE\_HARDWARE\_OPERATORS<br/>Value: `0x00000248`<br/>String value: `S-1-5-32-584` | Members of this group can access user mode mapper drivers. |
| DOMAIN\_ALIAS\_RID\_OPENSSH\_USERS<br/>Value: `0x00000249`<br/>String value: `S-1-5-32-585` | Members of this group can use OpenSSH to access the computer. |

The [WELL_KNOWN_SID_TYPE](/windows/win32/api/Winnt/ne-winnt-well_known_sid_type) enumeration defines the list of commonly used SIDs. Additionally, the [Security Descriptor Definition Language](security-descriptor-definition-language.md) (SDDL) uses [SID strings](sid-strings.md) to reference well-known SIDs in a string format.
