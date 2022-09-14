---
title: UpgradeEditionWithProductKeyMethod method of the MDM_WindowsLicensing class
description: Enters a product key for an edition upgrade of Windows 10 desktop devices. See also, UpgradeEditionWithProductKey.
ms.assetid: 6576fb5c-210c-4979-8c01-ed8f78e72c2c
keywords:
- UpgradeEditionWithProductKeyMethod method
- UpgradeEditionWithProductKeyMethod method, MDM_WindowsLicensing class
- MDM_WindowsLicensing class, UpgradeEditionWithProductKeyMethod method
topic_type:
- apiref
api_name:
- MDM_WindowsLicensing.UpgradeEditionWithProductKeyMethod
api_location:
- DMWmiBridgeProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# UpgradeEditionWithProductKeyMethod method of the MDM\_WindowsLicensing class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Enters a product key for an edition upgrade of Windows 10 desktop devices. See also, [UpgradeEditionWithProductKey](/windows/client-management/mdm/windowslicensing-csp).

## Syntax


```mof
uint32 UpgradeEditionWithProductKeyMethod(
  [in] string param
);
```



## Parameters

<dl> <dt>

*param* \[in\]
</dt> <dd>

The product key.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_WindowsLicensing**](mdm-windowslicensing.md)
</dt> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

