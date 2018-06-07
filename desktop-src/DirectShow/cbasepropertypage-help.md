---
Description: The Help method invokes the property page help. This method implements the IPropertyPage::Help method.
ms.assetid: 8fe72b2e-a9f1-435d-8eda-27056f112c6d
title: CBasePropertyPage.Help method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBasePropertyPage.Help method

The `Help` method invokes the property page help. This method implements the **IPropertyPage::Help** method.

## Syntax


```C++
HRESULT Help(
   LPCWSTR lpszHelpDir
);
```



## Parameters

<dl> <dt>

*lpszHelpDir* 
</dt> <dd>

Pointer to the string under the **HelpDir** key in the property page's CLSID information in the registry.

</dd> </dl>

## Return value

Returns E\_NOTIMPL.

## Remarks

In the base class, the method always returns E\_NOTIMPL. When the method fails, the frame calls **IPropertyPage::GetPageInfo** to get the name of the help file and context identifier. By default, these are **NULL**. To provide help, therefore, the derived class can override either the `Help` method or the [**CBasePropertyPage::GetPageInfo**](cbasepropertypage-getpageinfo.md) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




