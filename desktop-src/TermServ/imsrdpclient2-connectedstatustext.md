---
title: IMsRdpClient2 ConnectedStatusText property
description: Contains the text that is displayed in the client area of the control while the control is in the connected state.
ms.assetid: c3d8433b-2fb0-413d-88a3-667149f858ba
ms.tgt_platform: multiple
keywords:
- ConnectedStatusText property Remote Desktop Services
- ConnectedStatusText property Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , ConnectedStatusText property
- ConnectedStatusText property Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , ConnectedStatusText property
- ConnectedStatusText property Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , ConnectedStatusText property
- ConnectedStatusText property Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , ConnectedStatusText property
- ConnectedStatusText property Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , ConnectedStatusText property
- ConnectedStatusText property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , ConnectedStatusText property
- ConnectedStatusText property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , ConnectedStatusText property
- ConnectedStatusText property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , ConnectedStatusText property
- ConnectedStatusText property Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , ConnectedStatusText property
topic_type:
- apiref
api_name:
- IMsRdpClient2.ConnectedStatusText
- IMsRdpClient2.get_ConnectedStatusText
- IMsRdpClient2.put_ConnectedStatusText
- IMsRdpClient3.ConnectedStatusText
- IMsRdpClient3.get_ConnectedStatusText
- IMsRdpClient3.put_ConnectedStatusText
- IMsRdpClient4.ConnectedStatusText
- IMsRdpClient4.get_ConnectedStatusText
- IMsRdpClient4.put_ConnectedStatusText
- IMsRdpClient5.ConnectedStatusText
- IMsRdpClient5.get_ConnectedStatusText
- IMsRdpClient5.put_ConnectedStatusText
- IMsRdpClient6.ConnectedStatusText
- IMsRdpClient6.get_ConnectedStatusText
- IMsRdpClient6.put_ConnectedStatusText
- IMsRdpClient7.ConnectedStatusText
- IMsRdpClient7.get_ConnectedStatusText
- IMsRdpClient7.put_ConnectedStatusText
- IMsRdpClient8.ConnectedStatusText
- IMsRdpClient8.get_ConnectedStatusText
- IMsRdpClient8.put_ConnectedStatusText
- IMsRdpClient9.ConnectedStatusText
- IMsRdpClient9.get_ConnectedStatusText
- IMsRdpClient9.put_ConnectedStatusText
- IMsRdpClient10.ConnectedStatusText
- IMsRdpClient10.get_ConnectedStatusText
- IMsRdpClient10.put_ConnectedStatusText
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient2::ConnectedStatusText property

Contains the text that is displayed in the client area of the control while the control is in the connected state.

This property is read/write.

## Syntax


```C++
HRESULT put_ConnectedStatusText(
  [in]  BSTR newVal
);

HRESULT get_ConnectedStatusText(
  [out] BSTR *pConnectedStatusText
);
```



## Property value

The **ConnectedStatusText** property contains the text that is displayed in the client area of the control while the control is in the connected state.

## Error codes

Return **S\_OK** if successful.

## Remarks

Text to display in the client area of the control while the control is in the connected state. This is the text that is visible, for example, when the user switches the control to the full-screen mode in a web browser, a scenario that leaves a portion of the control hosted in the browser.

The **get\_ConnectedStatusText** method allocates the memory required for the buffer pointed to by the *pConnectedStatusText* parameter. Calling C/C++ applications must free the memory with a call to the [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) function. This is not required for Visual Basic and scripting clients.

This property cannot be set when the control is connected. You can check if the control is connected by calling the [**IMsTscAx::get\_Connected**](imstscax-connected.md) method.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClient2 is defined as e7e17dc4-3b71-4ba7-a8e6-281ffadca28f<br/>       |



## See also

<dl> <dt>

[**IMsRdpClient2**](imsrdpclient2.md)
</dt> <dt>

[**IMsRdpClient3**](imsrdpclient3.md)
</dt> <dt>

[**IMsRdpClient4**](imsrdpclient4.md)
</dt> <dt>

[**IMsRdpClient5**](imsrdpclient5.md)
</dt> <dt>

[**IMsRdpClient6**](imsrdpclient6.md)
</dt> <dt>

[**IMsRdpClient7**](imsrdpclient7.md)
</dt> <dt>

[**IMsRdpClient8**](imsrdpclient8.md)
</dt> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> <dt>

[**IMsRdpClient10**](imsrdpclient10.md)
</dt> </dl>

 

