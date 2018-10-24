---
Description: Provides access to all of the tablets attached to the computer.
ms.assetid: d0fd9a6f-93fe-43d6-97fd-fee45854dfa1
title: ITabletManager interface
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletManager
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletManager interface

Provides access to all of the tablets attached to the computer.

## Members

The **ITabletManager** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **ITabletManager** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITabletManager** interface has these methods.



| Method                                                  | Description                                                        |
|:--------------------------------------------------------|:-------------------------------------------------------------------|
| [**GetTablet**](https://msdn.microsoft.com/en-us/library/Aa373683(v=VS.85).aspx)           | Retrieves the specified tablet object.<br/>                  |
| [**GetTabletCount**](itabletmanager-gettabletcount.md) | Retrieves the number of tablets attached to the system.<br/> |



 

## Remarks

Developers should not use this interface.

The following code shows how the **ITabletManager** interface is implemented.

``` syntax
[
    object,
    uuid(764DE8AA-1867-47C1-8F6A-122445ABD89A),
    pointer_default(unique)
]
interface ITabletManager : IUnknown
{
    HRESULT GetDefaultTablet(
        [out] ITablet **ppTablet);

    HRESULT GetTabletCount(
        [out] ULONG *pcTablets);

    HRESULT GetTablet(
        [in] ULONG iTablet,
        [out] ITablet **ppTablet);

    HRESULT GetTabletContextById(
        [in] TABLET_CONTEXT_ID tcid,
        [out] ITabletContext **ppContext);

    HRESULT GetCursorById(
        [in] CURSOR_ID cid,
        [out] ITabletCursor **ppCursor);
};
        
        
```

Call [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) with a class ID of CLSID\_TabletManagerS, and then call [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) to get a pointer to the **ITabletManager Interface**. The CLSID\_TabletManagerS GUID is defined as follows:

``` syntax
#define CLSID_TabletManagerS uuid(A5B020FD-E04B-4e67-B65A-E7DEED25B2CF)
```

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



 

 




