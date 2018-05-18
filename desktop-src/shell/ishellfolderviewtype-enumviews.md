---
Description: 'Retrieves an enumerator that will return one pointer to an item identifier list (PIDL) for every extended view.'
title: 'IShellFolderViewType::EnumViews method'
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

Flags indicating which items to include in the enumeration. For a list of possible values, see the [**SHCONTF**](shcontf.md) enumerated type. This parameter may be ignored.

</dd> <dt>

*ppenum* \[out\]
</dt> <dd>

Type: **[**IEnumIDList**](ienumidlist.md)\*\***

The address of a pointer variable of type [**IEnumIDList**](ienumidlist.md) that receives the enumerator.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Views are represented to the user as hidden folders off the root directory (represented by PIDLs). Whenever appropriate, the default view (off the root folder) is represented as the **NULL**, or empty, PIDL.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




