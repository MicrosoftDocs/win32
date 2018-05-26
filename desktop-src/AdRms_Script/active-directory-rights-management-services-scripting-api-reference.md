---
Description: Enables you to create custom scripts to administer an RMS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a7b09f14-6e3d-43a5-8919-04a711958004
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Active Directory Rights Management Services Scripting API Reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Active Directory Rights Management Services Scripting API Reference

The Active Directory Rights Management Services (AD RMS) Scripting API enables you to create custom scripts to administer an RMS server. The examples in the following topics use Visual Basic Scripting Edition (VBScript) and Windows Script Host (WSH).

| Object                                                                                                  | Description                                                                                                                      |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**ADFederationService**](adfederationservice-object.md)                                               | Manages Active Directory Federation Services (ADFS) support.                                                                     |
| [**ApplicationSpecificDataItem**](applicationspecificdataitem-object.md)                               | Defines a name-value pair that can be added to a rights template and used by any AD RMS–enabled application that understands it. |
| [**ApplicationSpecificDataItemCollection**](applicationspecificdataitemcollection-object.md)           | Contains a collection of [**ApplicationSpecificDataItem**](applicationspecificdataitem-object.md) objects.                      |
| [**AuditReport**](auditreport-object.md)                                                               | Enables logging and retrieves information about the logging database.                                                            |
| [**ClusterInformation**](clusterinformation-object.md)                                                 | Contains AD RMS configuration information.                                                                                       |
| [**ConfigurationManager**](configurationmanager-object.md)                                             | Represents the top-level object in the AD RMS scripting API.                                                                     |
| [**Constants**](constants-object.md)                                                                   | Contains predefined constant values that can be used in various methods and properties to improve code readability.              |
| [**DatabaseInformation**](databaseinformation-object.md)                                               | Represents the database used to log information about the use of rights-protected content in an organization.                    |
| [**Enterprise**](enterprise-object.md)                                                                 | Manages enterprise administration.                                                                                               |
| [**EnterpriseDatabase**](enterprisedatabase-object.md)                                                 | Retrieves the configuration, directory services, and logging databases.                                                          |
| [**EnterpriseUrls**](enterpriseurls-object.md)                                                         | Contains enterprise licensing and account certification service URLs.                                                            |
| [**ExcludedApplication**](excludedapplication-object.md)                                               | Represents an application that is prohibited from decrypting AD RMS–protected content.                                           |
| [**ExcludedApplicationCollection**](excludedapplicationcollection-object.md)                           | Contains a collection of [**ExcludedApplication**](excludedapplication-object.md) objects.                                      |
| [**ExcludedLockbox**](excludedlockbox-object.md)                                                       | Identifies the minimum lockbox version that must be installed on the client before a use license can be granted.                 |
| [**ExcludedUserAccount**](excludeduseraccount-object.md)                                               | Identifies a user account for which new use license requests are denied.                                                         |
| [**ExcludedUserAccountCollection**](excludeduseraccountcollection-object.md)                           | Contains a collection of [**ExcludedUserAccount**](excludeduseraccount-object.md) objects.                                      |
| [**ExclusionPolicy**](exclusionpolicy-object.md)                                                       | Manages AD RMS exclusion policies.                                                                                               |
| [**ExpirationCondition**](expirationcondition-object.md)                                               | Represents a template condition that specifies when protected content expires and when a use license must be renewed.            |
| [**ExpirationData**](expirationdata-object.md)                                                         | Specifies the date at which AD RMS–protected content expires and can no longer be opened.                                        |
| [**ExtendedCondition**](extendedcondition-object.md)                                                   | Contains predefined policies that can be set on a rights template.                                                               |
| [**IssuancePolicy**](issuancepolicy-object.md)                                                         | Specifies the amount of time for which rights account certificates (RACs) are valid.                                             |
| [**LoggingSystemInformation**](loggingsysteminformation-object.md)                                     | Contains information about the AD RMS logging environment.                                                                       |
| [**OnlineTrustedServiceExcludedUserCollection**](onlinetrustedserviceexcludedusercollection-object.md) | Contains a collection of users excluded from the Windows Live ID user domain.                                                    |
| [**OnlineTrustedServiceUserDomain**](onlinetrustedserviceuserdomain-object.md)                         | Represents Windows Live ID user domains in the trust policy of an enterprise.                                                    |
| [**ProxyAuthentication**](proxyauthentication-object.md)                                               | Specifies the type of proxy server authentication required, if any, and sets the authentication credentials.                     |
| [**ProxySettings**](proxysettings-object.md)                                                           | Represents the configuration settings of a proxy server.                                                                         |
| [**RevocationCondition**](revocationcondition-object.md)                                               | Contains the revocation policy for a rights policy template.                                                                     |
| [**RightsTemplate**](rightstemplate-object.md)                                                         | Manages a rights policy template.                                                                                                |
| [**RightsTemplateCollection**](rightstemplatecollection-object.md)                                     | Contains a collection of [**RightsTemplate**](rightstemplate-object.md) objects                                                 |
| [**RightsTemplatePolicy**](rightstemplatepolicy-object.md)                                             | Retrieves a collection of rights policy templates and specifies the shared folder through which those templates are distributed. |
| [**SecurityPolicy**](securitypolicy-object.md)                                                         | Decommissions a server and specifies a super users group.                                                                        |
| [**ServerLicensorCertificate**](serverlicensorcertificate-object.md)                                   | Manages the AD RMS server licensor certificate.                                                                                  |
| [**ServiceConnectionPoint**](serviceconnectionpoint-object.md)                                         | Manages a service connection point (SCP).                                                                                        |
| [**ServiceIdentity**](serviceidentity-object.md)                                                       | Manages an AD RMS service account.                                                                                               |
| [**ServicePrivateKeyProtectionInformation**](serviceprivatekeyprotectioninformation-object.md)         | Contains information about the server licensor private key.                                                                      |
| [**StringCollection**](stringcollection-object.md)                                                     | Manages a collection of string objects.                                                                                          |
| [**TemplateLocaleName**](templatelocalename-object.md)                                                 | Defines a name and locale ID (LCID) pair for a template.                                                                         |
| [**TemplateLocaleNameCollection**](templatelocalenamecollection-object.md)                             | Contains a collection of [**TemplateLocaleName**](templatelocalename-object.md) objects.                                        |
| [**TemplateSummary**](templatesummary-object.md)                                                       | Contains descriptive information about a template.                                                                               |
| [**TemplateSummaryCollection**](templatesummarycollection-object.md)                                   | Contains a collection of [**TemplateSummary**](templatesummary-object.md) objects.                                              |
| [**TrustedDomainNameCollection**](trusteddomainnamecollection-object.md)                               | Contains a collection of the domain names that make up a trusted user domain.                                                    |
| [**TrustedPublishingDomain**](trustedpublishingdomain-object.md)                                       | Contains information about a trusted publishing domain.                                                                          |
| [**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md)                   | Contains a collection of [**TrustedPublishingDomain**](trustedpublishingdomain-object.md) objects.                              |
| [**TrustedUserDomain**](trusteduserdomain-object.md)                                                   | Represents a trusted user domain associated with an AD RMS installation.                                                         |
| [**TrustedUserDomainCollection**](trusteduserdomaincollection-object.md)                               | Contains a collection of [**TrustedUserDomain**](trusteduserdomain-object.md) objects.                                          |
| [**TrustPolicy**](trustpolicy-object.md)                                                               | Manages the AD RMS trust policy.                                                                                                 |
| [**Urls**](urls-object.md)                                                                             | Retrieves internal and external web service URLs.                                                                                |
| [**UserDomainAccount**](userdomainaccount-object.md)                                                   | Contains account credential information.                                                                                         |
| [**UserRightsItem**](userrightsitem-object.md)                                                         | Represents a user and identifies the rights granted to consume protected content.                                                |
| [**UserRightsItemCollection**](userrightsitemcollection-object.md)                                     | Contains a collection of [**UserRightsItem**](userrightsitem-object.md) objects.                                                |
| [**VariantObjectCollection**](variantobjectcollection-object.md)                                       | Contains abstract methods and properties that manage a generic collection.                                                       |
| [**Version**](version-object.md)                                                                       | Represents a version number in the format *Major.Minor.Build.Revision*.                                                          |



 

## Related topics

<dl> <dt>

[Active Directory Rights Management Services Scripting API](adrms-script-portal.md)
</dt> </dl>

 

 



