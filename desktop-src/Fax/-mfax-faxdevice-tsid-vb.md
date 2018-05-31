---
Description: The TSID property is a null-terminated string that contains the transmitting station identifier (TSID) for the device.
ms.assetid: fcd47515-7be5-46ba-837c-a6d644946638
title: FaxDevice.TSID property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDevice.TSID property

The **TSID** property is a null-terminated string that contains the transmitting station identifier (TSID) for the device.

This property is read/write.

## Syntax


```VB
Property TSID As String
```



## Property value

A **String** that specifies or receives the TSID for the fax device. The **String** is null-terminated.

## Remarks

> [!Note]  
> The TSID is limited to 20 characters. Also, because most fax machines accept a limited set of characters in the fax transmission called station identifier (CSID) and TSID strings, it is advisable to use only English letters, numeric symbols, and punctuation marks (ASCII range 0x20 to 0x7F) in these strings.

 

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

[**IFaxDevice**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdevice)
</dt> </dl>

 

 




