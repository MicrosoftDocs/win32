---
title: Support StartTracing method
description: Begins advanced ETW tracing using a Windows Performance Analyzer (WPA) profile.
ms.assetid: '559EC2A9-6264-4D62-B8F4-38D086E48BAA'
keywords: ["StartTracing method Access Execution Engine", "StartTracing method Access Execution Engine , Support interface", "Support interface Access Execution Engine , StartTracing method"]
topic_type:
- apiref
api_name:
- Support.StartTracing
api_location:
- AxeCore.dll
api_type:
- COM
---

# Support::StartTracing method

Begins advanced ETW tracing using a Windows Performance Analyzer (WPA) profile.

## Syntax


```C++
virtual HRESULT StartTracing(
  [in] LPCWSTR profileFileName,
  [in] LPCWSTR profileName
) = 0;
```



## Parameters

<dl> <dt>

*profileFileName* \[in\]
</dt> <dd>

The name of the WPA file that contains the profile.

</dd> <dt>

*profileName* \[in\]
</dt> <dd>

The name of the WPA profile to use for tracing.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method does not trace data to the Axe ETW logging session. Instead, it begins an advanced ETW tracing session using a profile from WPA.

Managed code uses the [**Support.StartTracing**](axe-support_starttracing_om) method.

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
</dt> <dt>

[**StopTracing**](support-stoptracing.md)
</dt> </dl>

 

 





