---
Description: This MSIscsiInitiator\_MethodClass structure contains all miscellaneous operation methods associated with the iSCSI Initiator.
ms.assetid: 2f5637fd-fc64-4887-8774-949e65620e59
title: MSIscsiInitiator\_MethodClass class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSIscsiInitiator\_MethodClass class

This **MSIscsiInitiator\_MethodClass** structure contains all miscellaneous operation methods associated with the iSCSI Initiator.

## Syntax

``` syntax
class MSIscsiInitiator_MethodClass
{
  string IscsiNodeName;
};
```

## Members

The **MSIscsiInitiator\_MethodClass** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSIscsiInitiator\_MethodClass** class has these methods.



| Method                                                                                                          | Description                                                                            |
|:----------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**ClearPersistentIscsiVolumes**](clearpersistentiscsivolumes-msiscsiinitiator-methodclass.md)                 | Clears Persistent iSCSI Volumes.<br/>                                            |
| [**RefreshTargetList**](refreshtargetlist-msiscsiinitiator-methodclass.md)                                     | Refreshes the entire list of targets using all available discovery methods.<br/> |
| [**SetIscsiGroupPresharedKey**](setiscsigrouppresharedkey-msiscsiinitiator-methodclass.md)                     | Sets the iSCSI Group Preshared Key.<br/>                                         |
| [**SetIscsiIKEInfo**](setiscsiikeinfo-msiscsiinitiator-methodclass.md)                                         | Sets the iSCSI IKE Information.<br/>                                             |
| [**SetIscsiInitiatorCHAPSharedSecret**](setiscsiinitiatorchapsharedsecret-msiscsiinitiator-methodclass.md)     | Sets the iSCSI CHAP Shared Secret.<br/>                                          |
| [**SetIscsiInitiatorNodeName**](setiscsiinitiatornodename-msiscsiinitiator-methodclass.md)                     | Sets the iSCSI Initiator Node Name.<br/>                                         |
| [**SetIscsiInitiatorRADIUSSharedSecret**](setiscsiinitiatorradiussharedsecret-msiscsiinitiator-methodclass.md) | Sets the iSCSI RADIUS Shared Secret.<br/>                                        |
| [**SetIscsiTunnelModeOuterAddress**](setiscsitunnelmodeouteraddress-msiscsiinitiator-methodclass.md)           | Sets the iSCSI Tunnel Mode Outer Address.<br/>                                   |
| [**SetupPersistentIscsiVolumes**](setuppersistentiscsivolumes-msiscsiinitiator-methodclass.md)                 | Sets associated iSCSI volumes to be persistent.<br/>                             |



 

### Properties

The **MSIscsiInitiator\_MethodClass** class has these properties.

<dl> <dt>

**IscsiNodeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The node name of the iSCSI Initiator.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 




