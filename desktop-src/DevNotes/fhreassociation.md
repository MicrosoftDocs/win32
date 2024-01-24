---
description: Represents the File History reassociation feature, which allows a user to reestablish a relationship with a backup target that was used by the same user in the past. Reassociation is performed by calling the methods of the IFhReassociation interface.
ms.assetid: BB81F8ED-4DFB-4FA5-B3ED-ACBAB32BBE3D
title: FhReassociation class (Fhcfg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FhReassociation
api_type: 
- COM
api_location: 
- Fhcfg.idl
---

# FhReassociation class

Represents the File History reassociation feature, which allows a user to reestablish a relationship with a backup target that was used by the same user in the past. Reassociation is performed by calling the methods of the [**IFhReassociation**](/windows/desktop/api/Fhcfg/nn-fhcfg-ifhreassociation) interface.

## When to implement

The File History API implements this class. To create an instance of this class, use the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Fhcfg.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Fhcfg.idl</dt> </dl> |



 

 
