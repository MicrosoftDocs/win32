---
Description: 'The Refresh method refreshes FaxInboundRoutingMethod object information from the fax server.'
ms.assetid: 'd15f5f98-7bcd-43db-81f2-46b6a3645582'
title: 'FaxInboundRoutingMethod.Refresh method'
---

# FaxInboundRoutingMethod.Refresh method

The **Refresh** method refreshes [**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md) object information from the fax server.

## Syntax


```VB
FaxInboundRoutingMethod.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxinboundroutingmethod-save-vb.md) method call are lost.

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

[Visual Basic Example](-mfax-managing-routing-extensions-and-routing-methods.md)
</dt> <dt>

[**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md)
</dt> <dt>

[**IFaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod-cpp.md)
</dt> </dl>

 

 




