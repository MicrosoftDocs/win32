---
Description: Retrieves the DeviceName property for the FaxStatus object of a parent FaxPort object. The DeviceName property is a null-terminated string that contains the user-friendly display name for the fax port.
ms.assetid: 8b775e6a-8797-4235-883e-af6488663d75
title: FaxStatus.DeviceName property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxStatus.DeviceName property

Retrieves the **DeviceName** property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **DeviceName** property is a null-terminated string that contains the user-friendly display name for the fax port.

This property is read-only.

## Syntax


```VB
Property DeviceName As String
```



## Property value

A **String** that receives the user-friendly name to associate with the fax port.

## Remarks

Note that it is possible for multiple fax ports to have the same user-friendly name. You can use the [**DeviceId**](-mfax-ifaxstatus-get-deviceid-vb.md) property of a [FaxStatus](-mfax-faxstatus.md) object to uniquely identify a fax port, and associate a FaxStatus object with a [FaxPort](-mfax-faxport.md) object.

The **IFaxStatus::get\_DeviceName** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**DeviceId**](-mfax-ifaxstatus-get-deviceid-vb.md)
</dt> <dt>

[**IFaxPorts**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxports?branch=master)
</dt> <dt>

[**IFaxPort**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxport?branch=master)
</dt> <dt>

[SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3)
</dt> </dl>

 

 




