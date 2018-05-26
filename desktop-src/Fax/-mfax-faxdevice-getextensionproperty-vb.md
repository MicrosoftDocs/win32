---
Description: The GetExtensionProperty method retrieves an extension configuration property stored at the device level.
ms.assetid: 5522b69f-c726-475f-9d36-0365196c47c1
title: FaxDevice.GetExtensionProperty method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDevice.GetExtensionProperty method

The **GetExtensionProperty** method retrieves an extension configuration property stored at the device level.

## Syntax


```VB
FaxDevice.GetExtensionProperty( _
  ByVal bstrGUID As String _
) As Variant
```



## Parameters

<dl> <dt>

*bstrGUID* \[in\]
</dt> <dd>

Type: **String**

Specifies a string GUID that uniquely identifies the data to be retrieved.

</dd> </dl>

## Return value

Type: **Variant\***

**Variant** that specifies the data.

## Remarks

> [!Note]  
> The returned data is a blob of bytes represented as a variant safe array of unsigned chars (VT\_UI1 \| VT\_ARRAY). The data is relevant only to the specific extension that uses it. For more information see [About the Fax Extension Configuration API](-mfax-about-the-fax-extension-configuration-api.md).

 

To use this method, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

[**IFaxDevice**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdevice?branch=master)
</dt> </dl>

 

 




