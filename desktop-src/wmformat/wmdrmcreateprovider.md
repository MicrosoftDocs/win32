---
title: WMDRMCreateProvider function (Wmdrmsdk.h)
description: The WMDRMCreateProvider function creates a class factory that can create the other objects of the Windows Media DRM Client Extended APIs.
ms.assetid: 25ec2fbf-136a-4f40-b2d3-f35b42178c60
keywords:
- WMDRMCreateProvider function windows Media Format
topic_type:
- apiref
api_name:
- WMDRMCreateProvider
api_location:
- Wmdrmsdk.dll
- Ext-MS-Win-mm-wmdrmsdk-l1-1-0.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMCreateProvider function

The **WMDRMCreateProvider** function creates a class factory that can create the other objects of the Windows Media DRM Client Extended APIs. This function does not require a stub library from Microsoft and creates objects that do not support the protected DRM features.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE WMDRMCreateProvider(
  _Out_ IWMDRMProvider **ppDRMProvider
);
```



## Parameters

<dl> <dt>

*ppDRMProvider* \[out\]
</dt> <dd>

Receives a pointer to the [**IWMDRMProvider**](iwmdrmprovider.md) interface of the newly created object.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Wmdrmsdk.dll</dt> </dl> |



## See also

<dl> <dt>

[**Functions**](drm-functions.md)
</dt> <dt>

[**WMDRMCreateProtectedProvider**](wmdrmcreateprotectedprovider.md)
</dt> </dl>

 

 





