---
title: MSISCSITARGET\_EndpointOfNetworkPipe class
description: Describes the endpoints between which a pipe transfers information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0cefe27b-5780-4e9a-a106-ced45c23572c
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_EndpointOfNetworkPipe class iSCSI Software Target API
- MSISCSITARGET_EndpointOfNetworkPipe class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_EndpointOfNetworkPipe
- MSISCSITARGET_EndpointOfNetworkPipe.Antecedent
- MSISCSITARGET_EndpointOfNetworkPipe.Dependent
- MSISCSITARGET_EndpointOfNetworkPipe.SourceOrSink
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_EndpointOfNetworkPipe class

Describes the endpoints between which a pipe transfers information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0"), MappingStrings("Recommendation.ITU|M3100.Pipe.a-TPInstance", "Recommendation.ITU|M3100.Pipe.z-TPInstance")]
class MSISCSITARGET_EndpointOfNetworkPipe : CIM_EndpointOfNetworkPipe
{
  CIM_ProtocolEndpoint REF Antecedent;
  CIM_NetworkPipe      REF Dependent;
  uint16                   SourceOrSink;
};
```

## Members

The **MSISCSITARGET\_EndpointOfNetworkPipe** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_EndpointOfNetworkPipe** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtocolEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (2), [**Max**](https://msdn.microsoft.com/library/aa393650) (2)
</dt> </dl>

One of the endpoints of the pipe.

This property is inherited from [**CIM\_EndpointOfNetworkPipe**](cim-endpointofnetworkpipe.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_NetworkPipe**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The pipe which is dependent on the endpoints as the source or sink of the transferred information.

This property is inherited from [**CIM\_EndpointOfNetworkPipe**](cim-endpointofnetworkpipe.md).

</dd> <dt>

**SourceOrSink**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the endpoint is a source (value = 2), or sink (value = 3) for the pipe. If this information is not applicable, the property is set to 4. If the information is not known, the property is set to 0.

This property is inherited from [**CIM\_EndpointOfNetworkPipe**](cim-endpointofnetworkpipe.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>

**Source** (2)


</dt> <dd></dd> <dt>

<span id="Sink"></span><span id="sink"></span><span id="SINK"></span>

**Sink** (3)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (4)


</dt> <dd></dd> </dl>

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

[**CIM\_EndpointOfNetworkPipe**](cim-endpointofnetworkpipe.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





