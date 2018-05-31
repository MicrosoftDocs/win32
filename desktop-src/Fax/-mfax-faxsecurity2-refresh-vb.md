---
Description: Refreshes FaxSecurity2 object information from the fax server.
ms.assetid: 49a5e89d-26af-4f78-b220-b3a539c28959
title: FaxSecurity2.Refresh method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxSecurity2.Refresh method

Refreshes [**FaxSecurity2**](-mfax-faxsecurity2.md) object information from the fax server.

## Syntax


```VB
FaxSecurity2.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxsecurity2-save-vb.md) method call are lost.

To use this method, a user must have the [****far2QUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxSecurity2**](-mfax-faxsecurity2.md)
</dt> <dt>

[**IFaxSecurity2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxsecurity2)
</dt> </dl>

 

 




