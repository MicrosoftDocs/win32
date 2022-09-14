---
title: IPsec Functions
description: IPsec Functions
ms.assetid: db656c58-7776-44c4-a7ce-c38e59b37c74
keywords:
- Windows Filtering Platform API IPsec Functions
ms.topic: article
ms.date: 05/31/2018
---

# IPsec Functions

The Windows Filtering Platform (WFP) functions that interact with Internet Protocol Security (IPsec) are as follows.

-   FwpmIPsecTunnelAdd:
    -   [**FwpmIPsecTunnelAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmipsectunneladd0) (Windows Vista)
    -   [**FwpmIPsecTunnelAdd1**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmipsectunneladd1) (Windows 7)
    -   [**FwpmIPsecTunnelAdd2**](/windows/desktop/api/fwpmu/nf-fwpmu-fwpmipsectunneladd2) (Windows 8)
-   [**FwpmIPsecTunnelDeleteByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmipsectunneldeletebykey0)
-   [**IPSEC\_KEY\_MANAGER\_KEY\_DICTATION\_CHECK0**](/windows/desktop/api/Fwpmu/nc-fwpmu-ipsec_key_manager_key_dictation_check0)
-   [**IPSEC\_KEY\_MANAGER\_DICTATE\_KEY0**](/windows/desktop/api/Fwpmu/nc-fwpmu-ipsec_key_manager_dictate_key0)
-   [**IPSEC\_KEY\_MANAGER\_NOTIFY\_KEY0**](/windows/desktop/api/fwpmu/nc-fwpmu-ipsec_key_manager_notify_key0)
-   [**IPSEC\_SA\_CONTEXT\_CALLBACK0**](/windows/win32/api/fwpmu/nc-fwpmu-ipsec_sa_context_callback0)
-   [**IPsecDospGetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecdospgetsecurityinfo0)
-   [**IPsecDospGetStatistics0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecdospgetstatistics0)
-   [**IPsecDospSetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecdospsetsecurityinfo0)
-   [**IPsecDospStateCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecdospstatecreateenumhandle0)
-   [**IPsecDospStateDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecdospstatedestroyenumhandle0)
-   [**IPsecDospStateEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecdospstateenum0)
-   IPsecGetStatistics:
    -   [**IPsecGetStatistics0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecgetstatistics0) (Windows Vista)
    -   [**IPsecGetStatistics1**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecgetstatistics1) (Windows 7 and later)
-   [**IPsecKeyManagerAddAndRegister0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanageraddandregister0)
-   [**IPsecKeyManagersGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanagersget0)
-   [**IPsecKeyManagerGetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanagergetsecurityinfobykey0)
-   [**IPsecKeyManagerSetSecurityInfoByKey0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanagersetsecurityinfobykey0)
-   [**IPsecKeyManagerUnregisterAndDelete0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipseckeymanagerunregisteranddelete0)
-   IPsecSaContextAddInbound:
    -   [**IPsecSaContextAddInbound0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddinbound0) (Windows Vista)
    -   [**IPsecSaContextAddInbound1**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddinbound1) (Windows 7 and later)
-   IPsecSaContextAddOutbound:
    -   [**IPsecSaContextAddOutbound0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddoutbound0) (Windows Vista)
    -   [**IPsecSaContextAddOutbound1**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddoutbound1) (Windows 7 and later)
-   IPsecSaContextCreate:
    -   [**IPsecSaContextCreate0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreate0) (Windows Vista)
    -   [**IPsecSaContextCreate1**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreate1) (Windows 7 and later)
-   [**IPsecSaContextCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreateenumhandle0)
-   [**IPsecSaContextDeleteById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextdeletebyid0)
-   [**IPsecSaContextDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextdestroyenumhandle0)
-   IPsecSaContextEnum:
    -   [**IPsecSaContextEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextenum0) (Windows Vista)
    -   [**IPsecSaContextEnum1**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextenum1) (Windows 7 and later)
-   [**IPsecSaContextExpire0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextexpire0)
-   IPsecSaContextGetById:
    -   [**IPsecSaContextGetById0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextgetbyid0) (Windows Vista)
    -   [**IPsecSaContextGetById1**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextgetbyid1) (Windows 7 and later)
-   IPsecSaContextGetSpi:
    -   [**IPsecSaContextGetSpi0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextgetspi0) (Windows Vista)
    -   [**IPsecSaContextGetSpi1**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextgetspi1) (Windows 7 and later)
-   [**IPsecSaContextSetSpi0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextsetspi0)
-   [**IPsecSaContextSubscribe0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextsubscribe0)
-   [**IPsecSaContextSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextsubscriptionsget0)
-   [**IPsecSaContextUpdate0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextupdate0)
-   [**IPsecSaContextUpdate0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextupdate0)
-   [**IPsecSaCreateEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacreateenumhandle0)
-   [**IPsecSaDbGetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsadbgetsecurityinfo0)
-   [**IPsecSaDbSetSecurityInfo0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsadbsetsecurityinfo0)
-   [**IPsecSaDestroyEnumHandle0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsadestroyenumhandle0)
-   IPsecSaEnum:
    -   [**IPsecSaEnum0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsaenum0) (Windows Vista)
    -   [**IPsecSaEnum1**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsaenum1) (Windows 7 and later)

 

 