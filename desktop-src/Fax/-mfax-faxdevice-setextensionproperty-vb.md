---
Description: The SetExtensionProperty method stores an extension configuration property at the device level.
ms.assetid: e18367a8-3dc8-4e19-8adb-60c465fa0f08
title: FaxDevice.SetExtensionProperty method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDevice.SetExtensionProperty method

The **SetExtensionProperty** method stores an extension configuration property at the device level.

## Syntax


```VB
FaxDevice.SetExtensionProperty( _
  ByVal bstrGUID As String, _
  ByVal vProperty As Variant _
) As Long
```



## Parameters

<dl> <dt>

*bstrGUID* \[in\]
</dt> <dd>

Type: **String**

Specifies a string GUID that identifies the data to set.

</dd> <dt>

*vProperty* \[in\]
</dt> <dd>

Type: **Variant**

**Variant** that specifies the data to be stored.

</dd> </dl>

## Remarks

To use this method, a user must have the [****farMANAGE\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

> [!Note]  
> The required data is a blob of bytes represented as a variant safe array of unsigned chars (VT\_UI1 \| VT\_ARRAY). The data is relevant only to the specific extension that uses it. For more information see [About the Fax Extension Configuration API](-mfax-about-the-fax-extension-configuration-api.md).

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-extension-configuration-properties.md)
</dt> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](-mfax-faxdevice-cpp.md)
</dt> </dl>

 

 




