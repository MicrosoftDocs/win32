---
Description: The AuthenticationType property specifies the type of authentication the fax service uses when connecting to an Simple Mail Transport Protocol (SMTP) server.
ms.assetid: 2d92c6f0-9037-4444-9ac1-714e05ef6236
title: FaxReceiptOptions.AuthenticationType property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxReceiptOptions.AuthenticationType property

The **AuthenticationType** property specifies the type of authentication the fax service uses when connecting to an Simple Mail Transport Protocol (SMTP) server.

This property is read/write.

## Syntax


```VB
Property AuthenticationType As Integer
```



## Property value

A variable of type [**FAX\_SMTP\_AUTHENTICATION\_TYPE\_ENUM**](-mfax-fax-smtp-authentication-type-enum.md) that specifies or receives the type of authentication. See the **FAX\_SMTP\_AUTHENTICATION\_TYPE\_ENUM** enumeration.

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

 

 




