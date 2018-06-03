---
title: GetRunningManifestVersion method of the PS\_NetworkControllerNode class
description: Returns the running application manifest version.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 92414a57-2c96-4f75-9284-0c1c1563fd9f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetRunningManifestVersion method
- GetRunningManifestVersion method, PS_NetworkControllerNode class
- PS_NetworkControllerNode class, GetRunningManifestVersion method
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode.GetRunningManifestVersion
api_location:
- NCServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetRunningManifestVersion method of the PS\_NetworkControllerNode class

Returns the running application manifest version.

## Syntax


```mof
uint32 GetRunningManifestVersion(
  [out] string RunningManifestVersion
);
```



## Parameters

<dl> <dt>

*RunningManifestVersion* \[out\]
</dt> <dd>

On success, contains the running application manifest version.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkControllerNode**](ps-networkcontrollernode.md)
</dt> </dl>

 

 





