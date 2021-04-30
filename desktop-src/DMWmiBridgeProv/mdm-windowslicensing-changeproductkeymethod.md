---
title: ChangeProductKeyMethod method of the MDM_WindowsLicensing class
description: This method installs a product key for Windows 10 desktop devices. Dot not reboot. See also ChangeProductKey.
ms.assetid: 1d9e3243-2ca4-427b-bda2-d33e1e70c80d
keywords:
- ChangeProductKeyMethod method
- ChangeProductKeyMethod method, MDM_WindowsLicensing class
- MDM_WindowsLicensing class, ChangeProductKeyMethod method
topic_type:
- apiref
api_name:
- MDM_WindowsLicensing.ChangeProductKeyMethod
api_location:
- DMWmiBridgeProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ChangeProductKeyMethod method of the MDM\_WindowsLicensing class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This method installs a product key for Windows 10 desktop devices. Dot not reboot. See also [ChangeProductKey](/windows/client-management/mdm/windowslicensing-csp)

## Syntax


```mof
uint32 ChangeProductKeyMethod(
  [in] string param
);
```



## Parameters

<dl> <dt>

*param* \[in\]
</dt> <dd></dd> </dl>

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
</dt> </dl>

 

