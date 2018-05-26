---
Description: The SMTPPassword property is a null-terminated string that contains the Simple Mail Transport Protocol (SMTP) password used for authenticated connections.
ms.assetid: 8641f1a8-2c50-4a58-9098-e1c42640286b
title: FaxReceiptOptions.SMTPPassword property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxReceiptOptions.SMTPPassword property

The **SMTPPassword** property is a null-terminated string that contains the Simple Mail Transport Protocol (SMTP) password used for authenticated connections.

This property is read/write.

## Syntax


```VB
Property SMTPPassword As String
```



## Property value

A **String** that specifies or receives the SMTP password used for authenticated connections. The string is null-terminated.

## Remarks

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxReceiptOptions**](-mfax-faxreceiptoptions.md)
</dt> <dt>

[**IFaxReceiptOptions**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxreceiptoptions?branch=master)
</dt> </dl>

 

 




