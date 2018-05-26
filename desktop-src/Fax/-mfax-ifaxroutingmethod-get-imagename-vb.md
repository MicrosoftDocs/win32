---
Description: The ImageName property is a null-terminated string that contains the executable image name of the fax routing extension DLL that implements the fax routing method.
ms.assetid: f5dd15c5-7367-4b66-8403-731072f9607f
title: FaxRoutingMethod.ImageName property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxRoutingMethod.ImageName property

The **ImageName** property is a null-terminated string that contains the executable image name of the fax routing extension DLL that implements the fax routing method.

This property is read-only.

## Syntax


```VB
Property ImageName As String
```



## Property value

A **String** that receives the unique executable image name of the fax routing extension DLL that exports the specified fax routing method.

## Remarks

A fax client application can use the **ImageName** property to uniquely identify the fax routing extension DLL that exports a fax routing method. Note that it is possible for multiple routing extensions to have the same user-friendly name.

**ImageName** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxRoutingMethod**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxroutingmethod?branch=master)
</dt> <dt>

[**IFaxRoutingMethods**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxroutingmethods?branch=master)
</dt> <dt>

[**ExtensionName**](-mfax-ifaxroutingmethod-get-extensionname-vb.md)
</dt> </dl>

 

 




