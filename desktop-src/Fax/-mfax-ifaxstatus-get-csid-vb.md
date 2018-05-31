---
Description: Retrieves the Csid property for the FaxStatus object of a parent FaxPort object. The Csid property is a string that contains called station identifier (CSID) information, typically the fax number of the receiving device.
ms.assetid: 92487616-728b-4432-8b38-a438b3186e79
title: FaxStatus.Csid property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxStatus.Csid property

Retrieves the **Csid** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Csid** property is a string that contains called station identifier (CSID) information, typically the fax number of the receiving device.

This property is read-only.

## Syntax


```VB
Property Csid As String
```



## Property value

A **String** that receives the CSID information for a fax job. The string is typically the telephone number associated with the receiving device, and it is transmitted to the sending device as part of the fax transmission.

## Remarks

If the CSID information is not available, the **IFaxStatus::get\_Csid** method returns an empty string.

The **IFaxStatus::get\_Csid** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxStatus**](-mfax-ifaxstatus.md)
</dt> <dt>

[**IFaxPorts**](-mfax-ifaxports.md)
</dt> <dt>

[**IFaxPort**](-mfax-ifaxport.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




