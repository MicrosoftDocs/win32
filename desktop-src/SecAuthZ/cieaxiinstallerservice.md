---
Description: 'Implements the IAxiService and IeAxiServiceCallback interfaces.'
ms.assetid: '39f2ee3a-d4fd-4091-acd6-3d6b715bea75'
title: CIeAxiInstallerService object
---

# CIeAxiInstallerService object

The **CIeAxiInstallerService** object implements the [**IAxiService**](ieaxiservice.md) and [**IeAxiServiceCallback**](ieaxiservicecallback.md) interfaces.

This object is not declared in a public header. Applications must define it themselves. The following Interface Definition Language (IDL) fragment describes this object, including its CLSID.

``` syntax
[
        uuid(90F18417-F0F1-484E-9D3C-59DCEEE5DBD8)
]
    coclass CIeAxiInstallerService
    {
        [default] interface IeAxiService;
        interface IeAxiServiceCallback;
    }

```

## Requirements



|                                     |                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Business, Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                 |



## See also

<dl> <dt>

[**IAxiService**](ieaxiservice.md)
</dt> <dt>

[**IeAxiServiceCallback**](ieaxiservicecallback.md)
</dt> </dl>

 

 




