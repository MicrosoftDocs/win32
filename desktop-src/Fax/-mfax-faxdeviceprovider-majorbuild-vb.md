---
Description: 'The MajorBuild property is a value that specifies the major part of the build number for the fax service provider (FSP) DLL.'
ms.assetid: 'fd535c96-c4ef-4835-ae2c-481acbb5dfbd'
title: 'FaxDeviceProvider.MajorBuild property'
---

# FaxDeviceProvider.MajorBuild property

The **MajorBuild** property is a value that specifies the major part of the build number for the fax service provider (FSP) DLL.

This property is read-only.

## Syntax


```VB
Property MajorBuild As Long
```



## Property value

A **Long** that receives the major part of the build number for the DLL.

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

[**IFaxDeviceProvider**](-mfax-faxdeviceprovider-cpp.md)
</dt> </dl>

 

 




