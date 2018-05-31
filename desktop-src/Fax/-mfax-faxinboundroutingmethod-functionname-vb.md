---
Description: The FunctionName property is a null-terminated string that contains the name of the function that executes a specific fax routing procedure.
ms.assetid: cccd2d5e-d1ac-4c56-8c50-1c8f5ca9692c
title: FaxInboundRoutingMethod.FunctionName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxInboundRoutingMethod.FunctionName property

The **FunctionName** property is a null-terminated string that contains the name of the function that executes a specific fax routing procedure.

This property is read-only.

## Syntax


```VB
Property FunctionName As String
```



## Property value

A **String** that receives the name of the function that executes the specified fax routing method (a procedure).

## Remarks

The fax routing extension DLL identified by the [**ExtensionImageName**](-mfax-faxinboundroutingmethod-extensionimagename-vb.md) property defines and exports the function.

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

[**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md)
</dt> <dt>

[**IFaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod-cpp.md)
</dt> </dl>

 

 




