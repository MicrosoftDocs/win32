---
title: Domain Controller and Replication Management Functions
description: This topic contains a list of functions used for domain controller and replication management.
ms.assetid: a92783c2-ffb8-473e-8484-1c05ca5453ff
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Domain Controller and Replication Management Functions

The domain controller (DC) and replication management functions provide tools for finding data about a DC, converting the names of network objects between different formats, manipulating service principal names (SPNs) and directory service agents (DSAs), and managing replication of servers. The following functions enable developers to work with domain controllers, replication, and the directory service:

-   [**DsAddSidHistory**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsaddsidhistorya)
-   [**DsBind**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsbinda)
-   [**DsBindingSetTimeout**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsbindingsettimeout)
-   [**DsBindToISTG**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsbindtoistga)
-   [**DsBindWithCred**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsbindwithcreda)
-   [**DsBindWithSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsbindwithspna)
-   [**DsBindWithSpnEx**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsbindwithspnexa)
-   [**DsClientMakeSpnForTargetServer**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsclientmakespnfortargetservera)
-   [**DsCrackNames**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dscracknamesa)
-   [**DsCrackSpn**](/windows/desktop/api/Dsparse/nf-dsparse-dscrackspna)
-   [**DsCrackUnquotedMangledRdn**](/windows/desktop/api/Dsparse/nf-dsparse-dscrackunquotedmangledrdna)
-   [**DsFreeDomainControllerInfo**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsfreedomaincontrollerinfoa)
-   [**DsFreeNameResult**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsfreenameresulta)
-   [**DsFreePasswordCredentials**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsfreepasswordcredentials)
-   [**DsFreeSchemaGuidMap**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsfreeschemaguidmapa)
-   [**DsFreeSpnArray**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsfreespnarraya)
-   [**DsGetDomainControllerInfo**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetdomaincontrollerinfoa)
-   [**DsGetRdnW**](/windows/desktop/api/Dsparse/nf-dsparse-dsgetrdnw)
-   [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna)
-   [**DsInheritSecurityIdentity**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsinheritsecurityidentitya)
-   [**DsIsMangledDn**](/windows/desktop/api/Dsparse/nf-dsparse-dsismangleddna)
-   [**DsIsMangledRdnValue**](/windows/desktop/api/Dsparse/nf-dsparse-dsismangledrdnvaluea)
-   [**DsListDomainsInSite**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dslistdomainsinsitea)
-   [**DsListInfoForServer**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dslistinfoforservera)
-   [**DsListRoles**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dslistrolesa)
-   [**DsListServersForDomainInSite**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dslistserversfordomaininsitea)
-   [**DsListServersInSite**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dslistserversinsitea)
-   [**DsListSites**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dslistsitesa)
-   [**DsMakePasswordCredentials**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsmakepasswordcredentialsa)
-   [**DsMakeSpn**](/windows/desktop/api/Dsparse/nf-dsparse-dsmakespna)
-   [**DsMapSchemaGuids**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsmapschemaguidsa)
-   [**DsQuerySitesByCost**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsquerysitesbycosta)
-   [**DsQuerySitesFree**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsquerysitesfree)
-   [**DsQuoteRdnValue**](/windows/desktop/api/Dsparse/nf-dsparse-dsquoterdnvaluea)
-   [**DsRemoveDsDomain**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsremovedsdomaina)
-   [**DsRemoveDsServer**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsremovedsservera)
-   [**DsReplicaAdd**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicaadda)
-   [**DsReplicaConsistencyCheck**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicaconsistencycheck)
-   [**DsReplicaDel**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicadela)
-   [**DsReplicaFreeInfo**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicafreeinfo)
-   [**DsReplicaGetInfo**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicagetinfow)
-   [**DsReplicaGetInfo2**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicagetinfo2w)
-   [**DsReplicaModify**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicamodifya)
-   [**DsReplicaSync**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicasynca)
-   [**DsReplicaSyncAll**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicasyncalla)
-   [**DsReplicaUpdateRefs**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicaupdaterefsa)
-   [**DsReplicaVerifyObjects**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicaverifyobjectsa)
-   [**DsServerRegisterSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsserverregisterspna)
-   [**DsUnBind**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsunbinda)
-   [**DsUnquoteRdnValue**](/windows/desktop/api/Dsparse/nf-dsparse-dsunquoterdnvaluea)
-   [**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna)
-   [**SyncUpdateProc**](/previous-versions/windows/desktop/legacy/ms677968(v=vs.85))

Most of these functions require a handle bound to the directory service. The [**DsBind**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsbinda) and [**DsBindWithCred**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsbindwithcreda) functions start an RPC session with a particular domain controller, then they bind a handle to the directory service and return the handle. When the handle is no longer required, use the [**DsUnBind**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsunbinda) function to end the RPC session and unbind the handle.

Replication occurs between a source server and a destination server. A source server maintains a list of destination servers to which it should replicate, and a destination server maintains a list of source servers from which it receives replication. Use the [**DsReplicaAdd**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicaadda) function to add to the list of source servers on a destination server, and use the [**DsReplicaDel**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicadela) function to remove references from the source server list on a destination server. The [**DsReplicaModify**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicamodifya) function may be used to change an existing source server reference on a destination server. To change the list of destination servers on a source server, use the [**DsReplicaUpdateRefs**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicaupdaterefsa) function.

Actual replication is performed by the [**DsReplicaSync**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicasynca) and [**DsReplicaSyncAll**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicasyncalla) functions. The **DsReplicaSync** function synchronizes a specific destination server with a single source server. Use the **DsReplicaSyncAll** function to synchronize a destination server with all other servers in the site.

 

 