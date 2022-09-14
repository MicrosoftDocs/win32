---
title: IMsTscAx SendOnVirtualChannel method
description: Sends data to the Remote Desktop Session Host (RD Session Host) server over a virtual channel that was created previously by using the CreateVirtualChannels method.
ms.assetid: 795ef508-bdf7-4897-84b1-931615262293
ms.tgt_platform: multiple
keywords:
- SendOnVirtualChannel method Remote Desktop Services
- SendOnVirtualChannel method Remote Desktop Services , IMsTscAx interface
- IMsTscAx interface Remote Desktop Services , SendOnVirtualChannel method
- SendOnVirtualChannel method Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , SendOnVirtualChannel method
- SendOnVirtualChannel method Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , SendOnVirtualChannel method
- SendOnVirtualChannel method Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , SendOnVirtualChannel method
- SendOnVirtualChannel method Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , SendOnVirtualChannel method
- SendOnVirtualChannel method Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , SendOnVirtualChannel method
- SendOnVirtualChannel method Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , SendOnVirtualChannel method
- SendOnVirtualChannel method Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , SendOnVirtualChannel method
- SendOnVirtualChannel method Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , SendOnVirtualChannel method
- SendOnVirtualChannel method Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , SendOnVirtualChannel method
topic_type:
- apiref
api_name:
- IMsTscAx.SendOnVirtualChannel
- IMsRdpClient.SendOnVirtualChannel
- IMsRdpClient2.SendOnVirtualChannel
- IMsRdpClient3.SendOnVirtualChannel
- IMsRdpClient4.SendOnVirtualChannel
- IMsRdpClient5.SendOnVirtualChannel
- IMsRdpClient6.SendOnVirtualChannel
- IMsRdpClient7.SendOnVirtualChannel
- IMsRdpClient8.SendOnVirtualChannel
- IMsRdpClient9.SendOnVirtualChannel
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAx::SendOnVirtualChannel method

Sends data to the Remote Desktop Session Host (RD Session Host) server over a virtual channel that was created previously by using the [**CreateVirtualChannels**](imstscax-createvirtualchannels.md) method.

## Syntax


```C++
HRESULT SendOnVirtualChannel(
  [in] BSTR ChanName,
  [in] BSTR ChanData
);
```



## Parameters

<dl> <dt>

*ChanName* \[in\]
</dt> <dd>

The virtual channel name that was specified in the call to [**CreateVirtualChannels**](imstscax-createvirtualchannels.md).

</dd> <dt>

*ChanData* \[in\]
</dt> <dd>

The data to send over the virtual channel, in **BSTR** form. There is no restriction that this data must be null-terminated strings.

</dd> </dl>

## Return value

Return **S\_OK** if successful.

## Remarks

Refer to [Virtual Channel Client Registration](virtual-channel-client-registration.md) for information about virtual channel naming restrictions.

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

[**CreateVirtualChannels**](imstscax-createvirtualchannels.md)
</dt> <dt>

[**IMsTscAx**](imstscax-interface.md)
</dt> </dl>

 

 





