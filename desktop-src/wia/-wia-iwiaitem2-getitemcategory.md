---
description: Gets an item's category information.
ms.assetid: 4d6f7a6a-280d-4b36-8e1d-8d9fcaa8a1de
title: IWiaItem2::GetItemCategory method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.GetItemCategory
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::GetItemCategory method

Gets an item's category information.

## Syntax


```C++
HRESULT GetItemCategory(
  [out] GUID *pItemCategoryGUID
);
```



## Parameters

<dl> <dt>

*pItemCategoryGUID* \[out\]
</dt> <dd>

Type: **GUID\***

Receives a pointer to the GUID that identifies the category of the item.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Every [**IWiaItem2**](-wia-iwiaitem2.md) object in the hierarchical tree of objects associated with a Windows Image Acquisition (WIA) 2.0 hardware device has a specific category. This method enables applications to identify the category of any item in a hierarchical tree of item objects in a device.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




