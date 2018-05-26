---
Description: Enables the image processing filter to write properties back to the driver (and device).
ms.assetid: b9bb8d81-2945-46ba-a0a2-7009000574aa
title: IWiaImageFilterApplyProperties method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWiaImageFilter::ApplyProperties method

Enables the image processing filter to write properties back to the driver (and device).

## Syntax


```C++
HRESULT ApplyProperties(
  [in] IWiaPropertyStorage *pWiaPropertyStorage
);
```



## Parameters

<dl> <dt>

*pWiaPropertyStorage* \[in\]
</dt> <dd>

Type: **[**IWiaPropertyStorage**](/windows/win32/wia_xp/nn-wia_xp-iwiapropertystorage?branch=master)\***

Specifies a pointer to the [**IWiaPropertyStorage**](/windows/win32/wia_xp/nn-wia_xp-iwiapropertystorage?branch=master) for the properties to be applied.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Do not call this method directly from your application. It is called by Windows Image Acquisition (WIA) 2.0 after the image processing filter has processed the raw data.

*pWiaPropertyStorage* is the [**IWiaPropertyStorage**](/windows/win32/wia_xp/nn-wia_xp-iwiapropertystorage?branch=master) interface into which the image processing filter should write properties. An image processing filter should use only the [IPropertyStorage::WriteMultiple](stg.ipropertystorage_writemultiple) method to write properties.

This method allows the image processing filter to write properties back to the driver (and device). This may be necessary for filters that implement features such as auto-exposure during film scanning.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




