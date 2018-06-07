---
title: Directory Service Functions
description: The network management directory service functions allow developers to work with the domain controller and domain membership in the directory service.
ms.assetid: 9eeb8f40-85c0-49db-a307-193703e4f463
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Directory Service Functions

The network management directory service functions allow developers to work with the domain controller and domain membership in the directory service.

The network management directory service functions are listed following.



| Function                                                                 | Description                                                                                                                                                                                 |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAddAlternateComputerName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netaddalternatecomputername)       | Adds an alternate name for the specified computer.                                                                                                                                          |
| [**NetEnumerateComputerNames**](/windows/desktop/api/Lmjoin/nf-lmjoin-netenumeratecomputernames)           | Enumerates names for the specified computer.                                                                                                                                                |
| [**NetGetJoinableOUs**](/windows/desktop/api/Lmjoin/nf-lmjoin-netgetjoinableous)                           | Retrieves a list of organizational units (OUs) in which a computer account can be created.                                                                                                  |
| [**NetGetJoinInformation**](/windows/desktop/api/Lmjoin/nf-lmjoin-netgetjoininformation)                   | Retrieves join status information for the specified computer.                                                                                                                               |
| [**NetJoinDomain**](/windows/desktop/api/Lmjoin/nf-lmjoin-netjoindomain)                                   | Joins a computer to a workgroup or domain.                                                                                                                                                  |
| [**NetLogonSetServiceBits**](netlogonsetservicebits.md)                 | Notifies the Netlogon service of the running state of the services on a domain controller. The caller must be running in the context of either the LocalSystem or the LocalService account. |
| [**NetProvisionComputerAccount**](/windows/desktop/api/Lmjoin/nf-lmjoin-netprovisioncomputeraccount)       | Provisions a computer account for later used in an offline domain join operation.                                                                                                           |
| [**NetRemoveAlternateComputerName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netremovealternatecomputername) | Removes an alternate name for the specified computer.                                                                                                                                       |
| [**NetRenameMachineInDomain**](/windows/desktop/api/Lmjoin/nf-lmjoin-netrenamemachineindomain)             | Changes the name of a computer in a domain.                                                                                                                                                 |
| [**NetSetPrimaryComputerName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netsetprimarycomputername)           | Sets the primary computer name for the specified computer.                                                                                                                                  |
| [**NetUnjoinDomain**](/windows/desktop/api/Lmjoin/nf-lmjoin-netunjoindomain)                               | Unjoins a computer from a workgroup or a domain.                                                                                                                                            |
| [**NetValidateName**](/windows/desktop/api/Lmjoin/nf-lmjoin-netvalidatename)                               | Verifies the validity of a computer name, workgroup name, or domain name.                                                                                                                   |



 

For more information about programming for Active Directory, see the [Active Directory Reference](https://msdn.microsoft.com/library/aa772146). For more information about organizational units, see [Managing Users](https://msdn.microsoft.com/library/ms677281) in the Active Directory documentation.

 

 




