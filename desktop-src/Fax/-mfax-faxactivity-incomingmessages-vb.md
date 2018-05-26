---
Description: The IncomingMessages property is a number that represents the total number of incoming fax jobs that the fax service is currently in the process of receiving.
ms.assetid: 08636ffe-19a5-4f8c-8e9c-ef42fd65cafb
title: FaxActivity.IncomingMessages property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxActivity.IncomingMessages property

The **IncomingMessages** property is a number that represents the total number of incoming fax jobs that the fax service is currently in the process of receiving.

This property is read-only.

## Syntax


```VB
Property IncomingMessages As Long
```



## Property value

A **Long** that receives the total number of incoming fax jobs that the fax service is currently receiving.

## Remarks

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

[Visual Basic Example](-mfax-monitoring-fax-activity.md)
</dt> <dt>

[**FaxActivity**](-mfax-faxactivity.md)
</dt> <dt>

[**IFaxActivity**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxactivity?branch=master)
</dt> </dl>

 

 




