---
title: Plug-in Wrapper Functions
description: Wrapper functions that allow you to call a public function on any adapter attached to the pipeline without manually acquiring a pointer to the adapter.
ms.assetid: a87536bf-3a10-4062-a509-db7f03172307
keywords:
- Windows Biometric Framework API Windows Biometric Framework API , plug-in wrapper functions
ms.topic: article
ms.date: 05/31/2018
---

# Plug-in Wrapper Functions

The Windows Biometric Framework API includes wrapper functions that allow you to call a public function on any adapter attached to the pipeline without manually acquiring a pointer to the adapter. Each wrapper checks the input arguments, retrieves an adapter pointer, and calls the requested function. For example, the **WbioEngineSetHashAlgorithm** wrapper has the following signature.


```C++
inline HRESULT
WbioEngineSetHashAlgorithm(
    __inout PWINBIO_PIPELINE Pipeline,
    __in SIZE_T AlgorithmBufferSize,
    __in PUCHAR AlgorithmBuffer
    )
{
    if (ARGUMENT_PRESENT(Pipeline) &&
        ARGUMENT_PRESENT(Pipeline->EngineInterface) &&
        ARGUMENT_PRESENT(Pipeline->EngineInterface->SetHashAlgorithm))
    {
        return Pipeline->EngineInterface->SetHashAlgorithm(
                                            Pipeline,
                                            AlgorithmBufferSize,
                                            AlgorithmBuffer
                                            );
    }
    else
    {
        return E_NOTIMPL;
    }
}
```



The function verifies that the *Pipeline* argument is not **NULL**, that an engine adapter exists, and that the [**EngineAdapterSetHashAlgorithm**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_set_hash_algorithm_fn) function exists. All wrapper functions are defined in the Winbio\_adapter.h header file. The following topics discuss the available wrappers.

## In this section



| Topic                                                               | Description                                                                                                                        |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [Engine Adapter Wrappers](engine-adapter-wrappers.md)<br/>   | Functions that you can use to call functions on your engine adapter. These functions are defined in Winbio\_adapter.h.<br/>  |
| [Sensor Adapter Wrappers](sensor-adapter-wrappers.md)<br/>   | Functions that you can use to call functions on your sensor adapter. These functions are defined in Winbio\_adapter.h.<br/>  |
| [Storage Adapter Wrappers](storage-adapter-wrappers.md)<br/> | Functions that you can use to call functions on your storage adapter. These functions are defined in Winbio\_adapter.h.<br/> |



 

## Related topics

<dl> <dt>

[Plug-in Reference](plug-in-reference.md)
</dt> </dl>

 

 





