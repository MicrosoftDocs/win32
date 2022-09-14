---
title: IMsTscAx Domain property
description: Specifies the domain to which the current user logs on.
ms.assetid: 5d9a2048-5f5d-43ca-a8b8-400dac7d7472
ms.tgt_platform: multiple
keywords:
- Domain property Remote Desktop Services
- Domain property Remote Desktop Services , IMsTscAx interface
- IMsTscAx interface Remote Desktop Services , Domain property
- Domain property Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , Domain property
- Domain property Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , Domain property
- Domain property Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , Domain property
- Domain property Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , Domain property
- Domain property Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , Domain property
- Domain property Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , Domain property
- Domain property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , Domain property
- Domain property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , Domain property
- Domain property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , Domain property
topic_type:
- apiref
api_name:
- IMsTscAx.Domain
- IMsTscAx.get_Domain
- IMsTscAx.put_Domain
- IMsRdpClient.Domain
- IMsRdpClient.get_Domain
- IMsRdpClient.put_Domain
- IMsRdpClient2.Domain
- IMsRdpClient2.get_Domain
- IMsRdpClient2.put_Domain
- IMsRdpClient3.Domain
- IMsRdpClient3.get_Domain
- IMsRdpClient3.put_Domain
- IMsRdpClient4.Domain
- IMsRdpClient4.get_Domain
- IMsRdpClient4.put_Domain
- IMsRdpClient5.Domain
- IMsRdpClient5.get_Domain
- IMsRdpClient5.put_Domain
- IMsRdpClient6.Domain
- IMsRdpClient6.get_Domain
- IMsRdpClient6.put_Domain
- IMsRdpClient7.Domain
- IMsRdpClient7.get_Domain
- IMsRdpClient7.put_Domain
- IMsRdpClient8.Domain
- IMsRdpClient8.get_Domain
- IMsRdpClient8.put_Domain
- IMsRdpClient9.Domain
- IMsRdpClient9.get_Domain
- IMsRdpClient9.put_Domain
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAx::Domain property

Specifies the domain to which the current user logs on.

This property is read/write.

## Syntax


```C++
HRESULT put_Domain(
  [in]  BSTR newVal
);

HRESULT get_Domain(
  [out] BSTR *pDomain
);
```



## Property value

The new domain name.

## Error codes

Return **S\_OK** if successful.

## Remarks

Setting the **Domain** property is optional. If it is not set, the user can choose a domain when the Windows Logon dialog box appears during the connection.

The **get\_Domain** method allocates the memory required for the buffer pointed to by the *pDomain* parameter. Calling C/C++ applications must free the memory with a call to the [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) function. This is not required for Visual Basic and scripting clients.

This property can be set only if the control is not in the connected state. It returns **E\_FAIL** if it is called when the control is connected. You can check if the control is connected by responding to connection events in [**IMsTscAxEvents**](imstscaxevents-interface.md) or examining the [**Connected**](imstscax-connected.md) property.

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

[**Connected**](imstscax-connected.md)
</dt> <dt>

[**IMsTscAx**](imstscax-interface.md)
</dt> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

