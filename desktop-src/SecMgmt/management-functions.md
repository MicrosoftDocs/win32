---
Description: Lists support functions provided by the Security Configuration tool set.
ms.assetid: 5a771014-1706-490f-8540-ec516652cb83
title: Security Management Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**PFSCE\_FREE\_INFO**](/windows/win32/Scesvc/nc-scesvc-pfsce_free_info?branch=master)<br/>   | Used to free memory allocated by these support functions.<br/>                        |
| [**PFSCE\_LOG\_INFO**](/windows/win32/Scesvc/nc-scesvc-pfsce_log_info?branch=master)<br/>     | Used to log message to the configuration log file or analysis log file.<br/>          |
| [**PFSCE\_QUERY\_INFO**](/windows/win32/Scesvc/nc-scesvc-pfsce_query_info?branch=master)<br/> | Used to query the configuration and analysis information for a specific service.<br/> |
| [**PFSCE\_SET\_INFO**](/windows/win32/Scesvc/nc-scesvc-pfsce_set_info?branch=master)<br/>     | Used to set configuration and analysis information for a specific service.<br/>       |



 

## Attachment Engine Functions



| Function                                                              | Description                                                                                                                                                                                       |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SceSvcAttachmentAnalyze**](scesvcattachmentanalyze.md)<br/> | Implemented by the attachment engine DLL. The Security Configuration Engine calls this function when the system is analyzed.<br/>                                                           |
| [**SceSvcAttachmentConfig**](scesvcattachmentconfig.md)<br/>   | Implemented by the attachment engine DLL. The Security Configuration Engine calls this function when the system is configured.<br/>                                                         |
| [**SceSvcAttachmentUpdate**](scesvcattachmentupdate.md)<br/>   | Implemented by the attachment engine DLL. The Security Configuration Engine calls this function when it receives a configuration update request from the attachment snap-in extension.<br/> |



 

## LSA Policy Functions

The following topics provide reference information for the [*Local Security Authority*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-local-security-authority-gly) (LSA) Policy functions.



| Topic                               | Description                                                                                                                                                                                   |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Policy Functions<br/>         | Details functions used to open the local [**Policy**](policy-object.md) object and to set or retrieve global policy information.<br/>                                                  |
| Account Functions<br/>        | Details functions used to manage account permissions and to create and delete user accounts.<br/>                                                                                       |
| Trusted Domain Functions<br/> | Details functions used to create and delete trusted domain relationships and to set and retrieve information about those trusted domains.<br/>                                          |
| Private Data Functions<br/>   | Do not use the LSA private data functions. Instead, use the [**CryptProtectData**](https://msdn.microsoft.com/library/windows/desktop/aa380261) and [**CryptUnprotectData**](https://msdn.microsoft.com/library/windows/desktop/aa380882) functions.<br/> |
| Miscellaneous Functions<br/>  | Details functions not described elsewhere.<br/>                                                                                                                                         |



 

### Policy Functions

The following functions enumerate user accounts and trusted domains, receive policy change notifications, and lookup account names and SIDs.



| Function                                                                                          | Description                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**LsaEnumerateAccountsWithUserRight**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaenumerateaccountswithuserright?branch=master)<br/>         | Enumerates all the accounts that have a specified user permission.<br/>                                                                                                                                                                                                                                                                         |
| [**LsaEnumerateTrustedDomainsEx**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaenumeratetrusteddomainsex?branch=master)<br/>                   | Enumerates the trusted domains.<br/>                                                                                                                                                                                                                                                                                                            |
| [**LsaLookupNames**](/windows/win32/Ntsecapi/nf-ntsecapi-lsalookupnames?branch=master)<br/>                                               | Maps the specified names to their SIDs. Returns the SID as an RID/Domain SID pair.<br/>                                                                                                                                                                                                                                                         |
| [**LsaLookupNames2**](/windows/win32/Ntsecapi/nf-ntsecapi-lsalookupnames2?branch=master)<br/>                                             | Maps the specified names to their SIDs. Returns the SID as a single element.<br/>                                                                                                                                                                                                                                                               |
| [**LsaLookupPrivilegeValue**](/windows/win32/ntlsa/nf-ntlsa-lsalookupprivilegevalue?branch=master)<br/>                             | Retrieves the [*locally unique identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-locally-unique-identifier-gly) (LUID) used by the [*Local Security Authority*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-local-security-authority-gly) (LSA) to represent the specified privilege name.<br/> |
| [**LsaLookupSids**](/windows/win32/Ntsecapi/nf-ntsecapi-lsalookupsids?branch=master)<br/>                                                 | Maps the specified account names to their SIDs.<br/>                                                                                                                                                                                                                                                                                            |
| [**LsaRegisterPolicyChangeNotification**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaregisterpolicychangenotification?branch=master)<br/>     | Registers an event object to receive notifications when the local policy information changes.<br/>                                                                                                                                                                                                                                              |
| [**LsaUnregisterPolicyChangeNotification**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaunregisterpolicychangenotification?branch=master)<br/> | Unregisters an event object that is receiving policy change notifications.<br/>                                                                                                                                                                                                                                                                 |



 

### Account Functions

The following functions add, enumerate, and delete permissions for an account.



| Function                                                                  | Description                                                                                                  |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**LsaAddAccountRights**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaaddaccountrights?branch=master)<br/>             | Add permissions to an account. If the account does not already exist, it is created.<br/>              |
| [**LsaEnumerateAccountRights**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaenumerateaccountrights?branch=master)<br/> | Enumerate the permissions granted to an account.<br/>                                                  |
| [**LsaRemoveAccountRights**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaremoveaccountrights?branch=master)<br/>       | Remove permissions from an account. When all the permissions are removed, the account is deleted.<br/> |



 

### Trusted Domain Functions

The following functions create, enumerate, and delete trusted domains and set and retrieve trusted domain information.



| Function                                                                                                                                                    | Description                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**LsaCreateTrustedDomainEx**](/windows/win32/Ntsecapi/nf-ntsecapi-lsacreatetrusteddomainex?branch=master)<br/>                                                                                     | Creates a new [**TrustedDomain**](trusteddomain-object.md) object.<br/>            |
| [**LsaDeleteTrustedDomain**](/windows/win32/Ntsecapi/nf-ntsecapi-lsadeletetrusteddomain?branch=master)<br/>                                                                                         | Removes a [**TrustedDomain**](trusteddomain-object.md) object.<br/>                |
| [**LsaEnumerateTrustedDomains**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaenumeratetrusteddomains?branch=master)<br/> [**LsaEnumerateTrustedDomainsEx**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaenumeratetrusteddomainsex?branch=master)<br/> | Enumerates the domains currently trusted by the local system.<br/>                  |
| [**LsaOpenTrustedDomainByName**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaopentrusteddomainbyname?branch=master)<br/>                                                                                 | Opens a handle to a [**TrustedDomain**](trusteddomain-object.md) object.<br/>      |
| [**LsaQueryTrustedDomainInfo**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaquerytrusteddomaininfo?branch=master)<br/>                                                                                   | Retrieves information about a trusted domain. The domain is specified by SID.<br/>  |
| [**LsaQueryTrustedDomainInfoByName**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaquerytrusteddomaininfobyname?branch=master)<br/>                                                                       | Retrieves information about a trusted domain. The domain is specified by name.<br/> |
| [**LsaSetTrustedDomainInfoByName**](/windows/win32/Ntsecapi/nf-ntsecapi-lsasettrusteddomaininfobyname?branch=master)<br/>                                                                           | Sets information for a trusted domain. The domain is specified by name.<br/>        |
| [**LsaSetTrustedDomainInformation**](/windows/win32/Ntsecapi/nf-ntsecapi-lsasettrusteddomaininformation?branch=master)<br/>                                                                         | Sets information for a trusted domain. The domain is specified by SID.<br/>         |



 

### Private Data Functions

Do not use the LSA private data functions. Instead, use the [**CryptProtectData**](https://msdn.microsoft.com/library/windows/desktop/aa380261) and [**CryptUnprotectData**](https://msdn.microsoft.com/library/windows/desktop/aa380882) functions.



| Function                                                            | Description                                 |
|---------------------------------------------------------------------|---------------------------------------------|
| [**LsaRetrievePrivateData**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaretrieveprivatedata?branch=master)<br/> | Retrieves and decrypts a string.<br/> |
| [**LsaStorePrivateData**](/windows/win32/Ntsecapi/nf-ntsecapi-lsastoreprivatedata?branch=master)<br/>       | Encrypts and stores a string.<br/>    |



 

### Miscellaneous Functions

The LSA Policy API has the following three functions that do not fit into any of the other LSA Policy function categories.



| Function                                                          | Description                                                                                                                       |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**LsaClose**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaclose?branch=master)<br/>                           | Closes a handle to a [**Policy**](policy-object.md) object or a [**TrustedDomain**](trusteddomain-object.md) object.<br/> |
| [**LsaFreeMemory**](/windows/win32/Ntsecapi/nf-ntsecapi-lsafreememory?branch=master)<br/>                 | Frees a buffer allocated by an LSA function.<br/>                                                                           |
| [**LsaNtStatusToWinError**](/windows/win32/Ntsecapi/nf-ntsecapi-lsantstatustowinerror?branch=master)<br/> | Converts an **NTSTATUS** value to a Windows error code.<br/>                                                                |



 

## Managed Service Account Functions

The following functions are used to create, enumerate, find, and delete managed service accounts.



| Function                                                                      | Description                                                                                                                 |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**NetAddServiceAccount**](/windows/win32/Lmaccess/nf-lmaccess-netaddserviceaccount?branch=master)<br/>               | Creates a managed service account.<br/>                                                                               |
| [**NetEnumerateServiceAccounts**](/windows/win32/Lmaccess/nf-lmaccess-netenumerateserviceaccounts?branch=master)<br/> | Enumerates the server accounts on the specified server.<br/>                                                          |
| [**NetIsServiceAccount**](/windows/win32/Lmaccess/nf-lmaccess-netisserviceaccount?branch=master)<br/>                 | Tests whether the specified service account exists in the Netlogon store on the specified server.<br/>                |
| [**NetRemoveServiceAccount**](/windows/win32/Lmaccess/nf-lmaccess-netremoveserviceaccount?branch=master)<br/>         | Deletes the specified service account from the [Active Directory](https://msdn.microsoft.com/library/aa362244) database.<br/> |



 

## Password Filter Functions

The following [*password filter*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-password-filter-gly) functions are implemented by custom password filter DLLs to provide password filtering and password change notification.



| Function                                                            | Description                                                     |
|---------------------------------------------------------------------|-----------------------------------------------------------------|
| [**InitializeChangeNotify**](/windows/win32/Ntsecapi/nc-ntsecapi-psam_init_notification_routine?branch=master)<br/> | Indicates that a password filter DLL is initialized.<br/> |
| [**PasswordChangeNotify**](/windows/win32/Ntsecapi/nc-ntsecapi-psam_password_notification_routine?branch=master)<br/>     | Indicates that a password has been changed.<br/>          |
| [**PasswordFilter**](/windows/win32/Ntsecapi/nc-ntsecapi-psam_password_filter_routine?branch=master)<br/>                 | Validates a new password based on password policy.<br/>   |



 

## Safer Functions

The following Safer functions can be used to check the safer level of any executable and to log events.



| Function                                                         | Description                                                                                                                                                                          |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SaferCloseLevel**](/windows/win32/WinSafer/nf-winsafer-safercloselevel?branch=master)                       | Closes a SAFER\_LEVEL\_HANDLE opened by using the [**SaferIdentifyLevel**](/windows/win32/WinSafer/nf-winsafer-saferidentifylevel?branch=master) function or the [**SaferCreateLevel**](/windows/win32/WinSafer/nf-winsafer-safercreatelevel?branch=master) function.<br/> |
| [**SaferComputeTokenFromLevel**](/windows/win32/WinSafer/nf-winsafer-safercomputetokenfromlevel?branch=master) | Restricts a token using restrictions specified by a SAFER\_LEVEL\_HANDLE.<br/>                                                                                                 |
| [**SaferCreateLevel**](/windows/win32/WinSafer/nf-winsafer-safercreatelevel?branch=master)                     | Opens a SAFER\_LEVEL\_HANDLE.<br/>                                                                                                                                             |
| [**SaferGetLevelInformation**](/windows/win32/WinSafer/nf-winsafer-safergetlevelinformation?branch=master)     | Retrieves information about a policy level.<br/>                                                                                                                               |
| [**SaferGetPolicyInformation**](/windows/win32/WinSafer/nf-winsafer-safergetpolicyinformation?branch=master)   | Retrieves information about a policy.<br/>                                                                                                                                     |
| [**SaferIdentifyLevel**](/windows/win32/WinSafer/nf-winsafer-saferidentifylevel?branch=master)                 | Retrieves information about a level.<br/>                                                                                                                                      |
| [**SaferiIsExecutableFileType**](/windows/win32/WinSafer/nf-winsafer-saferiisexecutablefiletype?branch=master) | Determines whether a specified file is an executable file.<br/>                                                                                                                |
| [**SaferRecordEventLogEntry**](/windows/win32/WinSafer/nf-winsafer-saferrecordeventlogentry?branch=master)     | Sends a message to the event log.<br/>                                                                                                                                         |
| [**SaferSetLevelInformation**](/windows/win32/WinSafer/nf-winsafer-safersetlevelinformation?branch=master)     | Sets the information about a policy level.<br/>                                                                                                                                |
| [**SaferSetPolicyInformation**](/windows/win32/WinSafer/nf-winsafer-safergetlevelinformation?branch=master)    | Sets the global policy controls.<br/>                                                                                                                                          |



 

 

 




