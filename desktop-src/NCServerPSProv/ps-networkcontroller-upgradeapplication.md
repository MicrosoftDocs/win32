---
title: UpgradeApplication method of the PS\_NetworkController class
description: This method upgrades the network controller.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4d809e83-7143-4385-b464-b81e007c2b83'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["UpgradeApplication method", "UpgradeApplication method, PS_NetworkController class", "PS_NetworkController class, UpgradeApplication method"]
topic_type:
- apiref
api_name:
- PS_NetworkController.UpgradeApplication
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# UpgradeApplication method of the PS\_NetworkController class

This method upgrades the network controller.

## Syntax


```mof
uint32 UpgradeApplication(
  [in] boolean IsForceUpgrade
);
```



## Parameters

<dl> <dt>

*IsForceUpgrade* \[in\]
</dt> <dd>

**true** to force the upgrade; otherwise, **false**.

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

[**PS\_NetworkController**](ps-networkcontroller.md)
</dt> </dl>

 

 





