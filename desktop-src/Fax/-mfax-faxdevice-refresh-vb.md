---
Description: The Refresh method refreshes FaxDevice object information from the fax server. When the Refresh method is called, any configuration changes made after the last Save method call are lost.
ms.assetid: 2723073a-f396-4ae2-9eb8-9b717cce55e5
title: FaxDevice.Refresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDevice.Refresh method

The **Refresh** method refreshes [**FaxDevice**](-mfax-faxdevice.md) object information from the fax server. When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxdevice-save-vb.md) method call are lost.

## Syntax


```VB
FaxDevice.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

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

[Visual Basic Example](-mfax-managing-the-fax-device-collection.md)
</dt> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdevice?branch=master)
</dt> </dl>

 

 




