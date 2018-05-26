---
title: RegistryEvent class
description: The RegistryEvent class is an abstract class from which the RegistryKeyChangeEvent, RegistryTreeChangeEvent, and RegistryValueChangeEvent classes are derived.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9eb0c515-21cd-4149-a1bf-cfd1014a9d41
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RegistryEvent class
- RegistryEvent class, described
topic_type:
- apiref
api_name:
- RegistryEvent
api_location:
- StdProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RegistryEvent class

The **RegistryEvent** class is an abstract class from which the [**RegistryKeyChangeEvent**](registrykeychangeevent.md), [**RegistryTreeChangeEvent**](registrytreechangeevent.md), and [**RegistryValueChangeEvent**](registryvaluechangeevent.md) classes are derived. For more information about using the WMI registry event classes, see the [Modifying the System Registry](https://msdn.microsoft.com/library/aa392388) section. For code examples, see [WMI Tasks: Registry](https://msdn.microsoft.com/library/aa394600).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class RegistryEvent : __ExtrinsicEvent
{
};
```

## Members

The **RegistryEvent** class does not define any members.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RegEvent.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StdProv.dll</dt> </dl>  |



## See also

<dl> <dt>

[**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646)
</dt> </dl>

 

 





