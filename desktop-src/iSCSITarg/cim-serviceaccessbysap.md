---
title: CIM\_ServiceAccessBySAP class
description: CIM\_ServiceAccessBySAP is an association that identifies the access points for a Service. For example, a printer might be accessed by NetWare, MacIntosh or Windows ServiceAccessPoints, which might all be hosted on different Systems.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '17cd6641-11bc-4663-8067-49d29a287307'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_ServiceAccessBySAP class iSCSI Software Target API", "CIM_ServiceAccessBySAP class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_ServiceAccessBySAP
- CIM_ServiceAccessBySAP.Antecedent
- CIM_ServiceAccessBySAP.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_ServiceAccessBySAP class

CIM\_ServiceAccessBySAP is an association that identifies the access points for a Service. For example, a printer might be accessed by NetWare, MacIntosh or Windows ServiceAccessPoints, which might all be hosted on different Systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Service")]
class CIM_ServiceAccessBySAP : CIM_Dependency
{
  CIM_Service            REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **CIM\_ServiceAccessBySAP** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ServiceAccessBySAP** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The Service.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

An Access Point for a Service. Access points are dependent in this relationship because they have no function without a corresponding Service.

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

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





