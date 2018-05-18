---
title: MSFTSM\_NamespaceInManager class
description: Associates CIM\_Namespace instances with the MSFTSM\_ObjectManager instance that hosts them.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ee2928db-64ab-43ef-bcc1-454da88cad89'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFTSM_NamespaceInManager class iSCSI Software Target API", "MSFTSM_NamespaceInManager class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSFTSM_NamespaceInManager
- MSFTSM_NamespaceInManager.Antecedent
- MSFTSM_NamespaceInManager.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSFTSM\_NamespaceInManager class

Associates **CIM\_Namespace** instances with the [**MSFTSM\_ObjectManager**](msftsm-objectmanager.md) instance that hosts them. This association is a one-to-many association.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), Provider("MSiSCSITargetProv")]
class MSFTSM_NamespaceInManager : CIM_NamespaceInManager
{
  CIM_ObjectManager REF Antecedent;
  CIM_Namespace     REF Dependent;
};
```

## Members

The **MSFTSM\_NamespaceInManager** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSM\_NamespaceInManager** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ObjectManager**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The ObjectManager containing a Namespace.

This property is inherited from [**CIM\_NamespaceInManager**](cim-namespaceinmanager.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Namespace**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The Namespace in an ObjectManager.

This property is inherited from [**CIM\_NamespaceInManager**](cim-namespaceinmanager.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>Smiscsitarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_NamespaceInManager**](cim-namespaceinmanager.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





