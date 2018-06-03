---
title: SystemState CheckBoolean method
description: Retrieves whether or not the specified system setting is enabled.
ms.assetid: 3A602EDC-0CC5-4374-A03A-CCAA2CDBBC6F
keywords:
- CheckBoolean method Access Execution Engine
- CheckBoolean method Access Execution Engine , SystemState interface
- SystemState interface Access Execution Engine , CheckBoolean method
topic_type:
- apiref
api_name:
- SystemState.CheckBoolean
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SystemState::CheckBoolean method

Retrieves whether or not the specified system setting is enabled.

## Syntax


```C++
virtual HRESULT CheckBoolean(
  [in]  SystemSetting setting,
  [out] BOOL          *enabled
) = 0;
```



## Parameters

<dl> <dt>

*setting* \[in\]
</dt> <dd>

The [**SystemSetting**](systemsetting.md) enumerator specifying which system setting to check. The enumerator must have the **SystemSettingFlagGetBool** bit set in it.

</dd> <dt>

*enabled* \[out\]
</dt> <dd>

True if the specified setting was configured.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

Managed code uses the [**SystemState.CheckBoolean**](https://www.bing.com/search?q=**SystemState.CheckBoolean**) method.

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

 

 





