---
Description: 'Sets or retrieves the DirtyDays property for a FaxServer object. The DirtyDays property is the number of days the fax server retains an unsent job in the fax job queue.'
ms.assetid: '0d1a3268-a5de-4e67-9800-13b87e449b2a'
title: 'FaxServer.DirtyDays property'
---

# FaxServer.DirtyDays property

Sets or retrieves the **DirtyDays** property for a [FaxServer](-mfax-faxserver-client.md) object. The **DirtyDays** property is the number of days the fax server retains an unsent job in the fax job queue.

This property is read/write.

## Syntax


```VB
Property DirtyDays As Long
```



## Property value

A **Long** that specifies or receives the number of days the fax server retains an unsent job in the fax job queue. A value of 1 indicates that the fax server should not remove the job from the job queue.

## Remarks

To minimize the amount of space unsent jobs use, the fax server removes unsent jobs after the number of days specified by the **DirtyDays** property have elapsed.

A transmission might not be sent for various reasons. Examples are if an invalid fax number is specified, or when the sending device receives a busy signal multiple times.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxServer**](-mfax-faxserver-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxServer](-mfax-faxserver-client.md)
</dt> </dl>

 

 




