---
description: When connecting remotely to an Active Directory server other than the one in your current domain, you must specify the name of a computer that is already a member of the domain belonging to the Active Directory you want.
ms.assetid: f1478b9d-4a92-4340-8721-1f443eb6ace2
ms.tgt_platform: multiple
title: Describing the LDAP Namespace
ms.topic: article
ms.date: 05/31/2018
---

# Describing the LDAP Namespace

When connecting remotely to an Active Directory server other than the one in your current domain, you must specify the name of a computer that is already a member of the domain belonging to the Active Directory you want.

To remotely connect to a computer that is already a member of the domain belonging to the Active Directory server, type the following command.

**\\\\RemoteComputer\\root\\directory\\LDAP**

This example shows that there are two parts that make up a fully qualified namespace name. The first part (\\\\RemoteComputer) represents the computer that is already a member of the domain belonging to the Active Directory server you want. The second part (\\root\\directory\\LDAP) represents the Active Directory schema in the Directory Services Provider.

> [!Note]  
> For more information about support and installation of this component on a specific operating system, see [Operating System Availability of WMI Components](operating-system-availability-of-wmi-components.md).

 

 

 



