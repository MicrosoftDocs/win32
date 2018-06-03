---
title: MicrosoftNLB\_NodeNodeSetting class
description: The MicrosoftNLB\_NodeNodeSetting association WMI class associates an instance of the MicrosoftNLB\_Node class to an instance of the MicrosoftNLB\_NodeSetting class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d6b7ba6-d690-49c4-b512-203111a4e16c
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_NodeNodeSetting class
- MicrosoftNLB_NodeNodeSetting class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_NodeNodeSetting
- MicrosoftNLB_NodeNodeSetting.Setting
- MicrosoftNLB_NodeNodeSetting.Element
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MicrosoftNLB\_NodeNodeSetting class

The **MicrosoftNLB\_NodeNodeSetting** association [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) associates an instance of the [**MicrosoftNLB\_Node**](microsoftnlb-node.md) class to an instance of the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_NodeNodeSetting : CIM_ElementSetting
{
  MicrosoftNLB_NodeSetting REF Setting;
  MicrosoftNLB_Node        REF Element;
};
```

## Members

The **MicrosoftNLB\_NodeNodeSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_NodeNodeSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftNLB\_Node**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Element"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A [**MicrosoftNLB\_Node**](microsoftnlb-node.md) that describes a node in the cluster.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftNLB\_NodeSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Setting")
</dt> </dl>

A [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) that containthe settings for a node.

</dd> </dl>

## Remarks

The **MicrosoftNLB\_NodeNodeSetting** class is derived from the **CIM\_ElementSetting** class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementSetting**](cim-elementsetting.md)
</dt> <dt>

[**MicrosoftNLB\_Node**](microsoftnlb-node.md)
</dt> <dt>

[**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md)
</dt> </dl>

 

 





