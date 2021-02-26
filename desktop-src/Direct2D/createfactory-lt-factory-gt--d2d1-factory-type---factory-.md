---
title: D2D1CreateFactory Factory (D2D1_FACTORY_TYPE,Factory  ) Function (D2d1.h)
description: Creates a factory object that can be used to create Direct2D resources. | D2D1CreateFactory Factory (D2D1_FACTORY_TYPE,Factory  ) Function (D2d1.h)
ms.assetid: c1c25d51-15ea-4075-a896-bd6501bf68c1
keywords:
- D2D1CreateFactory Factory (D2D1_FACTORY_TYPE,Factory ) Function Direct2D
topic_type:
- apiref
api_name:
- D2D1CreateFactory Factory (D2D1_FACTORY_TYPE,Factory ) Function
api_location:
- D2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# D2D1CreateFactory<Factory>(D2D1\_FACTORY\_TYPE,Factory\*\*) Function

Creates a factory object that can be used to create Direct2D resources.

``` syntax
template<class Factory>
HRESULT D2D1CreateFactory(
    __in D2D1_FACTORY_TYPE factoryType,
    __out Factory **factory
);
```

## Template Parameters



| Parameter | Description                                                 |
|-----------|-------------------------------------------------------------|
| *Factory* | The type of [**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory) to create. |



 

## Parameters



| Parameter     | Description                                                                     |
|---------------|---------------------------------------------------------------------------------|
| *factoryType* | The threading model of the factory and the resources it creates.                |
| *factory*     | When this method returns, contains the address of a pointer to the new factory. |



 

## Return Value

If the method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Examples

The following example creates a factory.


```C++
HRESULT DemoApp::CreateDeviceIndependentResources()
{
    HRESULT hr = S_OK;

    // Create a Direct2D factory.
    hr = D2D1CreateFactory(D2D1_FACTORY_TYPE_SINGLE_THREADED, &m_pDirect2dFactory);

    return hr;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>D2d1.h</dt> </dl>                                                        |
| Library<br/>                  | <dl> <dt>D2d1.lib</dt> </dl>                                                      |
| DLL<br/>                      | <dl> <dt>D2d1.dll</dt> </dl>                                                      |



 

