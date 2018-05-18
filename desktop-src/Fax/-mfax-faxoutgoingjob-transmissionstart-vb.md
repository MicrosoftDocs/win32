---
Description: 'The TransmissionStart property indicates the time that the fax outbound job began transmitting. This property will have a value only after the transmission has started.'
ms.assetid: '874c1087-d45d-4d0d-a43c-41b88180f39a'
title: 'FaxOutgoingJob.TransmissionStart property'
---

# FaxOutgoingJob.TransmissionStart property

The **TransmissionStart** property indicates the time that the fax outbound job began transmitting. This property will have a value only after the transmission has started.

This property is read-only.

## Syntax


```VB
Property TransmissionStart As Date
```



## Property value

**Date** value. An 8-byte floating-point number that contains the time, expressed in local system time, that the fax began transmitting.

For more information about the **Date** data type, see the *Microsoft Visual C++ Programmer's Guide*.

## Remarks

In the case of a failed fax, this property will be assigned a value of zero. If you try to retrieve the property for a failed fax, you will receive an error.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-outgoing-jobs.md)
</dt> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob**](-mfax-faxoutgoingjob-cpp.md)
</dt> </dl>

 

 




