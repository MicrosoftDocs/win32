---
Description: The Refresh method updates FaxStatus object information for the associated parent FaxPort object.
ms.assetid: a1bde405-eb60-4381-92d6-4da3a3208d6f
title: FaxStatus.Refresh method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus.Refresh method

The **Refresh** method updates [FaxStatus](-mfax-faxstatus.md) object information for the associated parent [FaxPort](-mfax-faxport.md) object.

## Syntax


```VB
FaxStatus.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

Call the **Refresh** method to update the information for a [FaxStatus](-mfax-faxstatus.md) object. An application must call this method to poll a fax port for new status information. After you successfully call **Refresh**, you must call the appropriate [**IFaxStatus**](-mfax-ifaxstatus.md) interface method to retrieve new attribute values that are valid.

It is recommended that you limit calls to this method because frequent calls to **Refresh** can affect system performance.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxStatus**](-mfax-faxstatus-object-visual-basic-.md)
</dt> </dl>

 

 




