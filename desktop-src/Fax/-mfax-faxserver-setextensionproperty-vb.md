---
Description: 'The SetExtensionProperty method stores an extension configuration property at the server level.'
ms.assetid: 'bbacddd0-c157-47b9-a171-8a12d2aef2f4'
title: 'FaxServer.SetExtensionProperty method'
---

# FaxServer.SetExtensionProperty method

The **SetExtensionProperty** method stores an extension configuration property at the server level.

## Syntax


```VB
FaxServer.SetExtensionProperty( _
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

[VARIANT](e305240e-9e11-4006-98cc-26f4932d2118) that specifies the data to be set.

</dd> </dl>

## Remarks

The extension configuration property is a blob of bytes represented as a variant safe array of unsigned chars (VT\_UI1 \| VT\_ARRAY). The data is only relevant to the specific extension that uses it. For more information see [About the Fax Extension Configuration API](-mfax-about-the-fax-extension-configuration-api.md).

To use this method, a user must have the [**farMANAGE\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](-mfax-faxserver-cpp.md)
</dt> </dl>

 

 




