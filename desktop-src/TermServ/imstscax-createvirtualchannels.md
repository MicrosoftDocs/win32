---
title: IMsTscAx CreateVirtualChannels method
description: Creates a client-side virtual channel object for each specified virtual channel name.
ms.assetid: 3afd2f1c-abd5-4f85-93fb-6d1173f09b07
ms.tgt_platform: multiple
keywords:
- CreateVirtualChannels method Remote Desktop Services
- CreateVirtualChannels method Remote Desktop Services , IMsTscAx interface
- IMsTscAx interface Remote Desktop Services , CreateVirtualChannels method
- CreateVirtualChannels method Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , CreateVirtualChannels method
- CreateVirtualChannels method Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , CreateVirtualChannels method
- CreateVirtualChannels method Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , CreateVirtualChannels method
- CreateVirtualChannels method Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , CreateVirtualChannels method
- CreateVirtualChannels method Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , CreateVirtualChannels method
- CreateVirtualChannels method Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , CreateVirtualChannels method
- CreateVirtualChannels method Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , CreateVirtualChannels method
- CreateVirtualChannels method Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , CreateVirtualChannels method
- CreateVirtualChannels method Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , CreateVirtualChannels method
topic_type:
- apiref
api_name:
- IMsTscAx.CreateVirtualChannels
- IMsRdpClient.CreateVirtualChannels
- IMsRdpClient2.CreateVirtualChannels
- IMsRdpClient3.CreateVirtualChannels
- IMsRdpClient4.CreateVirtualChannels
- IMsRdpClient5.CreateVirtualChannels
- IMsRdpClient6.CreateVirtualChannels
- IMsRdpClient7.CreateVirtualChannels
- IMsRdpClient8.CreateVirtualChannels
- IMsRdpClient9.CreateVirtualChannels
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAx::CreateVirtualChannels method

Creates a client-side virtual channel object for each specified virtual channel name.

## Syntax


```C++
HRESULT CreateVirtualChannels(
  [in] BSTR newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

A comma-separated list of valid virtual channel names. The length of each name in this list can be a minimum of one and a maximum of seven alphabetical characters. The length of the entire string can be a minimum of one and a maximum of 300 alphabetical characters.

</dd> </dl>

## Return value

Returns **S\_OK** if successful. Returns **E\_INVALIDARG** if the parameter that is passed does not meet the criteria that is specified.

## Remarks

Call this method before calling the [**Connect**](imstscax-connect.md) method.

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

[**IMsTscAx**](imstscax-interface.md)
</dt> </dl>

 

 





