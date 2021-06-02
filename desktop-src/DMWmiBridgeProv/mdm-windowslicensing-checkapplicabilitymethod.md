---
title: CheckApplicabilityMethod method of the MDM_WindowsLicensing class
description: Checks if the entered product key can be used for an edition upgrade, activation or changing a product key of Windows 10 for desktop devices. See also, CheckApplicability.
ms.assetid: b28ea397-72dd-4c10-a9fb-53087c3b654c
keywords:
- CheckApplicabilityMethod method
- CheckApplicabilityMethod method, MDM_WindowsLicensing class
- MDM_WindowsLicensing class, CheckApplicabilityMethod method
topic_type:
- apiref
api_name:
- MDM_WindowsLicensing.CheckApplicabilityMethod
api_location:
- DMWmiBridgeProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CheckApplicabilityMethod method of the MDM\_WindowsLicensing class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Checks if the entered product key can be used for an edition upgrade, activation or changing a product key of Windows 10 for desktop devices. See also, [CheckApplicability](/windows/client-management/mdm/windowslicensing-csp).

## Syntax


```mof
uint32 CheckApplicabilityMethod(
  [in] string param
);
```



## Parameters

<dl> <dt>

*param* \[in\]
</dt> <dd>

The product key.

</dd> </dl>

## Return value

TRUE or FALSE

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

 

