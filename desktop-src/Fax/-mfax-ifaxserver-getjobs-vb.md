---
Description: The GetJobs method creates and initializes a FaxJobs object for a specified FaxServer object. The FaxJobs object allows enumeration of the current queued jobs for the connected fax server.
ms.assetid: 54800b9b-4c22-4b8b-a098-41276e099b26
title: FaxServer.GetJobs method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.GetJobs method

The **GetJobs** method creates and initializes a [**FaxJobs**](-mfax-faxjobs-object-visual-basic-.md) object for a specified [FaxServer](-mfax-faxserver-client.md) object. The [FaxJobs](-mfax-faxjobs.md) object allows enumeration of the current queued jobs for the connected fax server.

## Syntax


```VB
FaxServer.GetJobs( _
  ByRef retVal As Variant _
) As Long
```



## Parameters

<dl> <dt>

*retVal* \[out\]
</dt> <dd>

Type: **Variant\***

Pointer to a [VARIANT](e305240e-9e11-4006-98cc-26f4932d2118) structure that receives an [IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface pointer to a [FaxJobs](-mfax-faxjobs.md) object. The method returns a pdispVal member with a VT\_DISPATCH data type.

</dd> </dl>

## Remarks

The **GetJobs** method retrieves an [IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface pointer to a [FaxJobs](-mfax-faxjobs.md) object. A fax client application can also access the [**IFaxJobs**](-mfax-ifaxjobs.md) interface directly by calling the [IUnknown::QueryInterface](http://msdn.microsoft.com/en-us/library/ms682521.aspx) method to retrieve an interface pointer.

A fax client application should not call the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615.aspx) function to retrieve an [**IFaxJobs**](-mfax-ifaxjobs.md) interface pointer because it will not be instantiated correctly.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxServer**](-mfax-faxserver-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxServer](-mfax-faxserver-client.md)
</dt> <dt>

[**IFaxJob**](-mfax-ifaxjob.md)
</dt> <dt>

[**IFaxJobs**](-mfax-ifaxjobs.md)
</dt> <dt>

[IUnknown::QueryInterface](http://msdn.microsoft.com/en-us/library/ms682521.aspx)
</dt> </dl>

 

 




