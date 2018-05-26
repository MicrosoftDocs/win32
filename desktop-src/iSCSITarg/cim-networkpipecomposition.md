---
title: CIM\_NetworkPipeComposition class
description: NetworkPipeComposition describes the makeup a pipe, based on lower-level ones.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 49460037-676a-4de3-b741-947a89b7db20
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_NetworkPipeComposition class iSCSI Software Target API
- CIM_NetworkPipeComposition class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_NetworkPipeComposition
- CIM_NetworkPipeComposition.GroupComponent
- CIM_NetworkPipeComposition.PartComponent
- CIM_NetworkPipeComposition.AggregationSequence
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_NetworkPipeComposition class

NetworkPipeComposition describes the makeup a pipe, based on lower-level ones. If the pipe is not composed of lower-level entities (i.e., its AggregationBehavior property is set to 2), then no instances of this association should be defined where the pipe has the role of GroupComponent.

In the context of M.3100, this semantic is modeled as a Trail that is made up of one or more Connections. Both Trails and Connections are subclasses of M.3100's Pipe. Because of the flexibility of the NetworkPipeComposition association, there is no need to subclass NetworkPipe, as was done in M.3100, but merely to instantiate this association to describe the bundling of the lower-level pipes (connections), or the sequencing of them. How the lower-level pipes are aggregated is described by the property, AggregationBehavior, of NetworkPipe. If the pipes are combined in a sequence, the ordering is conveyed via the property, AggregationSequence, on this association.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Aggregation, Composition, Version("2.7.0"), UMLPackagePath("CIM::Network::Pipes"), MappingStrings("Recommendation.ITU|M3100.TrailR1.serverConnectionListPackage", "Recommendation.ITU|M3100.TrailR1.clientConnectionListPackage")]
class CIM_NetworkPipeComposition : CIM_Component
{
  CIM_NetworkPipe REF GroupComponent;
  CIM_NetworkPipe REF PartComponent;
  uint16              AggregationSequence;
};
```

## Members

The **CIM\_NetworkPipeComposition** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_NetworkPipeComposition** class has these properties.

<dl> <dt>

**AggregationSequence**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the ordering of the PartComponent pipes in the GroupComponent. If the AggregationBehavior property of the GroupComponent pipe is set to 0 or 3 ("Unknown" or "Combined In Parallel"), then this property MUST be set to 0. If the AggregationBehavior is set to 4 ("Combined In Sequence"), then this property SHOULD indicate the ordering of the component pipes. Ordering starts with 1 and larger numbers indicate subsequent pipes. The numbering does not have to be in sequence. The word SHOULD is used in this Description, since the specific ordering of all the component pipes may not be known. In these cases, a value of 0 would be placed in AggregationSequence to indicate that ordering information is not available.

</dd> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_NetworkPipe**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent")
</dt> </dl>

The higher level pipe that is composed of lower-level parts/pipes.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_NetworkPipe**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

A pipe which is a part of a higher-level one.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> </dl>

 

 





