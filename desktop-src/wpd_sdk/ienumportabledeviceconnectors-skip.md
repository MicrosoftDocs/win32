---
description: Skips the specified number of devices in the enumeration sequence.
ms.assetid: 38b72b80-93f5-433e-977c-e3ee503daae5
title: IEnumPortableDeviceConnectors::Skip method (Devpkey.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumPortableDeviceConnectors.Skip
api_type: 
- COM
api_location: 
- PortableDeviceGuids.lib
- PortableDeviceGuids.dll
---

# IEnumPortableDeviceConnectors::Skip method

The **Skip** method skips the specified number of devices in the enumeration sequence.

## Syntax


```C++
HRESULT Skip(
  [in] UINT32 cConnectors
);
```



## Parameters

<dl> <dt>

*cConnectors* \[in\]
</dt> <dd>

The number of devices to skip.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                             | Description                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The method succeeded.<br/>                                                                                                                                                          |
| <dl> <dt>**S\_FALSE**</dt> </dl> | The specified number of devices could not be skipped. One possible cause: The *cConnectors* parameter specifies more devices than actually remain in the enumeration sequence.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                                   |
| Header<br/>                   | <dl> <dt>Devpkey.h; </dt> <dt>Portabledeviceconnectapi.h</dt> </dl> |
| IDL<br/>                      | <dl> <dt>Portabledeviceconnectapi.idl</dt> </dl>                                                                |
| Library<br/>                  | <dl> <dt>PortableDeviceGuids.lib</dt> </dl>                                                                     |



## See also

<dl> <dt>

[**IEnumPortableDeviceConnectors**](ienumportabledeviceconnectors.md)
</dt> </dl>

 

 




