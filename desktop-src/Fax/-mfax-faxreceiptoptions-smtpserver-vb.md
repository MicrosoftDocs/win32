---
Description: The SMTPServer property is a null-terminated string that contains the name of the Simple Mail Transport Protocol (SMTP) server.
ms.assetid: 7d1eb790-b7f0-47e0-ada5-87bf03830eea
title: FaxReceiptOptions.SMTPServer property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxReceiptOptions.SMTPServer property

The **SMTPServer** property is a null-terminated string that contains the name of the Simple Mail Transport Protocol (SMTP) server.

This property is read/write.

## Syntax


```VB
Property SMTPServer As String
```



## Property value

A **String** that specifies or receives the name of the SMTP server. The string is null-terminated.

## Remarks

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

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

[**IFaxReceiptOptions**](-mfax-faxreceiptoptions-cpp.md)
</dt> <dt>

[Setting Receipt Options](-mfax-setting-receipt-options.md)
</dt> </dl>

 

 




