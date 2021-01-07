---
description: CIM\_ProcessIndication is an abstract superclass for specialized indication classes, that address specific changes and alerts published by providers and instrumentation.
ms.assetid: b321b5ec-4868-4149-99ad-4596fd49c39b
title: CIM_ProcessIndication class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ProcessIndication
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_ProcessIndication class

**CIM\_ProcessIndication** is an abstract superclass for specialized indication classes, that address specific changes and alerts published by providers and instrumentation.

## Syntax

``` syntax
[Indication, Version("2.6.0"), UMLPackagePath("CIM::Event"), AMENDMENT]
class CIM_ProcessIndication : CIM_Indication
{
};
```

## Members

The **CIM\_ProcessIndication** class does not define any members.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Indication**](cim-indication.md)
</dt> </dl>

 

 




