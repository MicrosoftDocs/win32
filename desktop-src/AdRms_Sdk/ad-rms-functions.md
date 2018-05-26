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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
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
| [**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master)                                       | Obtains a lockbox for a [*machine certificate*](m-gly.md#-rm-machine-certificate-gly) or a [*rights account certificate*](r-gly.md#-rm-rights-account-certificate-gly) for a user.                   |
| [**DRMCheckSecurity**](/windows/previous-versions/Msdrm/nf-msdrm-drmchecksecurity?branch=master)                             | Performs a security check on all or part of the environment.                                                                                                                                           |
| [**DRMCloseSession**](/windows/previous-versions/Msdrm/nf-msdrm-drmclosesession?branch=master)                               | Closes a client session.                                                                                                                                                                               |
| [**DRMCreateClientSession**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateclientsession?branch=master)                 | Creates a client session, which hosts license storage sessions and allows activation and other functions.                                                                                              |
| [**DRMCreateLicenseStorageSession**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreatelicensestoragesession?branch=master) | Creates a license storage session, which is used in activation and other function calls.                                                                                                               |
| [**DRMDuplicateSession**](/windows/previous-versions/Msdrm/nf-msdrm-drmduplicatesession?branch=master)                       | Duplicates a client or license storage session.                                                                                                                                                        |
| [**DRMGetClientVersion**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetclientversion?branch=master)                       | Returns the version number of the Active Directory Rights Management Services client software and whether the hierarchy is for Production or Pre-production purposes.                                  |
| [**DRMGetEnvironmentInfo**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetenvironmentinfo?branch=master)                   | Returns information about a secure environment.                                                                                                                                                        |
| [**DRMGetIntervalTime**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetintervaltime?branch=master)                         | Retrieves the number of days from issuance that can pass before an end–user license must be renewed.                                                                                                   |
| [**DRMGetOwnerLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetownerlicense?branch=master)                         | Retrieves from memory an issuance license created by a call to the [**DRMGetSignedIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetsignedissuancelicense?branch=master) function with the **DRM\_OWNER\_LICENSE\_NO\_PERSIST** flag set. |
| [**DRMGetProcAddress**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetprocaddress?branch=master)                           | Returns the address of a function in a library. [**DRMGetProcAddress**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetprocaddress?branch=master) is the secure version of the [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) function.                        |
| [**DRMGetSecurityProvider**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetsecurityprovider?branch=master)                 | Retrieves the path to a lockbox file used in [**DRMInitEnvironment**](/windows/previous-versions/Msdrm/nf-msdrm-drminitenvironment?branch=master).                                                                                                         |
| [**DRMGetServiceLocation**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetservicelocation?branch=master)                   | Retrieves the URL of a server that can perform various AD RMS services, such as computer and user activation or license acquisition.                                                                   |
| [**DRMInitEnvironment**](/windows/previous-versions/Msdrm/nf-msdrm-drminitenvironment?branch=master)                         | Creates a secure environment for all other rights management functions to use.                                                                                                                         |
| [**DRMIsActivated**](/windows/previous-versions/Msdrm/nf-msdrm-drmisactivated?branch=master)                                 | Indicates whether the current user or machine is activated.                                                                                                                                            |
| [**DRMIsWindowProtected**](/windows/previous-versions/Msdrm/nf-msdrm-drmiswindowprotected?branch=master)                     | Indicates whether a window is associated with a protected environment.                                                                                                                                 |
| [**DRMLoadLibrary**](/windows/previous-versions/Msdrm/nf-msdrm-drmloadlibrary?branch=master)                                 | An authenticated method for loading DLLs.                                                                                                                                                              |
| [**DRMRegisterContent**](/windows/previous-versions/Msdrm/nf-msdrm-drmregistercontent?branch=master)                         | Allows the AD RMS system to keep a reference count of open AD RMS-protected documents. When the reference count is greater than zero, print screen is not enabled in all applications.                 |
| [**DRMRegisterRevocationList**](/windows/previous-versions/Msdrm/nf-msdrm-drmregisterrevocationlist?branch=master)           | Registers a rights revocation list on the client.                                                                                                                                                      |
| [**DRMRegisterProtectedWindow**](/windows/previous-versions/Msdrm/nf-msdrm-drmregisterprotectedwindow?branch=master)         | Registers a window in the protected environment.                                                                                                                                                       |
| [**DRMRepair**](/windows/previous-versions/Msdrm/nf-msdrm-drmrepair?branch=master)                                           | Repairs a client computer by deleting certificates previously created for the computer or user.                                                                                                        |
| [**DRMSetIntervalTime**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetintervaltime?branch=master)                         | Specifies the number of days from issuance that can pass before an end–user license must be renewed.                                                                                                   |
| [**DRMSetGlobalOptions**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetglobaloptions?branch=master)                       | Sets the transport protocol to a specified value and optionally specifies whether the AD RMS server lockbox is used.                                                                                   |



 

## Issuance License Creation and Property Setting Functions

The following functions are used to create an issuance license and to specify or retrieve information in the license.



| Function                                                                       | Description                                                                                                                               |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRMAcquireIssuanceLicenseTemplate**](/windows/previous-versions/Msdrm/nf-msdrm-drmacquireissuancelicensetemplate?branch=master) | Retrieves license templates from a server.                                                                                                |
| [**DRMAddRightWithUser**](/windows/previous-versions/Msdrm/nf-msdrm-drmaddrightwithuser?branch=master)                             | Adds a right tied to a specific user.                                                                                                     |
| [**DRMClearAllRights**](/windows/previous-versions/Msdrm/nf-msdrm-drmclearallrights?branch=master)                                 | Clears the rights from an existing issuance license.                                                                                      |
| [**DRMCreateIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateissuancelicense?branch=master)                   | Creates an issuance license from scratch or from a template.                                                                              |
| [**DRMCreateRight**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateright?branch=master)                                       | Creates an XrML right that will define the rights granted to a user or group.                                                             |
| [**DRMCreateUser**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateuser?branch=master)                                         | Creates a user object that will be assigned a right.                                                                                      |
| [**DRMGetApplicationSpecificData**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetapplicationspecificdata?branch=master)         | Retrieves a name-value pair of arbitrary application-specific information.                                                                |
| [**DRMGetIssuanceLicenseInfo**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetissuancelicenseinfo?branch=master)                 | Retrieves information about a prototype issuance license.                                                                                 |
| [**DRMGetIssuanceLicenseTemplate**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetissuancelicensetemplate?branch=master)         | Obtains a template from an issuance license.                                                                                              |
| [**DRMGetMetaData**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetmetadata?branch=master)                                       | Retrieves metadata about the content that the issuance license is associated with.                                                        |
| [**DRMGetNameAndDescription**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetnameanddescription?branch=master)                   | Retrieves information about a specific certificate in an issuance license chain.                                                          |
| [**DRMGetRevocationPoint**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetrevocationpoint?branch=master)                         | Retrieves a URL where a revocation list for a license can be obtained.                                                                    |
| [**DRMGetRightExtendedInfo**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetrightextendedinfo?branch=master)                     | Retrieves custom name-value pairs attached to a right.                                                                                    |
| [**DRMGetRightInfo**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetrightinfo?branch=master)                                     | Retrieves information about a previously created right.                                                                                   |
| [**DRMGetSignedIssuanceLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetsignedissuancelicense?branch=master)             | Acquires a signed issuance license online or offline, or produces an unsigned license that can be signed later.                           |
| [**DRMGetSignedIssuanceLicenseEx**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetsignedissuancelicenseex?branch=master)         | Acquires a signed issuance license offline, using a specified client licensor certificate (CLC) and rights account certificate (RAC).     |
| [**DRMGetUsagePolicy**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetusagepolicy?branch=master)                                 | Gets a usage policy that requires, or denies, access to a right based on application name, version, or other application characteristics. |
| [**DRMGetUserInfo**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetuserinfo?branch=master)                                       | Retrieves information about a user object.                                                                                                |
| [**DRMGetUserRights**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetuserrights?branch=master)                                   | Retrieves user/right pairs from a prototype issuance license.                                                                             |
| [**DRMGetUsers**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetusers?branch=master)                                             | Retrieves a specific user from the issuance license.                                                                                      |
| [**DRMSetApplicationSpecificData**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetapplicationspecificdata?branch=master)         | Allows an issuance license to store arbitrary name-value pairs for use by the content-consuming application.                              |
| [**DRMSetMetaData**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetmetadata?branch=master)                                       | Stores metadata about content associated with the issuance license.                                                                       |
| [**DRMSetNameAndDescription**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetnameanddescription?branch=master)                   | Specifies the content name and description in the issuance license in several (human-readable) languages.                                 |
| [**DRMSetRevocationPoint**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetrevocationpoint?branch=master)                         | Sets a refresh rate and a location to obtain a revocation list.                                                                           |
| [**DRMSetUsagePolicy**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetusagepolicy?branch=master)                                 | Sets a usage policy that requires, or denies, access to a right based on application name, version, or other application characteristics. |



 

## Handle Functions

AD RMS functions use handles to represent objects. You should create, copy, and delete these handles by using the appropriate function, so the system can maintain a correct reference count and manage resources appropriately. For more information, see [AD RMS Handles and Sessions](ad-rms-handles-and-sessions.md).



| Function                                                               | Description                                                                                              |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**DRMCloseEnvironmentHandle**](/windows/previous-versions/Msdrm/nf-msdrm-drmcloseenvironmenthandle?branch=master)         | Closes an environment handle.                                                                            |
| [**DRMCloseHandle**](/windows/previous-versions/Msdrm/nf-msdrm-drmclosehandle?branch=master)                               | Closes libraries, environments, and other miscellaneous bound license objects of the **DRMHANDLE** type. |
| [**DRMClosePubHandle**](/windows/previous-versions/Msdrm/nf-msdrm-drmclosepubhandle?branch=master)                         | Closes a previously created **DRMPUBHANDLE**.                                                            |
| [**DRMCloseQueryHandle**](/windows/previous-versions/Msdrm/nf-msdrm-drmclosequeryhandle?branch=master)                     | Closes a handle to an unbound license object.                                                            |
| [**DRMDuplicateEnvironmentHandle**](/windows/previous-versions/Msdrm/nf-msdrm-drmduplicateenvironmenthandle?branch=master) | Creates a copy of an environment handle.                                                                 |
| [**DRMDuplicateHandle**](/windows/previous-versions/Msdrm/nf-msdrm-drmduplicatehandle?branch=master)                       | Duplicates a handle.                                                                                     |
| [**DRMDuplicatePubHandle**](/windows/previous-versions/Msdrm/nf-msdrm-drmduplicatepubhandle?branch=master)                 | Used to copy a **DRMPUBHANDLE**.                                                                         |



 

## Unbound License Navigation

You can use the following functions to navigate the underlying XrML of a license in an object-oriented fashion. These functions makes it easier to create, retrieve, and modify rights, conditions, users, and other XrML structures.



| Function                                                                         | Description                                                                                             |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**DRMGetUnboundLicenseAttribute**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetunboundlicenseattribute?branch=master)           | Retrieves an unbound license attribute from the underlying XrML.                                        |
| [**DRMGetUnboundLicenseAttributeCount**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetunboundlicenseattributecount?branch=master) | Retrieves the number of occurrences of an attribute within an object in an unbound license.             |
| [**DRMGetUnboundLicenseObject**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetunboundlicenseobject?branch=master)                 | Retrieves an object of a specified type in an unbound license.                                          |
| [**DRMGetUnboundLicenseObjectCount**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetunboundlicenseobjectcount?branch=master)       | Counts the instances of an object within a given branch of the license.                                 |
| [**DRMParseUnboundLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmparseunboundlicense?branch=master)                         | Creates a handle to an unbound license, to allow an application to navigate its objects and attributes. |



 

## Bound License Navigation and Creation

The AD RMS system uses both bound and unbound licenses. Bound licenses include only information relevant to the current computer and user for the current task. Unbound licenses are not filtered in this manner. Bound licenses require a secure environment, but unbound licenses do not. The two license types are not interchangeable.



| Function                                                                     | Description                                                                          |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**DRMCreateBoundLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateboundlicense?branch=master)                       | Creates a bound license from a locally stored license.                               |
| [**DRMCreateEnablingPrincipal**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateenablingprincipal?branch=master)             | Creates an enabling principal.                                                       |
| [**DRMGetBoundLicenseAttribute**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetboundlicenseattribute?branch=master)           | Retrieves a bound license attribute.                                                 |
| [**DRMGetBoundLicenseAttributeCount**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetboundlicenseattributecount?branch=master) | Retrieves the number of occurrences of a particular attribute within a given object. |
| [**DRMGetBoundLicenseObject**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetboundlicenseobject?branch=master)                 | Retrieves an object of a specified type in a bound license.                          |
| [**DRMGetBoundLicenseObjectCount**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetboundlicenseobjectcount?branch=master)       | Retrieves the number of occurrences of a particular attribute within a given object. |



 

## License, Certificate, and Advisory List Management

The AD RMS system maintains a certificate store for each user who logs onto the computer. The AD RMS system also maintains a revocation list that describes licenses, secure repositories, or other objects that have had their rights revoked. This list must be periodically refreshed, in the interval specified by each license.



| Function                                                                 | Description                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRMAcquireAdvisories**](/windows/previous-versions/Msdrm/nf-msdrm-drmacquireadvisories?branch=master)                     | Retrieves revocation lists.                                                                                                                                                                                             |
| [**DRMAcquireLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmacquirelicense?branch=master)                           | Attempts to acquire an [*end-user license*](e-gly.md#-rm-end-user-license-gly) or [*client licensor certificate*](c-gly.md#-rm-client-licensor-certificate-gly) asynchronously.                                       |
| [**DRMAddLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmaddlicense?branch=master)                                   | Adds an [*end-user license*](e-gly.md#-rm-end-user-license-gly) to the temporary license store.                                                                                                                        |
| [**DRMConstructCertificateChain**](/windows/previous-versions/Msdrm/nf-msdrm-drmconstructcertificatechain?branch=master)     | Builds a certificate chain from an arbitrary number of certificates.                                                                                                                                                    |
| [**DRMDeconstructCertificateChain**](/windows/previous-versions/Msdrm/nf-msdrm-drmdeconstructcertificatechain?branch=master) | Retrieves a certificate from a certificate chain.                                                                                                                                                                       |
| [**DRMDeleteLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmdeletelicense?branch=master)                             | Deletes a license, [*client licensor certificate*](c-gly.md#-rm-client-licensor-certificate-gly), or revocation list.                                                                                                  |
| [**DRMEnumerateLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmenumeratelicense?branch=master)                       | Enumerates valid licenses, [*machine certificates*](m-gly.md#-rm-machine-certificate-gly) or [*rights account certificates*](r-gly.md#-rm-rights-account-certificate-gly), and revocation lists for the current user. |
| [**DRMGetCertificateChainCount**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetcertificatechaincount?branch=master)       | Retrieves the number of certificates in a certificate chain.                                                                                                                                                            |



 

## Cryptography

The AD RMS SDK contains the following cryptographic functions. You should not use other cryptographic systems to handle encryption or decryption of content.



| Function                                                                 | Description                                                   |
|--------------------------------------------------------------------------|---------------------------------------------------------------|
| [**DRMAttest**](/windows/previous-versions/Msdrm/nf-msdrm-drmattest?branch=master)                                           | Signs data.                                                   |
| [**DRMCreateEnablingBitsDecryptor**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateenablingbitsdecryptor?branch=master) | Creates a **DRMDecrypt** object for an enabling principal.    |
| [**DRMCreateEnablingBitsEncryptor**](/windows/previous-versions/Msdrm/nf-msdrm-drmcreateenablingbitsencryptor?branch=master) | Creates a **DRMEncrypt** object for an enabling principal.    |
| [**DRMDecrypt**](/windows/previous-versions/Msdrm/nf-msdrm-drmdecrypt?branch=master)                                         | Decrypts symmetrically encrypted data.                        |
| [**DRMEncrypt**](/windows/previous-versions/Msdrm/nf-msdrm-drmencrypt?branch=master)                                         | Encrypts data by using a content key.                         |
| [**DRMVerify**](/windows/previous-versions/Msdrm/nf-msdrm-drmverify?branch=master)                                           | Verifies data signed by using [**DRMAttest**](/windows/previous-versions/Msdrm/nf-msdrm-drmattest?branch=master). |



 

## Miscellaneous Functions and Topics



| Function                                                       | Description                                                               |
|----------------------------------------------------------------|---------------------------------------------------------------------------|
| [**DRMDecode**](/windows/previous-versions/Msdrm/nf-msdrm-drmdecode?branch=master)                                 | Decodes a string that is encoded with a common algorithm, such as base64. |
| [**DRMEncode**](/windows/previous-versions/Msdrm/nf-msdrm-drmencode?branch=master)                                 | Encodes data by using a public encoding method, such as base64.           |
| [**DRMGetInfo**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetinfo?branch=master)                               | Retrieves information about an object from its handle.                    |
| [**DRMGetTime**](/windows/previous-versions/Msdrm/nf-msdrm-drmgettime?branch=master)                               | Retrieves the time from a secure timer.                                   |
| [AD RMS Function Error Codes](ad-rms-function-error-codes.md) | Discusses common error codes returned by AD RMS functions.                |
| [AD RMS Handles and Sessions](ad-rms-handles-and-sessions.md) | Discusses handles to AD RMS objects.                                      |



 

## Related topics

<dl> <dt>

[AD RMS SDK Reference](ad-rms-sdk-reference.md)
</dt> </dl>

 

 



