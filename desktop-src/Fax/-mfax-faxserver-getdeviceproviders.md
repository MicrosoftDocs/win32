---
Description: The GetDeviceProviders method creates a FaxDeviceProviders object, a collection of fax service providers (FSPs) that are currently registered with the fax service.
ms.assetid: 073dea86-f8c5-42f6-a50d-f06a55d791ef
title: FaxServer.GetDeviceProviders method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.GetDeviceProviders method

The **GetDeviceProviders** method creates a [**FaxDeviceProviders**](-mfax-faxdeviceproviders.md) object, a collection of fax service providers (FSPs) that are currently registered with the fax service. You can use the **FaxDeviceProviders** object to enumerate the FSPs associated with a fax server and to create and access [**FaxDeviceProvider**](-mfax-faxdeviceprovider.md) objects for them.

## Syntax


```VB
FaxServer.GetDeviceProviders() As FaxDeviceProviders
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FaxDeviceProviders**](-mfax-faxdeviceproviders.md)\*\***

A [**FaxDeviceProviders**](-mfax-faxdeviceproviders.md) object.

## Remarks

To use this method, a user must have the [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver?branch=master)
</dt> </dl>

 

 




