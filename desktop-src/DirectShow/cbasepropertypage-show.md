---
Description: The Show method shows or hides the dialog box. This method implements the IPropertyPageShow method.
ms.assetid: 03796779-ed41-4b68-852d-6b1849a9dc10
title: CBasePropertyPage.Show method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePropertyPage.Show method

The `Show` method shows or hides the dialog box. This method implements the **IPropertyPage::Show** method.

## Syntax


```C++
HRESULT Show(
   UINT nCmdShow
);
```



## Parameters

<dl> <dt>

*nCmdShow* 
</dt> <dd>

Value that specifies whether to show or hide the window. For more information, see the Platform SDK documentaton.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                  | Description                    |
|----------------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid argument.<br/>   |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected failure.<br/> |



 

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




