---
description: Gets an item's type information.
ms.assetid: 9670f184-e8ba-4596-af6d-2967320dfd95
title: IWiaItem2::GetItemType method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.GetItemType
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::GetItemType method

Gets an item's type information.

## Syntax


```C++
HRESULT GetItemType(
  [out] LONG *pItemType
);
```



## Parameters

<dl> <dt>

*pItemType* \[out\]
</dt> <dd>

Type: **LONG\***

Receives a pointer to a **LONG** that contains a combination of type flags. See [**WIA Item Type Flags**](-wia-wia-item-type-flags.md).

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Every [**IWiaItem2**](-wia-iwiaitem2.md) object in the hierarchical tree of objects associated with a Windows Image Acquisition (WIA) 2.0 hardware device has a specific data type. Item objects represent folders and files. Folders contain file objects. File objects contain data acquired by the device such as images and sounds. This method enables applications to identify the type of any item in a hierarchical tree of item objects in a device.

An item may have more than one type. For example, an item that represents an audio file will have the type attributes [**WiaItemTypeAudio**](-wia-wia-item-type-flags.md) \| **WiaItemTypeFile**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




