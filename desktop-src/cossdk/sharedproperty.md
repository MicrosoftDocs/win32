---
description: Sets or retrieves the value of a shared property.
ms.assetid: '19ed8d50-3ac1-408e-9f25-09f284d025f1'
title: SharedProperty class (ComSvcs.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SharedProperty
api_type: 
- COM
---

# SharedProperty class

Sets or retrieves the value of a shared property.

For general information about using the Shared Property Manager in COM+, see [COM+ Shared Property Manager](com--shared-property-manager.md).

## When to implement

This class is implemented by COM+.



| Requirement | Value |
|------------|--------------------------------------------|
| Interfaces | [**ISharedProperty**](/windows/desktop/api/ComSvcs/nn-comsvcs-isharedproperty) |



 

## When to use

Use this class to access the methods of [**ISharedProperty**](/windows/desktop/api/ComSvcs/nn-comsvcs-isharedproperty).

## Remarks

You can create a **SharedProperty** object by using the [**CreateProperty**](/windows/desktop/api/ComSvcs/nf-comsvcs-isharedpropertygroup-createproperty) or [**CreatePropertyByPosition**](/windows/desktop/api/ComSvcs/nf-comsvcs-isharedpropertygroup-createpropertybyposition) methods of [**ISharedPropertyGroup**](/windows/desktop/api/ComSvcs/nn-comsvcs-isharedpropertygroup).

To use this class from Microsoft Visual Basic, add a reference to the COM+ Services Type Library. A SharedProperty object is created by calling the [**CreateProperty**](/windows/desktop/api/ComSvcs/nf-comsvcs-isharedpropertygroup-createproperty) or [**CreatePropertyByPosition**](/windows/desktop/api/ComSvcs/nf-comsvcs-isharedpropertygroup-createpropertybyposition) methods of the [**SharedPropertyGroup**](sharedpropertygroup.md) object.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>ComSvcs.h</dt> </dl> |



## See also

<dl> <dt>

[**ISharedProperty**](/windows/desktop/api/ComSvcs/nn-comsvcs-isharedproperty)
</dt> <dt>

[**SharedPropertyGroup**](sharedpropertygroup.md)
</dt> <dt>

[**SharedPropertyGroupManager**](sharedpropertygroupmanager.md)
</dt> </dl>

 

 




