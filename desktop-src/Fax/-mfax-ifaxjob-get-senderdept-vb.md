---
Description: 'The SenderDept property is a null-terminated string that contains the department identifier for the sender of the fax job. The SenderDept property applies only to outgoing fax transmissions.'
ms.assetid: '1c4996f2-d4b1-4658-8cdc-0e6d30aef88b'
title: 'FaxJob.SenderDept property'
---

# FaxJob.SenderDept property

The **SenderDept** property is a null-terminated string that contains the department identifier for the sender of the fax job. The **SenderDept** property applies only to outgoing fax transmissions.

This property is read-only.

## Syntax


```VB
Property SenderDept As String
```



## Property value

A **String** that receives the department identifier of the sender of the fax transmission.

## Remarks

If the sender's department is not available, the **SenderDept** property contains an empty string.

The **SenderDept** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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
</dt> </dl>

 

 




