---
description: Lists support functions provided by the Security Configuration tool set.
ms.assetid: 5a771014-1706-490f-8540-ec516652cb83
title: Security Management Functions
ms.topic: article
ms.date: 05/31/2018
---

# Security Management Functions

This section contains topics for the following groups of functions:

-   [Attachment Callback Functions](#attachment-callback-functions)
-   [Attachment Engine Functions](#attachment-engine-functions)
-   [LSA Policy Functions](#lsa-policy-functions)
    -   [Policy Functions](#lsa-policy-functions)
    -   [Account Functions](#account-functions)
    -   [Trusted Domain Functions](#trusted-domain-functions)
    -   [Private Data Functions](#private-data-functions)
    -   [Miscellaneous Functions](#miscellaneous-functions)
-   [Managed Service Account Functions](#managed-service-account-functions)
-   [Password Filter Functions](#password-filter-functions)
-   [Safer Functions](#safer-functions)

## Attachment Callback Functions

The following support functions are provided by the Security Configuration tool set and may be used by attachment engines and extension snap-ins to read and write configuration data.



| Callback function                                         | Description                                                                                 |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**PFSCE\_FREE\_INFO**](/windows/win32/api/scesvc/nc-scesvc-pfsce_free_info)<br/>   | Used to free memory allocated by these support functions.<br/>                        |
| [**PFSCE\_LOG\_INFO**](/windows/win32/api/scesvc/nc-scesvc-pfsce_log_info)<br/>     | Used to log message to the configuration log file or analysis log file.<br/>          |
| [**PFSCE\_QUERY\_INFO**](/windows/win32/api/scesvc/nc-scesvc-pfsce_query_info)<br/> | Used to query the configuration and analysis information for a specific service.<br/> |
| [**PFSCE\_SET\_INFO**](/windows/win32/api/scesvc/nc-scesvc-pfsce_set_info)<br/>     | Used to set configuration and analysis information for a specific service.<br/>       |



 

## Attachment Engine Functions



| Function                                                              | Description                                                                                                                                                                                       |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SceSvcAttachmentAnalyze**](scesvcattachmentanalyze.md)<br/> | Implemented by the attachment engine DLL. The Security Configuration Engine calls this function when the system is analyzed.<br/>                                                           |
| [**SceSvcAttachmentConfig**](scesvcattachmentconfig.md)<br/>   | Implemented by the attachment engine DLL. The Security Configuration Engine calls this function when the system is configured.<br/>                                                         |
| [**SceSvcAttachmentUpdate**](scesvcattachmentupdate.md)<br/>   | Implemented by the attachment engine DLL. The Security Configuration Engine calls this function when it receives a configuration update request from the attachment snap-in extension.<br/> |



 

## LSA Policy Functions

The following topics provide reference information for the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) Policy functions.



| Topic                               | Description                                                                                                                                                                                   |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Policy Functions<br/>         | Details functions used to open the local [**Policy**](policy-object.md) object and to set or retrieve global policy information.<br/>                                                  |
| Account Functions<br/>        | Details functions used to manage account permissions and to create and delete user accounts.<br/>                                                                                       |
| Trusted Domain Functions<br/> | Details functions used to create and delete trusted domain relationships and to set and retrieve information about those trusted domains.<br/>                                          |
| Private Data Functions<br/>   | Do not use the LSA private data functions. Instead, use the [**CryptProtectData**](/windows/desktop/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/desktop/api/dpapi/nf-dpapi-cryptunprotectdata) functions.<br/> |
| Miscellaneous Functions<br/>  | Details functions not described elsewhere.<br/>                                                                                                                                         |



 

### Policy Functions

The following functions enumerate user accounts and trusted domains, receive policy change notifications, and lookup account names and SIDs.



| Function                                                                                          | Description                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LsaEnumerateAccountsWithUserRight**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumerateaccountswithuserright)<br/>         | Enumerates all the accounts that have a specified user permission.<br/>                                                                                                                                                                                                                                                                         |
| [**LsaEnumerateTrustedDomainsEx**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumeratetrusteddomainsex)<br/>                   | Enumerates the trusted domains.<br/>                                                                                                                                                                                                                                                                                                            |
| [**LsaLookupNames**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalookupnames)<br/>                                               | Maps the specified names to their SIDs. Returns the SID as an RID/Domain SID pair.<br/>                                                                                                                                                                                                                                                         |
| [**LsaLookupNames2**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalookupnames2)<br/>                                             | Maps the specified names to their SIDs. Returns the SID as a single element.<br/>                                                                                                                                                                                                                                                               |
| [**LsaLookupPrivilegeValue**](/windows/desktop/api/ntlsa/nf-ntlsa-lsalookupprivilegevalue)<br/>                             | Retrieves the [*locally unique identifier*](/windows/desktop/SecGloss/l-gly) (LUID) used by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) to represent the specified privilege name.<br/> |
| [**LsaLookupSids**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalookupsids)<br/>                                                 | Maps the specified account names to their SIDs.<br/>                                                                                                                                                                                                                                                                                            |
| [**LsaRegisterPolicyChangeNotification**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaregisterpolicychangenotification)<br/>     | Registers an event object to receive notifications when the local policy information changes.<br/>                                                                                                                                                                                                                                              |
| [**LsaUnregisterPolicyChangeNotification**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaunregisterpolicychangenotification)<br/> | Unregisters an event object that is receiving policy change notifications.<br/>                                                                                                                                                                                                                                                                 |



 

### Account Functions

The following functions add, enumerate, and delete permissions for an account.



| Function                                                                  | Description                                                                                                  |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**LsaAddAccountRights**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaaddaccountrights)<br/>             | Add permissions to an account. If the account does not already exist, it is created.<br/>              |
| [**LsaEnumerateAccountRights**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumerateaccountrights)<br/> | Enumerate the permissions granted to an account.<br/>                                                  |
| [**LsaRemoveAccountRights**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaremoveaccountrights)<br/>       | Remove permissions from an account. When all the permissions are removed, the account is deleted.<br/> |



 

### Trusted Domain Functions

The following functions create, enumerate, and delete trusted domains and set and retrieve trusted domain information.



| Function                                                                                                                                                    | Description                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**LsaCreateTrustedDomainEx**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacreatetrusteddomainex)<br/>                                                                                     | Creates a new [**TrustedDomain**](trusteddomain-object.md) object.<br/>            |
| [**LsaDeleteTrustedDomain**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsadeletetrusteddomain)<br/>                                                                                         | Removes a [**TrustedDomain**](trusteddomain-object.md) object.<br/>                |
| [**LsaEnumerateTrustedDomains**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumeratetrusteddomains)<br/> [**LsaEnumerateTrustedDomainsEx**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumeratetrusteddomainsex)<br/> | Enumerates the domains currently trusted by the local system.<br/>                  |
| [**LsaOpenTrustedDomainByName**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaopentrusteddomainbyname)<br/>                                                                                 | Opens a handle to a [**TrustedDomain**](trusteddomain-object.md) object.<br/>      |
| [**LsaQueryTrustedDomainInfo**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaquerytrusteddomaininfo)<br/>                                                                                   | Retrieves information about a trusted domain. The domain is specified by SID.<br/>  |
| [**LsaQueryTrustedDomainInfoByName**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaquerytrusteddomaininfobyname)<br/>                                                                       | Retrieves information about a trusted domain. The domain is specified by name.<br/> |
| [**LsaSetTrustedDomainInfoByName**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsasettrusteddomaininfobyname)<br/>                                                                           | Sets information for a trusted domain. The domain is specified by name.<br/>        |
| [**LsaSetTrustedDomainInformation**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsasettrusteddomaininformation)<br/>                                                                         | Sets information for a trusted domain. The domain is specified by SID.<br/>         |



 

### Private Data Functions

Do not use the LSA private data functions. Instead, use the [**CryptProtectData**](/windows/desktop/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/desktop/api/dpapi/nf-dpapi-cryptunprotectdata) functions.



| Function                                                            | Description                                 |
|---------------------------------------------------------------------|---------------------------------------------|
| [**LsaRetrievePrivateData**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaretrieveprivatedata)<br/> | Retrieves and decrypts a string.<br/> |
| [**LsaStorePrivateData**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsastoreprivatedata)<br/>       | Encrypts and stores a string.<br/>    |



 

### Miscellaneous Functions

The LSA Policy API has the following three functions that do not fit into any of the other LSA Policy function categories.



| Function                                                          | Description                                                                                                                       |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**LsaClose**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaclose)<br/>                           | Closes a handle to a [**Policy**](policy-object.md) object or a [**TrustedDomain**](trusteddomain-object.md) object.<br/> |
| [**LsaFreeMemory**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsafreememory)<br/>                 | Frees a buffer allocated by an LSA function.<br/>                                                                           |
| [**LsaNtStatusToWinError**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsantstatustowinerror)<br/> | Converts an **NTSTATUS** value to a Windows error code.<br/>                                                                |



 

## Managed Service Account Functions

The following functions are used to create, enumerate, find, and delete managed service accounts.



| Function                                                                      | Description                                                                                                                 |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**NetAddServiceAccount**](/windows/desktop/api/Lmaccess/nf-lmaccess-netaddserviceaccount)<br/>               | Creates a managed service account.<br/>                                                                               |
| [**NetEnumerateServiceAccounts**](/windows/desktop/api/Lmaccess/nf-lmaccess-netenumerateserviceaccounts)<br/> | Enumerates the server accounts on the specified server.<br/>                                                          |
| [**NetIsServiceAccount**](/windows/desktop/api/Lmaccess/nf-lmaccess-netisserviceaccount)<br/>                 | Tests whether the specified service account exists in the Netlogon store on the specified server.<br/>                |
| [**NetRemoveServiceAccount**](/windows/desktop/api/Lmaccess/nf-lmaccess-netremoveserviceaccount)<br/>         | Deletes the specified service account from the [Active Directory](/windows/desktop/AD/active-directory-domain-services) database.<br/> |



 

## Password Filter Functions

The following [*password filter*](/windows/desktop/SecGloss/p-gly) functions are implemented by custom password filter DLLs to provide password filtering and password change notification.



| Function                                                            | Description                                                     |
|---------------------------------------------------------------------|-----------------------------------------------------------------|
| [**InitializeChangeNotify**](/windows/desktop/api/Ntsecapi/nc-ntsecapi-psam_init_notification_routine)<br/> | Indicates that a password filter DLL is initialized.<br/> |
| [**PasswordChangeNotify**](/windows/desktop/api/Ntsecapi/nc-ntsecapi-psam_password_notification_routine)<br/>     | Indicates that a password has been changed.<br/>          |
| [**PasswordFilter**](/windows/desktop/api/Ntsecapi/nc-ntsecapi-psam_password_filter_routine)<br/>                 | Validates a new password based on password policy.<br/>   |



 

## Safer Functions

The following Safer functions can be used to check the safer level of any executable and to log events.



| Function                                                         | Description                                                                                                                                                                          |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SaferCloseLevel**](/windows/desktop/api/WinSafer/nf-winsafer-safercloselevel)                       | Closes a SAFER\_LEVEL\_HANDLE opened by using the [**SaferIdentifyLevel**](/windows/desktop/api/WinSafer/nf-winsafer-saferidentifylevel) function or the [**SaferCreateLevel**](/windows/desktop/api/WinSafer/nf-winsafer-safercreatelevel) function.<br/> |
| [**SaferComputeTokenFromLevel**](/windows/desktop/api/WinSafer/nf-winsafer-safercomputetokenfromlevel) | Restricts a token using restrictions specified by a SAFER\_LEVEL\_HANDLE.<br/>                                                                                                 |
| [**SaferCreateLevel**](/windows/desktop/api/WinSafer/nf-winsafer-safercreatelevel)                     | Opens a SAFER\_LEVEL\_HANDLE.<br/>                                                                                                                                             |
| [**SaferGetLevelInformation**](/windows/desktop/api/WinSafer/nf-winsafer-safergetlevelinformation)     | Retrieves information about a policy level.<br/>                                                                                                                               |
| [**SaferGetPolicyInformation**](/windows/desktop/api/WinSafer/nf-winsafer-safergetpolicyinformation)   | Retrieves information about a policy.<br/>                                                                                                                                     |
| [**SaferIdentifyLevel**](/windows/desktop/api/WinSafer/nf-winsafer-saferidentifylevel)                 | Retrieves information about a level.<br/>                                                                                                                                      |
| [**SaferiIsExecutableFileType**](/windows/desktop/api/WinSafer/nf-winsafer-saferiisexecutablefiletype) | Determines whether a specified file is an executable file.<br/>                                                                                                                |
| [**SaferRecordEventLogEntry**](/windows/desktop/api/WinSafer/nf-winsafer-saferrecordeventlogentry)     | Sends a message to the event log.<br/>                                                                                                                                         |
| [**SaferSetLevelInformation**](/windows/desktop/api/WinSafer/nf-winsafer-safersetlevelinformation)     | Sets the information about a policy level.<br/>                                                                                                                                |
| [**SaferSetPolicyInformation**](/windows/desktop/api/WinSafer/nf-winsafer-safergetlevelinformation)    | Sets the global policy controls.<br/>                                                                                                                                          |



 

 

