---
Description: The Refresh method refreshes FaxSecurity object information from the fax server.
ms.assetid: 79d5e895-0306-4a40-a101-b83ab012d723
title: FaxSecurity.Refresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxSecurity.Refresh method

The **Refresh** method refreshes [**FaxSecurity**](-mfax-faxsecurity.md) object information from the fax server.

## Syntax


```VB
FaxSecurity.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

When the **Refresh** method is called, any configuration changes made after the last [**Save**](-mfax-faxsecurity-save-vb.md) method call are lost.

To read this property, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxSecurity**](-mfax-faxsecurity.md)
</dt> <dt>

[**IFaxSecurity**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxsecurity?branch=master)
</dt> </dl>

 

 




