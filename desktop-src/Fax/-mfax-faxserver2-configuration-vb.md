---
Description: The Configuration property holds a IFaxConfiguration object. The object permits a fax client application to access information about the configuration of the connected fax server.
ms.assetid: 2b7a5eb6-d7ca-418c-9dab-54dee8a7f9a5
title: FaxServer.Configuration property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.Configuration property

The **Configuration** property holds a [**IFaxConfiguration**](/windows/previous-versions/Faxcomex/nn-faxcomex-ifaxconfiguration?branch=master) object. The object permits a fax client application to access information about the configuration of the connected fax server.

This property is read-only.

## Syntax


```VB
Property Configuration As IFaxConfiguration
```



## Property value

An address of a pointer to an [**IFaxConfiguration**](/windows/previous-versions/Faxcomex/nn-faxcomex-ifaxconfiguration?branch=master) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**IFaxServer2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver2?branch=master)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> </dl>

 

 




