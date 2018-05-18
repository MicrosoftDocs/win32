---
title: CIM\_TransparentBridgingDynamicForwarding class
description: Associates a transparent bridging service with an entry of its forwarding database.
ms.assetid: 'c1bb7506-ecab-4bd9-bd5f-45037ebd0b01'
keywords: ["CIM_TransparentBridgingDynamicForwarding class Hyper-V", "CIM_TransparentBridgingDynamicForwarding class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_TransparentBridgingDynamicForwarding
- CIM_TransparentBridgingDynamicForwarding.Antecedent
- CIM_TransparentBridgingDynamicForwarding.Dependent
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_TransparentBridgingDynamicForwarding class

Associates a transparent bridging service with an entry of its forwarding database.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.6.0"), AMENDMENT]
class CIM_TransparentBridgingDynamicForwarding : CIM_Dependency
{
  CIM_TransparentBridgingService REF Antecedent;
  CIM_DynamicForwardingEntry     REF Dependent;
};
```

## Members

The **CIM\_TransparentBridgingDynamicForwarding** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_TransparentBridgingDynamicForwarding** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_TransparentBridgingService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the transparent bridging service.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_DynamicForwardingEntry**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A reference to the forwarding database entry.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





