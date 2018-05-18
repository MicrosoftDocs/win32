---
Description: 'The RingingNow property is a Boolean value that indicates whether the fax device is ringing at the moment the property is retrieved (the status could change immediately thereafter).'
ms.assetid: 'f92fd69d-7b7b-4130-a16a-02a226ee97e3'
title: 'FaxDevice.RingingNow property'
---

# FaxDevice.RingingNow property

The **RingingNow** property is a Boolean value that indicates whether the fax device is ringing at the moment the property is retrieved (the status could change immediately thereafter).

This property is read-only.

## Syntax


```VB
Property RingingNow As Boolean
```



## Property value

A **Boolean** that receives a value indicating whether the fax device is ringing at the moment the property is retrieved.

## Remarks

If this property is equal to **True**, the fax device is currently ringing. If this property is equal to **False**, the fax device is not ringing.

> [!Note]  
> The value of this property is set at the time that the [**FaxDevice**](-mfax-faxdevice.md) object is created, and is refreshed when you call the [**Refresh**](-mfax-faxdevice-refresh-vb.md) method.

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-fax-device-collection.md)
</dt> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](-mfax-faxdevice-cpp.md)
</dt> </dl>

 

 




