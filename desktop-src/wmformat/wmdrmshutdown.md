---
title: WMDRMShutdown function (Wmdrmsdk.h)
description: The WMDRMShutdown function releases resources used by the Windows Media DRM Client Extended APIs.
ms.assetid: fa99a07a-2f07-464b-b7a2-e8f3110389b5
keywords:
- WMDRMShutdown function windows Media Format
topic_type:
- apiref
api_name:
- WMDRMShutdown
api_location:
- Wmdrmsdk.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMShutdown function

The **WMDRMShutdown** function releases resources used by the Windows Media DRM Client Extended APIs.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE WMDRMShutdown(void);
```



## Parameters

This function has no parameters.

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

To avoid memory leaks, you must call this function for every call of the [**WMDRMStartup**](wmdrmstartup.md) function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Wmdrmsdk.dll</dt> </dl> |



## See also

<dl> <dt>

[**Functions**](drm-functions.md)
</dt> </dl>

 

 





