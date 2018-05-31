---
Description: The FaxNumber property is a null-terminated string that contains the fax number associated with the recipient.
ms.assetid: e1e84f89-00d5-4d4a-9c91-4462c117f0c5
title: FaxRecipient.FaxNumber property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxRecipient.FaxNumber property

The **FaxNumber** property is a null-terminated string that contains the fax number associated with the recipient.

This property is read/write.

## Syntax


```VB
Property FaxNumber As String
```



## Property value

A **String** that specifies or receives the fax number associated with the recipient. The string is null-terminated.

## Remarks

If this string contains a canonical fax number (defined in the [Address](http://msdn.microsoft.com/library/en-us/tapi/tapi3/address_ovr.asp) topic of the Telephony Application Programming Interface (TAPI) documentation—see the *Canonical Addresses* subheading), then the outbound routing rules will be applied. Otherwise, the first available device will be used and the fax number we be dialed as it appears in the string.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxRecipient**](-mfax-faxrecipient.md)
</dt> <dt>

[**IFaxRecipient**](-mfax-faxrecipient-cpp.md)
</dt> <dt>

[Broadcasting a Fax](-mfax-broadcasting-a-fax.md)
</dt> </dl>

 

 




