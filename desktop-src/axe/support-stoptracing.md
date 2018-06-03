---
title: Support StopTracing method
description: Finishes advanced ETW tracing using a Windows Performance Analyzer (WPA) profile.
ms.assetid: 51355786-10B0-412C-AD66-7136D5819C61
keywords:
- StopTracing method Access Execution Engine
- StopTracing method Access Execution Engine , Support interface
- Support interface Access Execution Engine , StopTracing method
topic_type:
- apiref
api_name:
- Support.StopTracing
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

# Support::StopTracing method

Finishes advanced ETW tracing using a Windows Performance Analyzer (WPA) profile.

## Syntax


```C++
virtual HRESULT StopTracing(
  [in] LPCWSTR profileFileName,
  [in] LPCWSTR propertyName,
  [in] LPCWSTR outputFileName
) = 0;
```



## Parameters

<dl> <dt>

*profileFileName* \[in\]
</dt> <dd>

The name of the WPA file that contains the profile.

</dd> <dt>

*propertyName* \[in\]
</dt> <dd>

The name of the property.

</dd> <dt>

*outputFileName* \[in\]
</dt> <dd>

The name of the file that will be created containing the tracing session.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method does not trace data to the Axe ETW logging session. Instead, it finishes an advanced ETW tracing session using a profile from WPA.

Managed code uses [**Support.StopTracing**](https://www.bing.com/search?q=**Support.StopTracing**) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> <dt>

[**StartTracing**](support-starttracing.md)
</dt> </dl>

 

 





