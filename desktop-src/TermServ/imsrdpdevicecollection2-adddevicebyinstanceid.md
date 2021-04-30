---
title: IMsRdpDeviceCollection2 AddDeviceByInstanceId method
description: Adds an unlisted device to the device collection.
ms.assetid: 7ef200c5-b99e-40c9-80e1-0758ddfa0902
ms.tgt_platform: multiple
keywords:
- AddDeviceByInstanceId method Remote Desktop Services
- AddDeviceByInstanceId method Remote Desktop Services , IMsRdpDeviceCollection2 interface
- IMsRdpDeviceCollection2 interface Remote Desktop Services , AddDeviceByInstanceId method
topic_type:
- apiref
api_name:
- IMsRdpDeviceCollection2.AddDeviceByInstanceId
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceCollection2::AddDeviceByInstanceId method

Adds an unlisted device to the device collection.

## Syntax


```C++
HRESULT AddDeviceByInstanceId(
  [in] RedirectDeviceType Type,
  [in] BSTR               InstanceId
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

Type: **[**RedirectDeviceType**](redirectdevicetype.md)**

A value of the [**RedirectDeviceType**](redirectdevicetype.md) enumeration that specifies the type of device being added.

</dd> <dt>

*InstanceId* \[in\]
</dt> <dd>

Type: **BSTR**

The instance identifier of the device to add.

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



## See also

<dl> <dt>

[**RedirectDeviceType**](redirectdevicetype.md)
</dt> <dt>

[**IMsRdpDeviceCollection2**](imsrdpdevicecollection2.md)
</dt> </dl>

 

 





