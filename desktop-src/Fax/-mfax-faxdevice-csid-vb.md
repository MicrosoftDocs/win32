---
Description: 'The CSID property is a null-terminated string that contains the called station identifier (CSID) for the device.'
ms.assetid: 'da5e17a8-8297-41e5-a046-d50dfc1dd4e1'
title: 'FaxDevice.CSID property'
---

# FaxDevice.CSID property

The **CSID** property is a null-terminated string that contains the called station identifier (CSID) for the device.

This property is read/write.

## Syntax


```VB
Property CSID As String
```



## Property value

A **String** that specifies or receives the CSID for the fax device.

## Remarks

> [!Note]  
> The CSID is limited to 20 characters. Also, because most fax machines accept a limited set of characters in the fax transmission CSID and transmitting station identifier (TSID) strings, it is advisable to use only English letters, numeric symbols, and punctuation marks (ASCII range 0x20 to 0x7F) in these strings.

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-configuring-a-fax-device.md)
</dt> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](-mfax-faxdevice-cpp.md)
</dt> </dl>

 

 




