---
title: IRdsCursorRedirector OnCursorChanged method
description: Called when the cursor changes on a remote machine.
ms.tgt_platform: multiple
keywords:
- IRdsCursorRedirector OnCursorChanged method
topic_type:
- apiref
api_name:
- IRdsCursorRedirector.OnCursorChanged
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 10/24/2025
---

# IRdsCursorRedirector::OnCursorChanged method

This is a callback defined by an app hosting a Remote Desktop control, which is called when the cursor on the remote session changes.


## Syntax

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


## Parameters

*hCursor* \[in\]

Type: **BYTE***

A handle to a cursor that contains the image of the cursor from the remote session.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client| Windows 8                                                                 |
| Minimum supported server | Windows Server 2012                                                       |
| Type library             |MsTscAx.dll |
| DLL                      |MsTscAx.dll |
| IID                      | IID\_IMsRdpClient8 is defined as 4247E044-9271-43A9-BC49-E2AD9E855D62      |

## See also

[**IRdsCursorRedirector**](irdscursorredirector.md)
