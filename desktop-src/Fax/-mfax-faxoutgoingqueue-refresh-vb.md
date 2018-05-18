---
Description: 'The Refresh method refreshes FaxOutgoingQueue object information from the fax server. When the Refresh method is called, any configuration changes made after the last Save method call are lost.'
ms.assetid: 'c1c106e8-b314-4788-9e65-b8ef961582c4'
title: 'FaxOutgoingQueue.Refresh method'
---

# FaxOutgoingQueue.Refresh method

The **Refresh** method refreshes [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md) object information from the fax server. When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxoutgoingqueue-save-vb.md) method call are lost.

## Syntax


```VB
FaxOutgoingQueue.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md)
</dt> <dt>

[**IFaxOutgoingQueue**](-mfax-faxoutgoingqueue-cpp.md)
</dt> <dt>

[Managing Outgoing Jobs](-mfax-managing-outgoing-jobs.md)
</dt> </dl>

 

 




