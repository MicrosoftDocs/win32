---
Description: The LoadDefaultSender method fills the FaxSender object with the default sender information.
ms.assetid: 97783f1e-51ba-49da-b178-5c62be537979
title: FaxSender.LoadDefaultSender method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxSender.LoadDefaultSender method

The **LoadDefaultSender** method fills the [**FaxSender**](-mfax-faxsender.md) object with the default sender information.

## Syntax


```VB
FaxSender.LoadDefaultSender() As Long
```



## Parameters

This method has no parameters.

## Remarks

The default sender information is saved using the [**SaveDefaultSender**](-mfax-faxsender-savedefaultsender-vb.md) method.

This method can return remote procedure call (RPC) return values. For more information, see [RPC Return Values](http://msdn.microsoft.com/library/en-us/rpc/rpc/rpc_return_values.asp).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-broadcasting-a-fax.md)
</dt> <dt>

[**FaxSender**](-mfax-faxsender.md)
</dt> <dt>

[**IFaxSender**](-mfax-faxsender-cpp.md)
</dt> </dl>

 

 




