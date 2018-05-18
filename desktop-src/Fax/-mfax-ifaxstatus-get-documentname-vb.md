---
Description: 'Retrieves the DocumentName property for the FaxStatus object of a parent FaxPort object. The DocumentName property is a null-terminated string that contains the user-friendly name associated with an active fax document.'
ms.assetid: '02222b39-c9b9-459a-989c-80e8d5d4636b'
title: 'FaxStatus.DocumentName property'
---

# FaxStatus.DocumentName property

Retrieves the **DocumentName** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **DocumentName** property is a null-terminated string that contains the user-friendly name associated with an active fax document.

This property is read-only.

## Syntax


```VB
Property DocumentName As String
```



## Property value

A **String** that receives the name of the fax document associated with the active outbound job on the specific fax port. The string is suitable for display to the user. The **DocumentName** property only has meaning for outbound transmissions.

## Remarks

You can use the **DocumentName** property of a [FaxStatus](-mfax-faxstatus.md) object in conjunction with the [**DocumentSize**](-mfax-ifaxstatus-get-documentsize-vb.md) property of the object to inform users about the size of outbound jobs.

The **IFaxStatus::get\_DocumentName** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**DocumentSize**](-mfax-ifaxstatus-get-documentsize-vb.md)
</dt> <dt>

[**IFaxPorts**](-mfax-ifaxports.md)
</dt> <dt>

[**IFaxPort**](-mfax-ifaxport.md)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




