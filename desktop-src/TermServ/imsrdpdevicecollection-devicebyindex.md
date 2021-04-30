---
title: IMsRdpDeviceCollection DeviceByIndex property
description: Retrieves the device at the specified index.
ms.assetid: fcfc459b-46e1-4f26-a331-745fcf06638b
ms.tgt_platform: multiple
keywords:
- DeviceByIndex property Remote Desktop Services
- DeviceByIndex property Remote Desktop Services , IMsRdpDeviceCollection interface
- IMsRdpDeviceCollection interface Remote Desktop Services , DeviceByIndex property
topic_type:
- apiref
api_name:
- IMsRdpDeviceCollection.DeviceByIndex
- IMsRdpDeviceCollection.get_DeviceByIndex
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceCollection::DeviceByIndex property

Retrieves the device at the specified index.

This property is read-only.

## Syntax


```C++
HRESULT get_DeviceByIndex(
  [in]          ULONG index,
  [out, retval] IMsRdpDevice **ppDevice
);
```



## Property value

An [**IMsRdpDevice**](imsrdpdevice.md) interface pointer.

## Error codes

If the method succeeds, **S\_OK** is returned. Any other **HRESULT** value indicates that the call failed.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| IID<br/>                      | IID\_IMsRdpDeviceCollection is defined as 56540617-d281-488c-8738-6a8fdf64a118<br/> |



## See also

<dl> <dt>

[**IMsRdpDeviceCollection**](imsrdpdevicecollection.md)
</dt> </dl>

 

 





