---
title: IRdsCursorRedirector OnCursorChanged method
description: Called when the cursor image in the remote session changesms.assetid: A2C4101D-780A-4973-B87C-025D9140C4BC
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
ms.date: 09/30/2025
---

# IRdsCursorRedirector::OnCursorChanged method

Called when the cursor image on the remote session changes.

## Syntax


```C++
    HRESULT STDMETHODCALLTYPE OnCursorChanged(HCURSOR hCursor);
```


## Parameters

<dl> <dt>
*hCursor* \[in\]
</dt> <dd>

Type: **BYTE***

A handle to a cursor that contains the image of the cursor from the remote session.
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

