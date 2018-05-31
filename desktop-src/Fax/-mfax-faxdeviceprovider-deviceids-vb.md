---
Description: The DeviceIds property returns a variant safe array of long (VT\_I4 \| VT\_ARRAY). Each long value in the array is a device ID.
ms.assetid: 6b9f70f5-25fc-43cf-84b2-60801c45b6e8
title: FaxDeviceProvider.DeviceIds property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDeviceProvider.DeviceIds property

The **DeviceIds** property returns a variant safe array of long (VT\_I4 \| VT\_ARRAY). Each long value in the array is a device ID.

This property is read-only.

## Syntax


```VB
Property DeviceIds As Variant
```



## Property value

A **Variant** that receives an array of device IDs.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-fax-device-providers.md)
</dt> <dt>

[**FaxDeviceProvider**](-mfax-faxdeviceprovider.md)
</dt> <dt>

[**IFaxDeviceProvider**](-mfax-faxdeviceprovider-cpp.md)
</dt> </dl>

 

 




