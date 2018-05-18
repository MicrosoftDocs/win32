---
title: Directory Service Functions
description: The network management directory service functions allow developers to work with the domain controller and domain membership in the directory service.
ms.assetid: '9eeb8f40-85c0-49db-a307-193703e4f463'
---

# Directory Service Functions

The network management directory service functions allow developers to work with the domain controller and domain membership in the directory service.

The network management directory service functions are listed following.



| Function                                                                 | Description                                                                                                                                                                                 |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetAddAlternateComputerName**](netaddalternatecomputername.md)       | Adds an alternate name for the specified computer.                                                                                                                                          |
| [**NetEnumerateComputerNames**](netenumeratecomputernames.md)           | Enumerates names for the specified computer.                                                                                                                                                |
| [**NetGetJoinableOUs**](netgetjoinableous.md)                           | Retrieves a list of organizational units (OUs) in which a computer account can be created.                                                                                                  |
| [**NetGetJoinInformation**](netgetjoininformation.md)                   | Retrieves join status information for the specified computer.                                                                                                                               |
| [**NetJoinDomain**](netjoindomain.md)                                   | Joins a computer to a workgroup or domain.                                                                                                                                                  |
| [**NetLogonSetServiceBits**](netlogonsetservicebits.md)                 | Notifies the Netlogon service of the running state of the services on a domain controller. The caller must be running in the context of either the LocalSystem or the LocalService account. |
| [**NetProvisionComputerAccount**](netprovisioncomputeraccount.md)       | Provisions a computer account for later used in an offline domain join operation.                                                                                                           |
| [**NetRemoveAlternateComputerName**](netremovealternatecomputername.md) | Removes an alternate name for the specified computer.                                                                                                                                       |
| [**NetRenameMachineInDomain**](netrenamemachineindomain.md)             | Changes the name of a computer in a domain.                                                                                                                                                 |
| [**NetSetPrimaryComputerName**](netsetprimarycomputername.md)           | Sets the primary computer name for the specified computer.                                                                                                                                  |
| [**NetUnjoinDomain**](netunjoindomain.md)                               | Unjoins a computer from a workgroup or a domain.                                                                                                                                            |
| [**NetValidateName**](netvalidatename.md)                               | Verifies the validity of a computer name, workgroup name, or domain name.                                                                                                                   |



 

For more information about programming for Active Directory, see the [Active Directory Reference](https://msdn.microsoft.com/library/aa772146). For more information about organizational units, see [Managing Users](https://msdn.microsoft.com/library/ms677281) in the Active Directory documentation.

 

 




