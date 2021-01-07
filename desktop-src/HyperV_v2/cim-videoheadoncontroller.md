---
description: Associates a video head with the video adapter that contains it.
ms.assetid: d15f4350-1529-4246-9ea2-8453e52516c6
title: CIM_VideoHeadOnController class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VideoHeadOnController
- CIM_VideoHeadOnController.Antecedent
- CIM_VideoHeadOnController.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_VideoHeadOnController class

Associates a video head with the video adapter that contains it.

## Syntax

``` syntax
[Association, Experimental, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Device::Controller"), AMENDMENT]
class CIM_VideoHeadOnController : CIM_HostedDependency
{
  CIM_DisplayController REF Antecedent;
  CIM_VideoHead         REF Dependent;
};
```

## Members

The **CIM\_VideoHeadOnController** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VideoHeadOnController** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_DisplayController**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

The video adapter that includes the head.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VideoHead**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

The head on the video adapter.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> </dl>

 

