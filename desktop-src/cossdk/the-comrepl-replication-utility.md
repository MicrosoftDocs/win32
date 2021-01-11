---
description: COMREPL is a utility that will replicate the COM+ catalog from a given source computer to one or more target computers.
ms.assetid: 11aa7603-61f1-4af0-b6f9-81f484788052
title: The COMREPL Replication Utility
ms.topic: article
ms.date: 05/31/2018
---

# The COMREPL Replication Utility

COMREPL is a utility that will replicate the COM+ catalog from a given source computer to one or more target computers. Think of the source computer representing a "master configuration." COMREPL is used to replicate this master configuration to maintain a set of identically configured computers.

The unit of replication is the entire COM+ configuration on the master computer. All COM+ applications on the master are replicated to the target computers; it's all or nothing. In addition, all COM+ applications previously installed on the target computers, with the exception of the COM+ preinstalled applications, will be deleted as part of the replication process.

COMREPL replicates only COM+ configuration data. This includes COM+ applications and COM+ specific computer settings. Microsoft Internet Information Services (IIS) has a similar utility (IISSync), which makes use of COMREPL to replicate IIS and COM+ configuration.

For detailed information on launching and using COMREPL, see the following topics in this section:

-   [Using COMREPL](using-comrepl.md)
-   [What Gets Replicated](what-gets-replicated.md)
-   [Replication Phases](replication-phases.md)
-   [File Management](file-management.md)
-   [Logging and Error Reporting](logging-and-error-reporting.md)

## Related topics

<dl> <dt>

[Creating Installation Packages for COM+ Applications](creating-installation-packages-for-com--applications.md)
</dt> <dt>

[Deploying Application Proxies](deploying-application-proxies.md)
</dt> <dt>

[The COM+ Catalog](the-com--catalog.md)
</dt> </dl>

 

 



