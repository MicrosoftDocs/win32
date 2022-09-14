---
description: Initializes a system service object to install an ActiveX object when the current user does not have permission to install the object.
ms.assetid: 42f7cf83-789b-42ea-bb1a-4b79137188ea
title: IeAxiService interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IeAxiService
api_type: 
- COM
api_location: 
---

# IeAxiService interface

The **IAxiService** interface initializes a system service object to install an ActiveX object when the current user does not have permission to install the object.

The [**CIeAxiInstallerService**](cieaxiinstallerservice.md) class implements this interface.

This interface is not declared in a public header. Applications must define it themselves. The following Interface Definition Language (IDL) fragment describes this interface, including its IID.

``` syntax
[
    object,
    uuid(E9E92380-9ECD-4982-A0EB-6815A56CCF27),
    pointer_default(unique)
]

interface IeAxiService : IUnknown{

    
    HRESULT Initialize(
            [in]        HWND            hwndParent,
            [in]        DWORD           dwClientPID,
            [in]        BSTR            bstrDesktop,
            [in]        BSTR            bstrClsID,              
            [in]        BSTR            bstrURL,                
            [out]       BSTR *          pbstrNonce,            
            [out]       IUnknown**      ppISyncBrokerInterface  
            );  
 
    HRESULT Cleanup();
};
```

## Members

The **IeAxiService** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IeAxiService** also has these types of members:

-   [Methods](#methods)

### Methods

The **IeAxiService** interface has these methods.



| Method                                        | Description                                                        |
|:----------------------------------------------|:-------------------------------------------------------------------|
| [**Cleanup**](ieaxiservice-cleanup.md)       | Frees resources used by the **IeAxiService** interface.<br/> |
| [**Initialize**](ieaxiservice-initialize.md) | Checks and downloads an ActiveX object.<br/>                 |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                 |
| IID<br/>                      | IID\_IeAxiService is defined as E9E92380-9ECD-4982-A0EB-6815A56CCF27<br/>                           |



 

