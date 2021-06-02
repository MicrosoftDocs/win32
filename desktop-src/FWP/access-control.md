---
title: Access Control (Windows Filtering Platform)
description: In Windows Filtering Platform (WFP), the Base Filtering Engine (BFE) service implements the standard Windows access control model based on access tokens and security descriptors.
ms.assetid: 936ad5f0-d5cd-47ed-b9e5-a7d82a4da603
ms.topic: article
ms.date: 05/31/2018
---

# Access Control (Windows Filtering Platform)

In Windows Filtering Platform (WFP), the Base Filtering Engine (BFE) service implements the standard [Windows access control model](/windows/desktop/SecAuthZ/access-control-model) based on access tokens and security descriptors.

## Access Control Model

Security descriptors can be specified when adding new WFP objects, such as filters and sub-layers. Security descriptors are managed using the WFP management functions **Fwpm\*GetSecurityInfo0** and **Fwpm\*SetSecurityInfo0**, where **\*** stands for the WFP object's name. These functions are semantically identical to the Windows [**GetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-getsecurityinfo) and [**SetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-setsecurityinfo) functions.

> [!Note]  
> The **Fwpm\*SetSecurityInfo0** functions cannot be called from within an explicit transaction.

 

> [!Note]  
> The **Fwpm\*SetSecurityInfo0** functions can only be called from within a dynamic session if they are being used to manage a dynamic object created within the same session.

 

The default security descriptor for the filter engine (the root Engine object in the diagram below) is as follows.

-   Grant **GENERIC\_ALL** (GA) access rights to the built-in Administrators group.
-   Grant **GENERIC\_READ** (GR) **GENERIC\_WRITE** (GW) **GENERIC\_EXECUTE** (GX) access rights to network configuration operators.
-   Grant **GRGWGX** access rights to the following service security identifiers (SSIDs): MpsSvc (Windows Firewall), NapAgent (Network Access Protection Agent), PolicyAgent (IPsec Policy Agent), RpcSs (Remote Procedure Call), and WdiServiceHost (Diagnostic Service Host).
-   Grant **FWPM\_ACTRL\_OPEN** and **FWPM\_ACTRL\_CLASSIFY** to everyone. (These are WFP-specific access rights, described in table below.)

The remaining default security descriptors are derived through inheritance.

There are some access checks, such as for **Fwpm\*Add0**, **Fwpm\*CreateEnumHandle0**, **Fwpm\*SubscribeChanges0** function calls, that cannot be done at the individual object level. For these functions, there are container objects for each object type. For the standard object types (for example, providers, callouts, filters), the existing **Fwpm\*GetSecurityInfo0** and **Fwpm\*SetSecurityInfo0** functions are overloaded, such that a null **GUID** parameter identifies the associated container. For the other object types (for example, network events and IPsec security associations), there are explicit functions for managing the container's security information.

BFE supports automatic inheritance of Discretionary Access Control List (DACL) access control entries (ACEs). BFE does not support System Access Control List (SACL) ACEs. Objects inherit ACEs from their container. Containers inherit ACEs from the filter engine. The propagation paths are shown in the diagram below.

![Diagram that shows the ACE propagation paths, starting with 'Engine'.](images/access-control.jpg)

For the standard object types, BFE enforces all the generic and standard access rights. In addition, WFP defines the following specific access rights.



| WFP Access Right                                                                                                                        | Description                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FWPM_ACTRL_ADD"></span><span id="fwpm_actrl_add"></span>**FWPM\_ACTRL\_ADD**<br/>                                       | Required to add an object to a container.<br/>                                                                                                                     |
| <span id="FWPM_ACTRL_ADD_LINK"></span><span id="fwpm_actrl_add_link"></span>**FWPM\_ACTRL\_ADD\_LINK**<br/>                       | Required to create an association to an object. For example, to add a filter that references a callout, the caller must have ADD\_LINK access to the callout.<br/> |
| <span id="FWPM_ACTRL_BEGIN_READ_TXN"></span><span id="fwpm_actrl_begin_read_txn"></span>**FWPM\_ACTRL\_BEGIN\_READ\_TXN**<br/>    | Required to begin an explicit read transaction.<br/>                                                                                                               |
| <span id="FWPM_ACTRL_BEGIN_WRITE_TXN"></span><span id="fwpm_actrl_begin_write_txn"></span>**FWPM\_ACTRL\_BEGIN\_WRITE\_TXN**<br/> | Required to begin an explicit write transaction.<br/>                                                                                                              |
| <span id="FWPM_ACTRL_CLASSIFY"></span><span id="fwpm_actrl_classify"></span>**FWPM\_ACTRL\_CLASSIFY**<br/>                        | Required to classify against a user-mode layer.<br/>                                                                                                               |
| <span id="FWPM_ACTRL_ENUM"></span><span id="fwpm_actrl_enum"></span>**FWPM\_ACTRL\_ENUM**<br/>                                    | Required to enumerate the objects in a container. However, the enumerator only returns objects to which the caller has FWPM\_ACTRL\_READ access.<br/>              |
| <span id="FWPM_ACTRL_OPEN"></span><span id="fwpm_actrl_open"></span>**FWPM\_ACTRL\_OPEN**<br/>                                    | Required to open a session with BFE.<br/>                                                                                                                          |
| <span id="FWPM_ACTRL_READ"></span><span id="fwpm_actrl_read"></span>**FWPM\_ACTRL\_READ**<br/>                                    | Required to read an object's properties.<br/>                                                                                                                      |
| <span id="FWPM_ACTRL_READ_STATS"></span><span id="fwpm_actrl_read_stats"></span>**FWPM\_ACTRL\_READ\_STATS**<br/>                 | Required to read statistics.<br/>                                                                                                                                  |
| <span id="FWPM_ACTRL_SUBSCRIBE"></span><span id="fwpm_actrl_subscribe"></span>**FWPM\_ACTRL\_SUBSCRIBE**<br/>                     | Required to subscribe for notifications. Subscribers will only receive notifications for objects to which they have FWPM\_ACTRL\_READ access.<br/>                 |
| <span id="FWPM_ACTRL_WRITE"></span><span id="fwpm_actrl_write"></span>**FWPM\_ACTRL\_WRITE**<br/>                                 | Required to set engine options.<br/>                                                                                                                               |



 

BFE skips all access checks for kernel-mode callers.

In order to prevent administrators from locking themselves out of BFE, members of the built-in administrators group are always granted **FWPM\_ACTRL\_OPEN** to the engine object. Thus, an administrator can regain access through the following steps.

-   Enable the **SE\_TAKE\_OWNERSHIP\_NAME** privilege.
-   Call [**FwpmEngineOpen0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineopen0). The call succeeds because the caller is a member of Built-in Administrators.
-   Take ownership of the engine object. This succeeds because the caller has the **SE\_TAKE\_OWNERSHIP\_NAME** privilege.
-   Update the DACL. This succeeds because the owner always has **WRITE\_DAC** access

Since BFE supports its own custom auditing, it does not generate generic object access audits. Thus, the SACL is ignored.

## WFP Required Access Rights

The table below shows the access rights required by the WFP functions in order to access various filtering platform objects. The **FwpmFilter\*** functions are listed as an example for accessing the standard objects. All the other functions that access standard objects follow the **FwpmFilter\*** functions access model.



Function

Object Checked

Access Required

[**FwpmEngineOpen0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineopen0)

Engine

**FWPM\_ACTRL\_OPEN**

[**FwpmEngineGetOption0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmenginegetoption0)

Engine

**FWPM\_ACTRL\_READ**

[**FwpmEngineSetOption0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmenginesetoption0)

Engine

**FWPM\_ACTRL\_WRITE**

[**FwpmSessionCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsessioncreateenumhandle0)

Engine

**FWPM\_ACTRL\_ENUM**

[**FwpmTransactionBegin0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmtransactionbegin0)

Engine

**FWPM\_ACTRL\_BEGIN\_READ\_TXN** & **FWPM\_ACTRL\_BEGIN\_WRITE\_TXN**

[**FwpmFilterAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilteradd0)

Container Provider<br/> Layer<br/> Sub-Layer<br/> Callout<br/> Provider Context<br/>

**FWPM\_ACTRL\_ADDFWPM\_ACTRL\_ADD\_LINK**<br/> **FWPM\_ACTRL\_ADD\_LINK**<br/> **FWPM\_ACTRL\_ADD\_LINK**<br/> **FWPM\_ACTRL\_ADD\_LINK**<br/> **FWPM\_ACTRL\_ADD\_LINK**<br/>

[**FwpmFilterDeleteById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilterdeletebyid0)[**FwpmFilterDeleteByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfilterdeletebykey0)<br/>

Filter

**DELETE**

[**FwpmFilterGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltergetbyid0)[**FwpmFilterGetByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltergetbykey0)<br/>

Filter

**FWPM\_ACTRL\_READ**

[**FwpmFilterCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltercreateenumhandle0)

Container Filter<br/>

**FWPM\_ACTRL\_ENUMFWPM\_ACTRL\_READ**<br/>

[**FwpmFilterSubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltersubscribechanges0)

Container

**FWPM\_ACTRL\_SUBSCRIBE**

[**FwpmFilterSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmfiltersubscriptionsget0)

Container

**FWPM\_ACTRL\_READ**

[**IPsecGetStatistics0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecgetstatistics0)

IPsec SA DB

**FWPM\_ACTRL\_READ\_STATS**

[**IPsecSaContextCreate0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreate0)[**IPsecSaContextGetSpi0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextgetspi0)<br/> [**IPsecSaContextAddInbound0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddinbound0)<br/> [**IPsecSaContextAddOutbound0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddoutbound0)<br/>

IPsec SA DB

**FWPM\_ACTRL\_ADD**

[**IPsecSaContextDeleteById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextdeletebyid0)[**IPsecSaContextExpire0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextexpire0)<br/>

IPsec SA DB

**DELETE**

[**IPsecSaContextGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextgetbyid0)

IPsec SA DB

**FWPM\_ACTRL\_READ**

[**IPsecSaContextCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreateenumhandle0)[**IPsecSaCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacreateenumhandle0)<br/>

IPsec SA DB

**FWPM\_ACTRL\_ENUM** & **FWPM\_ACTRL\_READ**

[**IkeextGetStatistics0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ikeextgetstatistics0)

IKE SA DB

**FWPM\_ACTRL\_READ\_STATS**

[**IkeextSaDeleteById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ikeextsadeletebyid0)

IKE SA DB

**DELETE**

[**IkeextSaGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ikeextsagetbyid0)

IKE SA DB

**FWPM\_ACTRL\_READ**

[**IkeextSaCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ikeextsacreateenumhandle0)

IKE SA DB

**FWPM\_ACTRL\_ENUM** & **FWPM\_ACTRL\_READ**

[**FwpmNetEventCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmneteventcreateenumhandle0)

Container

**FWPM\_ACTRL\_ENUM**

[**FwpmIPsecTunnelAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmipsectunneladd0)[**FwpmIPsecTunnelDeleteByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmipsectunneldeletebykey0)<br/>

No additional access checks beyond those for the individual filters and provider contexts



 

## Related topics

<dl> <dt>

[**Standard Access Rights**](/windows/desktop/SecAuthZ/standard-access-rights)
</dt> <dt>

[Windows access control model](/windows/desktop/SecAuthZ/access-control-model)
</dt> <dt>

[**Windows Filtering Platform Access Rights Identifiers**](access-right-identifiers.md)
</dt> </dl>

 

