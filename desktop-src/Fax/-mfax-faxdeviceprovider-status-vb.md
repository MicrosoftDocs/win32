---
Description: The Status property is a number that indicates whether the fax service provider (FSP) loaded and initialized successfully.
ms.assetid: c46c6123-da27-4a43-a2e6-cf451ecfdf83
title: FaxDeviceProvider.Status property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDeviceProvider.Status property

The [**Status**](/windows/previous-versions/FaxComex/nf-faxcomex-ifaxdeviceprovider-get_status?branch=master) property is a number that indicates whether the fax service provider (FSP) loaded and initialized successfully.

This property is read-only.

## Syntax


```VB
Property Status As Integer
```



## Property value

Receives a value from the [**FAX\_PROVIDER\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_provider_status_enum?branch=master) enumeration.

## Remarks

If the FSP did not load successfully, the property indicates the reason for the failure, and [**InitErrorCode**](-mfax-faxdeviceprovider-initerrorcode-vb.md) holds the last error code value. For more information, see [**FAX\_PROVIDER\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_provider_status_enum?branch=master).

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

[**IFaxDeviceProvider**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdeviceprovider?branch=master)
</dt> </dl>

 

 




