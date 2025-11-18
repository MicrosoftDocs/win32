---
title: IRdsFbrPresenter Present method
description: Called when the bytes of the frame buffer have changed
ms.assetid: A2C4101D-780A-4973-B87C-025D9140C4BC
ms.tgt_platform: multiple
keywords:
- IRdsFbrPresenter present method
topic_type:
- apiref
api_name:
- IRdsFbrPresenter.Present
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/30/2025
---


# IRdsFbrPresenter::Present method

Called when the frame buffer for the Remote Desktop control have changed.


## Syntax

```idl
cpp_quote("EXTERN_C __declspec(selectany) const IID IID_IRdsFbrPresenter = {0x45192c4c, 0xf827, 0x45cf, {0xb5, 0x97, 0x06, 0x71, 0xb4, 0xc5, 0xcf, 0xd3}};")
[
    object,
    uuid(45192c4c-f827-45cf-b597-0671b4c5cfd3),
    pointer_default(unique)
]
interface IRdsFbrPresenter: IUnknown
{
    HRESULT Present(
        [in, size_is(cFrameBufferWidth * cFrameBufferHeight * (cColorDepth / 8))]
            const BYTE *pbFrameBuffer,
        [in] UINT cFrameBufferWidth,
        [in] UINT cFrameBufferHeight,
        [in] UINT cColorDepth,
        [in] const HRGN hRgnDirty
        );
};
```


## Parameters

<dl> <dt>
*pbFrameBuffer* \[in\]
</dt> <dd>

Type: **BYTE***

A pointer to the BYTE array containing the contents of the frame buffer.

</dd> <dt>
*cFrameBufferWidth* \[in\]
</dt> <dd>

Type: **UINT**

The width of the frame buffer.

</dd> <dt>
*cFrameBufferHeight* \[out, retval\]
</dt> <dd>

Type: **UINT**

The height of the frame buffer.

</dd> <dt>
*cColorDepth* \[out, retval\]
</dt> <dd>

Type: **UINT**

The color depth of the frame buffer.

</dd> <dt>
*hRgnDirty* \[out, retval\]
</dt> <dd>

Type: **HRGN**

A handle to a region containing the area of the frame buffer that changed.

</dd> </dl>


## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.


## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClient8 is defined as 4247E044-9271-43A9-BC49-E2AD9E855D62<br/>       |


## See also

<dl> <dt>

[**IRdsFbrPresenter**](irdsfbrpresenter.md)
</dt> <dt>
