---
title: doWipeMethod method of the MDM_RemoteWipe class
description: Triggers the device to start the remote wipe.
ms.assetid: dc25dc09-6a74-4c08-b452-b1d83085bb41
keywords:
- doWipeMethod method
- doWipeMethod method, MDM_RemoteWipe class
- MDM_RemoteWipe class, doWipeMethod method
topic_type:
- apiref
api_name:
- MDM_RemoteWipe.doWipeMethod
api_location:
- DMWmiBridgeProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# doWipeMethod method of the MDM\_RemoteWipe class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Triggers the device to start the remote wipe. See also, [doWipe](/windows/client-management/mdm/remotewipe-csp).

## Syntax


```mof
uint32 doWipeMethod(
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
| Namespace<br/>                | Root\\CIMv2\\MDM\\DMMap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_RemoteWipe**](mdm-remotewipe.md)
</dt> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

