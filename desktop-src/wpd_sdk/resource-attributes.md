---
Description: Windows Portable Devices supports the following resource attributes.
ms.assetid: 0cbf8777-5cea-4839-a4c3-366bb9e18488
title: Resource Attributes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Attributes

Windows Portable Devices supports the following resource attributes. These attributes are returned by the following methods:

-   [**IPortableDeviceResources::GetResourceAttributes**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecapabilities-getfixedpropertyattributes?branch=master)



| Attribute                                                  | VarType      | Description                                                                                                                                 |
|------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_RESOURCE\_ATTRIBUTE\_CAN\_DELETE**                  | **VT\_BOOL** | A Boolean value that specifies whether a client has permission to delete the resource. If absent, it is assumed to be false.                |
| **WPD\_RESOURCE\_ATTRIBUTE\_CAN\_READ**                    | **VT\_BOOL** | A Boolean value that specifies whether a client has permission to open the resource for Read access. If absent, it is assumed to be False.  |
| **WPD\_RESOURCE\_ATTRIBUTE\_CAN\_WRITE**                   | **VT\_BOOL** | A Boolean value that specifies whether a client has permission to open the resource for Write access. If absent, it is assumed to be false. |
| **WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_READ\_BUFFER\_SIZE**  | **VT\_UI4**  | The recommended buffer size that a caller should use for buffered reads from the resource.                                                  |
| **WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_WRITE\_BUFFER\_SIZE** | **VT\_UI4**  | The recommended buffer size that a caller should use for buffered writes on the resource.                                                   |
| **WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE**                  | **VT\_UI8**  | The total size of the resource data, in bytes.                                                                                              |



 

## Requirements



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Properties**](properties-and-attributes.md)
</dt> </dl>

 

 




