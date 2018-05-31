---
Description: The GetDevices method creates a FaxDevices object, a collection of all the fax devices exposed by all the fax service providers (FSPs) currently registered with the fax service.
ms.assetid: 32507fd4-70cc-403b-bb4e-ea308e67a92f
title: FaxServer.GetDevices method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.GetDevices method

The **GetDevices** method creates a [**FaxDevices**](-mfax-faxdevices.md) object, a collection of all the fax devices exposed by all the fax service providers (FSPs) currently registered with the fax service.

## Syntax


```VB
FaxServer.GetDevices() As FaxDevices
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FaxDevices**](-mfax-faxdevices.md)\*\***

A [**FaxDevices**](-mfax-faxdevices.md) object.

## Remarks

You can use the [**FaxDevices**](-mfax-faxdevices.md) object to enumerate the fax devices associated with a connected fax server and to create [**FaxDevice**](-mfax-faxdevice.md) objects for them.

To use this method, a user must have the [**farQUERY\_CONFIG**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-configuring-a-fax-device.md)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxserver)
</dt> </dl>

 

 




