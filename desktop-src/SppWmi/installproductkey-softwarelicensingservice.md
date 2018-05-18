---
title: InstallProductKey method of the SoftwareLicensingService class
description: Installs a product key for the current product.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '620ce990-bc59-4161-930d-7893eedb3834'
keywords: ["InstallProductKey method Windows Management Instrumentation", "InstallProductKey method Windows Management Instrumentation , SoftwareLicensingService class", "SoftwareLicensingService class Windows Management Instrumentation , InstallProductKey method"]
topic_type:
- apiref
api_name:
- SoftwareLicensingService.InstallProductKey
api_location:
- SppWmi.dll
api_type:
- COM
---

# InstallProductKey method of the SoftwareLicensingService class

Installs a product key for the current product.

## Syntax


```mof
unit32 InstallProductKey(
  [in] string ProductKey
);
```



## Parameters

<dl> <dt>

*ProductKey* \[in\]
</dt> <dd>

Specifies the product key to install.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>SppWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SppWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingService**](softwarelicensingservice.md)
</dt> </dl>

 

 





