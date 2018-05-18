---
Description: 'The FaxNumber property is a null-terminated string that contains the fax number to which the fax server will transmit the fax job. The FaxNumber property applies only to outgoing fax transmissions.'
ms.assetid: '3cfb7a65-9269-46a9-8475-bd356e36f492'
title: 'FaxJob.FaxNumber property'
---

# FaxJob.FaxNumber property

The **FaxNumber** property is a null-terminated string that contains the fax number to which the fax server will transmit the fax job. The **FaxNumber** property applies only to outgoing fax transmissions.

This property is read-only.

## Syntax


```VB
Property FaxNumber As String
```



## Property value

A **String** that receives the fax number of the recipient of the transmission. The string can contain a number in canonical format. For more information, see [Address](http://msdn.microsoft.com/library/en-us/tapi/tapi3/address_ovr.asp) in the TAPI documentation (see the Canonical Address subheading).

## Remarks

A fax number is only available for faxes that have a [**Type**](-mfax-ifaxjob-get-type-vb.md) property equal to **JT\_SEND**. If the fax number is not available, the **FaxNumber** property contains an empty string.

**FaxNumber** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxJob**](-mfax-ifaxjob.md)
</dt> <dt>

[**IFaxJobs**](-mfax-ifaxjobs.md)
</dt> <dt>

[**Type**](-mfax-ifaxjob-get-type-vb.md)
</dt> </dl>

 

 




