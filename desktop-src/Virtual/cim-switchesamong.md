---
title: CIM\_SwitchesAmong class
description: Represents a switch service, which switches frames between switch ports.
ms.assetid: 3eb402f2-26e8-4fc5-a116-d3a83455cf75
keywords:
- CIM_SwitchesAmong class Hyper-V
- CIM_SwitchesAmong class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_SwitchesAmong
- CIM_SwitchesAmong.Antecedent
- CIM_SwitchesAmong.Dependent
api_location:
- Root\virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_SwitchesAmong class

Represents a switch service, which switches frames between switch ports.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.6.0")]
class CIM_SwitchesAmong : CIM_ForwardsAmong
{
  CIM_SwitchPort    REF Antecedent;
  CIM_SwitchService REF Dependent;
};
```

## Members

The **CIM\_SwitchesAmong** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SwitchesAmong** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SwitchPort**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A reference to the switch port.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SwitchService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the switching service.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ForwardsAmong**](cim-forwardsamong.md)
</dt> </dl>

 

 





