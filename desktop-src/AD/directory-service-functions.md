---
title: Directory Service Functions
description: The directory service functions provide a utility for locating a domain controller (DC) in a Windows NT or Windows 2000 domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7b519c81-5a6c-470a-a525-1894efd53305
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Directory Service Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Directory Service Functions

The directory service functions provide a utility for locating a domain controller (DC) in a Windows NT or Windows 2000 domain. The architecture interacts with clients as well as servers in all versions of Windows NT and Windows 2000. The following functions enable developers to work with the domain controller and domain membership in the directory service:

-   [**DsAddressToSiteNames**](/windows/win32/Dsgetdc/nf-dsgetdc-dsaddresstositenamesa?branch=master)
-   [**DsAddressToSiteNamesEx**](/windows/win32/Dsgetdc/nf-dsgetdc-dsaddresstositenamesexa?branch=master)
-   [**DsDeregisterDnsHostRecords**](/windows/win32/Dsgetdc/nf-dsgetdc-dsderegisterdnshostrecordsa?branch=master)
-   [**DsEnumerateDomainTrusts**](/windows/win32/Dsgetdc/nf-dsgetdc-dsenumeratedomaintrustsa?branch=master)
-   [**DsGetDcClose**](/windows/win32/Dsgetdc/nf-dsgetdc-dsgetdcclosew?branch=master)
-   [**DsGetDcName**](/windows/win32/DsGetDC/nf-dsgetdc-dsgetdcnamea?branch=master)
-   [**DsGetDcNext**](/windows/win32/Dsgetdc/nf-dsgetdc-dsgetdcnexta?branch=master)
-   [**DsGetDcOpen**](/windows/win32/Dsgetdc/nf-dsgetdc-dsgetdcopena?branch=master)
-   [**DsGetDcSiteCoverage**](/windows/win32/Dsgetdc/nf-dsgetdc-dsgetdcsitecoveragea?branch=master)
-   [**DsGetForestTrustInformationW**](/windows/win32/Dsgetdc/nf-dsgetdc-dsgetforesttrustinformationw?branch=master)
-   [**DsGetSiteName**](/windows/win32/Dsgetdc/nf-dsgetdc-dsgetsitenamea?branch=master)
-   [**DsMergeForestTrustInformationW**](/windows/win32/Dsgetdc/nf-dsgetdc-dsmergeforesttrustinformationw?branch=master)
-   [**DsRoleFreeMemory**](/windows/win32/Dsrole/nf-dsrole-dsrolefreememory?branch=master)
-   [**DsRoleGetPrimaryDomainInformation**](/windows/win32/Dsrole/nf-dsrole-dsrolegetprimarydomaininformation?branch=master)
-   [**DsValidateSubnetName**](/windows/win32/Dsgetdc/nf-dsgetdc-dsvalidatesubnetnamea?branch=master)

The DC locator, [**DsGetDcName**](/windows/win32/DsGetDC/nf-dsgetdc-dsgetdcnamea?branch=master), is implemented by the Netlogon service. Each DC registers its DNS name on the DNS server and its NetBIOS name using a transport-specific mechanism, for example, in WINS. The DC locator looks up the name, then sends a datagram to, or pings, the DC that registered the name. For NetBIOS domain names, the datagram is a mailslot message. For DNS domain names, the datagram is an LDAP UDP search. Each such DC responds indicating that it is currently operational. The first DC to respond is returned to the caller.

The returned DC is cached, so that subsequent callers need not repeat the preceding algorithm, and to encourage all callers to use that same DC. This ensures that a single client has a consistent view of the contents of the DC.

When searching for a DC by DNS domain name, the DC locator attempts to find a DC in the "closest" site. Each DC registers additional DNS records indicating what site that the DC is in and what sites the DC includes. The DC locator first searches for this site-specific DNS record before searching for the DNS record that is not site-specific, thus preferring a DC in that site. When the DC locator sends a datagram to the DC, the DC looks up the IP address of the client in the Configuration/Sites/Subnet container of the DS to find a subnet object. The **siteObject** property of the subnet object defines the name of the site that contains the client. The DC responds to the ping with the name of the site that contains the client, along with an indicator of whether this DC covers that site. If the DC does not include that site and the DC locator has not yet attempted to find a DC in that site, the DC locator tries again to find a DC in the site.

To find the name of the site containing the client, use the [**DsGetSiteName**](/windows/win32/Dsgetdc/nf-dsgetdc-dsgetsitenamea?branch=master) function. The names of the objects in the Configuration/Sites/Subnet container must be valid subnet names. The [**DsValidateSubnetName**](/windows/win32/Dsgetdc/nf-dsgetdc-dsvalidatesubnetnamea?branch=master) function indicates whether a specified subnet name is valid.

 

 




