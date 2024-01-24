---
description: Gets the Windows Image Acquisition (WIA) 2.0 preview component.
ms.assetid: 0b773c4c-f080-41fa-8902-4243a80fc67c
title: IWiaItem2::GetPreviewComponent method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaItem2.GetPreviewComponent
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaItem2::GetPreviewComponent method

Gets the Windows Image Acquisition (WIA) 2.0 preview component.

## Syntax


```C++
HRESULT GetPreviewComponent(
  [in]  LONG        lFlags,
  [out] IWiaPreview **ppWiaPreview
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Not used. Set to 0.

</dd> <dt>

*ppWiaPreview* \[out\]
</dt> <dd>

Type: **[**IWiaPreview**](-wia-iwiapreview.md)\*\***

Returns the address of a pointer to the [**IWiaPreview**](-wia-iwiapreview.md) interface of the preview component.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Use this function to return a pointer to the address of the WIA 2.0 preview component for any [**IWiaItem2**](-wia-iwiaitem2.md) object in the object tree of a WIA 2.0 hardware device.

Applications must call the [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) method on the interface pointers that they receive through the *ppWiaPreview* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWiaItem2**](-wia-iwiaitem2.md)
</dt> <dt>

[**IWiaPreview**](-wia-iwiapreview.md)
</dt> </dl>

 

 
