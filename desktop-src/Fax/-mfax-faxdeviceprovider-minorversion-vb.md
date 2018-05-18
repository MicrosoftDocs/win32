---
Description: 'The MinorVersion property is a value that specifies the minor part of the version number for the fax service provider (FSP) DLL.'
ms.assetid: '9914e533-1fd6-4409-8ae9-a1ff3d517f2f'
title: 'FaxDeviceProvider.MinorVersion property'
---

# FaxDeviceProvider.MinorVersion property

The **MinorVersion** property is a value that specifies the minor part of the version number for the fax service provider (FSP) DLL.

This property is read-only.

## Syntax


```VB
Property MinorVersion As Long
```



## Property value

A **Long** that receives the minor part of the version number (the decimal portion) for the DLL.

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

[**IFaxDeviceProvider**](-mfax-faxdeviceprovider-cpp.md)
</dt> </dl>

 

 




