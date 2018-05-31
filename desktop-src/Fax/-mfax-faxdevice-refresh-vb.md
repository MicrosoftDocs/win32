---
Description: The Refresh method refreshes FaxDevice object information from the fax server. When the Refresh method is called, any configuration changes made after the last Save method call are lost.
ms.assetid: 2723073a-f396-4ae2-9eb8-9b717cce55e5
title: FaxDevice.Refresh method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

To use this method, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**IFaxDevice**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdevice)
</dt> </dl>

 

 




