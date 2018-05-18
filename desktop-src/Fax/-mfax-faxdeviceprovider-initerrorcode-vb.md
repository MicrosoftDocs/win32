---
Description: 'The InitErrorCode property is a value that specifies the last error code that the fax service provider (FSP) returned while the fax service was loading and initializing the FSP DLL. This may be an HRESULT value or a Win32 error code.'
ms.assetid: 'f8472803-c30a-4128-8678-cf109cae45ca'
title: 'FaxDeviceProvider.InitErrorCode property'
---

# FaxDeviceProvider.InitErrorCode property

The **InitErrorCode** property is a value that specifies the last error code that the fax service provider (FSP) returned while the fax service was loading and initializing the FSP DLL. This may be an HRESULT value or a Win32 error code.

This property is read-only.

## Syntax


```VB
Property InitErrorCode As Long
```



## Property value

A **Long** that receives the last error code the FSP returned during loading and initialization of the DLL.

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

 

 




