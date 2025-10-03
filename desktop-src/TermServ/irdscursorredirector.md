---
title: IRdsCursorRedirector interface
description: Remote desktop cursor image changed presenter.
ms.assetid: 54ee23c4-8d8b-4911-9f24-db0d4ac1fec4
ms.tgt_platform: multiple
keywords:
- IRdsCursorRedirector interface Remote Desktop Services
topic_type:
- apiref
api_name:
- IRdsCursorRedirector
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/31/2025
---

# IRdsCursorRedirector interface

This registers for a callback with a Remote Desktop client that receives a
callback when the cursor on the remote session changes.

This is created using the property string `"CursorRedirector"` with
[IMsRdpExtendedSettings](imsrdpextendedsettings.md),
[put_Property](imsrdpextendedsettings-property.md).

```idl
cpp_quote("EXTERN_C __declspec(selectany) const IID IID_IRdsCursorRedirector = {0x54ee23c4, 0x8d8b, 0x4911, {0x9f, 0x24, 0xdb, 0x0d, 0x4a, 0xc1, 0xfe, 0xc4}};")
[
    object,
    uuid(54ee23c4-8d8b-4911-9f24-db0d4ac1fec4),
    pointer_default(unique)
]
interface IRdsCursorRedirector: IUnknown
{
    HRESULT OnCursorChanged([in] HCURSOR hCursor);
};
```


### Methods

| Method                                                               | Description                          |
|:---------------------------------------------------------------------|:-------------------------------------|
| [**OnCursorChanged**](irdscursorredirector-oncursorchanged.md)  | Called when frame buffer changes with updated byte array.<br/>  |


## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11<br/>                                                                 |
| Minimum supported server<br/> | <br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IRdsCursorRedirector is defined as 54ee23c4-8d8b-4911-9f24-db0d4ac1fec4<br/>     |


