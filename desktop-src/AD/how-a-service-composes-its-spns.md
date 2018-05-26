---
title: How a Service Composes its SPNs
description: A service can use two functions to compose its SPNs DsGetSpn is a general-purpose function for composing SPNs and DsServerRegisterSpn is a specialized function for composing and registering simple SPNs for a host-based service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8710409a-67b1-45e5-9cd7-5125443ab921
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- service principal name AD ,how a service composes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How a Service Composes its SPNs

A service can use two functions to compose its SPNs: [**DsGetSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dsgetspna?branch=master) is a general-purpose function for composing SPNs and [**DsServerRegisterSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dsserverregisterspna?branch=master) is a specialized function for composing and registering simple SPNs for a host-based service.

A service installer typically uses the [**DsGetSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dsgetspna?branch=master) function to compose SPNs, which it then registers on the service's logon account using the [**DsWriteAccountSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dswriteaccountspna?branch=master) function. The **DsGetSpn** can perform the following functions.

-   Create a simple SPN with the "&lt;service class&gt;/&lt;host&gt;" format for a host-based service.
-   Create a complex SPN that includes the "&lt;service name&gt;" component used by replicable services or the "&lt;port&gt;" component that distinguishes multiple instances of a service on a single host.
-   Create a single SPN with the "&lt;host&gt;" component set to either the name of a specified host or the name of the local computer by default.
-   Create an array of SPNs for multiple service instances that will run on multiple hosts throughout the forest. Each SPN specifies the name of the host for a service instance.
-   Create an array of SPNs for multiple service instances that will run on the same host. Each SPN specifies the name of the host and a port number for a service instance.

The array of names returned by [**DsGetSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dsgetspna?branch=master) must be freed by calling the [**DsFreeSpnArray**](/windows/win32/Ntdsapi/nf-ntdsapi-dsfreespnarraya?branch=master) function.

Be aware that the [**DsGetSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dsgetspna?branch=master), [**DsWriteAccountSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dswriteaccountspna?branch=master), and [**DsServerRegisterSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dsserverregisterspna?branch=master) functions do not verify that SPNs are unique. Because mutual authentication fails if a client presents an SPN that is not unique, verify uniqueness before registering an SPN. To do this, search the global catalog (GC) for **servicePrincipalName** attributes that match your SPN. For more information about searching the GC, see [Searching the Global Catalog](searching-global-catalog-contents.md).

 

 




