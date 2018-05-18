---
Description: 'Retrieves the ElapsedTime property for the FaxStatus object of a parent FaxPort object. The ElapsedTime property is a number that represents the elapsed time for an active fax job.'
ms.assetid: 'c0358eec-dcd2-442f-8627-ac235484d23e'
title: 'FaxStatus.ElapsedTime property'
---

# FaxStatus.ElapsedTime property

Retrieves the **ElapsedTime** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **ElapsedTime** property is a number that represents the elapsed time for an active fax job.

This property is read-only.

## Syntax


```VB
Property ElapsedTime As Date
```



## Property value

A **Date** that receives the time that has elapsed, in seconds, since the fax job began transmitting the document on the specified port.

For more information about the **Date** data type, see the *Microsoft Visual C++ Programmer's Guide*.

## Remarks

The value of this property is provided in **Date** format, but represents elapsed time, not the date and time. The value of this property is undefined if there is no job being executed on the device.

You can use the **ElapsedTime** property of a [FaxStatus](-mfax-faxstatus.md) object in conjunction with the [**StartTime**](-mfax-ifaxstatus-get-starttime-vb.md) property of the object to inform users about the transmission length of a fax job.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



 

 




