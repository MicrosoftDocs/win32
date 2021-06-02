---
description: The ITablet3 interface enables multitouch querying for input.
ms.assetid: 949f2d83-7761-4d60-b8fe-5a9ac7567238
title: ITablet3 interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet3
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet3 interface

The ITablet3 interface enables multitouch querying for input.

## Members

The **ITablet3** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITablet3** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITablet3** interface has these methods.



| Method                                                  | Description                                                         |
|:--------------------------------------------------------|:--------------------------------------------------------------------|
| [**GetMaximumCursors**](itablet3-getmaximumcursors.md) | Retrieves the maximum number of inputs supported.<br/>        |
| [**isMultiTouch**](itablet3-ismultitouch.md)           | Indicates whether multitouch is enabled for this object.<br/> |



 

## Remarks

Developers should not use this interface

The following code describes how the **ITablet3** interface is defined.

``` syntax
[
  object,
  uuid(AC0E3951-0A2F-448E-88D0-49DA0C453460)
  pointer_default(unique)
]
interface ITablet3 : IUnknown
{
    HRESULT IsMultiTouch([out] BOOL *pIsMultiTouch);

    HRESULT GetMaximumCursors([out] ULONG *pMaximumCursors);
};
  
```

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



 

