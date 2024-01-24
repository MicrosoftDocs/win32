---
description: What Gets Replicated
ms.assetid: d1f0bc92-37bc-4de2-876a-e6b8b09da58d
title: What Gets Replicated
ms.topic: article
ms.date: 05/31/2018
---

# What Gets Replicated

## Applications

All applications installed on the source computer are replicated except for the following:

<dl> <dt>

<span id="Non-COM__application_elements_and_dependencies"></span><span id="non-com__application_elements_and_dependencies"></span><span id="NON-COM__APPLICATION_ELEMENTS_AND_DEPENDENCIES"></span>Non-COM+ application elements and dependencies
</dt> <dd>

The administrator is responsible for replicating anything that a COM+ application depends on but which is not properly part of the application itself, such as data files and DLLs. COMREPL will not replicate anything outside of COM+ application elements.

</dd> <dt>

<span id="COM__preinstalled_applications"></span><span id="com__preinstalled_applications"></span><span id="COM__PREINSTALLED_APPLICATIONS"></span>COM+ preinstalled applications
</dt> <dd>

Applications that are used internally by COM+ and are installed via the COM+ setup program are not replicated. These include the following:

-   System application
-   COM+ utilities
-   COM+ QC Dead Letter Queue Listener

</dd> <dt>

<span id="Applications_created_by_IIS"></span><span id="applications_created_by_iis"></span><span id="APPLICATIONS_CREATED_BY_IIS"></span>Applications created by IIS
</dt> <dd>

These applications are not replicated and include the following:

-   IIS in-process applications
-   IIS utilities
-   All applications created for isolated or pooled virtual roots

</dd> </dl>

## Computer List

The remote computers named in the **Computers** folder in the Component Services administration tool will not be replicated from source to target computer.

## Properties

The following **LocalComputer** collection properties are replicated:

-   TransactionTimeout
-   ResourcePoolingEnabled
-   DCOMEnabled
-   DefaultAuthenticationLevel
-   DefaultImpersonationLevel
-   SecurityTrackingEnabled
-   CISEnabled
-   SecureReferencesEnabled
-   InternetPortsListed
-   DeafultToInternetPorts
-   Ports
-   RpcProxyEnabled

The following **LocalComputer** collection properties are not replicated:

-   Description
-   ApplicationProxyRSN
-   IsRouter

For descriptions of the **LocalComputer** collection properties, see [**LocalComputer**](localcomputer.md).

## Related topics

<dl> <dt>

[File Management](file-management.md)
</dt> <dt>

[Logging and Error Reporting](logging-and-error-reporting.md)
</dt> <dt>

[Replication Phases](replication-phases.md)
</dt> <dt>

[Using COMREPL](using-comrepl.md)
</dt> </dl>

 

 



