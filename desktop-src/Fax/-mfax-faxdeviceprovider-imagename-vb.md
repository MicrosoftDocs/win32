---
Description: 'The ImageName property is a null-terminated string that contains the executable image name (DLL path and file name) of the fax service provider (FSP).'
ms.assetid: '59b59cec-fe02-4623-9da1-eb04dd8541c3'
title: 'FaxDeviceProvider.ImageName property'
---

# FaxDeviceProvider.ImageName property

The **ImageName** property is a null-terminated string that contains the executable image name (DLL path and file name) of the fax service provider (FSP).

This property is read-only.

## Syntax


```VB
Property ImageName As String
```



## Property value

A **String** that receives the fully qualified path and file name of the FSP DLL. The path can include valid environment variables, for example, %SYSTEMDRIVE% and %SYSTEMROOT%.

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

 

 




