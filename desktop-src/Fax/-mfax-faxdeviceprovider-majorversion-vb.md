---
Description: The MajorVersion property is a value that specifies the major part of the version number for the fax service provider (FSP) DLL.
ms.assetid: 9c0b6457-7515-41d8-aff8-74cb21fcbd1e
title: FaxDeviceProvider.MajorVersion property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDeviceProvider.MajorVersion property

The **MajorVersion** property is a value that specifies the major part of the version number for the fax service provider (FSP) DLL.

This property is read-only.

## Syntax


```VB
Property MajorVersion As Long
```



## Property value

A **Long** that receives the major part of the version number for the DLL.

## Remarks

The standard format for version numbers is MajorVersion.MinorVersion.MajorBuild.MinorBuild.

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

[**IFaxDeviceProvider**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdeviceprovider)
</dt> </dl>

 

 




