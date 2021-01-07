---
description: Explains built-in and account domains on Windows-based systems.
ms.assetid: 306c258b-950e-4506-99e2-67a3714285ff
title: Built-in and Account Domains
ms.topic: article
ms.date: 05/31/2018
---

# Built-in and Account Domains

Domains on a Windows-based system fall into the following two categories:

-   [Computers that are not domain controllers](#computers-that-are-not-domain-controllers)
-   [Computers that are domain controllers](#computers-that-are-domain-controllers)

## Computers that are not domain controllers

The Security Accounts Manager (SAM) database resides on each computer and manages accounts for the built-in domain and the account domain.



| Domain          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Built-in domain | This domain contains default local groups, such as the Administrators and Users groups, that are established when the operating system is installed. The name of this domain is a localized version of BUILTIN.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Account domain  | The account domain can contain user, group, and local group accounts. The Administrator account is in this domain. The accounts defined in the account domain of a workstation or member server are limited to accessing resources located on the physical computer where the account resides. On a system that is not part of a network and therefore has no [primary domain](primary-and-trusted-domains.md), the account domain is used to house all accounts that provide access to the computer. On a system that is part of a network, the computer's account domain is used to house accounts that do not access network resources. Accounts that require access to the network must be defined in the account domain of a domain controller.<br/> The name of this domain is assigned at system installation time and is determined by the computer name. If the computer name is changed, the account domain name will not be updated until the computer is restarted.<br/> |



 

## Computers that are domain controllers

Domain controllers do not have built-in or account domains. Also, instead of a SAM database, these systems use the Microsoft Active Directory directory service to store account access information. For more information, see [Active Directory](/windows/desktop/AD/active-directory-domain-services).

 

