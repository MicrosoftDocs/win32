---
description: Parental Controls Key Design Decisions
ms.assetid: 0b41cf81-0770-4408-97a8-a178fae78d23
title: Parental Controls Key Design Decisions
ms.topic: article
ms.date: 05/31/2018
---

# Parental Controls Key Design Decisions

Major design decisions in the development of Windows Vista Parental Controls are:

## Essential Dependency on Windows Vista User Account Control (UAC) Feature

A key decision for Windows Vista Parental Controls is to rely on the new User Account Control (UAC) feature to implement the reduced rights account identities especially needed for offline restrictions on controlled users. For more information about UAC, see [The Windows Vista and Windows Server 2008 Developer Story: Windows Vista Application Development Requirements for User Account Control (UAC)](/previous-versions/aa905330(v=msdn.10)). In summary, every account with administrator rights effectively has privileges to perform the parent or guardian role of viewing log data and setting policies. Parental controls may only be set on standard-rights users (formerly called Least-privileged User Accounts, or LUAs), as only they cannot alter logs and settings with Access Control Lists (ACLs) configured only for administrators to write. In other words:

-   A parent or guardian identity implicitly equals an account that has rights of an administrator.
-   Parentally controlled users must be standard users.

## Nearly All Settings Are Available by APIs

With the exception of items such as ratings system definitions, settings available for manipulation by the Parental Controls User Interface may also be modified by exposed APIs. It is necessary for programs to implement elevation to administrative rights in order to alter settings, as noted above for UAC.

## Windows Vista Parental Controls Is a Consumer-only Technology

Windows Vista Parental Controls are not intended to be used with domain accounts. As a consumer technology, Parental Controls is not deployed in business SKUs of Windows Vista. If a computer is joined to a domain, the Family Safety user interface links will be suppressed.

A mechanism will be provided to expose the functionality for the domain-joined case, but only non-domain user accounts may be configured with Parental Controls.

 

 
