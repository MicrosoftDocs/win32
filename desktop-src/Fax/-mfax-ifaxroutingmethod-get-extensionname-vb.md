---
Description: The ExtensionName property is a null-terminated string that contains the user-friendly name for the fax routing extension DLL that implements the specified fax routing method.
ms.assetid: d0b42fc6-c797-4a51-a049-240ac0566b52
title: FaxRoutingMethod.ExtensionName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxRoutingMethod.ExtensionName property

The **ExtensionName** property is a null-terminated string that contains the user-friendly name for the fax routing extension DLL that implements the specified fax routing method.

This property is read-only.

## Syntax


```VB
Property ExtensionName As String
```



## Property value

A **String** that receives the user-friendly name to associate with the fax routing extension DLL that exports the specified fax routing method.

## Remarks

A fax client application can use the [**ImageName**](-mfax-ifaxroutingmethod-get-imagename-vb.md) property to uniquely identify the fax routing extension DLL that exports a fax routing method. Note that it is possible for multiple routing extensions to have the same user-friendly name.

**ExtensionName** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxRoutingMethod**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxroutingmethod)
</dt> <dt>

[**IFaxRoutingMethods**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxroutingmethods)
</dt> <dt>

[**ImageName**](-mfax-ifaxroutingmethod-get-imagename-vb.md)
</dt> </dl>

 

 




