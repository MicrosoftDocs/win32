---
title: Domain Controller and Replication Management Functions
description: This topic contains a list of functions used for domain controller and replication management.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a92783c2-ffb8-473e-8484-1c05ca5453ff
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Domain Controller and Replication Management Functions

The domain controller (DC) and replication management functions provide tools for finding data about a DC, converting the names of network objects between different formats, manipulating service principal names (SPNs) and directory service agents (DSAs), and managing replication of servers. The following functions enable developers to work with domain controllers, replication, and the directory service:

-   [**DsAddSidHistory**](/windows/win32/Ntdsapi/nf-ntdsapi-dsaddsidhistorya?branch=master)
-   [**DsBind**](/windows/win32/Ntdsapi/nf-ntdsapi-dsbinda?branch=master)
-   [**DsBindingSetTimeout**](/windows/win32/Ntdsapi/nf-ntdsapi-dsbindingsettimeout?branch=master)
-   [**DsBindToISTG**](/windows/win32/Ntdsapi/nf-ntdsapi-dsbindtoistga?branch=master)
-   [**DsBindWithCred**](/windows/win32/Ntdsapi/nf-ntdsapi-dsbindwithcreda?branch=master)
-   [**DsBindWithSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dsbindwithspna?branch=master)
-   [**DsBindWithSpnEx**](/windows/win32/Ntdsapi/nf-ntdsapi-dsbindwithspnexa?branch=master)
-   [**DsClientMakeSpnForTargetServer**](/windows/win32/Ntdsapi/nf-ntdsapi-dsclientmakespnfortargetservera?branch=master)
-   [**DsCrackNames**](/windows/win32/Ntdsapi/nf-ntdsapi-dscracknamesa?branch=master)
-   [**DsCrackSpn**](/windows/win32/Dsparse/nf-dsparse-dscrackspna?branch=master)
-   [**DsCrackUnquotedMangledRdn**](/windows/win32/Dsparse/nf-dsparse-dscrackunquotedmangledrdna?branch=master)
-   [**DsFreeDomainControllerInfo**](/windows/win32/Ntdsapi/nf-ntdsapi-dsfreedomaincontrollerinfoa?branch=master)
-   [**DsFreeNameResult**](/windows/win32/Ntdsapi/nf-ntdsapi-dsfreenameresulta?branch=master)
-   [**DsFreePasswordCredentials**](/windows/win32/Ntdsapi/nf-ntdsapi-dsfreepasswordcredentials?branch=master)
-   [**DsFreeSchemaGuidMap**](/windows/win32/Ntdsapi/nf-ntdsapi-dsfreeschemaguidmapa?branch=master)
-   [**DsFreeSpnArray**](/windows/win32/Ntdsapi/nf-ntdsapi-dsfreespnarraya?branch=master)
-   [**DsGetDomainControllerInfo**](/windows/win32/Ntdsapi/nf-ntdsapi-dsgetdomaincontrollerinfoa?branch=master)
-   [**DsGetRdnW**](/windows/win32/Dsparse/nf-dsparse-dsgetrdnw?branch=master)
-   [**DsGetSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dsgetspna?branch=master)
-   [**DsInheritSecurityIdentity**](/windows/win32/Ntdsapi/nf-ntdsapi-dsinheritsecurityidentitya?branch=master)
-   [**DsIsMangledDn**](/windows/win32/Dsparse/nf-dsparse-dsismangleddna?branch=master)
-   [**DsIsMangledRdnValue**](/windows/win32/Dsparse/nf-dsparse-dsismangledrdnvaluea?branch=master)
-   [**DsListDomainsInSite**](/windows/win32/Ntdsapi/nf-ntdsapi-dslistdomainsinsitea?branch=master)
-   [**DsListInfoForServer**](/windows/win32/Ntdsapi/nf-ntdsapi-dslistinfoforservera?branch=master)
-   [**DsListRoles**](/windows/win32/Ntdsapi/nf-ntdsapi-dslistrolesa?branch=master)
-   [**DsListServersForDomainInSite**](/windows/win32/Ntdsapi/nf-ntdsapi-dslistserversfordomaininsitea?branch=master)
-   [**DsListServersInSite**](/windows/win32/Ntdsapi/nf-ntdsapi-dslistserversinsitea?branch=master)
-   [**DsListSites**](/windows/win32/Ntdsapi/nf-ntdsapi-dslistsitesa?branch=master)
-   [**DsMakePasswordCredentials**](/windows/win32/Ntdsapi/nf-ntdsapi-dsmakepasswordcredentialsa?branch=master)
-   [**DsMakeSpn**](/windows/win32/Dsparse/nf-dsparse-dsmakespna?branch=master)
-   [**DsMapSchemaGuids**](/windows/win32/Ntdsapi/nf-ntdsapi-dsmapschemaguidsa?branch=master)
-   [**DsQuerySitesByCost**](/windows/win32/Ntdsapi/nf-ntdsapi-dsquerysitesbycosta?branch=master)
-   [**DsQuerySitesFree**](/windows/win32/Ntdsapi/nf-ntdsapi-dsquerysitesfree?branch=master)
-   [**DsQuoteRdnValue**](/windows/win32/Dsparse/nf-dsparse-dsquoterdnvaluea?branch=master)
-   [**DsRemoveDsDomain**](/windows/win32/Ntdsapi/nf-ntdsapi-dsremovedsdomaina?branch=master)
-   [**DsRemoveDsServer**](/windows/win32/Ntdsapi/nf-ntdsapi-dsremovedsservera?branch=master)
-   [**DsReplicaAdd**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicaadda?branch=master)
-   [**DsReplicaConsistencyCheck**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicaconsistencycheck?branch=master)
-   [**DsReplicaDel**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicadela?branch=master)
-   [**DsReplicaFreeInfo**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicafreeinfo?branch=master)
-   [**DsReplicaGetInfo**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicagetinfow?branch=master)
-   [**DsReplicaGetInfo2**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicagetinfo2w?branch=master)
-   [**DsReplicaModify**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicamodifya?branch=master)
-   [**DsReplicaSync**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicasynca?branch=master)
-   [**DsReplicaSyncAll**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicasyncalla?branch=master)
-   [**DsReplicaUpdateRefs**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicaupdaterefsa?branch=master)
-   [**DsReplicaVerifyObjects**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicaverifyobjectsa?branch=master)
-   [**DsServerRegisterSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dsserverregisterspna?branch=master)
-   [**DsUnBind**](/windows/win32/Ntdsapi/nf-ntdsapi-dsunbinda?branch=master)
-   [**DsUnquoteRdnValue**](/windows/win32/Dsparse/nf-dsparse-dsunquoterdnvaluea?branch=master)
-   [**DsWriteAccountSpn**](/windows/win32/Ntdsapi/nf-ntdsapi-dswriteaccountspna?branch=master)
-   [**SyncUpdateProc**](/windows/win32/Ntdsapi/?branch=master)

Most of these functions require a handle bound to the directory service. The [**DsBind**](/windows/win32/Ntdsapi/nf-ntdsapi-dsbinda?branch=master) and [**DsBindWithCred**](/windows/win32/Ntdsapi/nf-ntdsapi-dsbindwithcreda?branch=master) functions start an RPC session with a particular domain controller, then they bind a handle to the directory service and return the handle. When the handle is no longer required, use the [**DsUnBind**](/windows/win32/Ntdsapi/nf-ntdsapi-dsunbinda?branch=master) function to end the RPC session and unbind the handle.

Replication occurs between a source server and a destination server. A source server maintains a list of destination servers to which it should replicate, and a destination server maintains a list of source servers from which it receives replication. Use the [**DsReplicaAdd**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicaadda?branch=master) function to add to the list of source servers on a destination server, and use the [**DsReplicaDel**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicadela?branch=master) function to remove references from the source server list on a destination server. The [**DsReplicaModify**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicamodifya?branch=master) function may be used to change an existing source server reference on a destination server. To change the list of destination servers on a source server, use the [**DsReplicaUpdateRefs**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicaupdaterefsa?branch=master) function.

Actual replication is performed by the [**DsReplicaSync**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicasynca?branch=master) and [**DsReplicaSyncAll**](/windows/win32/Ntdsapi/nf-ntdsapi-dsreplicasyncalla?branch=master) functions. The **DsReplicaSync** function synchronizes a specific destination server with a single source server. Use the **DsReplicaSyncAll** function to synchronize a destination server with all other servers in the site.

 

 




