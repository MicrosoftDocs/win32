---
Description: You can add run-time parameter support to an XAPO by implementing the IXAPOParameters interface. Run-time parameter support allows an XAPO to change its behavior based on the parameters passed to it at run time.
ms.assetid: 13f974ec-fcf5-1749-e69d-88de79b7d82b
title: 'How to: Add Run-time Parameter Support to an XAPO'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to: Add Run-time Parameter Support to an XAPO

You can add run-time parameter support to an XAPO by implementing the [**IXAPOParameters**](/windows/desktop/api/XAPO/nn-xapo-ixapoparameters) interface. Run-time parameter support allows an XAPO to change its behavior based on the parameters passed to it at run time.

1.  Follow the steps in [How to: Create an XAPO](how-to--create-an-xapo.md).
2.  Change the XAPO to derive from [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) and [**CXAPOBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapobase).
3.  Add calls to the methods [**CXAPOParametersBase::BeginProcess**](https://www.bing.com/search?q=**CXAPOParametersBase::BeginProcess**) and [**CXAPOParametersBase::EndProcess**](https://www.bing.com/search?q=**CXAPOParametersBase::EndProcess**) to the implementation of [**IXAPO::Process**](https://www.bing.com/search?q=**IXAPO::Process**).

    > [!Note]  
    > Adding these methods to [IXAPO::Process](how-to--build-a-basic-audio-processing-graph.md) allows [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) to keep its copies of the effect parameters in a thread-safe state. Call [**CXAPOParametersBase::BeginProcess**](https://www.bing.com/search?q=**CXAPOParametersBase::BeginProcess**) at the beginning of [**IXAPO::Process**](https://www.bing.com/search?q=**IXAPO::Process**), and [**CXAPOParametersBase::EndProcess**](https://www.bing.com/search?q=**CXAPOParametersBase::EndProcess**) at the end of **IXAPO::Process**.

     

4.  Add more code to the [**IXAPO::Process**](https://www.bing.com/search?q=**IXAPO::Process**) implementation to change its behavior according to values stored by the [**SetParameters**](https://www.bing.com/search?q=**SetParameters**) method.

    > [!Note]  
    > Adding code to the [**IXAPO::Process**](https://www.bing.com/search?q=**IXAPO::Process**) method to use the parameters specified by [**SetParameters**](https://www.bing.com/search?q=**SetParameters**) allows the XAPO's behavior to be changed throughout its life.

     

5.  When you create an instance of the effect, allocate a buffer of three of the structures that will represent the effect's parameters, and pass it to the [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) constructor.

    > [!Note]  
    > The [**CXAPOParametersBase**](/windows/desktop/api/XAPOBase/nl-xapobase-cxapoparametersbase) instance internally uses this buffer to manage effect parameters passed to it when you call [**SetParameters**](https://www.bing.com/search?q=**SetParameters**). You must initialize all the process parameter blocks in *pParameterBlocks* to the same default value before you call any of the [**IXAPO::Process**](https://www.bing.com/search?q=**IXAPO::Process**), [**IXAPOParameters::GetParameters**](https://www.bing.com/search?q=**IXAPOParameters::GetParameters**), and **IXAPOParameters::SetParameters** methods. Usually this initialization is handled in [**IXAPO::Initialize**](https://www.bing.com/search?q=**IXAPO::Initialize**) or in [**IXAPO::LockForProcess**](https://www.bing.com/search?q=**IXAPO::LockForProcess**).

     

## Related topics

<dl> <dt>

[Audio Effects](audio-effects.md)
</dt> <dt>

[XAPO Overview](xapo-overview.md)
</dt> </dl>

 

 



