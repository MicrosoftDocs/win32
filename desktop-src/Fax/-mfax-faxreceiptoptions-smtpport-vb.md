---
Description: The SMTPPort property is a value that specifies the Simple Mail Transport Protocol (SMTP) port number.
ms.assetid: 082e122c-8e44-42d1-b16c-af40bf5188d6
title: FaxReceiptOptions.SMTPPort property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxReceiptOptions.SMTPPort property

The **SMTPPort** property is a value that specifies the Simple Mail Transport Protocol (SMTP) port number.

This property is read/write.

## Syntax


```VB
Property SMTPPort As Long
```



## Property value

A **Long** that specifies or receives the SMTP port number.

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

 

 




