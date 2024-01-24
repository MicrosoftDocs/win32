---
description: Enables the image processing filter to write properties back to the driver (and device).
ms.assetid: b9bb8d81-2945-46ba-a0a2-7009000574aa
title: IWiaImageFilter::ApplyProperties method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaImageFilter.ApplyProperties
api_type: 
- COM
api_location: 
- Wia.h
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

Type: **[**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage)\***

Specifies a pointer to the [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) for the properties to be applied.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Do not call this method directly from your application. It is called by Windows Image Acquisition (WIA) 2.0 after the image processing filter has processed the raw data.

*pWiaPropertyStorage* is the [**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage) interface into which the image processing filter should write properties. An image processing filter should use only the [IPropertyStorage::WriteMultiple](/windows/win32/api/propidlbase/nf-propidlbase-ipropertystorage-writemultiple) method to write properties.

This method allows the image processing filter to write properties back to the driver (and device). This may be necessary for filters that implement features such as auto-exposure during film scanning.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
