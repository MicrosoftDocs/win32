---
Description: The Item property returns a FaxDeviceProvider object from the FaxDeviceProviders collection.
ms.assetid: aafe3cf4-43d9-4ae8-87a8-4ee7e0af5cc3
title: FaxDeviceProviders.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDeviceProviders.Item property

The **Item** property returns a [**FaxDeviceProvider**](-mfax-faxdeviceprovider.md) object from the [**FaxDeviceProviders**](-mfax-faxdeviceproviders.md) collection.

This property is read/write.

## Syntax


```VB
Property Item( _
  ByVal vIndex As Variant _
) As IFaxDeviceProvider
```



## Property value

A variable of type [**IFaxDeviceProvider**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdeviceprovider) that specifies or receives a [**FaxDeviceProvider**](-mfax-faxdeviceprovider.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxDeviceProviders**](-mfax-faxdeviceproviders.md)
</dt> <dt>

[Visual Basic Example](-mfax-managing-fax-device-providers.md)
</dt> <dt>

[**FaxDeviceProvider**](-mfax-faxdeviceprovider.md)
</dt> <dt>

[**IFaxDeviceProvider**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdeviceprovider)
</dt> </dl>

 

 




