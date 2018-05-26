---
Description: The Tsid property is a null-terminated string that contains the transmitting station identifier (TSID)) associated with the fax job.
ms.assetid: 54c1e533-1846-4858-961d-ff0744473d50
title: FaxJob.Tsid property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxJob.Tsid property

The **Tsid** property is a null-terminated string that contains the transmitting station identifier (TSID)) associated with the fax job.

This property is read-only.

## Syntax


```VB
Property Tsid As String
```



## Property value

A **String** that receives a TSID associated with the fax transmission. The TSID is typically the fax number of the device sending the transmission.

## Remarks

If the TSID is not available, **Tsid** is an empty string.

You can use the [**UseDeviceTsid**](-mfax-ifaxserver-get-usedevicetsid-vb.md) property to determine if the fax server is configured to permit user-specified TSIDs.

Note that the T.30 specification of the International Telecommunication Union (ITU) restricts the value of a TSID to 20 ASCII characters. If a fax client application specifies a TSID that contains non-ASCII characters, the fax service removes them. If the TSID exceeds 20 characters, the service truncates the extra characters.

**Tsid** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxJob**](-mfax-faxjob-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxJob**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjob?branch=master)
</dt> <dt>

[**IFaxJobs**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjobs?branch=master)
</dt> <dt>

[**UseDeviceTsid**](-mfax-ifaxserver-get-usedevicetsid-vb.md)
</dt> </dl>

 

 




