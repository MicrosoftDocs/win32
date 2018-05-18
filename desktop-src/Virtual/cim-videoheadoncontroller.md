---
title: CIM\_VideoHeadOnController class
description: Associates a video head with the video adapter that contains it.
ms.assetid: '10546e11-9591-4c63-8248-cc664d3dfcc4'
keywords: ["CIM_VideoHeadOnController class Hyper-V", "CIM_VideoHeadOnController class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_VideoHeadOnController
- CIM_VideoHeadOnController.Antecedent
- CIM_VideoHeadOnController.Dependent
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_VideoHeadOnController class

Associates a video head with the video adapter that contains it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Experimental, Version("2.10.0"), AMENDMENT]
class CIM_VideoHeadOnController : CIM_HostedDependency
{
  CIM_DisplayController REF Antecedent;
  CIM_VideoHead         REF Dependent;
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

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The video adapter that includes the head.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VideoHead**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The head on the video adapter.

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

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> </dl>

 

 





