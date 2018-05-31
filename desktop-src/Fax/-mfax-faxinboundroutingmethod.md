---
Description: The FaxInboundRoutingMethod configuration object is used by a fax client application to retrieve information about an individual fax inbound routing method on a connected fax server.
ms.assetid: 8eb68201-4c87-41ce-a401-a039b5ad454d
title: FaxInboundRoutingMethod object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxInboundRoutingMethod object

The **FaxInboundRoutingMethod** configuration object is used by a fax client application to retrieve information about an individual fax inbound routing method on a connected fax server.

## Members

The **FaxInboundRoutingMethod** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxInboundRoutingMethod** object has these methods.



| Method                                                      | Description                                                                                                                                                     |
|:------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Refresh**](-mfax-faxinboundroutingmethod-refresh-vb.md) | The [**Refresh**](-mfax-faxinboundroutingmethod-refresh-vb.md) method refreshes **FaxInboundRoutingMethod** object information from the fax server.<br/> |
| [**Save**](-mfax-faxinboundroutingmethod-save-vb.md)       | The [**Save**](-mfax-faxinboundroutingmethod-save-vb.md) method saves the **FaxInboundRoutingMethod** object's data.<br/>                                |



 

### Properties

The **FaxInboundRoutingMethod** object has these properties.



| Property                                                                                           | Access type           | Description                                                                                                                                                                                                                                                              |
|:---------------------------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExtensionFriendlyName**](-mfax-faxinboundroutingmethod-extensionfriendlyname-vb.md)<br/> | Read-only<br/>  | The [**ExtensionFriendlyName**](-mfax-faxinboundroutingmethod-extensionfriendlyname-vb.md) property is the user-friendly name for the fax routing extension that exports the inbound fax routing method.<br/>                                                     |
| [**ExtensionImageName**](-mfax-faxinboundroutingmethod-extensionimagename-vb.md)<br/>       | Read-only<br/>  | The [**ExtensionImageName**](-mfax-faxinboundroutingmethod-extensionimagename-vb.md) property is a null-terminated string that contains the executable image name (DLL path and file name) of the fax routing extension that exports the fax routing method.<br/> |
| [**FunctionName**](-mfax-faxinboundroutingmethod-functionname-vb.md)<br/>                   | Read-only<br/>  | The [**FunctionName**](-mfax-faxinboundroutingmethod-functionname-vb.md) property is a null-terminated string that contains the name of the function that executes a specific fax routing procedure.<br/>                                                         |
| [**GUID**](-mfax-faxinboundroutingmethod-guid-vb.md)<br/>                                   | Read-only<br/>  | The [**GUID**](-mfax-faxinboundroutingmethod-guid-vb.md) property is a null-terminated string that specifies the GUID that uniquely identifies the fax routing method.<br/>                                                                                       |
| [**Name**](-mfax-faxinboundroutingmethod-name-vb.md)<br/>                                   | Read-only<br/>  | The [**Name**](-mfax-faxinboundroutingmethod-name-vb.md) property is a null-terminated string that contains the user-friendly name associated with the inbound fax routing method. The string is suitable for display to users.<br/>                              |
| [**Priority**](-mfax-faxinboundroutingmethod-priority.md)<br/>                              | Read/write<br/> | The [**Priority**](-mfax-faxinboundroutingmethod-priority.md) property is a value associated with the order in which the fax service calls the routing method when the service receives a fax job.<br/>                                                           |



 

## Remarks

A **FaxInboundRoutingMethod** object is accessed through a [**FaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods.md) object.

![faxinboundrouting, faxinboundroutingmethods, and faxinboundroutingmethod objects](images/faxinboundroutingmethod.png)

> [!Note]  
> Changes made to the **FaxInboundRoutingMethod** object will not be saved until you call the [**Save**](-mfax-faxinboundroutingmethod-save-vb.md) method.

 

To create a **FaxInboundRoutingMethod** object in Microsoft Visual Basic, call the [**Item**](-mfax-faxinboundroutingmethods-item.md) property of the [**FaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods.md) object.

To create a **FaxInboundRoutingMethod** object in C++, call the [**get\_Item**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxinboundroutingmethods-get_item) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxInboundRoutingMethod<br/>                                               |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxInboundRoutingMethod**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxinboundroutingmethod)
</dt> </dl>

 

 




