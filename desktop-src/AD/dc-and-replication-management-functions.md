---
title: Domain Controller and Replication Management Functions
description: This topic contains a list of functions used for domain controller and replication management.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'a92783c2-ffb8-473e-8484-1c05ca5453ff'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# Domain Controller and Replication Management Functions

The domain controller (DC) and replication management functions provide tools for finding data about a DC, converting the names of network objects between different formats, manipulating service principal names (SPNs) and directory service agents (DSAs), and managing replication of servers. The following functions enable developers to work with domain controllers, replication, and the directory service:

-   [**DsAddSidHistory**](dsaddsidhistory.md)
-   [**DsBind**](dsbind.md)
-   [**DsBindingSetTimeout**](dsbindingsettimeout.md)
-   [**DsBindToISTG**](dsbindtoistg.md)
-   [**DsBindWithCred**](dsbindwithcred.md)
-   [**DsBindWithSpn**](dsbindwithspn.md)
-   [**DsBindWithSpnEx**](dsbindwithspnex.md)
-   [**DsClientMakeSpnForTargetServer**](dsclientmakespnfortargetserver.md)
-   [**DsCrackNames**](dscracknames.md)
-   [**DsCrackSpn**](dscrackspn.md)
-   [**DsCrackUnquotedMangledRdn**](dscrackunquotedmangledrdn.md)
-   [**DsFreeDomainControllerInfo**](dsfreedomaincontrollerinfo.md)
-   [**DsFreeNameResult**](dsfreenameresult.md)
-   [**DsFreePasswordCredentials**](dsfreepasswordcredentials.md)
-   [**DsFreeSchemaGuidMap**](dsfreeschemaguidmap.md)
-   [**DsFreeSpnArray**](dsfreespnarray.md)
-   [**DsGetDomainControllerInfo**](dsgetdomaincontrollerinfo.md)
-   [**DsGetRdnW**](dsgetrdnw.md)
-   [**DsGetSpn**](dsgetspn.md)
-   [**DsInheritSecurityIdentity**](dsinheritsecurityidentity.md)
-   [**DsIsMangledDn**](dsismangleddn.md)
-   [**DsIsMangledRdnValue**](dsismangledrdnvalue.md)
-   [**DsListDomainsInSite**](dslistdomainsinsite.md)
-   [**DsListInfoForServer**](dslistinfoforserver.md)
-   [**DsListRoles**](dslistroles.md)
-   [**DsListServersForDomainInSite**](dslistserversfordomaininsite.md)
-   [**DsListServersInSite**](dslistserversinsite.md)
-   [**DsListSites**](dslistsites.md)
-   [**DsMakePasswordCredentials**](dsmakepasswordcredentials.md)
-   [**DsMakeSpn**](dsmakespn.md)
-   [**DsMapSchemaGuids**](dsmapschemaguids.md)
-   [**DsQuerySitesByCost**](dsquerysitesbycost.md)
-   [**DsQuerySitesFree**](dsquerysitesfree.md)
-   [**DsQuoteRdnValue**](dsquoterdnvalue.md)
-   [**DsRemoveDsDomain**](dsremovedsdomain.md)
-   [**DsRemoveDsServer**](dsremovedsserver.md)
-   [**DsReplicaAdd**](dsreplicaadd.md)
-   [**DsReplicaConsistencyCheck**](dsreplicaconsistencycheck.md)
-   [**DsReplicaDel**](dsreplicadel.md)
-   [**DsReplicaFreeInfo**](dsreplicafreeinfo.md)
-   [**DsReplicaGetInfo**](dsreplicagetinfo.md)
-   [**DsReplicaGetInfo2**](dsreplicagetinfo2.md)
-   [**DsReplicaModify**](dsreplicamodify.md)
-   [**DsReplicaSync**](dsreplicasync.md)
-   [**DsReplicaSyncAll**](dsreplicasyncall.md)
-   [**DsReplicaUpdateRefs**](dsreplicaupdaterefs.md)
-   [**DsReplicaVerifyObjects**](dsreplicaverifyobjects.md)
-   [**DsServerRegisterSpn**](dsserverregisterspn.md)
-   [**DsUnBind**](dsunbind.md)
-   [**DsUnquoteRdnValue**](dsunquoterdnvalue.md)
-   [**DsWriteAccountSpn**](dswriteaccountspn.md)
-   [**SyncUpdateProc**](syncupdateproc.md)

Most of these functions require a handle bound to the directory service. The [**DsBind**](dsbind.md) and [**DsBindWithCred**](dsbindwithcred.md) functions start an RPC session with a particular domain controller, then they bind a handle to the directory service and return the handle. When the handle is no longer required, use the [**DsUnBind**](dsunbind.md) function to end the RPC session and unbind the handle.

Replication occurs between a source server and a destination server. A source server maintains a list of destination servers to which it should replicate, and a destination server maintains a list of source servers from which it receives replication. Use the [**DsReplicaAdd**](dsreplicaadd.md) function to add to the list of source servers on a destination server, and use the [**DsReplicaDel**](dsreplicadel.md) function to remove references from the source server list on a destination server. The [**DsReplicaModify**](dsreplicamodify.md) function may be used to change an existing source server reference on a destination server. To change the list of destination servers on a source server, use the [**DsReplicaUpdateRefs**](dsreplicaupdaterefs.md) function.

Actual replication is performed by the [**DsReplicaSync**](dsreplicasync.md) and [**DsReplicaSyncAll**](dsreplicasyncall.md) functions. The **DsReplicaSync** function synchronizes a specific destination server with a single source server. Use the **DsReplicaSyncAll** function to synchronize a destination server with all other servers in the site.

 

 




