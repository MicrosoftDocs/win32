---
title: IVMUSBDeviceCollection Item property (VPCCOMInterfaces.h)
description: Retrieves the USB device object that corresponds to the specified index.
ms.assetid: 664a038e-7c86-43a9-a376-c913d431dc93
keywords:
- Item property Virtual PC
- Item property Virtual PC , IVMUSBDeviceCollection interface
- IVMUSBDeviceCollection interface Virtual PC , Item property
topic_type:
- apiref
api_name:
- IVMUSBDeviceCollection.Item
- IVMUSBDeviceCollection.get_Item
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMUSBDeviceCollection::Item property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the USB device object that corresponds to the specified index.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]          long         index,
  [out, retval] IVMUSBDevice **usbDevice
);
```



## Property value

The [**IVMUSBDevice**](ivmusbdevice.md) object.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful. <br/>                                                      |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The *usbDevice* parameter is **NULL**. <br/>                                             |
| <dl> <dt>DISP\_E\_BADINDEX</dt> <dt>0x8002000B</dt> </dl>  | The index of the requested item does not correspond to an item in this collection. <br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                                                   |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMUSBDeviceCollection is defined as 4FBCD6A5-F53C-4d1c-9F4D-E90ABB8B3749<br/>     |



## See also

<dl> <dt>

[**IVMUSBDevice**](ivmusbdevice.md)
</dt> <dt>

[**IVMUSBDeviceCollection**](ivmusbdevicecollection.md)
</dt> </dl>

 

