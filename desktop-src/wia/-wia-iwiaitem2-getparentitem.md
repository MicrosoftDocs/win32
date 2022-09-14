---
description: Gets the parent item in the tree that represents a Windows Image Acquisition (WIA) 2.0 hardware device.
ms.assetid: c6fdaf1d-9875-4852-893c-813894d89f6c
title: IWiaItem2::GetParentItem method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.GetParentItem
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::GetParentItem method

Gets the parent item in the tree that represents a Windows Image Acquisition (WIA) 2.0 hardware device.

## Syntax


```C++
HRESULT GetParentItem(
  [out] IWiaItem2 **ppIWiaItem2
);
```



## Parameters

<dl> <dt>

*ppIWiaItem2* \[out\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\*\***

Receives the address of a pointer to the [**IWiaItem2**](-wia-iwiaitem2.md) interface of the parent of the item in the tree of item objects. If this method is called on the root of the tree, then the returned address is **NULL**.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Given any [**IWiaItem2**](-wia-iwiaitem2.md) object in the object tree of a WIA 2.0 hardware device, the application retrieves a pointer to the parent item by calling this function.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers they receive through the *ppIWiaItem2* parameter if these pointers are not **NULL**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
