---
title: iSCSI WMI Operations Class Structures
description: iSCSI WMI Operations Class Structures
ms.assetid: 94a02740-b2bc-405e-be24-b1754abb7f2d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# iSCSI WMI Operations Class Structures

## 

The iSCSI WMI structures that this section describes are used in communication between the iSCSI user-mode library and iSCSI initiators. The WMI tool suite generates declarations for these structures in the *Iscsiop.h* file when it compiles *Operations.mof*.

This section describes the following structures:

<dl>

[**AddConnectionToSession\_IN**](addconnectiontosession-in.md)  
[**AddConnectionToSession\_OUT**](addconnectiontosession-out.md)  
[**AddiSNSServer\_IN**](addisnsserver-in.md)  
[**AddiSNSServer\_OUT**](addisnsserver-out.md)  
[**AddRADIUSServer\_IN**](addradiusserver-in.md)  
[**AddRADIUSServer\_OUT**](addradiusserver-out.md)  
[**ClearCache\_OUT**](clearcache-out.md)  
[**DeleteInitiatorNodeName\_IN**](deleteinitiatornodename-in.md)  
[**DeleteInitiatorNodeName\_OUT**](deleteinitiatornodename-out.md)  
[**GetPresharedKeyForId\_IN**](getpresharedkeyforid-in.md)  
[**GetPresharedKeyForId\_OUT**](getpresharedkeyforid-out.md)  
[**ISCSI\_ADAPTER\_EVENT\_CODE**](iscsi-adapter-event-code.md)  
[**ISCSI\_Persistent\_Login**](iscsi-persistent-login.md)  
[**LOGINSESSIONTYPE**](loginsessiontype.md)  
[**LoginToTarget\_IN**](logintotarget-in.md)  
[**LoginToTarget\_OUT**](logintotarget-out.md)  
[**LogoutFromTarget\_IN**](logoutfromtarget-in.md)  
[**LogoutFromTarget\_OUT**](logoutfromtarget-out.md)  
[**MSiSCSI\_AdapterEvent**](msiscsi-adapterevent.md)  
[**MSiSCSI\_BootInformation**](msiscsi-bootinformation.md)  
[**MSiSCSI\_LUNMappingInformation**](msiscsi-lunmappinginformation.md)  
[**MSiSCSI\_PersistentLogins**](msiscsi-persistentlogins.md)  
[**MSiSCSI\_TargetMappings**](msiscsi-targetmappings.md)  
[**RemoveConnectionFromSession\_IN**](removeconnectionfromsession-in.md)  
[**RemoveConnectionFromSession\_OUT**](removeconnectionfromsession-out.md)  
[**RemoveiSNSServer\_IN**](removeisnsserver-in.md)  
[**RemoveiSNSServer\_OUT**](removeisnsserver-out.md)  
[**RemovePersistentLogin\_IN**](removepersistentlogin-in.md)  
[**RemovePersistentLogin\_OUT**](removepersistentlogin-out.md)  
[**RemoveRADIUSServer\_IN**](removeradiusserver-in.md)  
[**RemoveRADIUSServer\_OUT**](removeradiusserver-out.md)  
[**ScsiInquiry\_IN**](scsiinquiry-in2.md)  
[**ScsiInquiry\_OUT**](scsiinquiry-out2.md)  
[**ScsiReadCapacity\_IN**](scsireadcapacity-in2.md)  
[**ScsiReadCapacity\_OUT**](scsireadcapacity-out2.md)  
[**ScsiReportLuns\_IN**](scsireportluns-in2.md)  
[**ScsiReportLuns\_OUT**](scsireportluns-out2.md)  
[**SendTargets\_IN**](sendtargets-in.md)  
[**SendTargets\_OUT**](sendtargets-out.md)  
[**SetCHAPSharedSecret\_IN**](setchapsharedsecret-in.md)  
[**SetCHAPSharedSecret\_OUT**](setchapsharedsecret-out.md)  
[**SetGenerationalGuid\_IN**](setgenerationalguid-in.md)  
[**SetGenerationalGuid\_OUT**](setgenerationalguid-out.md)  
[**SetGroupPresharedKey\_IN**](setgrouppresharedkey-in.md)  
[**SetGroupPresharedKey\_OUT**](setgrouppresharedkey-out.md)  
[**SetInitiatorNodeName\_IN**](setinitiatornodename-in.md)  
[**SetInitiatorNodeName\_OUT**](setinitiatornodename-out.md)  
[**SetPresharedKeyForId\_IN**](setpresharedkeyforid-in.md)  
[**SetPresharedKeyForId\_OUT**](setpresharedkeyforid-out.md)  
[**SetRADIUSSharedSecret\_IN**](setradiussharedsecret-in.md)  
[**SetRADIUSSharedSecret\_OUT**](setradiussharedsecret-out.md)  
[**SetTunnelModeOuterAddress\_IN**](settunnelmodeouteraddress-in.md)  
[**SetTunnelModeOuterAddress\_OUT**](settunnelmodeouteraddress-out.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20iSCSI%20WMI%20Operations%20Class%20Structures%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




