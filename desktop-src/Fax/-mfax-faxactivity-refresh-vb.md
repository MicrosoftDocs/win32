---
Description: The Refresh method refreshes FaxActivity information from the fax server.
ms.assetid: 3c6eafbc-bd21-42c7-b6a5-1f8825b283fc
title: FaxActivity.Refresh method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxActivity.Refresh method

The **Refresh** method refreshes [**FaxActivity**](-mfax-faxactivity.md) information from the fax server.

The **Refresh** method refreshes [**IFaxActivity**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxactivity) information from the fax server.

## Syntax


```VB
FaxActivity.Refresh() As Long
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

[Visual Basic Example](-mfax-monitoring-fax-activity.md)
</dt> <dt>

[**FaxActivity**](-mfax-faxactivity.md)
</dt> <dt>

[**IFaxActivity**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxactivity)
</dt> </dl>

 

 




