---
Description: The Dynamic qualifier indicates a class whose instances are created dynamically. The value of this qualifier must be set to TRUE.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 63286687-abbf-49f0-8061-3b47fba75806
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Dynamic Qualifier
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Qualifier

The **Dynamic** qualifier indicates a class whose instances are created dynamically. The value of this qualifier must be set to **TRUE**.

The **Dynamic** qualifier must be specified on all classes that contain data and for which instances are created dynamically. The [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifier is typically also specified to identify the provider responsible for supplying the data.

Classes that contain only methods that need implementation do not require the **Dynamic** qualifier. Only the [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifier is required to specify the name of the provider to supply the implementation.

All classes derived from a dynamic class must be dynamic. You cannot derive a static class from a dynamic class.

When **Dynamic** is specified on a property of an instance, the **PropertyContext** qualifier must also be specified.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**Standard WMI Qualifiers**](standard-wmi-qualifiers.md)
</dt> <dt>

[WMI Qualifiers](wmi-qualifiers.md)
</dt> <dt>

[Adding a Qualifier](adding-a-qualifier.md)
</dt> </dl>

 

 




