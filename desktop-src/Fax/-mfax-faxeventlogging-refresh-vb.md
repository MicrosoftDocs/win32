---
Description: The Refresh method refreshes FaxEventLogging object information from the fax server.
ms.assetid: 35400b0f-e902-48f9-bef2-71f62fd41552
title: FaxEventLogging.Refresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxEventLogging.Refresh method

The **Refresh** method refreshes [**FaxEventLogging**](-mfax-faxeventlogging.md) object information from the fax server.

## Syntax


```VB
FaxEventLogging.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

When the [**FaxEventLogging**](-mfax-faxeventlogging.md) method is called, any configuration changes made after the last [**Save**](-mfax-faxeventlogging-save-vb.md) method call are lost.

To use this method, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-setting-logging-options.md)
</dt> <dt>

[**FaxEventLogging**](-mfax-faxeventlogging.md)
</dt> <dt>

[**IFaxEventLogging**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxeventlogging?branch=master)
</dt> </dl>

 

 




