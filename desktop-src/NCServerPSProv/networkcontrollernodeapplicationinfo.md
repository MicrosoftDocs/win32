---
title: NetworkControllerNodeApplicationInfo class
description: Contains information on a network controller node application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1335e42b-6f7e-4586-810c-e884be2363be
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NetworkControllerNodeApplicationInfo class
- NetworkControllerNodeApplicationInfo class, described
topic_type:
- apiref
api_name:
- NetworkControllerNodeApplicationInfo
- NetworkControllerNodeApplicationInfo.Name
- NetworkControllerNodeApplicationInfo.RestInterfaceName
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NetworkControllerNodeApplicationInfo class

Contains information on a network controller node application.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class NetworkControllerNodeApplicationInfo
{
  string Name;
  string RestInterfaceName;
};
```

## Members

The **NetworkControllerNodeApplicationInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **NetworkControllerNodeApplicationInfo** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the node.

</dd> <dt>

**RestInterfaceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the interface on which to bind Rest server to.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 





