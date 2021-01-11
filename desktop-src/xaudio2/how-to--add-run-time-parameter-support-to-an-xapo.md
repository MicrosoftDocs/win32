---
description: You can add run-time parameter support to an XAPO by implementing the IXAPOParameters interface. Run-time parameter support allows an XAPO to change its behavior based on the parameters passed to it at run time.
ms.assetid: 13f974ec-fcf5-1749-e69d-88de79b7d82b
title: 'How to: Add Run-time Parameter Support to an XAPO'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Add Run-time Parameter Support to an XAPO

You can add run-time parameter support to an XAPO by implementing the [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters) interface. Run-time parameter support allows an XAPO to change its behavior based on the parameters passed to it at run time.

1.  Follow the steps in [How to: Create an XAPO](how-to--create-an-xapo.md).
2.  Change the XAPO to derive from [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) and [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase).
3.  Add calls to the methods [**CXAPOParametersBase::BeginProcess**](/windows/win32/api/xapobase/nf-xapobase-cxapoparametersbase-beginprocess) and [**CXAPOParametersBase::EndProcess**](/windows/win32/api/xapobase/nf-xapobase-cxapoparametersbase-endprocess) to the implementation of [**IXAPO::Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process).

    > [!Note]  
    > Adding these methods to [IXAPO::Process](how-to--build-a-basic-audio-processing-graph.md) allows [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) to keep its copies of the effect parameters in a thread-safe state. Call [**CXAPOParametersBase::BeginProcess**](/windows/win32/api/xapobase/nf-xapobase-cxapoparametersbase-beginprocess) at the beginning of [**IXAPO::Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process), and [**CXAPOParametersBase::EndProcess**](/windows/win32/api/xapobase/nf-xapobase-cxapoparametersbase-endprocess) at the end of **IXAPO::Process**.

     

4.  Add more code to the [**IXAPO::Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process) implementation to change its behavior according to values stored by the [**SetParameters**](/windows/win32/api/xapo/nf-xapo-ixapoparameters-setparameters) method.

    > [!Note]  
    > Adding code to the [**IXAPO::Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process) method to use the parameters specified by [**SetParameters**](/windows/win32/api/xapo/nf-xapo-ixapoparameters-setparameters) allows the XAPO's behavior to be changed throughout its life.

     

5.  When you create an instance of the effect, allocate a buffer of three of the structures that will represent the effect's parameters, and pass it to the [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) constructor.

    > [!Note]  
    > The [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) instance internally uses this buffer to manage effect parameters passed to it when you call [**SetParameters**](/windows/win32/api/xapo/nf-xapo-ixapoparameters-setparameters). You must initialize all the process parameter blocks in *pParameterBlocks* to the same default value before you call any of the [**IXAPO::Process**](/windows/win32/api/xapo/nf-xapo-ixapo-process), [**IXAPOParameters::GetParameters**](/windows/win32/api/xapo/nf-xapo-ixapoparameters-getparameters), and **IXAPOParameters::SetParameters** methods. Usually this initialization is handled in [**IXAPO::Initialize**](/windows/win32/api/xapo/nf-xapo-ixapo-initialize) or in [**IXAPO::LockForProcess**](/windows/win32/api/xapo/nf-xapo-ixapo-lockforprocess).

     

## Related topics

<dl> <dt>

[Audio Effects](audio-effects.md)
</dt> <dt>

[XAPO Overview](xapo-overview.md)
</dt> </dl>

 

 
