---
title: Support SystemSettingCheckBoolean method
description: Retrieves the current setting of a specific system configuration item.
ms.assetid: '524366CA-04A4-42B5-AB3F-E9822C3F1F1D'
keywords: ["SystemSettingCheckBoolean method Access Execution Engine", "SystemSettingCheckBoolean method Access Execution Engine , Support interface", "Support interface Access Execution Engine , SystemSettingCheckBoolean method"]
topic_type:
- apiref
api_name:
- Support.SystemSettingCheckBoolean
api_location:
- AxeCore.dll
api_type:
- COM
---

# Support::SystemSettingCheckBoolean method

Retrieves the current setting of a specific system configuration item.

## Syntax


```C++
virtual HRESULT SystemSettingCheckBoolean(
  [in]  SystemSetting setting,
  [out] BOOL          *enabled
) const = 0;
```



## Parameters

<dl> <dt>

*setting* \[in\]
</dt> <dd>

A single value of a [**SystemSetting**](systemsetting.md) enumeration specifying which system setting to retrieve.

</dd> <dt>

*enabled* \[out\]
</dt> <dd>

A Boolean that indicates whether the specified setting is enabled.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method allows an assessment to determine the current state of a system setting.

Managed code uses the [**Support.SystemSettingCheckBoolean**](axe-support_systemsettingcheckboolean_om) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





