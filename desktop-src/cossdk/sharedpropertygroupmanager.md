---
Description: Creates shared property groups and to obtain access to existing shared property groups.
ms.assetid: 71c0a1de-5ea5-4496-b0e9-56d0cc8129a9
title: SharedPropertyGroupManager class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# SharedPropertyGroupManager class

Creates shared property groups and to obtain access to existing shared property groups.

For more information about using the Shared Property Manager in COM+, see [COM+ Shared Property Manager](com--shared-property-manager.md).

## When to implement

This class is implemented by COM+.



|            |                                                                    |
|------------|--------------------------------------------------------------------|
| CLSID      | CLSID\_SharedPropertyGroupManager                                  |
| ProgID     | L"MTxSpm.SharedPropertyGroupManager"                               |
| Interfaces | [**ISharedPropertyGroupManager**](/windows/desktop/api/ComSvcs/nn-comsvcs-isharedpropertygroupmanager) |



 

## When to use

Use this class to access the methods of [**ISharedPropertyGroupManager**](/windows/desktop/api/ComSvcs/nn-comsvcs-isharedpropertygroupmanager).

## Remarks

To create this object, call [**IObjectContext::CreateInstance**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-createinstance).

To use this class from Microsoft Visual Basic, add a reference to the COM+ Services Type Library. A SharedPropertyGroupManager object can be declared using "COMSVCSLib.SharedPropertyGroupManager" as the class name.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>ComSvcs.h</dt> </dl> |



## See also

<dl> <dt>

[**ISharedPropertyGroupManager**](/windows/desktop/api/ComSvcs/nn-comsvcs-isharedpropertygroupmanager)
</dt> <dt>

[**SharedProperty**](sharedproperty.md)
</dt> <dt>

[**SharedPropertyGroup**](sharedpropertygroup.md)
</dt> </dl>

 

 




