---
title: IMsRdpDeviceCollection RescanDevices method
description: Refreshes the list of objects in the collection. | IMsRdpDeviceCollection RescanDevices method
ms.assetid: 2e2a959d-0a1d-4aca-9daf-3c24fb9b3b08
ms.tgt_platform: multiple
keywords:
- RescanDevices method Remote Desktop Services
- RescanDevices method Remote Desktop Services , IMsRdpDeviceCollection interface
- IMsRdpDeviceCollection interface Remote Desktop Services , RescanDevices method
topic_type:
- apiref
api_name:
- IMsRdpDeviceCollection.RescanDevices
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceCollection::RescanDevices method

Refreshes the list of objects in the collection.

## Syntax


```C++
HRESULT RescanDevices(
  [in] VARIANT_BOOL vboolDynRedir
);
```



## Parameters

<dl> <dt>

*vboolDynRedir* \[in\]
</dt> <dd>

The default redirection state that will be applied to any newly discovered devices or drives.

</dd> </dl>

## Return value

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

 

 





