---
title: MSISCSITARGET\_NetworkPipeComposition class
description: Describes the makeup of a pipe that is based on aggregating lower-level pipes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e808af97-e61d-4801-8440-e7c4bfe0bf1e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_NetworkPipeComposition class iSCSI Software Target API", "MSISCSITARGET_NetworkPipeComposition class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_NetworkPipeComposition
- MSISCSITARGET_NetworkPipeComposition.GroupComponent
- MSISCSITARGET_NetworkPipeComposition.PartComponent
- MSISCSITARGET_NetworkPipeComposition.AggregationSequence
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_NetworkPipeComposition class

Describes the makeup of a pipe that is based on aggregating lower-level pipes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Aggregation, Composition, Version("1.0.0"), MappingStrings("Recommendation.ITU|M3100.TrailR1.serverConnectionListPackage", "Recommendation.ITU|M3100.TrailR1.clientConnectionListPackage")]
class MSISCSITARGET_NetworkPipeComposition : CIM_NetworkPipeComposition
{
  CIM_NetworkPipe REF GroupComponent;
  CIM_NetworkPipe REF PartComponent;
  uint16              AggregationSequence;
};
```

## Members

The **MSISCSITARGET\_NetworkPipeComposition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_NetworkPipeComposition** class has these properties.

<dl> <dt>

**AggregationSequence**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the ordering of the PartComponent pipes in the GroupComponent. If the AggregationBehavior property of the GroupComponent pipe is set to 0 or 3 ("Unknown" or "Combined In Parallel"), then this property MUST be set to 0. If the AggregationBehavior is set to 4 ("Combined In Sequence"), then this property SHOULD indicate the ordering of the component pipes. Ordering starts with 1 and larger numbers indicate subsequent pipes. The numbering does not have to be in sequence. The word SHOULD is used in this Description, since the specific ordering of all the component pipes may not be known. In these cases, a value of 0 would be placed in AggregationSequence to indicate that ordering information is not available.

This property is inherited from [**CIM\_NetworkPipeComposition**](cim-networkpipecomposition.md).

</dd> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_NetworkPipe**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The higher level pipe that is composed of lower-level parts/pipes.

This property is inherited from [**CIM\_NetworkPipeComposition**](cim-networkpipecomposition.md).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_NetworkPipe**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A pipe which is a part of a higher-level one.

This property is inherited from [**CIM\_NetworkPipeComposition**](cim-networkpipecomposition.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_NetworkPipeComposition**](cim-networkpipecomposition.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





