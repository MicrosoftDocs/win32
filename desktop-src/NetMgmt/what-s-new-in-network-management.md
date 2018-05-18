---
title: What's New in Network Management
description: What's New in Network Management
ms.assetid: 'f805b662-1807-4703-b27e-4721895fe450'
---

# What's New in Network Management

## Windows 8 and Windows Server 2012

Microsoft Windows 8 introduces new Network Management programming features. These new elements extend the capability of Network Management to create provisioning packages for offline domain join operations when provisioning computers with Windows 8.

The following are new Network Management functions:

-   [**NetCreateProvisioningPackage**](netprovisioncomputeraccount.md)
-   [**NetRequestProvisioningPackageInstall**](netrequestprovisioningpackageinstall.md)

The following are new Network Management structures:

-   [**NETSETUP\_PROVISIONING\_PARAMS**](netsetup-provisioning-params.md)
-   [**USER\_INFO\_24**](user-info-24.md)

The [**NetUserGetInfo**](netusergetinfo.md) function has been enhanced on Windows 8 to support a new information level and return a [**USER\_INFO\_24**](user-info-24.md) structure with user account information for an account connected to an Internet identity.

## Windows 7 and Windows Server 2008 R2

Microsoft Windows 7 introduces new Network Management programming features. These elements extend the capability of Network Management to allow offline domain join operations when provisioning computers with Windows 7.

The following are new Network Management functions:

-   [**NetProvisionComputerAccount**](netprovisioncomputeraccount.md)
-   [**NetRequestOfflineDomainJoin**](netrequestofflinedomainjoin.md)

The following existing Network Management functions were enhanced to support additional options:

-   [**NetJoinDomain**](netjoindomain.md)

## Windows Server 2003

Microsoft Windows Server 2003 introduces new Network Management programming features. These elements extend the capability of Network Management operations on Windows Server 2003 and later.

The following are new Network Management functions:

-   [**NetLogonSetServiceBits**](netlogonsetservicebits.md)

## Windows XP

Microsoft Windows XP introduces new Network Management programming features. These elements extend the capability of Network Management operations on Windows XP and later.

The following are new Network Management functions:

-   [**NetAddAlternateComputerName**](netaddalternatecomputername.md)
-   [**NetEnumerateComputerNames**](netenumeratecomputernames.md)
-   [**NetRemoveAlternateComputerName**](netremovealternatecomputername.md)
-   [**NetSetPrimaryComputerName**](netsetprimarycomputername.md)
-   [**SetNetScheduleAccountInformation**](setnetscheduleaccountinformation.md)

 

 




