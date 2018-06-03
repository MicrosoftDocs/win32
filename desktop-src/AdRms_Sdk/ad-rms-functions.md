---
Description: The Active Directory Rights Management Services (AD RMS) SDK provides the following functions, grouped by use.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b3b4e7c6-d3d3-4bf7-b6c4-9502a56a7223
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS Functions

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) SDK provides the following functions, grouped by use.

-   [Environment Management and Setup](#environment-management-and-setup)
-   [Issuance License Creation and Property Setting Functions](#issuance-license-creation-and-property-setting-functions)
-   [Handle Functions](#handle-functions)
-   [Unbound License Navigation](#unbound-license-navigation)
-   [Bound License Navigation and Creation](#unbound-license-navigation)
-   [License, Certificate, and Advisory List Management](#license-certificate-and-advisory-list-management)
-   [Cryptography](#cryptography)
-   [Miscellaneous Functions and Topics](#miscellaneous-functions-and-topics)
-   [Related topics](#related-topics)

## Environment Management and Setup

To use the AD RMS infrastructure, the client computer and the Active Directory user account must be activated. Your application also must acquire handles to a secure environment, a client session, a license storage session, and more.



| Function                                                                 | Description                                                                                                                                                                                            |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRMActivate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmactivate)                                       | Obtains a lockbox for a [*machine certificate*](https://www.bing.com/search?q=*machine certificate*) or a [*rights account certificate*](https://www.bing.com/search?q=*rights account certificate*) for a user.                   |
| [**DRMCheckSecurity**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmchecksecurity)                             | Performs a security check on all or part of the environment.                                                                                                                                           |
| [**DRMCloseSession**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosesession)                               | Closes a client session.                                                                                                                                                                               |
| [**DRMCreateClientSession**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateclientsession)                 | Creates a client session, which hosts license storage sessions and allows activation and other functions.                                                                                              |
| [**DRMCreateLicenseStorageSession**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreatelicensestoragesession) | Creates a license storage session, which is used in activation and other function calls.                                                                                                               |
| [**DRMDuplicateSession**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmduplicatesession)                       | Duplicates a client or license storage session.                                                                                                                                                        |
| [**DRMGetClientVersion**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetclientversion)                       | Returns the version number of the Active Directory Rights Management Services client software and whether the hierarchy is for Production or Pre-production purposes.                                  |
| [**DRMGetEnvironmentInfo**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetenvironmentinfo)                   | Returns information about a secure environment.                                                                                                                                                        |
| [**DRMGetIntervalTime**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetintervaltime)                         | Retrieves the number of days from issuance that can pass before an end–user license must be renewed.                                                                                                   |
| [**DRMGetOwnerLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetownerlicense)                         | Retrieves from memory an issuance license created by a call to the [**DRMGetSignedIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicense) function with the **DRM\_OWNER\_LICENSE\_NO\_PERSIST** flag set. |
| [**DRMGetProcAddress**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetprocaddress)                           | Returns the address of a function in a library. [**DRMGetProcAddress**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetprocaddress) is the secure version of the [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) function.                        |
| [**DRMGetSecurityProvider**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsecurityprovider)                 | Retrieves the path to a lockbox file used in [**DRMInitEnvironment**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drminitenvironment).                                                                                                         |
| [**DRMGetServiceLocation**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetservicelocation)                   | Retrieves the URL of a server that can perform various AD RMS services, such as computer and user activation or license acquisition.                                                                   |
| [**DRMInitEnvironment**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drminitenvironment)                         | Creates a secure environment for all other rights management functions to use.                                                                                                                         |
| [**DRMIsActivated**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmisactivated)                                 | Indicates whether the current user or machine is activated.                                                                                                                                            |
| [**DRMIsWindowProtected**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmiswindowprotected)                     | Indicates whether a window is associated with a protected environment.                                                                                                                                 |
| [**DRMLoadLibrary**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmloadlibrary)                                 | An authenticated method for loading DLLs.                                                                                                                                                              |
| [**DRMRegisterContent**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmregistercontent)                         | Allows the AD RMS system to keep a reference count of open AD RMS-protected documents. When the reference count is greater than zero, print screen is not enabled in all applications.                 |
| [**DRMRegisterRevocationList**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmregisterrevocationlist)           | Registers a rights revocation list on the client.                                                                                                                                                      |
| [**DRMRegisterProtectedWindow**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmregisterprotectedwindow)         | Registers a window in the protected environment.                                                                                                                                                       |
| [**DRMRepair**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmrepair)                                           | Repairs a client computer by deleting certificates previously created for the computer or user.                                                                                                        |
| [**DRMSetIntervalTime**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetintervaltime)                         | Specifies the number of days from issuance that can pass before an end–user license must be renewed.                                                                                                   |
| [**DRMSetGlobalOptions**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetglobaloptions)                       | Sets the transport protocol to a specified value and optionally specifies whether the AD RMS server lockbox is used.                                                                                   |



 

## Issuance License Creation and Property Setting Functions

The following functions are used to create an issuance license and to specify or retrieve information in the license.



| Function                                                                       | Description                                                                                                                               |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRMAcquireIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireissuancelicensetemplate) | Retrieves license templates from a server.                                                                                                |
| [**DRMAddRightWithUser**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmaddrightwithuser)                             | Adds a right tied to a specific user.                                                                                                     |
| [**DRMClearAllRights**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclearallrights)                                 | Clears the rights from an existing issuance license.                                                                                      |
| [**DRMCreateIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateissuancelicense)                   | Creates an issuance license from scratch or from a template.                                                                              |
| [**DRMCreateRight**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateright)                                       | Creates an XrML right that will define the rights granted to a user or group.                                                             |
| [**DRMCreateUser**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateuser)                                         | Creates a user object that will be assigned a right.                                                                                      |
| [**DRMGetApplicationSpecificData**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetapplicationspecificdata)         | Retrieves a name-value pair of arbitrary application-specific information.                                                                |
| [**DRMGetIssuanceLicenseInfo**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetissuancelicenseinfo)                 | Retrieves information about a prototype issuance license.                                                                                 |
| [**DRMGetIssuanceLicenseTemplate**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetissuancelicensetemplate)         | Obtains a template from an issuance license.                                                                                              |
| [**DRMGetMetaData**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetmetadata)                                       | Retrieves metadata about the content that the issuance license is associated with.                                                        |
| [**DRMGetNameAndDescription**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetnameanddescription)                   | Retrieves information about a specific certificate in an issuance license chain.                                                          |
| [**DRMGetRevocationPoint**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetrevocationpoint)                         | Retrieves a URL where a revocation list for a license can be obtained.                                                                    |
| [**DRMGetRightExtendedInfo**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetrightextendedinfo)                     | Retrieves custom name-value pairs attached to a right.                                                                                    |
| [**DRMGetRightInfo**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetrightinfo)                                     | Retrieves information about a previously created right.                                                                                   |
| [**DRMGetSignedIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicense)             | Acquires a signed issuance license online or offline, or produces an unsigned license that can be signed later.                           |
| [**DRMGetSignedIssuanceLicenseEx**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetsignedissuancelicenseex)         | Acquires a signed issuance license offline, using a specified client licensor certificate (CLC) and rights account certificate (RAC).     |
| [**DRMGetUsagePolicy**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetusagepolicy)                                 | Gets a usage policy that requires, or denies, access to a right based on application name, version, or other application characteristics. |
| [**DRMGetUserInfo**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetuserinfo)                                       | Retrieves information about a user object.                                                                                                |
| [**DRMGetUserRights**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetuserrights)                                   | Retrieves user/right pairs from a prototype issuance license.                                                                             |
| [**DRMGetUsers**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetusers)                                             | Retrieves a specific user from the issuance license.                                                                                      |
| [**DRMSetApplicationSpecificData**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetapplicationspecificdata)         | Allows an issuance license to store arbitrary name-value pairs for use by the content-consuming application.                              |
| [**DRMSetMetaData**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetmetadata)                                       | Stores metadata about content associated with the issuance license.                                                                       |
| [**DRMSetNameAndDescription**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetnameanddescription)                   | Specifies the content name and description in the issuance license in several (human-readable) languages.                                 |
| [**DRMSetRevocationPoint**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetrevocationpoint)                         | Sets a refresh rate and a location to obtain a revocation list.                                                                           |
| [**DRMSetUsagePolicy**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmsetusagepolicy)                                 | Sets a usage policy that requires, or denies, access to a right based on application name, version, or other application characteristics. |



 

## Handle Functions

AD RMS functions use handles to represent objects. You should create, copy, and delete these handles by using the appropriate function, so the system can maintain a correct reference count and manage resources appropriately. For more information, see [AD RMS Handles and Sessions](ad-rms-handles-and-sessions.md).



| Function                                                               | Description                                                                                              |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**DRMCloseEnvironmentHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcloseenvironmenthandle)         | Closes an environment handle.                                                                            |
| [**DRMCloseHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosehandle)                               | Closes libraries, environments, and other miscellaneous bound license objects of the **DRMHANDLE** type. |
| [**DRMClosePubHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosepubhandle)                         | Closes a previously created **DRMPUBHANDLE**.                                                            |
| [**DRMCloseQueryHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosequeryhandle)                     | Closes a handle to an unbound license object.                                                            |
| [**DRMDuplicateEnvironmentHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmduplicateenvironmenthandle) | Creates a copy of an environment handle.                                                                 |
| [**DRMDuplicateHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmduplicatehandle)                       | Duplicates a handle.                                                                                     |
| [**DRMDuplicatePubHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmduplicatepubhandle)                 | Used to copy a **DRMPUBHANDLE**.                                                                         |



 

## Unbound License Navigation

You can use the following functions to navigate the underlying XrML of a license in an object-oriented fashion. These functions makes it easier to create, retrieve, and modify rights, conditions, users, and other XrML structures.



| Function                                                                         | Description                                                                                             |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**DRMGetUnboundLicenseAttribute**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseattribute)           | Retrieves an unbound license attribute from the underlying XrML.                                        |
| [**DRMGetUnboundLicenseAttributeCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseattributecount) | Retrieves the number of occurrences of an attribute within an object in an unbound license.             |
| [**DRMGetUnboundLicenseObject**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseobject)                 | Retrieves an object of a specified type in an unbound license.                                          |
| [**DRMGetUnboundLicenseObjectCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseobjectcount)       | Counts the instances of an object within a given branch of the license.                                 |
| [**DRMParseUnboundLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmparseunboundlicense)                         | Creates a handle to an unbound license, to allow an application to navigate its objects and attributes. |



 

## Bound License Navigation and Creation

The AD RMS system uses both bound and unbound licenses. Bound licenses include only information relevant to the current computer and user for the current task. Unbound licenses are not filtered in this manner. Bound licenses require a secure environment, but unbound licenses do not. The two license types are not interchangeable.



| Function                                                                     | Description                                                                          |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**DRMCreateBoundLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateboundlicense)                       | Creates a bound license from a locally stored license.                               |
| [**DRMCreateEnablingPrincipal**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateenablingprincipal)             | Creates an enabling principal.                                                       |
| [**DRMGetBoundLicenseAttribute**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseattribute)           | Retrieves a bound license attribute.                                                 |
| [**DRMGetBoundLicenseAttributeCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseattributecount) | Retrieves the number of occurrences of a particular attribute within a given object. |
| [**DRMGetBoundLicenseObject**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseobject)                 | Retrieves an object of a specified type in a bound license.                          |
| [**DRMGetBoundLicenseObjectCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseobjectcount)       | Retrieves the number of occurrences of a particular attribute within a given object. |



 

## License, Certificate, and Advisory List Management

The AD RMS system maintains a certificate store for each user who logs onto the computer. The AD RMS system also maintains a revocation list that describes licenses, secure repositories, or other objects that have had their rights revoked. This list must be periodically refreshed, in the interval specified by each license.



| Function                                                                 | Description                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRMAcquireAdvisories**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquireadvisories)                     | Retrieves revocation lists.                                                                                                                                                                                             |
| [**DRMAcquireLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquirelicense)                           | Attempts to acquire an [*end-user license*](https://www.bing.com/search?q=*end-user license*) or [*client licensor certificate*](https://www.bing.com/search?q=*client licensor certificate*) asynchronously.                                       |
| [**DRMAddLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmaddlicense)                                   | Adds an [*end-user license*](https://www.bing.com/search?q=*end-user license*) to the temporary license store.                                                                                                                        |
| [**DRMConstructCertificateChain**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmconstructcertificatechain)     | Builds a certificate chain from an arbitrary number of certificates.                                                                                                                                                    |
| [**DRMDeconstructCertificateChain**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmdeconstructcertificatechain) | Retrieves a certificate from a certificate chain.                                                                                                                                                                       |
| [**DRMDeleteLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmdeletelicense)                             | Deletes a license, [*client licensor certificate*](https://www.bing.com/search?q=*client licensor certificate*), or revocation list.                                                                                                  |
| [**DRMEnumerateLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmenumeratelicense)                       | Enumerates valid licenses, [*machine certificates*](https://www.bing.com/search?q=*machine certificates*) or [*rights account certificates*](https://www.bing.com/search?q=*rights account certificates*), and revocation lists for the current user. |
| [**DRMGetCertificateChainCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetcertificatechaincount)       | Retrieves the number of certificates in a certificate chain.                                                                                                                                                            |



 

## Cryptography

The AD RMS SDK contains the following cryptographic functions. You should not use other cryptographic systems to handle encryption or decryption of content.



| Function                                                                 | Description                                                   |
|--------------------------------------------------------------------------|---------------------------------------------------------------|
| [**DRMAttest**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmattest)                                           | Signs data.                                                   |
| [**DRMCreateEnablingBitsDecryptor**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateenablingbitsdecryptor) | Creates a **DRMDecrypt** object for an enabling principal.    |
| [**DRMCreateEnablingBitsEncryptor**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateenablingbitsencryptor) | Creates a **DRMEncrypt** object for an enabling principal.    |
| [**DRMDecrypt**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmdecrypt)                                         | Decrypts symmetrically encrypted data.                        |
| [**DRMEncrypt**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmencrypt)                                         | Encrypts data by using a content key.                         |
| [**DRMVerify**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmverify)                                           | Verifies data signed by using [**DRMAttest**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmattest). |



 

## Miscellaneous Functions and Topics



| Function                                                       | Description                                                               |
|----------------------------------------------------------------|---------------------------------------------------------------------------|
| [**DRMDecode**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmdecode)                                 | Decodes a string that is encoded with a common algorithm, such as base64. |
| [**DRMEncode**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmencode)                                 | Encodes data by using a public encoding method, such as base64.           |
| [**DRMGetInfo**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetinfo)                               | Retrieves information about an object from its handle.                    |
| [**DRMGetTime**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgettime)                               | Retrieves the time from a secure timer.                                   |
| [AD RMS Function Error Codes](ad-rms-function-error-codes.md) | Discusses common error codes returned by AD RMS functions.                |
| [AD RMS Handles and Sessions](ad-rms-handles-and-sessions.md) | Discusses handles to AD RMS objects.                                      |



 

## Related topics

<dl> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> </dl>

 

 



