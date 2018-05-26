---
Description: The Debug property is a Boolean value that indicates whether the fax service provider (FSP) DLL was created in a debug environment.
ms.assetid: 91296037-6846-4def-bf3f-33fa559b3f3b
title: FaxDeviceProvider.Debug property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDeviceProvider.Debug property

The **Debug** property is a Boolean value that indicates whether the fax service provider (FSP) DLL was created in a debug environment.

This property is read-only.

## Syntax


```VB
Property Debug As Boolean
```



## Property value

A **Boolean** that receives a value indicating whether the FSP DLL was created in a debug environment.

## Remarks

If this property is equal to **True**, the FSP DLL was created in a debug environment. If this property is equal to **False**, the DLL was not created in a debug environment.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-fax-device-providers.md)
</dt> <dt>

[**FaxDeviceProvider**](-mfax-faxdeviceprovider.md)
</dt> <dt>

[**IFaxDeviceProvider**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdeviceprovider?branch=master)
</dt> </dl>

 

 




