---
description: Explains the differences between SSP/APs and SSPs.
ms.assetid: 0ed4291b-6562-440f-b892-4e6e5b4b49c8
title: SSP/APs vs. SSPs
ms.topic: article
ms.date: 05/31/2018
---

# SSP/APs vs. SSPs

[*Security packages*](../secgloss/s-gly.md) are deployed in one of the following types of dynamic-link libraries (DLLs):

-   [SSP/APs](#sspaps-vs-ssps)
-   [SSPs](#sspaps-vs-ssps)

Whether a security package is in a security support provider/[*authentication package*](../secgloss/a-gly.md) (SSP/AP) or a [*security support provider*](../secgloss/s-gly.md) (SSP) DLL is determined by the types of security services it provides and the extent to which it requires integration with the [*Local Security Authority*](../secgloss/l-gly.md) (LSA). These differences also determine the API implemented in a custom security package.

## SSP/APs

An SSP/AP is a DLL that contains one or more [*Security packages*](../secgloss/s-gly.md) and can function as an SSP for client/server applications and as an [authentication package](authentication-packages.md) for logon applications. To function in both of these roles, SSP/APs are loaded into the LSA process space at system startup and can be loaded into client/server application processes as well.

Custom SSP/AP security packages must implement both the [Functions Implemented by User-mode SSP/APs](authentication-functions.md), and [Functions Implemented by SSP/APs](authentication-functions.md). These function implementations can make use of LSA support functions to offer advanced security features such as token creation, [*supplemental credentials*](../secgloss/s-gly.md) support, and pass-through authentication.

If a custom SSP/AP security package provides the full range of message [*integrity*](../secgloss/i-gly.md) and privacy functions, it will also implement the [Functions Implemented by User-mode SSP/APs](authentication-functions.md).

## SSPs

An SSP is a DLL that contains one or more security packages that provide authenticated connection, message integrity, and message encryption services to client/server applications. SSPs implement [Security Support Provider Interface](sspi.md) (SSPI) functions. Applications can access the security packages in an SSP by calling the SSPI functions directly. SSPs are loaded into the client and server processes; they are not integrated with the LSA.

 

 
