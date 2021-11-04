---
title: IMsRdpDeviceCollection DeviceCount property
description: Retrieves the count of objects in the collection. | IMsRdpDeviceCollection DeviceCount property
ms.assetid: dc44f3b8-52c4-4e5f-a633-ea7555fd01dd
ms.tgt_platform: multiple
keywords:
- DeviceCount property Remote Desktop Services
- DeviceCount property Remote Desktop Services , IMsRdpDeviceCollection interface
- IMsRdpDeviceCollection interface Remote Desktop Services , DeviceCount property
topic_type:
- apiref
api_name:
- IMsRdpDeviceCollection.DeviceCount
- IMsRdpDeviceCollection.get_DeviceCount
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceCollection::DeviceCount property

Retrieves the count of objects in the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_DeviceCount(
  [out] ULONG *pDeviceCount
);
```



## Property value

The object count.

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

 

 





