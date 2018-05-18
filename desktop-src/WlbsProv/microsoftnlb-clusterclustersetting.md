---
title: MicrosoftNLB\_ClusterClusterSetting class
description: The MicrosoftNLB\_ClusterClusterSetting association WMI class associates an instance of the MicrosoftNLB\_Cluster class to an instance of the MicrosoftNLB\_ClusterSetting class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1bc9fbc2-321e-411c-94dc-e53200267605'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MicrosoftNLB_ClusterClusterSetting class", "MicrosoftNLB_ClusterClusterSetting class, described"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_ClusterClusterSetting
- MicrosoftNLB_ClusterClusterSetting.Setting
- MicrosoftNLB_ClusterClusterSetting.Element
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# MicrosoftNLB\_ClusterClusterSetting class

The **MicrosoftNLB\_ClusterClusterSetting** association [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) associates an instance of the **MicrosoftNLB\_Cluster** class to an instance of the [**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md) class.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_ClusterClusterSetting : CIM_ElementSetting
{
  MicrosoftNLB_ClusterSetting REF Setting;
  MicrosoftNLB_Cluster        REF Element;
};
```

## Members

The **MicrosoftNLB\_ClusterClusterSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_ClusterClusterSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftNLB\_Cluster**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Element"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A **MicrosoftNLB\_Cluster** that represents a cluster.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftNLB\_ClusterSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Setting")
</dt> </dl>

A [**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md) that represents the cluster settings for a node.

</dd> </dl>

## Remarks

The **MicrosoftNLB\_ClusterClusterSetting** class is derived from the [**CIM\_ElementSetting**](https://msdn.microsoft.com/library/aa387263) class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementSetting**](cim-elementsetting.md)
</dt> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> </dl>

 

 





