---
Description: A static creator function that can create a XamlUIPresenter for a render surface in a desktop app.
ms.assetid: 3160E4C2-39D3-8FF5-ED37-78E645D1AC2E
title: CreateXamlUIPresenter function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateXamlUIPresenter function

A static creator function that can create a [**XamlUIPresenter**](https://msdn.microsoft.com/en-us/library/Hh701914(v=WIN.10).aspx) for a render surface in a desktop app.

## Syntax


```C++
 static HRESULT WINAPI CreateXamlUIPresenter(
  _In_  IViewObjectPresentNotifySite                 *pPresentSite,
  _Out_ Windows::UI::Xaml::Hosting::IXamlUIPresenter **ppPresenter
);
```



## Parameters

<dl> <dt>

*pPresentSite* \[in\]
</dt> <dd>

An existing hosting interface. See **IViewObjectPresentNotifySite** in Internet Explorer documentation.

</dd> <dt>

*ppPresenter* \[out\]
</dt> <dd>

The **\[exclusiveto\]** interface for a [**XamlUIPresenter**](https://msdn.microsoft.com/en-us/library/Hh701914(v=WIN.10).aspx).

</dd> </dl>

## Return value

A standard **HResult**, **S\_OK** for success.

## Remarks

Calling this method requires a **DllImport** from Windows.UI.Xaml.dll.

You cannot call this method from a Windows Store app.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Windows.ui.xaml-coretypes.idl</dt> </dl> |
| DLL<br/>    | <dl> <dt>Windows.UI.Xaml.dll</dt> </dl>           |



## See also

<dl> <dt>

[**XamlUIPresenter**](https://msdn.microsoft.com/en-us/library/Hh701914(v=WIN.10).aspx)
</dt> </dl>

 

 




