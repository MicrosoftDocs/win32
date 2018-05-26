---
Description: Represents general information about a button on a stylus device.
ms.assetid: 20c9f8bb-8f8d-4469-baff-b9001c8adb3b
title: ITabletCursorButton interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ITabletCursorButton interface

Represents general information about a button on a stylus device.

## Members

The **ITabletCursorButton** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **ITabletCursorButton** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITabletCursorButton** interface has these methods.



| Method                                         | Description                                                      |
|:-----------------------------------------------|:-----------------------------------------------------------------|
| [**GetGuid**](itabletcursorbutton-getguid.md) | Retrieves the unique identifier of the stylus button.<br/> |
| [**GetName**](itabletcursorbutton-getname.md) | Retrieves the name of the stylus button.<br/>              |



 

## Remarks

Developers should not use this interface.

The following code shows how the **ITabletCursorButton** interface is defined.

``` syntax
[
    object,
    uuid(997A992E-8B6C-4945-BC17-A1EE563B3AB7),
    pointer_default(unique)
]
interface ITabletCursorButton : IUnknown
{
    HRESULT GetName(
        [out] LPWSTR *ppwszName);

    HRESULT GetGuid(
        [out] GUID *pguidBtn);
};
```

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITabletCursorButton Interface**](itabletcursorbutton.md)
</dt> </dl>

 

 




