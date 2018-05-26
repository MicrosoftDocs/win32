---
title: NetworkControllerManifestVersion class
description: Describes the network Controller cluster and application manifest version.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fe4ef919-02be-47d7-b610-f51b7c7d8092
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NetworkControllerManifestVersion class
- NetworkControllerManifestVersion class, described
topic_type:
- apiref
api_name:
- NetworkControllerManifestVersion
- NetworkControllerManifestVersion.ClusterVersion
- NetworkControllerManifestVersion.ApplicationVersion
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# NetworkControllerManifestVersion class

Describes the network Controller cluster and application manifest version.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class NetworkControllerManifestVersion
{
  string ClusterVersion;
  string ApplicationVersion;
};
```

## Members

The **NetworkControllerManifestVersion** class has these types of members:

-   [Properties](#properties)

### Properties

The **NetworkControllerManifestVersion** class has these properties.

<dl> <dt>

**ApplicationVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the version of the application manifest template.

</dd> <dt>

**ClusterVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the version of the cluster manifest template.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 





