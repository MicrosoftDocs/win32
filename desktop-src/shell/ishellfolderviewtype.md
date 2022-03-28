---
description: Exposes methods that enable a Shell folder to support different views on its content (different hierarchical layouts of its data).
title: IShellFolderViewType interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellFolderViewType
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 9b597f6b-ef27-4fa1-ad00-e131dbd979e7

---

# IShellFolderViewType interface

Exposes methods that enable a Shell folder to support different views on its content (different hierarchical layouts of its data).

## Members

The **IShellFolderViewType** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IShellFolderViewType** also has these types of members:

- [Methods](#methods)

### Methods

The **IShellFolderViewType** interface has these methods.



| Method                                                                      | Description                                                                                                                                                          |
|:----------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumViews**](ishellfolderviewtype-enumviews.md)                         | Retrieves an enumerator that will return one PIDL for every extended view.<br/>                                                                                |
| [**GetDefaultViewName**](ishellfolderviewtype-getdefaultviewname.md)       | Gets the name of the default view. Call [**IShellFolder::GetDisplayNameOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof) to retrieve the names of the other views.<br/> |
| [**GetViewTypeProperties**](ishellfolderviewtype-getviewtypeproperties.md) | Gets the properties of the view.<br/>                                                                                                                          |
| [**TranslateViewPidl**](ishellfolderviewtype-translateviewpidl.md)         | Reconstructs a PIDL from one hierarchical representation of the Shell folder into a different representation.<br/>                                             |



 

## Remarks

This enumerator returns PIDLs that are special hidden folders at the top level of the Shell folder, which are not otherwise enumerated. The default view is the one the Shell folder displays normally.

This interface is not defined in any public header file. Should you choose to implement this interface, you can use the following C/C++ code to declare its methods.


```
#undef  INTERFACE
#define INTERFACE   IShellFolderViewType
DECLARE_INTERFACE_IID_(IShellFolderViewType, IUnknown, "49422C1E-1C03-11d2-8DAB-0000F87A556C")
{
    // *** IUnknown methods ***
    STDMETHOD(QueryInterface) (THIS_ REFIID riid, __out void **ppv) PURE;
    STDMETHOD_(ULONG,AddRef)  (THIS) PURE;
    STDMETHOD_(ULONG,Release) (THIS) PURE;

    // *** IShellFolderViewType Methods ***

    // EnumViews:
    //   Returns an enumerator which will give out one pidl for every extended view.
    STDMETHOD(EnumViews)(THIS_ ULONG grfFlags, __out IEnumIDList **ppenum) PURE;

    // GetDefaultViewName:
    //   Returns the name of the default view.  The names of the other views
    //   can be retrieved by calling GetDisplayNameOf.
    STDMETHOD(GetDefaultViewName)(THIS_ DWORD  uFlags, __out LPWSTR *ppwszName) PURE;
    STDMETHOD(GetViewTypeProperties)(THIS_ PCUITEMID_CHILD pidl, __out DWORD *pdwFlags)  PURE;

    // TranslateViewPidl:
    //   Attempts to take a pidl represented in one hierarchical representation of
    //   the Shell folder, and find it in a different representation.
    //   pidl should be relative to the root folder.
    //   Remember to ILFree ppidlOut
    STDMETHOD(TranslateViewPidl)(THIS_ PCUIDLIST_RELATIVE pidl, PCUIDLIST_RELATIVE pidlView,
              __out PIDLIST_RELATIVE *ppidlOut) PURE;
};

#define SFVTFLAG_NOTIFY_CREATE  0x00000001
#define SFVTFLAG_NOTIFY_RESORT  0x00000002
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 
