---
description: Gets the ISearchItem object if the URL represents an actual Shell data source (also known as a Shell namespace extension).
ms.assetid: 7da6344d-b433-48c3-8f75-7bef0295b9ea
title: ISearchItem::GetParentFolder method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISearchItem.GetParentFolder
api_type: 
- COM
api_location: 
---

# ISearchItem::GetParentFolder method

Gets the [**ISearchItem**](-search-isearchitem.md) object if the URL represents an actual Shell data source (also known as a Shell namespace extension).

## Syntax


```C++
HRESULT GetParentFolder(
  [out] ppShellFolder **IShellFolder,
  [out] ppidl         *LPITEMIDLIST
);
```



## Parameters

<dl> <dt>

*IShellFolder* \[out\]
</dt> <dd>

Type: **ppShellFolder\*\***

On return, contains the address of a pointer to the folder that contains the current URL. [IShellFolder Interface](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) is exposed by all Shell namespace folder objects, and its methods are used to manage folders.

</dd> <dt>

*LPITEMIDLIST* \[out\]
</dt> <dd>

Type: **ppidl\***

On return, contains the address of a pointer to an item identifier list (PIDL) that identifies the parent folder. The *LPITEMIDLIST* parameter can refer to an object at any level below the parent folder in the namespace hierarchy, and can thus be a multi-level pointer to a **pidl** relative to the parent folder.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The **ISearchItem::GetParentFolder** method is supported only on Windows XP and Windows Server 2003, and should no longer be used.

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the [**ISearchItem**](-search-isearchitem.md) interface, and the following APIs: the [**IItemPreviewerExt**](-search-iitempreviewerext.md), [**IItemPropertyBag**](iitempropertybag.md), and [**ISearchProtocolUI**](-search-isearchprotocolui.md) interfaces, the [**LINKINFO**](-search-linkinfo.md) structure, and the [**LINKTYPE**](-search-linktype.md) enumeration.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>          |



## See also

<dl> <dt>

[**ISearchItem**](-search-isearchitem.md)
</dt> </dl>

 

 
