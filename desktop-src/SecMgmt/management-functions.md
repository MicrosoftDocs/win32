---
Description: 'Lists support functions provided by the Security Configuration tool set.'
ms.assetid: '5a771014-1706-490f-8540-ec516652cb83'
title: Security Management Functions
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
| [**PFSCE\_FREE\_INFO**](pfsce-free-info.md)<br/>   | Used to free memory allocated by these support functions.<br/>                        |
| [**PFSCE\_LOG\_INFO**](pfsce-log-info.md)<br/>     | Used to log message to the configuration log file or analysis log file.<br/>          |
| [**PFSCE\_QUERY\_INFO**](pfsce-query-info.md)<br/> | Used to query the configuration and analysis information for a specific service.<br/> |
| [**PFSCE\_SET\_INFO**](pfsce-set-info.md)<br/>     | Used to set configuration and analysis information for a specific service.<br/>       |



 

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
| [**LsaEnumerateAccountsWithUserRight**](lsaenumerateaccountswithuserright.md)<br/>         | Enumerates all the accounts that have a specified user permission.<br/>                                                                                                                                                                                                                                                                         |
| [**LsaEnumerateTrustedDomainsEx**](lsaenumeratetrusteddomainsex.md)<br/>                   | Enumerates the trusted domains.<br/>                                                                                                                                                                                                                                                                                                            |
| [**LsaLookupNames**](lsalookupnames.md)<br/>                                               | Maps the specified names to their SIDs. Returns the SID as an RID/Domain SID pair.<br/>                                                                                                                                                                                                                                                         |
| [**LsaLookupNames2**](lsalookupnames2.md)<br/>                                             | Maps the specified names to their SIDs. Returns the SID as a single element.<br/>                                                                                                                                                                                                                                                               |
| [**LsaLookupPrivilegeValue**](lsalookupprivilegevalue.md)<br/>                             | Retrieves the [*locally unique identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-locally-unique-identifier-gly) (LUID) used by the [*Local Security Authority*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-local-security-authority-gly) (LSA) to represent the specified privilege name.<br/> |
| [**LsaLookupSids**](lsalookupsids.md)<br/>                                                 | Maps the specified account names to their SIDs.<br/>                                                                                                                                                                                                                                                                                            |
| [**LsaRegisterPolicyChangeNotification**](lsaregisterpolicychangenotification.md)<br/>     | Registers an event object to receive notifications when the local policy information changes.<br/>                                                                                                                                                                                                                                              |
| [**LsaUnregisterPolicyChangeNotification**](lsaunregisterpolicychangenotification.md)<br/> | Unregisters an event object that is receiving policy change notifications.<br/>                                                                                                                                                                                                                                                                 |



 

### Account Functions

The following functions add, enumerate, and delete permissions for an account.



| Function                                                                  | Description                                                                                                  |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**LsaAddAccountRights**](lsaaddaccountrights.md)<br/>             | Add permissions to an account. If the account does not already exist, it is created.<br/>              |
| [**LsaEnumerateAccountRights**](lsaenumerateaccountrights.md)<br/> | Enumerate the permissions granted to an account.<br/>                                                  |
| [**LsaRemoveAccountRights**](lsaremoveaccountrights.md)<br/>       | Remove permissions from an account. When all the permissions are removed, the account is deleted.<br/> |



 

### Trusted Domain Functions

The following functions create, enumerate, and delete trusted domains and set and retrieve trusted domain information.



| Function                                                                                                                                                    | Description                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**LsaCreateTrustedDomainEx**](lsacreatetrusteddomainex.md)<br/>                                                                                     | Creates a new [**TrustedDomain**](trusteddomain-object.md) object.<br/>            |
| [**LsaDeleteTrustedDomain**](lsadeletetrusteddomain.md)<br/>                                                                                         | Removes a [**TrustedDomain**](trusteddomain-object.md) object.<br/>                |
| [**LsaEnumerateTrustedDomains**](lsaenumeratetrusteddomains.md)<br/> [**LsaEnumerateTrustedDomainsEx**](lsaenumeratetrusteddomainsex.md)<br/> | Enumerates the domains currently trusted by the local system.<br/>                  |
| [**LsaOpenTrustedDomainByName**](lsaopentrusteddomainbyname.md)<br/>                                                                                 | Opens a handle to a [**TrustedDomain**](trusteddomain-object.md) object.<br/>      |
| [**LsaQueryTrustedDomainInfo**](lsaquerytrusteddomaininfo.md)<br/>                                                                                   | Retrieves information about a trusted domain. The domain is specified by SID.<br/>  |
| [**LsaQueryTrustedDomainInfoByName**](lsaquerytrusteddomaininfobyname.md)<br/>                                                                       | Retrieves information about a trusted domain. The domain is specified by name.<br/> |
| [**LsaSetTrustedDomainInfoByName**](lsasettrusteddomaininfobyname.md)<br/>                                                                           | Sets information for a trusted domain. The domain is specified by name.<br/>        |
| [**LsaSetTrustedDomainInformation**](lsasettrusteddomaininformation.md)<br/>                                                                         | Sets information for a trusted domain. The domain is specified by SID.<br/>         |



 

### Private Data Functions

Do not use the LSA private data functions. Instead, use the [**CryptProtectData**](https://msdn.microsoft.com/library/windows/desktop/aa380261) and [**CryptUnprotectData**](https://msdn.microsoft.com/library/windows/desktop/aa380882) functions.



| Function                                                            | Description                                 |
|---------------------------------------------------------------------|---------------------------------------------|
| [**LsaRetrievePrivateData**](lsaretrieveprivatedata.md)<br/> | Retrieves and decrypts a string.<br/> |
| [**LsaStorePrivateData**](lsastoreprivatedata.md)<br/>       | Encrypts and stores a string.<br/>    |



 

### Miscellaneous Functions

The LSA Policy API has the following three functions that do not fit into any of the other LSA Policy function categories.



| Function                                                          | Description                                                                                                                       |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**LsaClose**](lsaclose.md)<br/>                           | Closes a handle to a [**Policy**](policy-object.md) object or a [**TrustedDomain**](trusteddomain-object.md) object.<br/> |
| [**LsaFreeMemory**](lsafreememory.md)<br/>                 | Frees a buffer allocated by an LSA function.<br/>                                                                           |
| [**LsaNtStatusToWinError**](lsantstatustowinerror.md)<br/> | Converts an **NTSTATUS** value to a Windows error code.<br/>                                                                |



 

## Managed Service Account Functions

The following functions are used to create, enumerate, find, and delete managed service accounts.



| Function                                                                      | Description                                                                                                                 |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**NetAddServiceAccount**](netaddserviceaccount.md)<br/>               | Creates a managed service account.<br/>                                                                               |
| [**NetEnumerateServiceAccounts**](netenumerateserviceaccounts.md)<br/> | Enumerates the server accounts on the specified server.<br/>                                                          |
| [**NetIsServiceAccount**](netisserviceaccount.md)<br/>                 | Tests whether the specified service account exists in the Netlogon store on the specified server.<br/>                |
| [**NetRemoveServiceAccount**](netremoveserviceaccount.md)<br/>         | Deletes the specified service account from the [Active Directory](https://msdn.microsoft.com/library/aa362244) database.<br/> |



 

## Password Filter Functions

The following [*password filter*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-password-filter-gly) functions are implemented by custom password filter DLLs to provide password filtering and password change notification.



| Function                                                            | Description                                                     |
|---------------------------------------------------------------------|-----------------------------------------------------------------|
| [**InitializeChangeNotify**](initializechangenotify.md)<br/> | Indicates that a password filter DLL is initialized.<br/> |
| [**PasswordChangeNotify**](passwordchangenotify.md)<br/>     | Indicates that a password has been changed.<br/>          |
| [**PasswordFilter**](passwordfilter.md)<br/>                 | Validates a new password based on password policy.<br/>   |



 

## Safer Functions

The following Safer functions can be used to check the safer level of any executable and to log events.



| Function                                                         | Description                                                                                                                                                                          |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SaferCloseLevel**](safercloselevel.md)                       | Closes a SAFER\_LEVEL\_HANDLE opened by using the [**SaferIdentifyLevel**](saferidentifylevel.md) function or the [**SaferCreateLevel**](safercreatelevel.md) function.<br/> |
| [**SaferComputeTokenFromLevel**](safercomputetokenfromlevel.md) | Restricts a token using restrictions specified by a SAFER\_LEVEL\_HANDLE.<br/>                                                                                                 |
| [**SaferCreateLevel**](safercreatelevel.md)                     | Opens a SAFER\_LEVEL\_HANDLE.<br/>                                                                                                                                             |
| [**SaferGetLevelInformation**](safergetlevelinformation.md)     | Retrieves information about a policy level.<br/>                                                                                                                               |
| [**SaferGetPolicyInformation**](safergetpolicyinformation.md)   | Retrieves information about a policy.<br/>                                                                                                                                     |
| [**SaferIdentifyLevel**](saferidentifylevel.md)                 | Retrieves information about a level.<br/>                                                                                                                                      |
| [**SaferiIsExecutableFileType**](saferiisexecutablefiletype.md) | Determines whether a specified file is an executable file.<br/>                                                                                                                |
| [**SaferRecordEventLogEntry**](saferrecordeventlogentry.md)     | Sends a message to the event log.<br/>                                                                                                                                         |
| [**SaferSetLevelInformation**](safersetlevelinformation.md)     | Sets the information about a policy level.<br/>                                                                                                                                |
| [**SaferSetPolicyInformation**](safergetlevelinformation.md)    | Sets the global policy controls.<br/>                                                                                                                                          |



 

 

 




