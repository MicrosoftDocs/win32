---
title: SSPI Architectural Overview
description: SSPI is a software interface.
ms.assetid: 2497afea-33dd-45ae-891b-bacf390ef338
ms.topic: article
ms.date: 05/31/2018
---

# SSPI Architectural Overview

SSPI is a software interface. Distributed programming libraries such as RPC can use it for authenticated communications. One or more software modules provide the actual authentication capabilities. Each module, called a security support provider (SSP), is implemented as a dynamic link library (DLL). An SSP provides one or more security packages.

A variety of SSPs and packages are available. Windows ships with the NTLM security package and the Microsoft Kerberos protocol security package. In addition, you may choose to install the Secure Socket Layer (SSL) security package, or any other SSPI-compatible SSP.

Using SSPI ensures that no matter which SSP you select, your application accesses the authentication features in a uniform manner. This capability provides your application greater independence from the implementation of the network than was available in the past.

Distributed applications communicate through the RPC interface. The RPC software in turn, accesses the authentication features of an SSP through the SSPI.

For more information, see [SSPI](/windows/desktop/SecAuthN/sspi).

 

 