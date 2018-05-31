---
Description: The MinorBuild property is a value that specifies the minor part of the build number for the fax service provider (FSP) DLL.
ms.assetid: 60aad1c5-04b7-4e01-bbf2-400267cc98b8
title: FaxDeviceProvider.MinorBuild property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDeviceProvider.MinorBuild property

The **MinorBuild** property is a value that specifies the minor part of the build number for the fax service provider (FSP) DLL.

This property is read-only.

## Syntax


```VB
Property MinorBuild As Long
```



## Property value

A **Long** that receives the minor part of the build number (the decimal portion) for the DLL.

## Remarks

The standard format for build numbers is MajorVersion.MinorVersion.MajorBuild.MinorBuild.

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

 

 




