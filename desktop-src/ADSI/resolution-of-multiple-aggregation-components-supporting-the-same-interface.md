---
title: Resolution of Multiple Aggregation Components Supporting the Same Interface
description: It is uncommon that two extensions expose the same interface to ADSI.
ms.assetid: 87cb1a17-04f7-4ad0-989a-a9506dfdca05
ms.tgt_platform: multiple
keywords:
- Resolution of Multiple Aggregation Components Supporting the Same Interface ADSI
- resolution of multiple aggregation components supporting the same interface ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Resolution of Multiple Aggregation Components Supporting the Same Interface

It is uncommon that two extensions expose the same interface to ADSI. If this happens, the following rules apply:

-   If an interface, such as **IMyInterface**, is supported by both the aggregator (ADSI) and any extension objects, **QueryInterface** always returns the **IMyInterface** for ADSI.
-   If an interface, such as **IMyInterface**, is not supported by the aggregator (ADSI), but is supported by more than one extension object, **QueryInterface** returns the **IMyInterface** of the first extension object listed in the registry that supports the interface.

Be aware that the order of components in the registry also affects the resolution of name conflicts in Automation. For more information, see [Resolution of Function/Property Name Conflicts in Automation in Extensions](resolution-of-functionproperty-name-conflicts-in-automation-in-extensions.md).

 

 




