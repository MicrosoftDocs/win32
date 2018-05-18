---
Description: 'The DeviceName property is a null-terminated string that contains the user-friendly display name for a fax port.'
ms.assetid: '0768dd6f-bb55-45b4-bb87-b79d5c250a18'
title: 'FaxRoutingMethod.get\_DeviceName property'
---

# FaxRoutingMethod.get\_DeviceName property

The **DeviceName** property is a null-terminated string that contains the user-friendly display name for a fax port.

This property is read-only.

## Syntax


```VB
Property get_DeviceName As String
```



## Property value

A **String** that receives the user-friendly name for the fax port associated with the specified fax routing method.

## Remarks

Note that it is possible for multiple fax ports to have the same user-friendly name. You can use the [**DeviceId**](-mfax-ifaxroutingmethod-get-deviceid-vb.md) property to uniquely identify a fax port.

**DeviceName** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxRoutingMethod**](-mfax-faxroutingmethod-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxRoutingMethod**](-mfax-ifaxroutingmethod.md)
</dt> <dt>

[**IFaxRoutingMethods**](-mfax-ifaxroutingmethods.md)
</dt> <dt>

[**DeviceId**](-mfax-ifaxroutingmethod-get-deviceid-vb.md)
</dt> <dt>

[**IFaxPort**](-mfax-ifaxport.md)
</dt> <dt>

[**IFaxPorts**](-mfax-ifaxports.md)
</dt> </dl>

 

 




