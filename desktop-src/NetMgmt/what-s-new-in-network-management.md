---
title: Whats New in Network Management
description: Whats New in Network Management
ms.assetid: f805b662-1807-4703-b27e-4721895fe450
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in Network Management

## Windows 8 and Windows Server 2012

Microsoft Windows 8 introduces new Network Management programming features. These new elements extend the capability of Network Management to create provisioning packages for offline domain join operations when provisioning computers with Windows 8.

The following are new Network Management functions:

-   [**NetCreateProvisioningPackage**](/windows/win32/Lmjoin/nf-lmjoin-netprovisioncomputeraccount?branch=master)
-   [**NetRequestProvisioningPackageInstall**](/windows/win32/Lmjoin/nf-lmjoin-netrequestprovisioningpackageinstall?branch=master)

The following are new Network Management structures:

-   [**NETSETUP\_PROVISIONING\_PARAMS**](/windows/win32/Lmjoin/ns-lmjoin-_netsetup_provisioning_params?branch=master)
-   [**USER\_INFO\_24**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_24?branch=master)

The [**NetUserGetInfo**](/windows/win32/Lmaccess/nf-lmaccess-netusergetinfo?branch=master) function has been enhanced on Windows 8 to support a new information level and return a [**USER\_INFO\_24**](/windows/win32/Lmaccess/ns-lmaccess-_user_info_24?branch=master) structure with user account information for an account connected to an Internet identity.

## Windows 7 and Windows Server 2008 R2

Microsoft Windows 7 introduces new Network Management programming features. These elements extend the capability of Network Management to allow offline domain join operations when provisioning computers with Windows 7.

The following are new Network Management functions:

-   [**NetProvisionComputerAccount**](/windows/win32/Lmjoin/nf-lmjoin-netprovisioncomputeraccount?branch=master)
-   [**NetRequestOfflineDomainJoin**](/windows/win32/Lmjoin/nf-lmjoin-netrequestofflinedomainjoin?branch=master)

The following existing Network Management functions were enhanced to support additional options:

-   [**NetJoinDomain**](/windows/win32/Lmjoin/nf-lmjoin-netjoindomain?branch=master)

## Windows Server 2003

Microsoft Windows Server 2003 introduces new Network Management programming features. These elements extend the capability of Network Management operations on Windows Server 2003 and later.

The following are new Network Management functions:

-   [**NetLogonSetServiceBits**](netlogonsetservicebits.md)

## Windows XP

Microsoft Windows XP introduces new Network Management programming features. These elements extend the capability of Network Management operations on Windows XP and later.

The following are new Network Management functions:

-   [**NetAddAlternateComputerName**](/windows/win32/Lmjoin/nf-lmjoin-netaddalternatecomputername?branch=master)
-   [**NetEnumerateComputerNames**](/windows/win32/Lmjoin/nf-lmjoin-netenumeratecomputernames?branch=master)
-   [**NetRemoveAlternateComputerName**](/windows/win32/Lmjoin/nf-lmjoin-netremovealternatecomputername?branch=master)
-   [**NetSetPrimaryComputerName**](/windows/win32/Lmjoin/nf-lmjoin-netsetprimarycomputername?branch=master)
-   [**SetNetScheduleAccountInformation**](/windows/win32/AtAcct/nf-atacct-setnetscheduleaccountinformation?branch=master)

 

 




