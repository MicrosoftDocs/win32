---
description: Explains how to create a custom security package.
ms.assetid: af8b9796-77e7-43c1-8f8e-acee01a62bf9
title: Creating Custom Security Packages
ms.topic: article
ms.date: 05/31/2018
---

# Creating Custom Security Packages

## SSP Security Packages

If a custom security support provider (SSP) security package will be used exclusively for client/server security support it can implement the Microsoft [Security Support Provider Interface](sspi.md).

The SampSSP sample shipped with the Platform Software Development Kit (SDK) contains a sample SSP security package implementation.

## SSP/AP Security Packages

Custom [*security support provider*](/windows/desktop/SecGloss/s-gly)/[*authentication packages*](/windows/desktop/SecGloss/a-gly) (SSP/APs) contain security packages that function as authentication packages (APs) and security support providers (SSPs). These packages implement separate APIs to support each role.

Because it functions as an AP, a custom SSP/AP [*security package*](/windows/desktop/SecGloss/s-gly) must provide implementations for all of the [Functions Implemented by Authentication Packages](authentication-functions.md).

To provide integrated security support, a custom SSP/AP security package must provide implementations for the [Functions implemented by SSP/APs](authentication-functions.md). [LSA Functions Called by SSP/APs](authentication-functions.md) describes the support functions available to the SSP/AP developers that want to interact with the LSA.

SSP/AP security packages, in order to perform as both an AP and an SSP, may execute as part of the operating system and as part of a user application. These two modes of execution are known as LSA mode and user mode, respectively. For details about custom security packages in LSA mode see [LSA Mode Initialization](lsa-mode-initialization.md). For details about user mode, see [User Mode Initialization](user-mode-initialization.md).

If a custom SSP/AP security package offers services for client/server applications it should provide implementations for the functions described in [Functions Implemented by User-mode SSP/APs](authentication-functions.md). [LSA Functions Called By User-mode SSP/APs](authentication-functions.md) describes the support functions available to an SSP/AP executing in a client or server process.

For information about registering an SSP/AP DLL, see [Registering SSP/AP DLLs](registering-ssp-ap-dlls.md).

## Related topics

<dl> <dt>

[Restrictions around Registering and Installing a Security Package](restrictions-around-registering-and-installing-a-security-package.md)
</dt> </dl>

 

 
