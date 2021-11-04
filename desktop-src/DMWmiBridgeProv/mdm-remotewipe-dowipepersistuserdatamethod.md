---
title: doWipePersistUserDataMethod method of the MDM_RemoteWipe class
description: Triggers the device to start the remote wipe while persisting user accounts and data.
keywords:
- doWipePersistUserDataMethod method
- doWipePersistUserDataMethod method, MDM_RemoteWipe class
- MDM_RemoteWipe class, doWipePersistUserDataMethod method
topic_type:
- apiref
api_name:
- MDM_RemoteWipe.doWipePersistUserDataMethod
api_location:
- DMWmiBridgeProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/17/2021
---

# doWipePersistUserDataMethod method of the MDM_RemoteWipe class

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

Triggers the device to start the remote wipe while persisting user accounts and data. Also see [doWipePersistUserDataMethod](/windows/client-management/mdm/remotewipe-csp).

## Syntax

```mof
uint32 doWipePersistUserDataMethod(
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
