---
title: IMsRdpClient7 GetStatusText method (Openservice.h)
description: Retrieves the status text for the specified status code.
ms.assetid: 1da2280a-c26d-4caa-b227-c289055f3aa9
ms.tgt_platform: multiple
keywords:
- GetStatusText method Remote Desktop Services
- GetStatusText method Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , GetStatusText method
- GetStatusText method Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , GetStatusText method
- GetStatusText method Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , GetStatusText method
- GetStatusText method Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , GetStatusText method
topic_type:
- apiref
api_name:
- IMsRdpClient7.GetStatusText
- IMsRdpClient8.GetStatusText
- IMsRdpClient9.GetStatusText
- IMsRdpClient10.GetStatusText
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient7::GetStatusText method

Retrieves the status text for the specified status code.

## Syntax


```C++
HRESULT GetStatusText(
  [in]          UINT statusCode,
  [out, retval] BSTR *pBstrStatusText
);
```



## Parameters

<dl> <dt>

*statusCode* \[in\]
</dt> <dd>

A **UINT** that specifies the status code to retrieve the text for.

</dd> <dt>

*pBstrStatusText* \[out, retval\]
</dt> <dd>

The address of a **BSTR** that receives the status text.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                        |
| Header<br/>                   | <dl> <dt>Openservice.h</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| IID<br/>                      | IID\_IMsRdpClient7 is defined as b2a5b5ce-3461-444a-91d4-add26d070638<br/>         |



## See also

<dl> <dt>

[**IMsRdpClient7**](imsrdpclient7.md)
</dt> <dt>

[**IMsRdpClient8**](imsrdpclient8.md)
</dt> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> <dt>

[**IMsRdpClient10**](imsrdpclient10.md)
</dt> </dl>

 

 





