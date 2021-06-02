---
description: Creates an enumerator object and passes back a pointer to its IEnumWiaItem2 interface for folders with items in the IWiaItem2 tree of a Windows Image Acquisition (WIA) 2.0 device.
ms.assetid: 0862bb6f-0464-491a-8cad-60b92d9609f1
title: IWiaItem2::EnumChildItems method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.EnumChildItems
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::EnumChildItems method

Creates an enumerator object and passes back a pointer to its [**IEnumWiaItem2**](-wia-ienumwiaitem2.md) interface for folders with items in the [**IWiaItem2**](-wia-iwiaitem2.md) tree of a Windows Image Acquisition (WIA) 2.0 device.

## Syntax


```C++
HRESULT EnumChildItems(
  [in]  const GUID          *pCategoryGUID,
  [out]       IEnumWiaItem2 **ppIEnumWiaItem2
);
```



## Parameters

<dl> <dt>

*pCategoryGUID* \[in\]
</dt> <dd>

Type: **const GUID\***

Specifies a pointer to a category for which child nodes are enumerated. If **NULL**, then all child nodes are enumerated.

</dd> <dt>

*ppIEnumWiaItem2* \[out\]
</dt> <dd>

Type: **[**IEnumWiaItem2**](-wia-ienumwiaitem2.md)\*\***

Receives the address of a pointer to the [**IEnumWiaItem2**](-wia-ienumwiaitem2.md) interface that this method creates.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The WIA 2.0 run-time system represents each WIA 2.0 hardware device as a hierarchical tree of [**IWiaItem2**](-wia-iwiaitem2.md) objects. The **IWiaItem2::EnumChildItems** method enables applications to enumerate child items in the current item. However, it can only be applied to items that are folders.

If the folder is not empty, it contains a subtree of [**IWiaItem2**](-wia-iwiaitem2.md) objects. The **IWiaItem2::EnumChildItems** method enumerates all of the items contained in the folder. It stores a pointer to an enumerator in the *ppIEnumWiaItem2* parameter. Applications use the enumerator pointer to perform the enumeration of an object's child items.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers they receive through the *ppIEnumWiaItem2* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
