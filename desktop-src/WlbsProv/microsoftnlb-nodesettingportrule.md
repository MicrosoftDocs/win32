---
title: MicrosoftNLB\_NodeSettingPortRule class
description: The MicrosoftNLB\_NodeSettingPortRule association WMI class associates an instance of the MicrosoftNLB\_NodeSetting class to an instance of the MicrosoftNLB\_PortRule class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f0731912-4947-4023-b728-bf7b160e512e
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_NodeSettingPortRule class
- MicrosoftNLB_NodeSettingPortRule class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_NodeSettingPortRule
- MicrosoftNLB_NodeSettingPortRule.PartComponent
- MicrosoftNLB_NodeSettingPortRule.GroupComponent
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MicrosoftNLB\_NodeSettingPortRule class

The **MicrosoftNLB\_NodeSettingPortRule** association [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) associates an instance of the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class to an instance of the [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md) class.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_NodeSettingPortRule : CIM_Component
{
  MicrosoftNLB_PortRule    REF PartComponent;
  MicrosoftNLB_NodeSetting REF GroupComponent;
};
```

## Members

The **MicrosoftNLB\_NodeSettingPortRule** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_NodeSettingPortRule** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftNLB\_NodeSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftNLB\_PortRule**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md) that represents the settings for the node.

</dd> </dl>

## Remarks

[**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md) does not contain a virtual IP address property. Because port rules have a virtual IP address property, this may produce unexpected results. [**MicrosoftNLB\_PortRuleEx**](microsoftnlb-portruleex.md) has a **VIP** property, so it is better to use this class.

There is not an association class that associates an instance of the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class to an instance of the [**MicrosoftNLB\_PortRuleEx**](https://msdn.microsoft.com/library/aa371416) class. Use the common properties of these two classes (**Name** and **AdapterGuid**) to associate instances of the **MicrosoftNLB\_NodeSetting** class and the **MicrosoftNLB\_PortRuleEx** class.

The **MicrosoftNLB\_NodeSettingPortRule** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





