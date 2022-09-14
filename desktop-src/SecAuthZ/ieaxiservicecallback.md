---
description: Called by the IeAxiSystemInstaller interface to verify that an ActiveX object can be installed.
ms.assetid: d5cd6263-d07e-4261-9463-b9a06e883f16
title: IeAxiServiceCallback interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IeAxiServiceCallback
api_type: 
- COM
api_location: 
---

# IeAxiServiceCallback interface

The **IeAxiServiceCallback** interface is called by the [**IeAxiSystemInstaller**](ieaxisysteminstaller.md) interface to verify that an ActiveX object can be installed.

The [**CIeAxiInstallerService**](cieaxiinstallerservice.md) class implements this interface.

This interface is not declared in a public header. Applications must define it themselves. The following Interface Definition Language (IDL) fragment describes this interface, including its IID.

``` syntax
[
    object,
    uuid(1823E7BA-EC36-447a-9B2E-B4912E15AFE7),
    dual,
    nonextensible,
    pointer_default(unique)
]

interface IeAxiServiceCallback : IUnknown
{
    HRESULT VerifyFile(
                       [in] BSTR bstrFileUrl,
                       [out] BSTR * bstrApprovedFileName);
}

```

## Members

The **IeAxiServiceCallback** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IeAxiServiceCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IeAxiServiceCallback** interface has these methods.



| Method                                                | Description                                                                                                                                    |
|:------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**VerifyFile**](ieaxiservicecallback-verifyfile.md) | Performs security checks on the specified ActiveX object and returns the location where the corresponding .cab file was downloaded.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                 |
| IID<br/>                      | IID\_IeAxiServiceCallback is defined as 1823E7BA-EC36-447a-9B2E-B4912E15AFE7<br/>                   |



 

