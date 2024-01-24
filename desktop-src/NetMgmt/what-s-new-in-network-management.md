---
title: What's New in Network Management
description: What's New in Network Management
ms.assetid: f805b662-1807-4703-b27e-4721895fe450
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Network Management

## Windows 8 and Windows Server 2012

Microsoft Windows 8 introduces new Network Management programming features. These new elements extend the capability of Network Management to create provisioning packages for offline domain join operations when provisioning computers with Windows 8.

The following are new Network Management functions:

-   [**NetCreateProvisioningPackage**](/windows/desktop/api/Lmjoin/nf-lmjoin-netprovisioncomputeraccount)
-   [**NetRequestProvisioningPackageInstall**](/windows/desktop/api/Lmjoin/nf-lmjoin-netrequestprovisioningpackageinstall)

The following are new Network Management structures:

-   [**NETSETUP\_PROVISIONING\_PARAMS**](/windows/desktop/api/Lmjoin/ns-lmjoin-netsetup_provisioning_params)
-   [**USER\_INFO\_24**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_24)

The [**NetUserGetInfo**](/windows/desktop/api/Lmaccess/nf-lmaccess-netusergetinfo) function has been enhanced on Windows 8 to support a new information level and return a [**USER\_INFO\_24**](/windows/desktop/api/Lmaccess/ns-lmaccess-user_info_24) structure with user account information for an account connected to an Internet identity.

## Windows 7 and Windows Server 2008 R2

Microsoft Windows 7 introduces new Network Management programming features. These elements extend the capability of Network Management to allow offline domain join operations when provisioning computers with Windows 7.

The following are new Network Management functions:

-   [**NetProvisionComputerAccount**](/windows/desktop/api/Lmjoin/nf-lmjoin-netprovisioncomputeraccount)
-   [**NetRequestOfflineDomainJoin**](/windows/desktop/api/Lmjoin/nf-lmjoin-netrequestofflinedomainjoin)

The following existing Network Management functions were enhanced to support additional options:

-   [**NetJoinDomain**](/windows/desktop/api/Lmjoin/nf-lmjoin-netjoindomain)

## Windows Server 2003

Microsoft Windows Server 2003 introduces new Network Management programming features. These elements extend the capability of Network Management operations on Windows Server 2003 and later.

## Windows XP

Microsoft Windows XP introduces new Network Management programming features. These elements extend the capability of Network Management operations on Windows XP and later.

The following are new Network Management functions:

-   [**NetAddAlternateComputerName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netaddalternatecomputername)
-   [**NetEnumerateComputerNames**](/windows/desktop/api/Lmjoin/nf-lmjoin-netenumeratecomputernames)
-   [**NetRemoveAlternateComputerName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netremovealternatecomputername)
-   [**NetSetPrimaryComputerName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netsetprimarycomputername)
-   [**SetNetScheduleAccountInformation**](/windows/desktop/api/AtAcct/nf-atacct-setnetscheduleaccountinformation)

 

 




