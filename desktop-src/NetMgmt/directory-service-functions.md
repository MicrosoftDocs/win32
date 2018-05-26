---
title: Directory Service Functions
description: The network management directory service functions allow developers to work with the domain controller and domain membership in the directory service.
ms.assetid: 9eeb8f40-85c0-49db-a307-193703e4f463
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Directory Service Functions

The network management directory service functions allow developers to work with the domain controller and domain membership in the directory service.

The network management directory service functions are listed following.



| Function                                                                 | Description                                                                                                                                                                                 |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAddAlternateComputerName**](/windows/win32/Lmjoin/nf-lmjoin-netaddalternatecomputername?branch=master)       | Adds an alternate name for the specified computer.                                                                                                                                          |
| [**NetEnumerateComputerNames**](/windows/win32/Lmjoin/nf-lmjoin-netenumeratecomputernames?branch=master)           | Enumerates names for the specified computer.                                                                                                                                                |
| [**NetGetJoinableOUs**](/windows/win32/Lmjoin/nf-lmjoin-netgetjoinableous?branch=master)                           | Retrieves a list of organizational units (OUs) in which a computer account can be created.                                                                                                  |
| [**NetGetJoinInformation**](/windows/win32/Lmjoin/nf-lmjoin-netgetjoininformation?branch=master)                   | Retrieves join status information for the specified computer.                                                                                                                               |
| [**NetJoinDomain**](/windows/win32/Lmjoin/nf-lmjoin-netjoindomain?branch=master)                                   | Joins a computer to a workgroup or domain.                                                                                                                                                  |
| [**NetLogonSetServiceBits**](netlogonsetservicebits.md)                 | Notifies the Netlogon service of the running state of the services on a domain controller. The caller must be running in the context of either the LocalSystem or the LocalService account. |
| [**NetProvisionComputerAccount**](/windows/win32/Lmjoin/nf-lmjoin-netprovisioncomputeraccount?branch=master)       | Provisions a computer account for later used in an offline domain join operation.                                                                                                           |
| [**NetRemoveAlternateComputerName**](/windows/win32/Lmjoin/nf-lmjoin-netremovealternatecomputername?branch=master) | Removes an alternate name for the specified computer.                                                                                                                                       |
| [**NetRenameMachineInDomain**](/windows/win32/Lmjoin/nf-lmjoin-netrenamemachineindomain?branch=master)             | Changes the name of a computer in a domain.                                                                                                                                                 |
| [**NetSetPrimaryComputerName**](/windows/win32/Lmjoin/nf-lmjoin-netsetprimarycomputername?branch=master)           | Sets the primary computer name for the specified computer.                                                                                                                                  |
| [**NetUnjoinDomain**](/windows/win32/Lmjoin/nf-lmjoin-netunjoindomain?branch=master)                               | Unjoins a computer from a workgroup or a domain.                                                                                                                                            |
| [**NetValidateName**](/windows/win32/Lmjoin/nf-lmjoin-netvalidatename?branch=master)                               | Verifies the validity of a computer name, workgroup name, or domain name.                                                                                                                   |



 

For more information about programming for Active Directory, see the [Active Directory Reference](https://msdn.microsoft.com/library/aa772146). For more information about organizational units, see [Managing Users](https://msdn.microsoft.com/library/ms677281) in the Active Directory documentation.

 

 




