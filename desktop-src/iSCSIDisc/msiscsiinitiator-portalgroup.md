---
Description: This MSIscsiInitiator\_PortalGroup structure describes the characteristics of the Initiator portal group.
ms.assetid: 52a61a1c-51a3-4826-9f4c-a284b154f4d8
title: MSIscsiInitiator\_PortalGroup class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSIscsiInitiator\_PortalGroup class

This **MSIscsiInitiator\_PortalGroup** structure describes the characteristics of the Initiator portal group.

## Syntax

``` syntax
class MSIscsiInitiator_PortalGroup
{
  uint32                  Index;
  MSIscsiInitiator_Portal Portals[];
};
```

## Members

The **MSIscsiInitiator\_PortalGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_PortalGroup** class has these properties.

<dl> <dt>

**Index**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The index number associated with the portal group.

</dd> <dt>

**Portals**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_Portal** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of [**MSiSCSIInitiator\_Portal**](msiscsiinitiator-portal.md) structures representing portals within the portal group.

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

[**MSIscsiInitiator\_Portal**](msiscsiinitiator-portal.md)
</dt> </dl>

 

 




