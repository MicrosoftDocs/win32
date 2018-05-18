---
Description: 'You can add run-time parameter support to an XAPO by implementing the IXAPOParameters interface. Run-time parameter support allows an XAPO to change its behavior based on the parameters passed to it at run time.'
ms.assetid: '13f974ec-fcf5-1749-e69d-88de79b7d82b'
title: 'How to: Add Run-time Parameter Support to an XAPO'
---

# How to: Add Run-time Parameter Support to an XAPO

You can add run-time parameter support to an XAPO by implementing the [**IXAPOParameters**](ixapoparameters.md) interface. Run-time parameter support allows an XAPO to change its behavior based on the parameters passed to it at run time.

1.  Follow the steps in [How to: Create an XAPO](how-to--create-an-xapo.md).
2.  Change the XAPO to derive from [**CXAPOParametersBase**](cxapoparametersbase.md) and [**CXAPOBase**](cxapobase.md).
3.  Add calls to the methods [**CXAPOParametersBase::BeginProcess**](cxapoparametersbase-beginprocess.md) and [**CXAPOParametersBase::EndProcess**](cxapoparametersbase-endprocess.md) to the implementation of [**IXAPO::Process**](ixapo-interface-process.md).

    > [!Note]  
    > Adding these methods to [IXAPO::Process](how-to--build-a-basic-audio-processing-graph.md) allows [**CXAPOParametersBase**](cxapoparametersbase.md) to keep its copies of the effect parameters in a thread-safe state. Call [**CXAPOParametersBase::BeginProcess**](cxapoparametersbase-beginprocess.md) at the beginning of [**IXAPO::Process**](ixapo-interface-process.md), and [**CXAPOParametersBase::EndProcess**](cxapoparametersbase-endprocess.md) at the end of **IXAPO::Process**.

     

4.  Add more code to the [**IXAPO::Process**](ixapo-interface-process.md) implementation to change its behavior according to values stored by the [**SetParameters**](ixapoparameters-interface-setparameters.md) method.

    > [!Note]  
    > Adding code to the [**IXAPO::Process**](ixapo-interface-process.md) method to use the parameters specified by [**SetParameters**](ixapoparameters-interface-setparameters.md) allows the XAPO's behavior to be changed throughout its life.

     

5.  When you create an instance of the effect, allocate a buffer of three of the structures that will represent the effect's parameters, and pass it to the [**CXAPOParametersBase**](cxapoparametersbase.md) constructor.

    > [!Note]  
    > The [**CXAPOParametersBase**](cxapoparametersbase.md) instance internally uses this buffer to manage effect parameters passed to it when you call [**SetParameters**](ixapoparameters-interface-setparameters.md). You must initialize all the process parameter blocks in *pParameterBlocks* to the same default value before you call any of the [**IXAPO::Process**](ixapo-interface-process.md), [**IXAPOParameters::GetParameters**](ixapoparameters-interface-getparameters.md), and **IXAPOParameters::SetParameters** methods. Usually this initialization is handled in [**IXAPO::Initialize**](ixapo-interface-initialize.md) or in [**IXAPO::LockForProcess**](ixapo-interface-lockforprocess.md).

     

## Related topics

<dl> <dt>

[Audio Effects](audio-effects.md)
</dt> <dt>

[XAPO Overview](xapo-overview.md)
</dt> </dl>

 

 



