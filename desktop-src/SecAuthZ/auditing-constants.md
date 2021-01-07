---
description: Represent categories and subcategories of audit-policy events.
ms.assetid: e3b12139-947d-4922-91fd-f9833c069011
title: Auditing Constants (Ntsecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Auditing Constants

The following constants represent categories and subcategories of audit-policy events.

The following constants represent categories of audit-policy events. These constants are defined as **GUID** structures in Ntsecapi.h.

<dl> <dt>

<span id="Audit_System"></span><span id="audit_system"></span><span id="AUDIT_SYSTEM"></span>**Audit\_System**
</dt> <dd> <dl> <dt>

69979848-797a-11d9-bed3-505054503030
</dt> <dt>



Audit attempts to shut down or restart the computer. Also, audit events that affect system security or the security log.


</dt> </dl> </dd> <dt>

<span id="Audit_Logon"></span><span id="audit_logon"></span><span id="AUDIT_LOGON"></span>**Audit\_Logon**
</dt> <dd> <dl> <dt>

69979849-797a-11d9-bed3-505054503030
</dt> <dt>



Audit attempts to log on to or log off of the system. Also, audit attempts to make a network connection.


</dt> </dl> </dd> <dt>

<span id="Audit_ObjectAccess"></span><span id="audit_objectaccess"></span><span id="AUDIT_OBJECTACCESS"></span>**Audit\_ObjectAccess**
</dt> <dd> <dl> <dt>

6997984a-797a-11d9-bed3-505054503030
</dt> <dt>



Audit attempts to access securable objects.


</dt> </dl> </dd> <dt>

<span id="Audit_PrivilegeUse"></span><span id="audit_privilegeuse"></span><span id="AUDIT_PRIVILEGEUSE"></span>**Audit\_PrivilegeUse**
</dt> <dd> <dl> <dt>

6997984b-797a-11d9-bed3-505054503030
</dt> <dt>



Audit attempts to use [*privileges*](/windows/desktop/SecGloss/p-gly).


</dt> </dl> </dd> <dt>

<span id="Audit_DetailedTracking"></span><span id="audit_detailedtracking"></span><span id="AUDIT_DETAILEDTRACKING"></span>**Audit\_DetailedTracking**
</dt> <dd> <dl> <dt>

6997984c-797a-11d9-bed3-505054503030
</dt> <dt>



Audit-specific events, such as program activation, some forms of handle duplication, indirect access to an object, and process exit.


</dt> </dl> </dd> <dt>

<span id="Audit_PolicyChange"></span><span id="audit_policychange"></span><span id="AUDIT_POLICYCHANGE"></span>**Audit\_PolicyChange**
</dt> <dd> <dl> <dt>

6997984d-797a-11d9-bed3-505054503030
</dt> <dt>



Audit attempts to change [**Policy**](/windows/desktop/SecMgmt/the-policy-object-type) object rules.


</dt> </dl> </dd> <dt>

<span id="Audit_AccountManagement"></span><span id="audit_accountmanagement"></span><span id="AUDIT_ACCOUNTMANAGEMENT"></span>**Audit\_AccountManagement**
</dt> <dd> <dl> <dt>

6997984e-797a-11d9-bed3-505054503030
</dt> <dt>



Audit attempts to create, delete, or change user or group accounts. Also, audit password changes.


</dt> </dl> </dd> <dt>

<span id="Audit_DirectoryServiceAccess"></span><span id="audit_directoryserviceaccess"></span><span id="AUDIT_DIRECTORYSERVICEACCESS"></span>**Audit\_DirectoryServiceAccess**
</dt> <dd> <dl> <dt>

6997984f-797a-11d9-bed3-505054503030
</dt> <dt>



Audit attempts to access the directory service.


</dt> </dl> </dd> <dt>

<span id="Audit_AccountLogon"></span><span id="audit_accountlogon"></span><span id="AUDIT_ACCOUNTLOGON"></span>**Audit\_AccountLogon**
</dt> <dd> <dl> <dt>

69979850-797a-11d9-bed3-505054503030
</dt> <dt>



Audit logon attempts by privileged accounts that log on to the domain controller. These audit events are generated when the Kerberos [*Key Distribution Center*](/windows/desktop/SecGloss/k-gly) (KDC) logs on to the domain controller.


</dt> </dl> </dd> </dl>

The following constants represent subcategories of audit-policy events. These constants are defined as **GUID** structures in Ntsecapi.h.

<dl> <span id="Audit_System_SecurityStateChange"></span><span id="audit_system_securitystatechange"></span><span id="AUDIT_SYSTEM_SECURITYSTATECHANGE"></span>**Audit\_System\_SecurityStateChange** (0cce9210-69ae-11d9-bed3-505054503030)  
<span id="Audit_System_SecuritySubsystemExtension"></span><span id="audit_system_securitysubsystemextension"></span><span id="AUDIT_SYSTEM_SECURITYSUBSYSTEMEXTENSION"></span>**Audit\_System\_SecuritySubsystemExtension** (0cce9211-69ae-11d9-bed3-505054503030)  
<span id="Audit_System_Integrity"></span><span id="audit_system_integrity"></span><span id="AUDIT_SYSTEM_INTEGRITY"></span>**Audit\_System\_Integrity** (0cce9212-69ae-11d9-bed3-505054503030)  
<span id="Audit_System_IPSecDriverEvents"></span><span id="audit_system_ipsecdriverevents"></span><span id="AUDIT_SYSTEM_IPSECDRIVEREVENTS"></span>**Audit\_System\_IPSecDriverEvents** (0cce9213-69ae-11d9-bed3-505054503030)  
<span id="Audit_System_Others"></span><span id="audit_system_others"></span><span id="AUDIT_SYSTEM_OTHERS"></span>**Audit\_System\_Others** (0cce9214-69ae-11d9-bed3-505054503030)  
<span id="Audit_Logon_Logon"></span><span id="audit_logon_logon"></span><span id="AUDIT_LOGON_LOGON"></span>**Audit\_Logon\_Logon** (0cce9215-69ae-11d9-bed3-505054503030)  
<span id="Audit_Logon_Logoff"></span><span id="audit_logon_logoff"></span><span id="AUDIT_LOGON_LOGOFF"></span>**Audit\_Logon\_Logoff** (0cce9216-69ae-11d9-bed3-505054503030)  
<span id="Audit_Logon_AccountLockout"></span><span id="audit_logon_accountlockout"></span><span id="AUDIT_LOGON_ACCOUNTLOCKOUT"></span>**Audit\_Logon\_AccountLockout** (0cce9217-69ae-11d9-bed3-505054503030)  
<span id="Audit_Logon_IPSecMainMode"></span><span id="audit_logon_ipsecmainmode"></span><span id="AUDIT_LOGON_IPSECMAINMODE"></span>**Audit\_Logon\_IPSecMainMode** (0cce9218-69ae-11d9-bed3-505054503030)  
<span id="Audit_Logon_IPSecQuickMode"></span><span id="audit_logon_ipsecquickmode"></span><span id="AUDIT_LOGON_IPSECQUICKMODE"></span>**Audit\_Logon\_IPSecQuickMode** (0cce9219-69ae-11d9-bed3-505054503030)  
<span id="Audit_Logon_IPSecUserMode"></span><span id="audit_logon_ipsecusermode"></span><span id="AUDIT_LOGON_IPSECUSERMODE"></span>**Audit\_Logon\_IPSecUserMode** (0cce921a-69ae-11d9-bed3-505054503030)  
<span id="Audit_Logon_SpecialLogon"></span><span id="audit_logon_speciallogon"></span><span id="AUDIT_LOGON_SPECIALLOGON"></span>**Audit\_Logon\_SpecialLogon** (0cce921b-69ae-11d9-bed3-505054503030)  
<span id="Audit_Logon_Others"></span><span id="audit_logon_others"></span><span id="AUDIT_LOGON_OTHERS"></span>**Audit\_Logon\_Others** (0cce921c-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_FileSystem"></span><span id="audit_objectaccess_filesystem"></span><span id="AUDIT_OBJECTACCESS_FILESYSTEM"></span>**Audit\_ObjectAccess\_FileSystem** (0cce921d-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_Registry"></span><span id="audit_objectaccess_registry"></span><span id="AUDIT_OBJECTACCESS_REGISTRY"></span>**Audit\_ObjectAccess\_Registry** (0cce921e-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_Kernel"></span><span id="audit_objectaccess_kernel"></span><span id="AUDIT_OBJECTACCESS_KERNEL"></span>**Audit\_ObjectAccess\_Kernel** (0cce921f-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_Sam"></span><span id="audit_objectaccess_sam"></span><span id="AUDIT_OBJECTACCESS_SAM"></span>**Audit\_ObjectAccess\_Sam** (0cce9220-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_CertificationServices"></span><span id="audit_objectaccess_certificationservices"></span><span id="AUDIT_OBJECTACCESS_CERTIFICATIONSERVICES"></span>**Audit\_ObjectAccess\_CertificationServices** (0cce9221-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_ApplicationGenerated"></span><span id="audit_objectaccess_applicationgenerated"></span><span id="AUDIT_OBJECTACCESS_APPLICATIONGENERATED"></span>**Audit\_ObjectAccess\_ApplicationGenerated** (0cce9222-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_Handle"></span><span id="audit_objectaccess_handle"></span><span id="AUDIT_OBJECTACCESS_HANDLE"></span>**Audit\_ObjectAccess\_Handle** (0cce9223-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_Share"></span><span id="audit_objectaccess_share"></span><span id="AUDIT_OBJECTACCESS_SHARE"></span>**Audit\_ObjectAccess\_Share** (0cce9224-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_FirewallPacketDrops"></span><span id="audit_objectaccess_firewallpacketdrops"></span><span id="AUDIT_OBJECTACCESS_FIREWALLPACKETDROPS"></span>**Audit\_ObjectAccess\_FirewallPacketDrops** (0cce9225-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_FirewallConnection"></span><span id="audit_objectaccess_firewallconnection"></span><span id="AUDIT_OBJECTACCESS_FIREWALLCONNECTION"></span>**Audit\_ObjectAccess\_FirewallConnection** (0cce9226-69ae-11d9-bed3-505054503030)  
<span id="Audit_ObjectAccess_Other"></span><span id="audit_objectaccess_other"></span><span id="AUDIT_OBJECTACCESS_OTHER"></span>**Audit\_ObjectAccess\_Other** (0cce9227-69ae-11d9-bed3-505054503030)  
<span id="Audit_PrivilegeUse_Sensitive"></span><span id="audit_privilegeuse_sensitive"></span><span id="AUDIT_PRIVILEGEUSE_SENSITIVE"></span>**Audit\_PrivilegeUse\_Sensitive** (0cce9228-69ae-11d9-bed3-505054503030)  
<span id="Audit_PrivilegeUse_NonSensitive"></span><span id="audit_privilegeuse_nonsensitive"></span><span id="AUDIT_PRIVILEGEUSE_NONSENSITIVE"></span>**Audit\_PrivilegeUse\_NonSensitive** (0cce9229-69ae-11d9-bed3-505054503030)  
<span id="Audit_PrivilegeUse_Others"></span><span id="audit_privilegeuse_others"></span><span id="AUDIT_PRIVILEGEUSE_OTHERS"></span>**Audit\_PrivilegeUse\_Others** (0cce922a-69ae-11d9-bed3-505054503030)  
<span id="Audit_DetailedTracking_ProcessCreation"></span><span id="audit_detailedtracking_processcreation"></span><span id="AUDIT_DETAILEDTRACKING_PROCESSCREATION"></span>**Audit\_DetailedTracking\_ProcessCreation** (0cce922b-69ae-11d9-bed3-505054503030)  
<span id="Audit_DetailedTracking_ProcessTermination"></span><span id="audit_detailedtracking_processtermination"></span><span id="AUDIT_DETAILEDTRACKING_PROCESSTERMINATION"></span>**Audit\_DetailedTracking\_ProcessTermination** (0cce922c-69ae-11d9-bed3-505054503030)  
<span id="Audit_DetailedTracking_DpapiActivity"></span><span id="audit_detailedtracking_dpapiactivity"></span><span id="AUDIT_DETAILEDTRACKING_DPAPIACTIVITY"></span>**Audit\_DetailedTracking\_DpapiActivity** (0cce922d-69ae-11d9-bed3-505054503030)  
<span id="Audit_DetailedTracking_RpcCall"></span><span id="audit_detailedtracking_rpccall"></span><span id="AUDIT_DETAILEDTRACKING_RPCCALL"></span>**Audit\_DetailedTracking\_RpcCall** (0cce922e-69ae-11d9-bed3-505054503030)  
<span id="Audit_PolicyChange_AuditPolicy"></span><span id="audit_policychange_auditpolicy"></span><span id="AUDIT_POLICYCHANGE_AUDITPOLICY"></span>**Audit\_PolicyChange\_AuditPolicy** (0cce922f-69ae-11d9-bed3-505054503030)  
<span id="Audit_PolicyChange_AuthenticationPolicy"></span><span id="audit_policychange_authenticationpolicy"></span><span id="AUDIT_POLICYCHANGE_AUTHENTICATIONPOLICY"></span>**Audit\_PolicyChange\_AuthenticationPolicy** (0cce9230-69ae-11d9-bed3-505054503030)  
<span id="Audit_PolicyChange_AuthorizationPolicy"></span><span id="audit_policychange_authorizationpolicy"></span><span id="AUDIT_POLICYCHANGE_AUTHORIZATIONPOLICY"></span>**Audit\_PolicyChange\_AuthorizationPolicy** (0cce9231-69ae-11d9-bed3-505054503030)  
<span id="Audit_PolicyChange_MpsscvRulePolicy"></span><span id="audit_policychange_mpsscvrulepolicy"></span><span id="AUDIT_POLICYCHANGE_MPSSCVRULEPOLICY"></span>**Audit\_PolicyChange\_MpsscvRulePolicy** (0cce9232-69ae-11d9-bed3-505054503030)  
<span id="Audit_PolicyChange_WfpIPSecPolicy"></span><span id="audit_policychange_wfpipsecpolicy"></span><span id="AUDIT_POLICYCHANGE_WFPIPSECPOLICY"></span>**Audit\_PolicyChange\_WfpIPSecPolicy** (0cce9233-69ae-11d9-bed3-505054503030)  
<span id="Audit_PolicyChange_Others"></span><span id="audit_policychange_others"></span><span id="AUDIT_POLICYCHANGE_OTHERS"></span>**Audit\_PolicyChange\_Others** (0cce9234-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountManagement_UserAccount"></span><span id="audit_accountmanagement_useraccount"></span><span id="AUDIT_ACCOUNTMANAGEMENT_USERACCOUNT"></span>**Audit\_AccountManagement\_UserAccount** (0cce9235-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountManagement_ComputerAccount"></span><span id="audit_accountmanagement_computeraccount"></span><span id="AUDIT_ACCOUNTMANAGEMENT_COMPUTERACCOUNT"></span>**Audit\_AccountManagement\_ComputerAccount** (0cce9236-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountManagement_SecurityGroup"></span><span id="audit_accountmanagement_securitygroup"></span><span id="AUDIT_ACCOUNTMANAGEMENT_SECURITYGROUP"></span>**Audit\_AccountManagement\_SecurityGroup** (0cce9237-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountManagement_DistributionGroup"></span><span id="audit_accountmanagement_distributiongroup"></span><span id="AUDIT_ACCOUNTMANAGEMENT_DISTRIBUTIONGROUP"></span>**Audit\_AccountManagement\_DistributionGroup** (0cce9238-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountManagement_ApplicationGroup"></span><span id="audit_accountmanagement_applicationgroup"></span><span id="AUDIT_ACCOUNTMANAGEMENT_APPLICATIONGROUP"></span>**Audit\_AccountManagement\_ApplicationGroup** (0cce9239-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountManagement_Others"></span><span id="audit_accountmanagement_others"></span><span id="AUDIT_ACCOUNTMANAGEMENT_OTHERS"></span>**Audit\_AccountManagement\_Others** (0cce923a-69ae-11d9-bed3-505054503030)  
<span id="Audit_DSAccess_DSAccess"></span><span id="audit_dsaccess_dsaccess"></span><span id="AUDIT_DSACCESS_DSACCESS"></span>**Audit\_DSAccess\_DSAccess** (0cce923b-69ae-11d9-bed3-505054503030)  
<span id="Audit_DsAccess_AdAuditChanges"></span><span id="audit_dsaccess_adauditchanges"></span><span id="AUDIT_DSACCESS_ADAUDITCHANGES"></span>**Audit\_DsAccess\_AdAuditChanges** (0cce923c-69ae-11d9-bed3-505054503030)  
<span id="Audit_Ds_Replication"></span><span id="audit_ds_replication"></span><span id="AUDIT_DS_REPLICATION"></span>**Audit\_Ds\_Replication** (0cce923d-69ae-11d9-bed3-505054503030)  
<span id="Audit_Ds_DetailedReplication"></span><span id="audit_ds_detailedreplication"></span><span id="AUDIT_DS_DETAILEDREPLICATION"></span>**Audit\_Ds\_DetailedReplication** (0cce923e-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountLogon_CredentialValidation"></span><span id="audit_accountlogon_credentialvalidation"></span><span id="AUDIT_ACCOUNTLOGON_CREDENTIALVALIDATION"></span>**Audit\_AccountLogon\_CredentialValidation** (0cce923f-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountLogon_Kerberos"></span><span id="audit_accountlogon_kerberos"></span><span id="AUDIT_ACCOUNTLOGON_KERBEROS"></span>**Audit\_AccountLogon\_Kerberos** (0cce9240-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountLogon_Others"></span><span id="audit_accountlogon_others"></span><span id="AUDIT_ACCOUNTLOGON_OTHERS"></span>**Audit\_AccountLogon\_Others** (0cce9241-69ae-11d9-bed3-505054503030)  
<span id="Audit_AccountLogon_KerbCredentialValidation"></span><span id="audit_accountlogon_kerbcredentialvalidation"></span><span id="AUDIT_ACCOUNTLOGON_KERBCREDENTIALVALIDATION"></span>**Audit\_AccountLogon\_KerbCredentialValidation** (0cce9242-69ae-11d9-bed3-505054503030)  
<span id="Audit_Logon_NPS"></span><span id="audit_logon_nps"></span><span id="AUDIT_LOGON_NPS"></span>**Audit\_Logon\_NPS** (0cce9243-69ae-11d9-bed3-505054503030)  
</dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Ntsecapi.h</dt> </dl> |



 

