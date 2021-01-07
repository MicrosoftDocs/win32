---
description: Exposes callback routines to monitor the search process.
title: IShellFolderSearchableCallback interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellFolderSearchableCallback
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 3412a01b-d5ea-44e1-819c-f10f81fac391
api_name: 
 - IShellFolderSearchableCallback
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# IShellFolderSearchableCallback interface

Exposes callback routines to monitor the search process.

## Members

The **IShellFolderSearchableCallback** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IShellFolderSearchableCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IShellFolderSearchableCallback** interface has these methods.



| Method                                                      | Description                                      |
|:------------------------------------------------------------|:-------------------------------------------------|
| [**RunBegin**](ishellfoldersearchablecallback-runbegin.md) | Indicates that a search was started.<br/>  |
| [**RunEnd**](ishellfoldersearchablecallback-runend.md)     | Indicates that a search has finished.<br/> |



 

## Remarks

This interface is not defined in any public header files. Should you choose to implement this interface, you can use the following C/C++ code to declare its methods.


```
#undef  INTERFACE
#define INTERFACE IShellFolderSearchableCallback
DECLARE_INTERFACE_IID_(IShellFolderSearchableCallback, IUnknown, "F98D8294-2BBC-11d2-8DBD-0000F87A556C")
{
    // *** IUnknown methods ***
    STDMETHOD(QueryInterface) (THIS_ REFIID riid, __out void **ppv) PURE;
    STDMETHOD_(ULONG,AddRef)  (THIS) PURE;
    STDMETHOD_(ULONG,Release) (THIS) PURE;

    // *** IShellFolderSearchableCallback Methods ***

    STDMETHOD(RunBegin)(THIS_ DWORD dwReserved) PURE;
    STDMETHOD(RunEnd)(THIS_ DWORD dwReserved) PURE;
};
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 
