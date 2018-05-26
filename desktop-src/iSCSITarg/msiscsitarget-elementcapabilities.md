---
title: MSISCSITARGET\_ElementCapabilities class
description: Represents the association between a managed element and the CIM\_Capabilities instances that describe it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8bf9df3c-350c-45b2-8948-b71e9498cb73
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_ElementCapabilities class iSCSI Software Target API
- MSISCSITARGET_ElementCapabilities class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_ElementCapabilities
- MSISCSITARGET_ElementCapabilities.ManagedElement
- MSISCSITARGET_ElementCapabilities.Capabilities
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_ElementCapabilities class

Represents the association between a managed element and the [**CIM\_Capabilities**](cim-capabilities.md) instances that describe it. This association defines a one-to-many relationship between [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and [**CIM\_Capabilities**](https://msdn.microsoft.com/library/cc136806) instances, therefor the **CIM\_ManagedElement** must exist .

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_ElementCapabilities : CIM_ElementCapabilities
{
  CIM_ManagedElement REF ManagedElement;
  CIM_Capabilities   REF Capabilities;
};
```

## Members

The **MSISCSITARGET\_ElementCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_ElementCapabilities** class has these properties.

<dl> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Capabilities**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**CIM\_Capabilities**](cim-capabilities.md) containing the Capabilities object associated with the element.

This property is inherited from [**CIM\_ElementCapabilities**](cim-elementcapabilities.md).

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A [**CIM\_ManagedElement**](cim-managedelement.md) containing the managed element.

This property is inherited from [**CIM\_ElementCapabilities**](cim-elementcapabilities.md).

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

[**CIM\_ElementCapabilities**](cim-elementcapabilities.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**CIM\_Capabilities**](https://msdn.microsoft.com/library/cc136806)
</dt> <dt>

[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871)
</dt> </dl>

 

 





