---
title: Msvm\_VideoHeadOnController class
description: Associates a video head with the video controller that includes it.
ms.assetid: 6f295d02-66e7-486f-9cb4-c82cbd4e5a2c
keywords:
- Msvm_VideoHeadOnController class Hyper-V
- Msvm_VideoHeadOnController class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VideoHeadOnController
- Msvm_VideoHeadOnController.Antecedent
- Msvm_VideoHeadOnController.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_VideoHeadOnController class

Associates a video head with the video controller that includes it.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VideoHeadOnController : CIM_VideoHeadOnController
{
  CIM_DisplayController REF Antecedent;
  Msvm_VideoHead        REF Dependent;
};
```

## Members

The **Msvm\_VideoHeadOnController** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VideoHeadOnController** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_DisplayController**](https://msdn.microsoft.com/library/cc136810)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The video controller that includes the head.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VideoHead**](msvm-videohead.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The head on the video device.

</dd> </dl>

## Remarks

Access to the **Msvm\_VideoHeadOnController** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_VideoHeadOnController**](cim-videoheadoncontroller.md)
</dt> <dt>

[**CIM\_VideoHeadOnController**](https://msdn.microsoft.com/library/cc136950)
</dt> <dt>

[Video Classes](video-classes.md)
</dt> </dl>

 

 





