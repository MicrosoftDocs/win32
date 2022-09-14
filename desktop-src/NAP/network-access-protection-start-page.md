---
title: Network Access Protection
description: Note The Network Access Protection platform is not available starting with Windows 10 Network Access Protection (NAP) is a set of operating system components that provide a platform for protected access to private networks.
ms.assetid: f562f5f1-c05a-4e4e-bcd9-a302c61f2a5e
keywords:
- Network Access Protection
- Network Access Protection,start page
ms.topic: article
ms.date: 05/31/2018
---

# Network Access Protection

## Purpose

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

Network Access Protection (NAP) is a set of operating system components that provide a platform for protected access to private networks. The NAP platform provides an integrated way of evaluating the system health state of a network client that is attempting to connect to or communicate on a network and restricting the access of the network client until health policy requirements have been met.

NAP is an extensible platform that provides an infrastructure and an API set for adding components that store, report, validate, and correct a computer's system health state. By itself, the NAP platform does not provide components to accumulate and evaluate attributes of a computer's health state. Other components, known as system health agents (SHAs) and system health validators (SHVs), provide network policy validation and network policy compliance.

## Where applicable

NAP is designed to be extensible. It can interoperate with any vendor software that provides SHAs and SHVs or that recognizes its published API set. NAP helps provide a solution for the following common scenarios:

-   Check the health and status of roaming laptops.
-   Ensure the health of desktop computers.
-   Verify the compliance and health of computers in remote offices.
-   Determine the health of visiting laptops.
-   Verify the compliance and health of unmanaged home computers.

## Developer audience

The NAP API is designed for C/C++ developers. For the NAP enforcement methods, programmers should be familiar with networking protocols and technologies such as Remote Authentication Dial-in User Service (RADIUS), Dynamic Host Configuration Protocol (DHCP), virtual private networks (VPNs), the IEEE 802.1X standard for wired and wireless access, and Internet Protocol security (IPsec).

## Run-time requirements

The NAP platform requires NAP infrastructure servers running Windows Server 2008 or later and NAP clients running Windows XP with Service Pack 3 (SP3), Windows Vista, or later operating systems. For specific information about which operating systems support a particular programming element, refer to the Requirements sections of the NAP APIs in the NAP Reference documentation.

## In this section



| Topic                                         | Description                                                                       |
|-----------------------------------------------|-----------------------------------------------------------------------------------|
| [About NAP](about-nap.md)<br/>         | General information about NAP API.<br/>                                     |
| [Using NAP](using-nap.md)<br/>         | Usage examples for NAP API.<br/>                                            |
| [NAP Reference](nap-reference.md)<br/> | Documentation for NAP interfaces, structures, and other code elements.<br/> |



 

 

 





