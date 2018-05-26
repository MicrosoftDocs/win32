---
Description: Retrieves the Tsid property for the FaxStatus object of a parent FaxPort object. The Tsid property is a null-terminated string that contains the transmitting station identifier (TSID) associated with the fax port.
ms.assetid: d347c9df-22d9-4aa0-b23e-2810420f83bc
title: FaxStatus.Tsid property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxStatus.Tsid property

Retrieves the **Tsid** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Tsid** property is a null-terminated string that contains the transmitting station identifier (TSID) associated with the fax port.

This property is read-only.

## Syntax


```VB
Property Tsid As String
```



## Property value

A **String** that receives the TSID associated with the fax port that is sending a fax transmission. This identifier is typically the fax number for the port. The TSID is transmitted to the receiving device as part of a fax transmission.

## Remarks

The **Tsid** property is set for both inbound and outbound fax transmissions. If the TSID information is not available, the **IFaxStatus::get\_Tsid** method returns an empty string.

The **IFaxStatus::get\_Tsid** method allocates the memory required for the buffer pointed to by the pVal parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxStatus**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxstatus?branch=master)
</dt> <dt>

[**IFaxPorts**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxports?branch=master)
</dt> <dt>

[**IFaxPort**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxport?branch=master)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




