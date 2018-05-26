---
title: IPsec Functions
description: IPsec Functions
ms.assetid: db656c58-7776-44c4-a7ce-c38e59b37c74
keywords:
- Windows Filtering Platform API IPsec Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPsec Functions

The Windows Filtering Platform (WFP) functions that interact with Internet Protocol Security (IPsec) are as follows.

-   FwpmIPsecTunnelAdd:
    -   [**FwpmIPsecTunnelAdd0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmipsectunneladd0?branch=master) (Windows Vista)
    -   [**FwpmIPsecTunnelAdd1**](/windows/win32/Fwpmu/nf-fwpmu-fwpmipsectunneladd1?branch=master) (Windows 7)
    -   [**FwpmIPsecTunnelAdd2**](/windows/win32/fwpmu/nf-fwpmu-fwpmipsectunneladd2?branch=master) (Windows 8)
-   [**FwpmIPsecTunnelDeleteByKey0**](/windows/win32/Fwpmu/nf-fwpmu-fwpmipsectunneldeletebykey0?branch=master)
-   [**IPSEC\_KEY\_MANAGER\_KEY\_DICTATION\_CHECK0**](/windows/win32/Fwpmu/nc-fwpmu-ipsec_key_manager_key_dictation_check0?branch=master)
-   [**IPSEC\_KEY\_MANAGER\_DICTATE\_KEY0**](/windows/win32/Fwpmu/nc-fwpmu-ipsec_key_manager_dictate_key0?branch=master)
-   [**IPSEC\_KEY\_MANAGER\_NOTIFY\_KEY0**](/windows/win32/fwpmu/nc-fwpmu-ipsec_key_manager_notify_key0?branch=master)
-   [**IPSEC\_SA\_CONTEXT\_CALLBACK0**](/windows/win32/fwpmu/nc-fwpmu-ipsec_sa_context_callback0?branch=master)
-   [**IPsecDospGetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecdospgetsecurityinfo0?branch=master)
-   [**IPsecDospGetStatistics0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecdospgetstatistics0?branch=master)
-   [**IPsecDospSetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecdospsetsecurityinfo0?branch=master)
-   [**IPsecDospStateCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecdospstatecreateenumhandle0?branch=master)
-   [**IPsecDospStateDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecdospstatedestroyenumhandle0?branch=master)
-   [**IPsecDospStateEnum0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecdospstateenum0?branch=master)
-   IPsecGetStatistics:
    -   [**IPsecGetStatistics0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecgetstatistics0?branch=master) (Windows Vista)
    -   [**IPsecGetStatistics1**](/windows/win32/Fwpmu/nf-fwpmu-ipsecgetstatistics1?branch=master) (Windows 7 and later)
-   [**IPsecKeyManagerAddAndRegister0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanageraddandregister0?branch=master)
-   [**IPsecKeyManagersGet0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanagersget0?branch=master)
-   [**IPsecKeyManagerGetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanagergetsecurityinfobykey0?branch=master)
-   [**IPsecKeyManagerSetSecurityInfoByKey0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanagersetsecurityinfobykey0?branch=master)
-   [**IPsecKeyManagerUnregisterAndDelete0**](/windows/win32/Fwpmu/nf-fwpmu-ipseckeymanagerunregisteranddelete0?branch=master)
-   IPsecSaContextAddInbound:
    -   [**IPsecSaContextAddInbound0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextaddinbound0?branch=master) (Windows Vista)
    -   [**IPsecSaContextAddInbound1**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextaddinbound1?branch=master) (Windows 7 and later)
-   IPsecSaContextAddOutbound:
    -   [**IPsecSaContextAddOutbound0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextaddoutbound0?branch=master) (Windows Vista)
    -   [**IPsecSaContextAddOutbound1**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextaddoutbound1?branch=master) (Windows 7 and later)
-   IPsecSaContextCreate:
    -   [**IPsecSaContextCreate0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextcreate0?branch=master) (Windows Vista)
    -   [**IPsecSaContextCreate1**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextcreate1?branch=master) (Windows 7 and later)
-   [**IPsecSaContextCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextcreateenumhandle0?branch=master)
-   [**IPsecSaContextDeleteById0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextdeletebyid0?branch=master)
-   [**IPsecSaContextDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextdestroyenumhandle0?branch=master)
-   IPsecSaContextEnum:
    -   [**IPsecSaContextEnum0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextenum0?branch=master) (Windows Vista)
    -   [**IPsecSaContextEnum1**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextenum1?branch=master) (Windows 7 and later)
-   [**IPsecSaContextExpire0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextexpire0?branch=master)
-   IPsecSaContextGetById:
    -   [**IPsecSaContextGetById0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextgetbyid0?branch=master) (Windows Vista)
    -   [**IPsecSaContextGetById1**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextgetbyid1?branch=master) (Windows 7 and later)
-   IPsecSaContextGetSpi:
    -   [**IPsecSaContextGetSpi0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextgetspi0?branch=master) (Windows Vista)
    -   [**IPsecSaContextGetSpi1**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextgetspi1?branch=master) (Windows 7 and later)
-   [**IPsecSaContextSetSpi0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextsetspi0?branch=master)
-   [**IPsecSaContextSubscribe0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextsubscribe0?branch=master)
-   [**IPsecSaContextSubscriptionsGet0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextsubscriptionsget0?branch=master)
-   [**IPsecSaContextUpdate0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextupdate0?branch=master)
-   [**IPsecSaContextUpdate0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacontextupdate0?branch=master)
-   [**IPsecSaCreateEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsacreateenumhandle0?branch=master)
-   [**IPsecSaDbGetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsadbgetsecurityinfo0?branch=master)
-   [**IPsecSaDbSetSecurityInfo0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsadbsetsecurityinfo0?branch=master)
-   [**IPsecSaDestroyEnumHandle0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsadestroyenumhandle0?branch=master)
-   IPsecSaEnum:
    -   [**IPsecSaEnum0**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsaenum0?branch=master) (Windows Vista)
    -   [**IPsecSaEnum1**](/windows/win32/Fwpmu/nf-fwpmu-ipsecsaenum1?branch=master) (Windows 7 and later)

 

 




