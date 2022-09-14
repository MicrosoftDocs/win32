---
description: Retrieves an enumerator that will return one pointer to an item identifier list (PIDL) for every extended view.
title: IShellFolderViewType::EnumViews method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellFolderViewType.EnumViews
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: e44cd774-1d16-4faa-b5ca-fcaf2740cdca

---

# IShellFolderViewType::EnumViews method

Retrieves an enumerator that will return one pointer to an item identifier list (PIDL) for every extended view.

## Syntax


```C++
HRESULT EnumViews(
  [in]  ULONG       grfFlags,
  [out] IEnumIDList **ppenum
);
```



## Parameters

<dl> <dt>

*grfFlags* \[in\]
</dt> <dd>

Type: **ULONG**

Flags indicating which items to include in the enumeration. For a list of possible values, see the [**SHCONTF**](/windows/win32/api/shobjidl_core/ne-shobjidl_core-_shcontf) enumerated type. This parameter may be ignored.

</dd> <dt>

*ppenum* \[out\]
</dt> <dd>

Type: **[**IEnumIDList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumidlist)\*\***

The address of a pointer variable of type [**IEnumIDList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumidlist) that receives the enumerator.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Views are represented to the user as hidden folders off the root directory (represented by PIDLs). Whenever appropriate, the default view (off the root folder) is represented as the **NULL**, or empty, PIDL.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




