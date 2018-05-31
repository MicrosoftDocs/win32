---
Description: The ProviderUniqueName property is a null-terminated string that contains the unique name for the fax service provider (FSP) associated with the device.
ms.assetid: c4ce229a-e0e0-413b-95cf-6dc194d68dce
title: FaxDevice.ProviderUniqueName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDevice.ProviderUniqueName property

The **ProviderUniqueName** property is a null-terminated string that contains the unique name for the fax service provider (FSP) associated with the device.

This property is read-only.

## Syntax


```VB
Property ProviderUniqueName As String
```



## Property value

A **String** that receives the unique name for the FSP associated with the device. The **String** is null-terminated.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-configuring-a-fax-device.md)
</dt> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdevice)
</dt> </dl>

 

 




