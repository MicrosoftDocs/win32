---
description: Represents a stylus object.
ms.assetid: c55945b7-59df-49b5-b25f-fa96056889fc
title: ITabletCursor interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletCursor
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletCursor interface

Represents a stylus object.

## Members

The **ITabletCursor** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITabletCursor** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITabletCursor** interface has these methods.



| Method                                                 | Description                                                            |
|:-------------------------------------------------------|:-----------------------------------------------------------------------|
| [**GetButton**](itabletcursor-getbutton.md)           | Retrieves the specified button object from a tablet stylus.<br/> |
| [**GetButtonCount**](itabletcursor-getbuttoncount.md) | Retrieves the number of buttons on the tablet stylus.<br/>       |
| [**GetId**](itabletcursor-getid.md)                   | Retrieves the stylus identifier.<br/>                            |
| [**GetName**](itabletcursor-getname.md)               | Retrieves the name of the tablet stylus.<br/>                    |
| [**IsInverted**](itabletcursor-isinverted.md)         | Indicates if the stylus is upside down.<br/>                     |



 

## Remarks

Do not use this interface.

The following code describes how the **ITabletCursor** interface is defined.

``` syntax
[
    object,
    uuid(EF9953C6-B472-4B02-9D22-D0E247ADE0E8,
    pointer_default(unique)
]
interface ITabletCursor : IUnknown
{
    HRESULT GetName(
        [out] LPWSTR *ppwszName);

    HRESULT IsInverted();

    HRESULT GetId(
        [out] CURSOR_ID *pCid);

    HRESULT GetTablet(
        [out] ITablet **ppTablet);

    HRESULT GetButtonCount(
        [out] ULONG *pcButtons);

    HRESULT GetButton(
        [in] ULONG iButton,
        [out] ITabletCursorButton **ppButton);
};

     
```

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



 

