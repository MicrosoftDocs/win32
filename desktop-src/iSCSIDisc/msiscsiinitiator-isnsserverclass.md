---
Description: This MSIscsiInitiator\_IsnsServerClass class retrieves and contains information about the iSNS server, which is used to discover targets on a network.
ms.assetid: d22afb5d-0c48-48b9-97d9-ee2871c9c4e0
title: MSIscsiInitiator\_IsnsServerClass class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSIscsiInitiator\_IsnsServerClass class

This **MSIscsiInitiator\_IsnsServerClass** class retrieves and contains information about the iSNS server, which is used to discover targets on a network.

## Syntax

``` syntax
class MSIscsiInitiator_IsnsServerClass
{
  string IsnsServerAddress;
};
```

## Members

The **MSIscsiInitiator\_IsnsServerClass** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSIscsiInitiator\_IsnsServerClass** class has these methods.



| Method                                                      | Description                                                                      |
|:------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**Refresh**](refresh-msiscsiinitiator-isnsserverclass.md) | Refreshes the list of discovered targets supplied by the iSNS server.<br/> |



 

### Properties

The **MSIscsiInitiator\_IsnsServerClass** class has these properties.

<dl> <dt>

**IsnsServerAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The iSNS server address.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 




