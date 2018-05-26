---
title: ServiceFabricVersion class
description: Describes the service fabric installed version.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 582bad86-6f0c-4e58-a78b-5b2e8b4a5d1f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ServiceFabricVersion class
- ServiceFabricVersion class, described
topic_type:
- apiref
api_name:
- ServiceFabricVersion
- ServiceFabricVersion.InstalledVersion
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ServiceFabricVersion class

Describes the service fabric installed version.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class ServiceFabricVersion
{
  string InstalledVersion;
};
```

## Members

The **ServiceFabricVersion** class has these types of members:

-   [Properties](#properties)

### Properties

The **ServiceFabricVersion** class has these properties.

<dl> <dt>

**InstalledVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version installed Service Fabric (i.e: Cab).

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 





