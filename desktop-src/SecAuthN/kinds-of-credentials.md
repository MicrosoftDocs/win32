---
description: Explains the two kinds of credentials with which the Credentials Management API works.
ms.assetid: eaf1c298-f0af-4b29-a09a-f399da20335d
title: Kinds of Credentials
ms.topic: article
ms.date: 05/31/2018
---

# Kinds of Credentials

The Credentials Management API works with two kinds of credentials:

-   [Domain Credentials](#domain-credentials)
-   [Generic Credentials](#generic-credentials)

## Domain Credentials

Domain credentials are used by the operating system and authenticated by the Local Security Authority (LSA). Typically, domain credentials are established for a user when a registered security package, such as the Kerberos protocol, authenticates logon data that is provided by the user. The logon credentials are cached by the operating system so that a single sign-on gives the user access to many different resources. For example, network connections can occur transparently, and access to protected system objects can be granted based on the user's cached domain credentials.

Credentials Management functions provide a mechanism for applications to prompt a user for domain credentials after the user logs on, and to have the operating system authenticate the information that is provided by the user.

The secret part of domain credentials, the password, is protected by the operating system. Only code running in-process with the LSA can read and write domain credentials. Applications are limited to writing domain credentials.

Windows supports expanded use of smart card and certificate credentials. To help ensure security, the Credentials Management API never stores the smart card PIN on the computer.

## Generic Credentials

Generic credentials are defined and authenticated by applications that manage authorization and security directly instead of delegating these tasks to the operating system. For example, an application can require users to enter a user name and password provided by the application or to produce a [*certificate*](../secgloss/c-gly.md) to access a website.

Applications use Credentials Management functions to prompt users for application-defined, generic, credential information, such as user name, certificate, smart card, or password. The information entered by the user is returned to the application for authentication.

Credentials Management provides customizable cache management and long-term storage for generic credentials. Generic credentials can be read and written by user processes.

 

 
