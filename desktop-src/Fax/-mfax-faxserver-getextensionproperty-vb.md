---
Description: 'The GetExtensionProperty method retrieves an extension configuration property stored at the server level.'
ms.assetid: 'f5c5df93-9bd3-43c3-8a5d-c97d890b2fa1'
title: 'FaxServer.GetExtensionProperty method'
---

# FaxServer.GetExtensionProperty method

The **GetExtensionProperty** method retrieves an extension configuration property stored at the server level.

## Syntax


```VB
FaxServer.GetExtensionProperty( _
  ByVal bstrGUID As String, _
  ByRef vProperty As Variant _
) As Long
```



## Parameters

<dl> <dt>

*bstrGUID* \[in\]
</dt> <dd>

Type: **String**

Specifies a string GUID that uniquely identifies the data to be retrieved.

</dd> <dt>

*vProperty* \[out\]
</dt> <dd>

Type: **Variant\***

[VARIANT](e305240e-9e11-4006-98cc-26f4932d2118) that specifies the data.

</dd> </dl>

## Remarks

The returned data is a blob of bytes represented as a variant safe array of unsigned chars (VT\_UI1 \| VT\_ARRAY). The data is only relevant to the specific extension that uses it. For more information see [About the Fax Extension Configuration API](-mfax-about-the-fax-extension-configuration-api.md).

To use this method, a user must have the [**farQUERY\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

 

 




