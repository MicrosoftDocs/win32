---
Description: Retrieves the RawReceiveTime property for a FaxTiff object.
ms.assetid: 420ff6e8-5020-459e-980b-af93c35fca98
title: FaxTiff.RawReceiveTime property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxTiff.RawReceiveTime property

Retrieves the **RawReceiveTime** property for a [FaxTiff](-mfax-faxtiff.md) object. The **RawReceiveTime** property is the time at which reception began for an inbound fax file, expressed in Coordinated Universal Time (UTC). This property can also be the time at which reception or transmission began for an archived file.

This property is read-only.

## Syntax


```VB
Property RawReceiveTime As Variant
```



## Property value

A **Variant** that receives the time at which reception or transmission began for the specified fax file, expressed in UTC. The method returns a **vt** member with the value VT\_CY, and a **cyVal** member that contains a [FILETIME](http://msdn.microsoft.com/library/en-us/sysinfo/base/filetime_str.asp) structure.

## Remarks

A fax client application must set the [**Image**](-mfax-ifaxtiff-get-image-vb.md) property before retrieving another property for a [FaxTiff](-mfax-faxtiff.md) object.

The **get\_RawReceiveTime** method sets the *pVal* parameter to the local time at which the fax job started receiving or transmitting the fax file.

The **RawReceiveTime** property contains the local time at which the fax job started receiving or transmitting the fax file.

The [**get\_ReceiveTime**](-mfax-ifaxtiff-get-receivetime-vb.md) method returns the time in a formatted string.

The [**ReceiveTime**](-mfax-ifaxtiff-get-receivetime-vb.md) property contains the time in a formatted string.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxTiff**](-mfax-faxtiff-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxTiff**](-mfax-ifaxtiff.md)
</dt> <dt>

[**Image**](-mfax-ifaxtiff-get-image-vb.md)
</dt> <dt>

[FILETIME](http://msdn.microsoft.com/library/en-us/sysinfo/base/filetime_str.asp)
</dt> <dt>

[**ReceiveTime**](-mfax-ifaxtiff-get-receivetime-vb.md)
</dt> </dl>

 

 




