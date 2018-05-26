---
Description: The InitErrorCode property is a value that specifies the last error code that the fax routing extension returned while the fax service was loading and initializing the fax routing extensions DLL.
ms.assetid: 566c146d-57e2-4043-a221-cc134994690d
title: FaxInboundRoutingExtension.InitErrorCode property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxInboundRoutingExtension.InitErrorCode property

The **InitErrorCode** property is a value that specifies the last error code that the fax routing extension returned while the fax service was loading and initializing the fax routing extension's DLL.

This property is read-only.

## Syntax


```VB
Property InitErrorCode As Long
```



## Property value

A **Long** that receives the last error code that the fax routing extension reported during loading and initialization of the DLL.

## Remarks

The error code may be an HRESULT value or a Win32 error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-routing-extensions-and-routing-methods.md)
</dt> <dt>

[**FaxInboundRoutingExtension**](-mfax-faxinboundroutingextension.md)
</dt> <dt>

[**IFaxInboundRoutingExtension**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxinboundroutingextension?branch=master)
</dt> </dl>

 

 




