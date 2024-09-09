---
title: IMsRdpClient SetVirtualChannelOptions method
description: Sets the virtual channel options for the Remote Desktop ActiveX control.
ms.assetid: c74c3917-5766-4d5b-8458-b051eb91cb28
ms.tgt_platform: multiple
keywords:
- SetVirtualChannelOptions method Remote Desktop Services
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , SetVirtualChannelOptions method
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , SetVirtualChannelOptions method
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , SetVirtualChannelOptions method
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , SetVirtualChannelOptions method
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , SetVirtualChannelOptions method
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , SetVirtualChannelOptions method
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , SetVirtualChannelOptions method
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , SetVirtualChannelOptions method
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , SetVirtualChannelOptions method
- SetVirtualChannelOptions method Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , SetVirtualChannelOptions method
topic_type:
- apiref
api_name:
- IMsRdpClient.SetVirtualChannelOptions
- IMsRdpClient2.SetVirtualChannelOptions
- IMsRdpClient3.SetVirtualChannelOptions
- IMsRdpClient4.SetVirtualChannelOptions
- IMsRdpClient5.SetVirtualChannelOptions
- IMsRdpClient6.SetVirtualChannelOptions
- IMsRdpClient7.SetVirtualChannelOptions
- IMsRdpClient8.SetVirtualChannelOptions
- IMsRdpClient9.SetVirtualChannelOptions
- IMsRdpClient10.SetVirtualChannelOptions
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient::SetVirtualChannelOptions method

Sets the virtual channel options for the Remote Desktop ActiveX control.

Call this method after calling the [**CreateVirtualChannels**](imstscax-createvirtualchannels.md) method, but before establishing a connection with the [**Connect**](imstscax-connect.md) method. This method sets additional options on virtual channels that have been created with **CreateVirtualChannels**.

## Syntax


```C++
HRESULT SetVirtualChannelOptions(
  [in] BSTR ChanName,
  [in] LONG chanOptions
);
```



## Parameters

<dl> <dt>

*ChanName* \[in\]
</dt> <dd>

The name of the virtual channel that was specified in the call to the [**CreateVirtualChannels**](imstscax-createvirtualchannels.md) method.

</dd> <dt>

*chanOptions* \[in\]
</dt> <dd>

The options to set for the virtual channel specified by the *ChanName* parameter. For a description of possible options, see [**CHANNEL\_DEF**](/previous-versions/windows/embedded/aa513856(v=msdn.10)). For more information, see the following Remarks section.

</dd> </dl>

## Return value

Return **S\_OK** if successful.

## Remarks

An example of using this method would be to declare the channel as remote control persistent by setting the **CHANNEL\_OPTION\_REMOTE\_CONTROL\_PERSISTENT** flag. This means that the channel would not be closed when a remote control connects to or disconnects from the session connected to the client. For more information, see [Remote Control Persistent Virtual Channels](remote-control-persistent-virtual-channels.md).

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClient is defined as 92b4a539-7115-4b7c-a5a9-e5d9efc2780a<br/>        |



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

[**IMsRdpClient10**](imsrdpclient10.md)
</dt> <dt>

[**CHANNEL\_DEF**](/previous-versions/windows/embedded/aa513856(v=msdn.10))
</dt> <dt>

[**CreateVirtualChannels**](imstscax-createvirtualchannels.md)
</dt> <dt>

[**GetVirtualChannelOptions**](imsrdpclient-getvirtualchanneloptions.md)
</dt> </dl>

 

 





