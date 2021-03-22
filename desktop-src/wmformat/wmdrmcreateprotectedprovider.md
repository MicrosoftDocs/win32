---
title: WMDRMCreateProtectedProvider function (Wmdrmsdk.h)
description: The WMDRMCreateProtectedProvider function creates a class factory that can create the other objects of the Windows Media DRM Client Extended APIs.
ms.assetid: 0882062f-48a2-43bc-8853-a8a3d6bc2f52
keywords:
- WMDRMCreateProtectedProvider function windows Media Format
topic_type:
- apiref
api_name:
- WMDRMCreateProtectedProvider
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMCreateProtectedProvider function

The **WMDRMCreateProtectedProvider** function creates a class factory that can create the other objects of the Windows Media DRM Client Extended APIs. This function requires a stub library from Microsoft and creates objects that support the protected DRM features.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE WMDRMCreateProtectedProvider(
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



 

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Functions**](drm-functions.md)
</dt> <dt>

[**WMDRMCreateProvider**](wmdrmcreateprovider.md)
</dt> </dl>

 

 





