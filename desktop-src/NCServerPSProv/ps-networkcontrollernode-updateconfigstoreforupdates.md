---
title: UpdateConfigStoreForUpdates method of the PS\_NetworkControllerNode class
description: Updates the configuration store based on the update parameters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4b57b8c6-f55d-45b5-88e3-e610829ee1b6'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["UpdateConfigStoreForUpdates method", "UpdateConfigStoreForUpdates method, PS_NetworkControllerNode class", "PS_NetworkControllerNode class, UpdateConfigStoreForUpdates method"]
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode.UpdateConfigStoreForUpdates
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# UpdateConfigStoreForUpdates method of the PS\_NetworkControllerNode class

Updates the configuration store based on the update parameters.

## Syntax


```mof
uint32 UpdateConfigStoreForUpdates(
  [in] string  HotFixName,
  [in] string  UpdateIds,
  [in] boolean DeleteAllUpdateConfigSettings
);
```



## Parameters

<dl> <dt>

*HotFixName* \[in\]
</dt> <dd>

Name of the hotfix.

</dd> <dt>

*UpdateIds* \[in\]
</dt> <dd>

String containing the update ids.

</dd> <dt>

*DeleteAllUpdateConfigSettings* \[in\]
</dt> <dd>

Set **true** to delete all update configuration settings; otherwise, **false**.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkControllerNode**](ps-networkcontrollernode.md)
</dt> </dl>

 

 





