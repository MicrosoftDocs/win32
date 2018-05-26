---
Description: This MSIscsiInitiator\_TargetClass provides information about connected iSCSI targets as well the ability to login to a specified target.
ms.assetid: e86bb4d8-fcf1-480a-b267-33ff4d55f03a
title: MSIscsiInitiator\_TargetClass class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSIscsiInitiator\_TargetClass class

This **MSIscsiInitiator\_TargetClass** provides information about connected iSCSI targets as well the ability to login to a specified target.

## Syntax

``` syntax
class MSIscsiInitiator_TargetClass
{
  string                              TargetName;
  string                              DiscoveryMechanism;
  string                              InitiatorName;
  uint32                              ProtocolType;
  string                              TargetAlias;
  MSIscsiInitiator_PortalGroup        PortalGroups[];
  MSIscsiInitiator_TargetMappings     Mappings;
  uint32                              TargetFlags;
  MSIscsiInitiator_TargetLoginOptions LoginOptions;
};
```

## Members

The **MSIscsiInitiator\_TargetClass** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSIscsiInitiator\_TargetClass** class has these methods.



| Method                                              | Description                     |
|:----------------------------------------------------|:--------------------------------|
| [**Login**](login-msiscsiinitiator-targetclass.md) | Login to the target.<br/> |



 

### Properties

The **MSIscsiInitiator\_TargetClass** class has these properties.

<dl> <dt>

**DiscoveryMechanism**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the available discovery mechanism for the target.

</dd> <dt>

**InitiatorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the name of the iSCSI initiator the target is connected to.

</dd> <dt>

**LoginOptions**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_TargetLoginOptions**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of [**MSIscsiInitiator\_TargetLoginOptions**](msiscsiinitiator-targetloginoptions.md) structures which contain information about target login options.

</dd> <dt>

**Mappings**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_TargetMappings**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of [**MSIscsiInitiator\_TargetMappings**](msiscsiinitiator-targetmappings.md) structures which contain information about LUN mapping.

</dd> <dt>

**PortalGroups**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_PortalGroup** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of [**MSIscsiInitiator\_PortalGroup**](msiscsiinitiator-portalgroup.md) structures containing information about an initiator portal group.

</dd> <dt>

**ProtocolType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the potocol used to establish the connection between the target and initiator.

</dd> <dt>

**TargetAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name or description that is assigned to the target device by its host operating system. You can use this name in user interfaces, but it is not unique, you should not use it in authentication decisions.

</dd> <dt>

**TargetFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A bitmap of flags that affect how, and under what circumstances, a target is discovered and enumerated.



| Flag                                            | Meaning                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ISCSI\_TARGET\_FLAG\_HIDE\_STATIC\_TARGET       | The target is added to the list of static targets. However, ReportIscsiTargets does not report the target, unless it was also discovered dynamically by the iSCSI initiator, the Internet Storage Name Service (iSNS), or a SendTargets request. <br/>                                                                              |
| ISCSI\_TARGET\_FLAG\_MERGE\_TARGET\_INFORMATION | The iSCSI initiator service merges the information (if any) that it already has for this static target with the information that the caller passes to AddIscsiStaticTarget. <br/> If this flag is not set, the iSCSI initiator service overwrites the stored information with the information that the caller passes in.<br/> |



 

</dd> <dt>

**TargetName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name assigned to the iSCSI target.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSIscsiInitiator\_PortalGroup**](msiscsiinitiator-portalgroup.md)
</dt> <dt>

[**MSIscsiInitiator\_TargetMappings**](msiscsiinitiator-targetmappings.md)
</dt> <dt>

[**MSIscsiInitiator\_TargetLoginOptions**](msiscsiinitiator-targetloginoptions.md)
</dt> </dl>

 

 




