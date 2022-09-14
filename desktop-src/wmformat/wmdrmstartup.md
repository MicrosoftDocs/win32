---
title: WMDRMStartup function (Wmdrmsdk.h)
description: The WMDRMStartup function initializes resources used by the Windows Media DRM Client Extended APIs.
ms.assetid: 2fd26bcc-8106-4356-933a-d4cf3536f4fb
keywords:
- WMDRMStartup function windows Media Format
topic_type:
- apiref
api_name:
- WMDRMStartup
api_location:
- Wmdrmsdk.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMStartup function

The **WMDRMStartup** function initializes resources used by the Windows Media DRM Client Extended APIs.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE WMDRMStartup(void);
```



## Parameters

This function has no parameters.

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

For every call of this function, you must call [**WMDRMShutdown**](wmdrmshutdown.md) to release the resources used.

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

 

 





