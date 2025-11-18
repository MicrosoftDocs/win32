---
title: IRdsFbrPresenter interface
description: Remote Desktop interface to register for changes to pixels on the remote machine.
ms.assetid: 45192c4c-f827-45cf-b597-0671b4c5cfd3
ms.tgt_platform: multiple
keywords:
- IRdsFbrPresenter interface Remote Desktop Services
topic_type:
- apiref
api_name:
- IRdsFbrPresenter
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/30/2025
---


# IRdsFbrPresenter interface

Registers for a callback with a Remote Desktop client that is callled with a
raw bytes array when the content of the remote session changes.

This is created using the property string `"FrameBufferRedirectionPresenter"`
with [IMsRdpExtendedSettings](imsrdpextendedsettings.md),
[put_Property](imsrdpextendedsettings-property.md).


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


## Members

The **IRdsFbrPresenter** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface.


### Methods

| Method                                                               | Description                          |
|:---------------------------------------------------------------------|:-------------------------------------|
| [**Present**](irdsfbrpresenter-present.md)   | Called when frame buffer changes with updated byte array.<br/>  |


## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11<br/>                                                                 |
| Minimum supported server<br/> | <br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IRdsFbrPresenter is defined as 45192c4c-f827-45cf-b597-0671b4c5cfd3<br/>     |
