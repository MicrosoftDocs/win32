---
title: How a Service Composes its SPNs
description: A service can use two functions to compose its SPNs DsGetSpn is a general-purpose function for composing SPNs and DsServerRegisterSpn is a specialized function for composing and registering simple SPNs for a host-based service.
ms.assetid: 8710409a-67b1-45e5-9cd7-5125443ab921
ms.tgt_platform: multiple
keywords:
- service principal name AD ,how a service composes
ms.topic: article
ms.date: 05/31/2018
---

# How a Service Composes its SPNs

A service can use two functions to compose its SPNs: [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna) is a general-purpose function for composing SPNs and [**DsServerRegisterSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsserverregisterspna) is a specialized function for composing and registering simple SPNs for a host-based service.

A service installer typically uses the [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna) function to compose SPNs, which it then registers on the service's logon account using the [**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna) function. The **DsGetSpn** can perform the following functions.

-   Create a simple SPN with the "<service class>/&lt;host&gt;" format for a host-based service.
-   Create a complex SPN that includes the "&lt;service name&gt;" component used by replicable services or the "&lt;port&gt;" component that distinguishes multiple instances of a service on a single host.
-   Create a single SPN with the "&lt;host&gt;" component set to either the name of a specified host or the name of the local computer by default.
-   Create an array of SPNs for multiple service instances that will run on multiple hosts throughout the forest. Each SPN specifies the name of the host for a service instance.
-   Create an array of SPNs for multiple service instances that will run on the same host. Each SPN specifies the name of the host and a port number for a service instance.

The array of names returned by [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna) must be freed by calling the [**DsFreeSpnArray**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsfreespnarraya) function.

Be aware that the [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna), [**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna), and [**DsServerRegisterSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsserverregisterspna) functions do not verify that SPNs are unique. Because mutual authentication fails if a client presents an SPN that is not unique, verify uniqueness before registering an SPN. To do this, search the global catalog (GC) for **servicePrincipalName** attributes that match your SPN. For more information about searching the GC, see [Searching the Global Catalog](searching-global-catalog-contents.md).

 

 




