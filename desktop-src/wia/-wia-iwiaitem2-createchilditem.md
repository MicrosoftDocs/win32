---
description: Create a new child item. Adds IWiaItem2 objects to a device's IWiaItem2 tree.
ms.assetid: 525ee788-3ff4-4def-ae71-4a405c04c6a3
title: IWiaItem2::CreateChildItem method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.CreateChildItem
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::CreateChildItem method

Create a new child item. Adds [**IWiaItem2**](-wia-iwiaitem2.md) objects to a device's **IWiaItem2** tree.

## Syntax


```C++
HRESULT CreateChildItem(
  [in]  LONG      lItemFlags,
  [in]  LONG      lCreationFlags,
  [in]  BSTR      bstrItemName,
  [out] IWiaItem2 **ppIWiaItem2
);
```



## Parameters

<dl> <dt>

*lItemFlags* \[in\]
</dt> <dd>

Type: **LONG**

Specifies the WIA 2.0 item type. See [**WIA Item Type Flags**](-wia-wia-item-type-flags.md).

</dd> <dt>

*lCreationFlags* \[in\]
</dt> <dd>

Type: **LONG**

Specifies how to create the new item.

<dt>

<span id="0"></span>

<span id="0"></span>**0** (0)


</dt> <dd>

Set the default values for the properties of the child.

</dd> <dt>

<span id="COPY_PARENT_PROPERTY_VALUES"></span><span id="copy_parent_property_values"></span>

<span id="COPY_PARENT_PROPERTY_VALUES"></span><span id="copy_parent_property_values"></span>**COPY\_PARENT\_PROPERTY\_VALUES** (0x40000000)


</dt> <dd>

Copy the values of all Read/Write properties from the parent.

</dd> </dl> </dd> <dt>

*bstrItemName* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the item name. This name is appended to the end of the parent item's name to generate the full item name.

</dd> <dt>

*ppIWiaItem2* \[out\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\*\***

Receives the address of a pointer to the [**IWiaItem2**](-wia-iwiaitem2.md) interface that sets the **IWiaItem2::CreateChildItem** method.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Some WIA 2.0 hardware devices allow applications to create new items in the [**IWiaItem2**](-wia-iwiaitem2.md) tree that represents the device. Applications must test the devices to see if they support this capability. Use the IEnumWIA\_DEV\_CAPS interface to enumerate the current device's capabilities.

If the device allows the creation of new items in the [**IWiaItem2**](-wia-iwiaitem2.md) tree, invoking **IWiaItem2::CreateChildItem** creates a new **IWiaItem2** object that is a child of the current node. It passes a pointer to the new node to the application through the *ppIWiaItem2* parameter. Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers they receive through the *ppIWiaItem2* parameter.

If *lCreationFlags* is COPY\_PARENT\_PROPERTY\_VALUES and *lItemFlags* is zero, the function returns E\_INVALIDARG.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
