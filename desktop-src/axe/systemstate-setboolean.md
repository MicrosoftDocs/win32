---
title: SystemState SetBoolean method
description: Sets specified system settings.
ms.assetid: 8C223BDE-2AF5-44DE-9462-CE06DC99FAA5
keywords:
- SetBoolean method Access Execution Engine
- SetBoolean method Access Execution Engine , SystemState interface
- SystemState interface Access Execution Engine , SetBoolean method
topic_type:
- apiref
api_name:
- SystemState.SetBoolean
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SystemState::SetBoolean method

Sets specified system settings.

## Syntax


```C++
virtual HRESULT SetBoolean(
  [in] SystemSetting setting,
  [in] BOOL          enable
) = 0;
```



## Parameters

<dl> <dt>

*setting* \[in\]
</dt> <dd>

The [**SystemSetting**](systemsetting.md) enumerator specifying which system setting to set. The enumerator must have the **SystemSettingFlagSetBoolFalse** or **SystemSettingFlagSetBoolFalse** bit set in it depending on the value of enabled passed in.

</dd> <dt>

*enable* \[in\]
</dt> <dd>

True if the specified setting is to be set to enable.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

When an assessment calls this method, the original value is stored in the state file that was created by [**ManageSystemState**](support-managesystemstate.md) when this [**SystemState**](systemstate.md) object was created. If the value of *enabled* does not match the **SystemSettingFlagSetBoolFalse** or **SystemSettingFlagSetBoolTrue** values in the [**SystemSetting**](systemsetting.md) bits set in the setting enumerator, an error will be returned.

Managed code uses [**SystemState.SetBoolean**](axe-systemstate_setboolean_om) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**SystemState**](systemstate.md)
</dt> </dl>

 

 





