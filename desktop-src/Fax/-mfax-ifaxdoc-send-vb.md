---
Description: 'The Send method transmits the document specified by the FileName property of a FaxDoc object. The method can send the fax to the fax number specified by the FaxNumber property.'
ms.assetid: 'efe70850-ad4e-4e64-b3a8-40d3ce2535f8'
title: 'FaxDoc.Send method'
---

# FaxDoc.Send method

The **Send** method transmits the document specified by the [**FileName**](-mfax-ifaxdoc-get-filename-vb.md) property of a [FaxDoc](-mfax-faxdoc.md) object. The method can send the fax to the fax number specified by the [**FaxNumber**](-mfax-ifaxdoc-get-faxnumber-vb.md) property.

## Syntax


```VB
FaxDoc.Send() As Long
```



## Parameters

This method has no parameters.

## Return value

Type: **Long\***

Specifies a pointer to a variable to receive a unique number that identifies the queued job that will send the fax transmission.

## Remarks

The [**FileName**](-mfax-ifaxdoc-get-filename-vb.md) property is required to send a fax transmission using a call to the **Send** method. The [**FaxNumber**](-mfax-ifaxdoc-get-faxnumber-vb.md) property is also required. For more information, see [Transmitting Faxes](-mfax-transmitting-faxes.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxDoc**](-mfax-ifaxdoc.md)
</dt> </dl>

 

 




