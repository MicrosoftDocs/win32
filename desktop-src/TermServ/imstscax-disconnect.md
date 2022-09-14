---
title: IMsTscAx Disconnect method
description: Disconnects the active connection.
ms.assetid: 9fcffd45-b293-4650-be8f-1b0d01d592a2
ms.tgt_platform: multiple
keywords:
- Disconnect method Remote Desktop Services
- Disconnect method Remote Desktop Services , IMsTscAx interface
- IMsTscAx interface Remote Desktop Services , Disconnect method
- Disconnect method Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , Disconnect method
- Disconnect method Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , Disconnect method
- Disconnect method Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , Disconnect method
- Disconnect method Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , Disconnect method
- Disconnect method Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , Disconnect method
- Disconnect method Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , Disconnect method
- Disconnect method Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , Disconnect method
- Disconnect method Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , Disconnect method
- Disconnect method Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , Disconnect method
topic_type:
- apiref
api_name:
- IMsTscAx.Disconnect
- IMsRdpClient.Disconnect
- IMsRdpClient2.Disconnect
- IMsRdpClient3.Disconnect
- IMsRdpClient4.Disconnect
- IMsRdpClient5.Disconnect
- IMsRdpClient6.Disconnect
- IMsRdpClient7.Disconnect
- IMsRdpClient8.Disconnect
- IMsRdpClient9.Disconnect
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAx::Disconnect method

Disconnects the active connection.

## Syntax


```C++
HRESULT Disconnect();
```



## Parameters

This method has no parameters.

## Return value

Return **S\_OK** if successful.

## Remarks

This method returns a failure error value if it is called when the control is not connected.

It is also possible to disconnect the control by closing its main window. For example, if the control is hosted in a webpage, it is not necessary to call this method before leaving the page; the closing of the control triggers a disconnection.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsTscAx is defined as 8C11EFAE-92C3-11D1-BC1E-00C04FA31489<br/>            |



## See also

<dl> <dt>

[**IMsRdpClient**](imsrdpclient-interface.md)
</dt> <dt>

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

[**Connect**](imstscax-connect.md)
</dt> <dt>

[**IMsTscAx**](imstscax-interface.md)
</dt> </dl>

 

 





