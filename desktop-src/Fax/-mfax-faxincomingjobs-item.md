---
Description: The Item property returns a FaxIncomingJob object from the FaxIncomingJobs collection.
ms.assetid: c1c84f4b-5184-4233-bd97-3b7c586f45a3
title: FaxIncomingJobs.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJobs.Item property

The **Item** property returns a [**FaxIncomingJob**](-mfax-faxincomingjob.md) object from the [**FaxIncomingJobs**](-mfax-faxincomingjobs.md) collection.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal vIndex As Variant _
) As IFaxIncomingJob
```



## Property value

A variable of type [**IFaxIncomingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingjob) that receives a [**FaxIncomingJob**](-mfax-faxincomingjob.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-incoming-queue.md)
</dt> <dt>

[**FaxIncomingJobs**](-mfax-faxincomingjobs.md)
</dt> <dt>

[**get\_Item**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxincomingjobs-get_item)
</dt> </dl>

 

 




