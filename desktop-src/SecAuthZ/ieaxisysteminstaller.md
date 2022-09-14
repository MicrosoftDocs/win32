---
description: Installs an ActiveX object.
ms.assetid: 0eb725a9-ceb8-40e5-808d-ac2b286a48b6
title: IeAxiSystemInstaller interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IeAxiSystemInstaller
api_type: 
- COM
api_location: 
---

# IeAxiSystemInstaller interface

The **IeAxiSystemInstaller** interface installs an ActiveX object.

This interface is not declared in a public header. Applications must define it themselves. The following Interface Definition Language (IDL) fragment describes this interface, including its IID.

``` syntax
[
    object,
    uuid(a50ea6f8-4764-4299-b309-022b2a8b4d8d),
    
]
interface IeAxiSystemInstaller : IUnknown
{
    
    HRESULT InitializeSystemInstaller(  [in] BSTR bstrUrl,
                                  [in] DWORD dwClientPID,
                                  [in] IUnknown* pCallback,
                                  [out] BSTR * pbstrNonce);
}

```

## Members

The **IeAxiSystemInstaller** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IeAxiSystemInstaller** also has these types of members:

-   [Methods](#methods)

### Methods

The **IeAxiSystemInstaller** interface has these methods.



| Method                                                                              | Description                                       |
|:------------------------------------------------------------------------------------|:--------------------------------------------------|
| [**InitializeSystemInstaller**](ieaxisysteminstaller-initializesysteminstaller.md) | Installs the specified ActiveX object.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                 |
| IID<br/>                      | IID\_IeAxiSystemInstaller is defined as a50ea6f8-4764-4299-b309-022b2a8b4d8d<br/>                   |



 

